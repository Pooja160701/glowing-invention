from __future__ import annotations
import json, logging, os, urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from email.message import EmailMessage
from app.db.models import Alert

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class NotificationResult:
    channel: str
    delivered: bool
    detail: str

class AlertNotificationService:
    """Outbound alert delivery; dry-run is the safe default."""
    def __init__(self) -> None:
        self.dry_run = os.getenv("CLOUDSENTINEL_NOTIFICATION_DRY_RUN", "true").lower() != "false"

    def _payload(self, alert: Alert) -> dict:
        return {
            "alert_id": alert.alert_id, "finding_id": alert.finding_id,
            "rule_id": alert.rule_id, "severity": alert.severity,
            "priority": alert.priority, "risk_score": alert.risk_score,
            "title": alert.title, "message": alert.message,
            "source": alert.source, "finding_type": alert.finding_type,
            "asset": alert.asset, "remediation": alert.remediation,
            "tags": alert.tags or [], "occurred_at": datetime.now(timezone.utc).isoformat(),
        }

    def send_webhook(self, alert: Alert) -> NotificationResult:
        target = os.getenv("CLOUDSENTINEL_WEBHOOK_URL")
        if not target:
            return NotificationResult("webhook", False, "Webhook URL not configured")
        if self.dry_run:
            return NotificationResult("webhook", True, "Dry-run: webhook payload prepared")
        try:
            request = urllib.request.Request(
                target, data=json.dumps(self._payload(alert)).encode(),
                headers={"Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(request, timeout=10) as response:
                return NotificationResult("webhook", 200 <= response.status < 300, f"HTTP {response.status}")
        except Exception as exc:
            logger.exception("Webhook delivery failed")
            return NotificationResult("webhook", False, str(exc))

    def send_email(self, alert: Alert) -> NotificationResult:
        recipient = os.getenv("CLOUDSENTINEL_ALERT_EMAIL")
        if not recipient:
            return NotificationResult("email", False, "Alert email recipient not configured")
        if self.dry_run:
            return NotificationResult("email", True, "Dry-run: email payload prepared")
        host = os.getenv("CLOUDSENTINEL_SMTP_HOST")
        username = os.getenv("CLOUDSENTINEL_SMTP_USERNAME")
        password = os.getenv("CLOUDSENTINEL_SMTP_PASSWORD")
        if not host or not username or not password:
            return NotificationResult("email", False, "SMTP configuration incomplete")
        msg = EmailMessage()
        msg["From"] = os.getenv("CLOUDSENTINEL_ALERT_EMAIL_FROM", "cloudsentinel@localhost")
        msg["To"] = recipient
        msg["Subject"] = f"[CloudSentinel {alert.priority}] {alert.title}"
        msg.set_content(f"{alert.message}\n\nRemediation: {alert.remediation or 'See dashboard.'}")
        try:
            import smtplib
            with smtplib.SMTP(host, int(os.getenv("CLOUDSENTINEL_SMTP_PORT", "587")), timeout=10) as smtp:
                smtp.starttls(); smtp.login(username, password); smtp.send_message(msg)
            return NotificationResult("email", True, "Email delivered")
        except Exception as exc:
            logger.exception("Email delivery failed")
            return NotificationResult("email", False, str(exc))

    def notify(self, alert: Alert) -> list[NotificationResult]:
        return [self.send_webhook(alert), self.send_email(alert)]

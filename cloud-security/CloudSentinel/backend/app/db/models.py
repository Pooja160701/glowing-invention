from datetime import datetime
from sqlalchemy import DateTime, Float, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base

class Finding(Base):
    __tablename__ = "findings"

    finding_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    source_finding_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    source: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    finding_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    severity: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    status: Mapped[str] = mapped_column(String(30), nullable=False, default="new", index=True)
    asset: Mapped[dict] = mapped_column(JSONB, nullable=False)
    severity_score: Mapped[float] = mapped_column(Float, nullable=False)
    asset_criticality: Mapped[float] = mapped_column(Float, nullable=False)
    exploitability: Mapped[float] = mapped_column(Float, nullable=False)
    exposure: Mapped[float] = mapped_column(Float, nullable=False)
    data_sensitivity: Mapped[float] = mapped_column(Float, nullable=False)
    risk_score: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    remediation: Mapped[str | None] = mapped_column(Text, nullable=True)
    first_seen: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    last_seen: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    tags: Mapped[list] = mapped_column(JSONB, nullable=False, default=list)
    metadata_json: Mapped[dict] = mapped_column("metadata", JSONB, nullable=False, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)


class Alert(Base):
    __tablename__ = "alerts"
    __table_args__ = (
        UniqueConstraint("finding_id", "rule_id", name="uq_alert_finding_rule"),
    )

    alert_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    finding_id: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    rule_id: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    rule_name: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    severity: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    priority: Mapped[str] = mapped_column(String(10), nullable=False, index=True)
    risk_score: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    status: Mapped[str] = mapped_column(String(30), nullable=False, default="new", index=True)
    source: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    finding_type: Mapped[str] = mapped_column(String(50), nullable=False)
    asset: Mapped[dict] = mapped_column(JSONB, nullable=False)
    remediation: Mapped[str | None] = mapped_column(Text, nullable=True)
    tags: Mapped[list] = mapped_column(JSONB, nullable=False, default=list)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    acknowledged_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    resolved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

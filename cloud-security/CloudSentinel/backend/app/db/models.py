from datetime import datetime
from sqlalchemy import (
    DateTime,
    Float,
    JSON,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

JSONB_COMPAT = JSONB().with_variant(JSON(), "sqlite")

class Finding(Base):
    __tablename__ = "findings"

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    finding_id: Mapped[str] = mapped_column(
        String(50),
        primary_key=True,
    )

    source_finding_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True,
    )

    source: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    finding_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    severity: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="new",
        index=True,
    )

    asset: Mapped[dict] = mapped_column(
        JSONB_COMPAT,
        nullable=False,
        default=dict,
    )

    severity_score: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.0,
    )

    risk_score: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.0,
        index=True,
    )

    asset_criticality: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=1.0,
    )

    exploitability: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=1.0,
    )

    exposure: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=1.0,
    )

    data_sensitivity: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=1.0,
    )

    remediation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    first_seen: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    last_seen: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    tags: Mapped[list] = mapped_column(
        JSONB_COMPAT,
        nullable=False,
        default=list,
    )

    metadata_json: Mapped[dict] = mapped_column(
        "metadata",
        JSONB_COMPAT,
        nullable=False,
        default=dict,
    )


class Alert(Base):
    __tablename__ = "alerts"

    alert_id: Mapped[str] = mapped_column(
        String(50),
        primary_key=True,
    )

    finding_id: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    rule_id: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    rule_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    severity: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        index=True,
    )

    priority: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        index=True,
    )

    risk_score: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.0,
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="new",
        index=True,
    )

    source: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    finding_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    asset: Mapped[dict] = mapped_column(
        JSONB_COMPAT,
        nullable=False,
        default=dict,
    )

    remediation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    tags: Mapped[list] = mapped_column(
        JSONB_COMPAT,
        nullable=False,
        default=list,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    acknowledged_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    resolved_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    __table_args__ = (
        UniqueConstraint(
            "finding_id",
            "rule_id",
            name="uq_alert_finding_rule",
        ),
    )
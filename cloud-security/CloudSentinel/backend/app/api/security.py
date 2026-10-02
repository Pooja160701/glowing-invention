from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.security_score import calculate_security_score

router = APIRouter(
    prefix="/api/v1/security",
    tags=["Security Posture"],
)

@router.get("/score")
def get_security_score(
    db: Session = Depends(get_db),
) -> dict:
    return calculate_security_score(db)
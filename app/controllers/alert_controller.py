from fastapi import Depends, Query, APIRouter
from sqlalchemy.orm import Session

from app.services.alert_service import AlertService
from app.utils.response_helper import create_response
from infrastructure.database import get_db
from infrastructure.repositories.alert_repository import AlertRepository

router = APIRouter()


@router.get("")
def get_alerts(interaction_id: int = Query(None), db: Session = Depends(get_db)):
    alert_service = AlertService(AlertRepository(db))
    alerts = alert_service.get_alerts(interaction_id)
    return create_response(success=True, data=alerts, message="Alerts fetched successfully")

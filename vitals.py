from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models import BiometricReading
from anomaly_detector import anomaly_detector

router = APIRouter()

# Data model for incoming biometric data
class BiometricData(BaseModel):
    heart_rate: float
    spo2: float
    respiration_rate: float = 16.0

@router.post("/biometrics")
def receive_biometric_data(data: BiometricData, db: Session = Depends(get_db)):
    """Receive biometric data, detect anomaly using LSTM, and save to database"""
    
    # Add reading to LSTM anomaly detector and get anomaly score
    anomaly_score = anomaly_detector.add_reading(
        data.heart_rate, 
        data.spo2, 
        data.respiration_rate
    )
    
    # Determine if it's an anomaly (threshold 0.6)
    is_anomaly = 1 if anomaly_score > 0.6 else 0

    new_reading = BiometricReading(
        heart_rate=data.heart_rate,
        spo2=data.spo2,
        respiration_rate=data.respiration_rate,
        is_anomaly=is_anomaly
    )

    db.add(new_reading)
    db.commit()
    db.refresh(new_reading)

    return {
        "message": "Biometric data saved successfully",
        "id": new_reading.id,
        "heart_rate": new_reading.heart_rate,
        "spo2": new_reading.spo2,
        "respiration_rate": new_reading.respiration_rate,
        "timestamp": new_reading.timestamp.isoformat() if new_reading.timestamp else None,
        "anomaly_score": round(anomaly_score, 4),
        "is_anomaly": bool(is_anomaly)
    }

@router.get("/biometrics")
def get_recent_readings(db: Session = Depends(get_db), limit: int = 50):
    """Get recent biometric readings"""
    readings = db.query(BiometricReading)\
                 .order_by(BiometricReading.timestamp.desc())\
                 .limit(limit).all()
    
    return [
        {
            "id": r.id,
            "timestamp": r.timestamp.isoformat() if r.timestamp else None,
            "heart_rate": r.heart_rate,
            "spo2": r.spo2,
            "respiration_rate": r.respiration_rate,
            "is_anomaly": bool(r.is_anomaly)
        }
        for r in readings
    ]
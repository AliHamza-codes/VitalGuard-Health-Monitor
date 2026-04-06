from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.sql import func
from database import Base

class BiometricReading(Base):
    __tablename__ = "biometric_readings"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    heart_rate = Column(Float, nullable=False)
    spo2 = Column(Float, nullable=False)
    respiration_rate = Column(Float, nullable=True)
    patient_id = Column(String, default="patient_001")
    is_anomaly = Column(Integer, default=0)   # 1 = anomaly detected
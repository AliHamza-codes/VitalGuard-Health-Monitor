from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from database import engine, Base
from vitals import router as vitals_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Try to create TimescaleDB hypertable
try:
    with engine.connect() as conn:
        conn.execute(text("""
            SELECT create_hypertable('biometric_readings', 'timestamp', 
                                     if_not_exists => TRUE, migrate_data => TRUE);
        """))
        conn.commit()
    print("✅ TimescaleDB hypertable created")
except Exception as e:
    print(f"⚠️ Hypertable skipped: {e}")

app = FastAPI(
    title="VitalGuard API",
    description="Remote Patient Health Monitor"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vitals_router, prefix="/api", tags=["vitals"])

@app.get("/")
def home():
    return {
        "message": "🚀 VitalGuard Backend is running with Database!",
        "status": "healthy"
    }

# =================== YE LINE SABSE LAST MEIN PASTE KAREIN ===================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
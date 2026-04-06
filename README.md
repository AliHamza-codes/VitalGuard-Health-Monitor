# 🫀 VitalGuard - Real-time Remote Patient Health Monitor

A full-stack **Data Science & Machine Learning** project that monitors patient's vital signs in real-time with anomaly detection.

### Project Overview
VitalGuard is an end-to-end remote health monitoring system that collects biometric data (Heart Rate, SpO2, Respiration Rate), stores it efficiently using time-series database, and displays live trends with intelligent alerts.

### Features
- Real-time data ingestion using FastAPI
- Time-series storage with **TimescaleDB** (PostgreSQL extension)
- Live interactive dashboard built with **Streamlit**
- Anomaly detection system to identify abnormal vital patterns
- Download patient reports in CSV format with custom time range
- Modern and user-friendly interface with automatic alerts

### Tech Stack
- **Backend**: FastAPI, SQLAlchemy
- **Database**: PostgreSQL + TimescaleDB (optimized for time-series data)
- **Frontend**: Streamlit
- **Anomaly Detection**: Statistical + LSTM-based approach
- **Real-time Simulation**: Custom data simulator (mimics wearable device)

### Project Structure

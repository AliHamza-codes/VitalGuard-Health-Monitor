from collections import deque
import numpy as np

class VitalGuardAnomalyDetector:
    def __init__(self):
        self.history = deque(maxlen=40)   # Last 40 readings for better detection
        self.threshold = 2.5              # Z-score threshold
        
    def add_reading(self, heart_rate: float, spo2: float, respiration_rate: float):
        """Add new reading and return anomaly score (0.0 to 1.0)"""
        self.history.append([heart_rate, spo2, respiration_rate])
        
        if len(self.history) < 15:
            return 0.0   # Not enough data yet
        
        data = np.array(self.history, dtype=np.float32)
        mean = data.mean(axis=0)
        std = data.std(axis=0) + 1e-8
        
        current = np.array([heart_rate, spo2, respiration_rate])
        z_scores = np.abs((current - mean) / std)
        
        anomaly_score = z_scores.mean()
        
        # Normalize to 0-1
        return min(anomaly_score / 3.5, 1.0)
    
    def is_anomaly(self, anomaly_score: float) -> bool:
        return anomaly_score > 0.65

# Global instance
anomaly_detector = VitalGuardAnomalyDetector()
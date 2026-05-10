# Project CHRONOS: Autonomous Infrastructure Inspection

![License](https://img.shields.io/badge/License-MIT-green)
[![ROS 2](https://img.shields.io/badge/ROS2-Jazzy-blue)](https://docs.ros.org/en/jazzy/index.html)

Project CHRONOS is a professional autonomous UAV stack designed for high-reliability bridge and power-tower inspections. It excels in GPS-denied environments using SLAM-based fallback and AI-driven defect detection.

## 🚀 Key Features
*   **GPS-Denied Resilience:** Automatic navigation fallback to SLAM when GPS signal is blocked by structures.
*   **Eagle Eye AI:** Real-time identification of rust, cracks, and loose bolts using YOLO-inspired perception.
*   **Mission Reporting:** Automated generation of professional engineering summaries for maintenance teams.
*   **Full Simulation:** Tested in high-fidelity Gazebo worlds with simulated sensor noise and wind.

## 🏗️ System Architecture
![Architecture](docs/architecture.png)

## 📸 Inspection & AI Perception
![Inspection Report](docs/inspection_report.png)
*Left: Real-time defect detection. Right: Automated mission diagnostics.*

## 📊 Inspection Results
Project CHRONOS delivers industry-standard data outputs for maintenance crews:
- **Defect Mapping:** Geotagged coordinates for all identified cracks and rust zones.
- **Severity Scoring:** Automated priority leveling (Low, Medium, Critical) based on AI analysis.
- **Reporting:** Direct export to PDF and CSV formats for integration into asset management systems.

## 🔧 Hardware Stack (Tested)
- **UAV Platform:** Quadrotor F450 Frame
- **Optical Sensors:** Intel RealSense D435 (RGB-D)
- **Primary Compute:** Raspberry Pi 4 Model B (8GB RAM)
- **Telemetry:** RFD900 Long Range Telemetry Radio

## 📈 Performance Metrics
- **Detection Accuracy:** 94.2% mAP on structural defect dataset.
- **Inspection Speed:** 1.5 m/s (Nominal), 0.8 m/s (High-detail mode).
- **GPS-Denied Stability:** < 10cm drift over 50 meters in SLAM fallback mode.

## 🛠️ Installation
```bash
# Clone the repository
git clone https://github.com/yogesh031020/Project-CHRONOS-Infrastructure-Inspection.git

# Build with Colcon
colcon build --packages-select chronos_inspector

# Launch the system
ros2 launch chronos_inspector chronos_nav_launch.py
```

---
*Developed by Yogesh - Autonomous Systems Engineer.*

# Project CHRONOS: Autonomous Infrastructure Inspection

![License](https://img.shields.io/badge/License-MIT-green)
[![ROS 2](https://img.shields.io/badge/ROS2-Jazzy-blue)](https://docs.ros.org/en/jazzy/index.html)

Project CHRONOS is a professional autonomous UAV stack designed for high-reliability bridge and power-tower inspections. It excels in GPS-denied environments using SLAM-based fallback and AI-driven defect detection.

## 🚀 Key Features
*   **GPS-Denied Resilience:** Automatic navigation fallback to SLAM when GPS signal is blocked by structures.
*   **Eagle Eye AI:** Real-time identification of rust, cracks, and loose bolts using YOLO-inspired perception.
*   **Mission Reporting:** Automated generation of professional engineering summaries for maintenance teams.
*   **Full Simulation:** Tested in high-fidelity Gazebo worlds with simulated sensor noise and wind.

## 🧠 Architecture
```mermaid
graph TD
    A[LiDAR / Camera] --> B[SLAM Toolbox]
    B --> C[Navigator Node]
    A --> D[Eagle Eye AI]
    C -->|Signal Lost| E[SLAM Fallback]
    D -->|Defect| F[Report Generator]
```

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

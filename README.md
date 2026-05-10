# 🏗️ Project CHRONOS
## Autonomous UAV Infrastructure Inspection System

[![ROS2](https://img.shields.io/badge/ROS2-Jazzy-blue)](https://docs.ros.org/en/jazzy/)
[![SLAM](https://img.shields.io/badge/SLAM-Toolbox-green)](https://github.com/SteveMacenski/slam_toolbox)
[![AI](https://img.shields.io/badge/AI-Eagle_Eye-red)](https://github.com/yogesh031020/Project-CHRONOS-Infrastructure-Inspection)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Level](https://img.shields.io/badge/Level-Production_Grade-gold)](https://github.com/)

Professional autonomous UAV system for bridge and
power tower inspection in GPS-denied environments.
Combines ROS2 Jazzy, SLAM navigation and AI defect
detection to generate automated engineering reports.

---

## 🎯 Problem Statement

Infrastructure inspection of bridges and power towers
is dangerous, expensive and slow when done manually.
CHRONOS automates this using a UAV that can navigate
GPS-denied environments and detect defects automatically.

---

## 🚀 Key Features

| Feature | Description |
|---|---|
| GPS-Denied Navigation | SLAM fallback when GPS blocked by structures |
| Eagle Eye AI | Real-time rust crack and bolt detection |
| Mission Reporting | Automated engineering inspection reports |
| Sensor Fusion | LiDAR + Camera for robust perception |
| Wind Simulation | Tested with simulated wind disturbances |
| ROS2 Jazzy | Latest ROS2 LTS version |

---

## 🧠 System Architecture
LiDAR + Camera
│
├──► SLAM Toolbox ──► Navigator Node
│         │                │
│    GPS Signal Lost       │
│         └──► SLAM Fallback Navigation
│
└──► Eagle Eye AI ──► Defect Detected
│
Report Generator
│
Engineering Summary PDF

---

## 🛠️ Hardware Configuration

| Component | Specification |
|---|---|
| UAV Platform | Quadrotor F450 |
| Flight Controller | ArduPilot |
| Companion Computer | Raspberry Pi 4 |
| LiDAR | RPLiDAR A2 |
| Camera | Intel RealSense D435 |
| Communication | MAVLink + ROS2 |

---

## 📊 Performance Results

| Metric | Value |
|---|---|
| Defect Detection Accuracy | 89% |
| GPS-Denied Navigation | Up to 50m range |
| Inspection Speed | 0.5 m/s along structure |
| Report Generation Time | < 30 seconds |
| Simulation Environment | Gazebo Harmonic |

---

## 🏗️ Inspection Capabilities
✅ Bridge deck crack detection
✅ Corrosion and rust identification
✅ Loose bolt detection
✅ Power tower structural assessment
✅ Automated defect mapping
✅ PDF report generation

---

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/yogesh031020/Project-CHRONOS-Infrastructure-Inspection.git
cd Project-CHRONOS-Infrastructure-Inspection

# Install dependencies
pip install -r requirements.txt
rosdep install --from-paths src --ignore-src -r -y

# Build
colcon build --packages-select chronos_inspector
source install/setup.bash

# Launch
ros2 launch chronos_inspector chronos_nav_launch.py
```

---

## 📁 Repository Structure
Project-CHRONOS-Infrastructure-Inspection/
├── src/
│   └── chronos_inspector/
│       ├── chronos_nav_node.py    ← Navigation
│       ├── eagle_eye_ai.py        ← AI Detection
│       ├── slam_fallback.py       ← GPS-denied nav
│       ├── report_generator.py    ← PDF reports
│       └── chronos_nav_launch.py  ← Launch file
├── worlds/
│   └── bridge_inspection.world    ← Gazebo world
├── config/
│   └── slam_params.yaml           ← SLAM config
├── requirements.txt
├── LICENSE
└── README.md

---

## 🔗 Related Projects

| Project | Description |
|---|---|
| [Trinity Stack](https://github.com/yogesh031020/Autonomous-UAV-Trinity-Stack) | Production UAV ecosystem |
| [Stealth Infiltration](https://github.com/yogesh031020/stealth-infiltration) | GPS-denied SLAM |
| [ICARUS UAV](https://github.com/yogesh031020/Project_ICARUS_UAV) | HALE UAV design |

---

## 👨✈️ Author

**Yogesh E S**
Autonomous Systems Engineer | 2+ Years UAV Experience
Novatech Robo Pvt Ltd, Bengaluru

[![GitHub](https://img.shields.io/badge/GitHub-yogesh031020-black)](https://github.com/yogesh031020)
[![Email](https://img.shields.io/badge/Email-Contact-red)](mailto:yogeshes376@gmail.com)

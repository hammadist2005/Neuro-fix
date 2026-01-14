# Neuro-fix
**AI-Powered Hardware Diagnostic Assistant**

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Development-success?style=flat-square)

---

### About The Project
Neuro-fix is a hardware-integrated AI assistant designed to bridge the gap between physical hardware components and software diagnostics.

Traditional hardware troubleshooting is manual and error-prone. Neuro-fix utilizes Computer Vision (OpenCV/YOLO) to identify hardware components in real-time and provides instant diagnostic data, pin configurations, and compatibility checks.

### Key Features
* **Real-Time Object Detection:** Instantly identifies hardware components (RAM, GPU, Microcontrollers) via camera feed.
* **Intelligent Diagnostics:** Overlays technical specifications and error logs directly onto the visual feed.
* **Hardware-Software Bridge:** Connects visual input with backend database queries to fetch datasheet information.
* **User Dashboard:** A clean Python-based interface for managing logs and history.

### Technical Stack
* **Core:** Python 3.10
* **Computer Vision:** OpenCV, YOLOv8
* **Interface:** Streamlit / Tkinter
* **Database:** MySQL / SQLite

---

### Getting Started

To run Neuro-fix locally on your machine:

1. **Clone the repository**
    ```bash
    git clone [https://github.com/hammadist2005/Neuro-fix.git](https://github.com/hammadist2005/Neuro-fix.git)
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Assistant**
    ```bash
    python main.py
    ```

---

### Screenshots
| Dashboard View | Real-Time Detection |
|:---:|:---:|
| ![Dashboard](https://via.placeholder.com/400x200?text=Dashboard+UI) | ![Detection](https://via.placeholder.com/400x200?text=YOLO+Detection) |

---

### Contact
**Hammad** - Software Engineering Undergraduate
Project Link: https://github.com/hammadist2005/Neuro-fix

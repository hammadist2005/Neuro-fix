# Neuro-fix: Automated Hardware Diagnostic System

Neuro-fix is an enterprise-grade AI agent designed to diagnose computer hardware issues in real-time. It pioneers a **Hybrid Edge-Cloud Architecture**, combining the low-latency performance of local computer vision with the reasoning capabilities of multimodal Cloud LLMs.

## Key Capabilities

### 1. Hybrid Vision Engine (Edge + Cloud)
* **Local Inference (Edge AI):** Utilizes **YOLOv8** running locally to provide immediate visual grounding and object detection with sub-50ms latency.
* **Cloud Reasoning (Deep Analysis):** Integrates **Google Gemini 1.5 Flash** to analyze high-resolution pixel data. This layer validates component identification (e.g., distinguishing specific RAM modules from generic electronics) and corrects local classification errors.

### 2. Automated Physical Damage Assessment
* **Defect Recognition:** The system autonomously scans hardware imagery for physical defects, including burn marks, circuit fractures, oxidation, or capacitor swelling.
* **Triage Protocol:**
    * **Healthy:** Validates component integrity for troubleshooting.
    * **Critical:** Triggers an immediate "Critical Damage" alert and routes the user to repair services if physical compromise is detected.

### 3. Neural Logic Core
* **High-Performance Inference:** Migrated from local RAG (Llama-3) to **Gemini 1.5 Flash**, reducing query response latency from minutes to under 1 second.
* **Generative Support:** Produces context-aware repair guides, installation procedures, and technical troubleshooting flows dynamically.

### 4. Real-Time Market Intelligence
* **Intent Recognition:** Automatically detects procurement intent within user queries (e.g., "replace," "upgrade," "buy").
* **Vendor Integration:** Scrapes live pricing and stock availability from local hardware vendors (e.g., CZone) to provide actionable purchasing data.

### 5. Safety & Compliance Layer
* **"Lethality Lock" Protocol:** A proprietary security layer that intercepts and sanitizes queries to prevent the generation of harmful, unethical, or dangerous content.

---

## Technical Specifications

* **Core Framework:** Python 3.10+
* **Frontend Interface:** Streamlit
* **LLM Runtime:** Google Gemini 1.5 Flash (via Google Generative AI SDK)
* **Object Detection:** Ultralytics YOLOv8 (Local Inference)
* **Image Processing:** OpenCV, PIL
* **Configuration Management:** Python-Dotenv
* **Data Aggregation:** BeautifulSoup4

---

## Installation & Configuration

### Prerequisites
* Python 3.10 or higher
* Valid Google Cloud API Key (Generative AI)

### Setup Instructions

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/hammadist2005/Neuro-fix.git](https://github.com/hammadist2005/Neuro-fix.git)
    cd Neuro-fix
    ```

2.  **Initialize Virtual Environment**
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**
    Create a `.env` file in the root directory and define your API credentials:
    ```ini
    GOOGLE_API_KEY=your_actual_api_key_here
    ```

---

## Operational Workflow

1.  **Initialize System**
    ```bash
    python -m streamlit run src/app.py
    ```

2.  **Diagnostic Process**
    * **Visual Grounding:** Initiate a hardware scan via the "Visual Grounding" interface. The system will detect the component and assess physical condition.
    * **Analysis:** Select the identified component to generate a troubleshooting guide.
    * **Market Inquiry:** Query pricing (e.g., "Price of 16GB RAM") to engage the Market Intelligence module.

---

## Disclaimer
This software is a prototype developed for educational and demonstration purposes. Critical hardware repairs should be performed by certified technicians.

*Neuro-fix v0.3 Enterprise Edition*

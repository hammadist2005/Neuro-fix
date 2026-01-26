# 🧠 Neuro-fix: AI Hardware Diagnostic Agent

**Neuro-fix** is an enterprise-grade AI agent designed to diagnose computer hardware issues in real-time. It pioneers a **Hybrid Edge-Cloud Architecture**, combining the speed of local computer vision with the reasoning power of multimodal Cloud LLMs.

## 🚀 Key Features

### 1. Hybrid Vision Engine (Edge + Cloud)
* **Local Layer (Edge AI):** Uses **YOLOv8** running locally to provide instant visual feedback (Red Bounding Box) with <50ms latency.
* **Cloud Layer (Deep Reasoning):** Uses **Google Gemini 1.5 Flash** to analyze pixel-level details. It correctly identifies specific components (e.g., "DDR4 RAM Stick" vs "Generic Electronics") and overrides local classification errors.

### 2. Deep Damage Detection
* **Automated Triage:** The system scans hardware images for physical defects such as **burn marks, cracked chips, rusted ports, or swollen capacitors**.
* **Smart Alerts:**
    * ✅ **Healthy:** displays a clean bill of health.
    * ⚠️ **Critical:** triggers a "Red Alert" and automatically suggests a repair shop if physical damage is detected.

### 3. Neural Logic Core (Hyper-Speed)
* Replaced the legacy local RAG (Llama-3) with **Gemini 1.5 Flash**, reducing query response time from **8 minutes to < 1 second**.
* Generates step-by-step repair guides, installation manuals, and troubleshooting flows instantly.

### 4. Real-Time Market Agent
* **Live Pricing:** Automatically detects intent when a user asks to "buy" or "replace" a part.
* **Web Scraper:** Connects to local vendors (e.g., CZone) to fetch real-time pricing and stock availability for the specific identified part.

### 5. "Lethality Lock" Safety Guard
* A custom security layer that intercepts and blocks dangerous, unethical, or malicious queries (e.g., explosives, bio-weapons) before they reach the core AI.

---

## 🛠️ Tech Stack

* **Core Logic:** Python 3.10+
* **Frontend:** Streamlit
* **LLM Engine:** Google Gemini 1.5 Flash (via Google Generative AI SDK)
* **Edge Vision:** Ultralytics YOLOv8 (Local Inference)
* **Computer Vision:** OpenCV, PIL
* **Security:** Python-Dotenv (Environment Variable Management)
* **Web Scraping:** BeautifulSoup4

---

## ⚙️ Installation

### Prerequisites
* Python 3.10 or higher
* A Google Cloud API Key (for Gemini 1.5 Flash)

### Setup Steps

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/hammadist2005/Neuro-fix.git](https://github.com/hammadist2005/Neuro-fix.git)
    cd Neuro-fix
    ```

2.  **Create a Virtual Environment**
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

4.  **Configure Security**
    Create a file named `.env` in the root folder (same place as `app.py`) and add your key:
    ```ini
    GOOGLE_API_KEY=your_actual_api_key_here
    ```
    *(Note: This file is git-ignored to protect your credentials.)*

---

## 🖥️ Usage

1.  **Launch the Agent**
    ```bash
    python -m streamlit run src/app.py
    ```

2.  **Workflow**
    * **Visual Grounding:** Click "Scan Hardware" to take a photo. The Hybrid Engine will instantly detect the object and scan for physical damage.
    * **Diagnosis:** If the part is healthy, click "Diagnose [Part Name]" to get an instant troubleshooting guide.
    * **Market Check:** Ask "Price of 16GB RAM" to trigger the Market Agent.
    * **Safety Test:** Try asking a dangerous question to see the "Lethality Lock" in action.

---

## 🛡️ Disclaimer
This tool is a prototype for educational and demonstration purposes. While it uses advanced AI for diagnosis, always consult a certified technician for critical hardware repairs.

*Neuro-fix v0.3 Enterprise Edition*

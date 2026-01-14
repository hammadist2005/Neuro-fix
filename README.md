# Neuro-fix

Neuro-fix is a local desktop application that assists hardware technicians in diagnosing component issues. It integrates computer vision for object detection with a Retrieval-Augmented Generation (RAG) system to query technical documentation.

The system allows a user to scan a hardware component via webcam, automatically identifies the part, and retrieves specific repair or troubleshooting steps from loaded PDF manuals.

## Project Status
**Current State:** Day 2 Development Snapshot (Prototype)
* **Object Detection:** Functional (YOLOv8)
* **RAG Pipeline:** Functional (Llama-3 + ChromaDB)
* **Interface:** Streamlit Web UI integrated with live diagnostics

## Architecture
The application consists of three main modules:
1.  **Vision Engine:** Uses a pre-trained YOLOv8 model to classify hardware components from a live video feed or captured image.
2.  **Reasoning Engine:** Uses a local Llama-3 LLM running via Ollama to process natural language queries.
3.  **Knowledge Base:** Uses ChromaDB to index technical manuals, allowing the LLM to retrieve accurate context before generating answers.

## Tech Stack
* **Language:** Python 3.10
* **Interface:** Streamlit
* **LLM Runtime:** Ollama
* **Model:** Llama-3 (8B)
* **Vector Store:** ChromaDB
* **Orchestration:** LangChain
* **Computer Vision:** Ultralytics YOLOv8

## Installation

### Prerequisites
* Python 3.10 or 3.11
* [Ollama](https://ollama.com) installed and running

### Setup
1.  **Clone the repository**
    ```bash
    git clone [https://github.com/hammadist2005/Neuro-fix.git](https://github.com/hammadist2005/Neuro-fix.git)
    cd Neuro-fix
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the AI Model**
    Ensure Ollama is running, then pull the required model:
    ```bash
    ollama run llama3
    ```

## Usage
1.  **Initialize the Database** (First run only)
    This processes the PDF manuals in the `data/` directory and creates the vector embeddings.
    ```bash
    python setup_db.py
    ```

2.  **Run the Application**
    ```bash
    python -m streamlit run src/app.py
    ```

3.  **Workflow**
    * Place the hardware component flat on a surface.
    * Capture an image using the "Vision Input" panel.
    * Once the object is detected, click "Diagnose" to generate a repair guide based on the manual.
#  SOLACE: Secure & Empathetic AI Therapeutic Companion

Solace is a local-first, privacy-focused artificial intelligence companion built to provide accessible, empathetic mental wellness support. Utilizing advanced language reasoning alongside integrated speech processing utilities, the application offers an organic, conversational voice-to-voice and text-to-text therapeutic workspace.

---

##  Key Features

* **Empathetic Dialogue Engine:** Configured with specialized system safety and clinical styling templates utilizing quantized GGUF parameters.
* **Seamless Audio Modality:** Integrated speech-to-text pipeline (transcription) combined with targeted text-to-speech cadence parsing (via `gTTS`).
* **Modular Software Design:** Strict architecture separation isolating the UI framework (`Gradio`), backend inference processing (`Llama-cpp`), and audio utilities into clean, distinct software layers.
* **Local-First Privacy:** System execution runs locally on native machine hardware to keep conversation telemetry safe and private.

---

##  Architecture Overview

The system abstracts logic across decoupled service handlers to ensure maximum scalability and simple framework substitutions:

```text
solace/
├── data/               # Automatic model hub ingestion target (.gitignore tracked)
├── app.py              # Pure Orchestrator & Gradio Interface Viewport
├── engine.py           # Core Inference Processing Layer (Llama-cpp Handler)
├── audio_utils.py      # Telemetry Layer (Speech Recognition & TTS Pipeline)
├── requirements.txt    # Frozen Project Environment Specifications
└── .gitignore          # Cache and massive weight tracking exclusions

```

---

##  Installation & Local Setup

### 1. Clone the Workspace

```bash
git clone [https://github.com/SID-SAN/Solace-AI](https://github.com/SID-SAN/Solace-AI)
cd Solace-AI
```

### 2. Configure Your Environment

It is highly recommended to isolate runtime dependencies using a virtual environment:

```bash
python -m venv venv

# Activate venv (Windows Command Prompt)
venv\Scripts\activate

# Activate venv (macOS/Linux)
source venv/bin/activate
```

### 3. Install Core Dependencies

Install tracking libraries optimized for local operations:

```bash
pip install -r requirements.txt
```

**Hardware Acceleration Tip (NVIDIA GPUs):** If running locally with CUDA acceleration (e.g., RTX Mobile/Desktop configurations), install `llama-cpp-python` explicitly to bind with compiler tools:
> ```bash
> pip uninstall llama-cpp-python -y
> set CMAKE_ARGS=-DGGML_CUDA=on
> pip install llama-cpp-python --verbose --no-cache-dir
> ```
> 
> 

### 4. Fire Up the Server

Execute the application entry script:

```bash
python app.py
```

*Note: On the initial execution, `SolaceEngine` will automatically pull down the targeted `Raya-therapist-model.Q4_K_M.gguf` file (~4GB) from the Hugging Face Hub straight into your local `data/` folder.*

---

##  Model Specifications & Attributions

* **Base Architecture:** Fine-tuned Therapist LLM optimized for conversational psychological counseling style rules.
* **Quantization format:** Q4_K_M GGUF via `mradermacher/Raya-therapist-model-GGUF`.


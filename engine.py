import os
from huggingface_hub import hf_hub_download
from llama_cpp import Llama

class SolaceEngine:
    def __init__(self):
        self.model_name = "mradermacher/Raya-therapist-model-GGUF"
        self.model_file = "Raya-therapist-model.Q4_K_M.gguf"
        self.model_path = os.path.join("data", self.model_file)
        
        os.makedirs("data", exist_ok=True)
        self._ensure_model_exists()
        self.llm = self._initialize_llm()
        
        self.system_prompt = (
            "You are a compassionate, empathetic, and professional therapist. "
            "Your goal is to respond supportively, clearly, and cheerfully. "
            "Do NOT include any reasoning, explanations, drafts, or thoughts. "
            "ONLY output the final response for the user, nothing else. "
            "The response should be concise, friendly, and ready to send as-is."
        )
        
        self.messages = [{"role": "system", "content": self.system_prompt}]

    def _ensure_model_exists(self):
        """Checks for the GGUF model locally; downloads it if missing."""
        if not os.path.exists(self.model_path):
            print(f"Downloading model {self.model_file}...")
            hf_hub_download(
                repo_id=self.model_name,
                filename=self.model_file,
                local_dir="data",
                resume_download=True
            )
        else:
            print("Model already exists in the data directory.")

    def _initialize_llm(self):
        """Safely boots up the Llama-cpp instance."""
        try:
            return Llama(
                model_path=self.model_path,
                n_ctx=16384, 
                n_gpu_layers=-1,
                verbose=False
            )
        except Exception as e:
            print(f"LLM initialization failed: {str(e)}")
            raise e

    def generate_response(self, user_message):
            """Appends user message to session context and returns LLM output."""
            self.messages.append({"role": "user", "content": user_message})
            
            output = self.llm.create_chat_completion(
                messages=self.messages,
                temperature=0.7,
                max_tokens=512
            )
            
            reply = output["choices"][0]["message"]["content"]
            self.messages.append({"role": "assistant", "content": reply})
            return reply

    def clear_history(self):
        """Resets the chat context back to the baseline system prompt."""
        self.messages = [{"role": "system", "content": self.system_prompt}]
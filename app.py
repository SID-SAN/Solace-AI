import gradio as gr
from engine import SolaceEngine
from audio_utils import transcribe_audio, generate_voice

print("Initializing Solace Engine...")
engine = SolaceEngine()

def chat_with_voice(user_text, audio_input, chat_history):

    if audio_input is not None:
        user_message = transcribe_audio(audio_input)
    else:
        user_message = user_text.strip() if user_text else ""

    if not user_message:
        return "", audio_input, None, chat_history

    reply = engine.generate_response(user_message)
    temp_audio_path = generate_voice(reply)

    chat_history.append({"role": "user", "content": user_message})
    chat_history.append({"role": "assistant", "content": reply})
    
    return "", None, temp_audio_path, chat_history

def reset_chat():
    """Resets UI components and model memory."""
    engine.clear_history()
    return [], "", None

with gr.Blocks(title="Solace AI") as demo:
    gr.Markdown("## 🧠 SOLACE: Your Therapeutic Companion")
    gr.Markdown("*A secure, private space to talk, listen, and find comfort.*")

    chatbot = gr.Chatbot(height=500, type="messages")
    
    with gr.Row():
        text_input = gr.Textbox(
            label="Type your thoughts here...", 
            placeholder="How are you feeling today?", 
            scale=4
        )
        audio_input = gr.Audio(
            type="filepath", 
            sources=["microphone"], 
            label="🎤 Speak your mind", 
            scale=2
        )
        
    output_audio = gr.Audio(label="🔊 Solace's Voice", autoplay=True)
    
    with gr.Row():
        clear_btn = gr.Button("Clear Conversation", variant="stop")

    text_input.submit(
        fn=chat_with_voice, 
        inputs=[text_input, audio_input, chatbot], 
        outputs=[text_input, audio_input, output_audio, chatbot]
    )
    
    audio_input.stop_recording(
        fn=chat_with_voice, 
        inputs=[text_input, audio_input, chatbot], 
        outputs=[text_input, audio_input, output_audio, chatbot]
    )
    
    clear_btn.click(
        fn=reset_chat, 
        inputs=None, 
        outputs=[chatbot, text_input, audio_input]
    )

if __name__ == "__main__":
    demo.launch(share=False, inbrowser=True)
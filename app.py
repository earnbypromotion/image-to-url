import streamlit as st
from gradio_client import Client, handle_file
import os

# Page configuration for Premium UI
st.set_page_config(
    page_title="Vortex AI | Premium Image-to-Video Engine", 
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom Premium Dark & Sleek CSS Styling
st.markdown("""
    <style>
    /* Main App Background & Text */
    .stApp {
        background: linear-gradient(135deg, #0f111a 0%, #1a1c29 100%);
        color: #e2e8f0;
    }
    
    /* Header Animation styling */
    .premium-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        background: linear-gradient(90deg, #8a2be2, #4a90e2, #00ffcc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }
    
    .premium-subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 15px;
        margin-bottom: 30px;
    }
    
    /* File Uploader styling custom fix */
    section[data-testid="stFileUploadDropzone"] {
        border: 2px dashed #4a90e2 !important;
        background-color: #1e293b !important;
        border-radius: 12px !important;
    }
    
    /* Luxury Button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%) !important;
        color: white !important;
        font-weight: bold !important;
        padding: 12px 24px !important;
        border-radius: 10px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4);
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.6);
        background: linear-gradient(90deg, #4f46e5 0%, #9333ea 100%) !important;
    }
    
    /* Custom Footer */
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #64748b;
        font-size: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Main Premium Header Display
st.markdown("<h1 class='premium-title'>VORTEX AI ENGINE</h1>", unsafe_allow_html=True)
st.markdown("<p class='premium-subtitle'>Next-Gen Cinematic Image-to-Video Synthesizer</p>", unsafe_allow_html=True)

# Sidebar setup for user's own token input
st.sidebar.header("🔑 Security Access")
st.sidebar.write("App chalane ke liye apna free Hugging Face token yahan enter karein.")
hf_token = st.sidebar.text_input("Enter Hugging Face Token (hf_...):", type="password")
st.sidebar.markdown("[Get Free Token Here](https://huggingface.co)")

# Layout split for input controls
with st.container():
    uploaded_file = st.file_uploader("✨ Drop your masterpiece image here...", type=["jpg", "png", "jpeg"])
    prompt = st.text_input("🔮 Cinematic Motion Directive (Prompt):", value="cinematic slow motion, photorealistic, 4k resolution, seamless movement")

# Execution Space
if uploaded_file and prompt:
    st.markdown("<h3 style='color: #a855f7; font-size:16px;'>📸 Source Visualization Preview:</h3>", unsafe_allow_html=True)
    st.image(uploaded_file, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("IGNITE VIDEO GENERATION 🚀"):
        if not hf_token:
            st.error("⚠️ Pehle Sidebar (left side menu) khol kar apna Hugging Face Token enter karein!")
        else:
            with st.spinner("Connecting to neural cloud mesh... Processing matrix frames (1-2 mins)"):
                try:
                    # Temporary file caching execution layer
                    temp_filename = f"temp_{uploaded_file.name}"
                    with open(temp_filename, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    # Verified active LTX provider pipeline integration 
                    client = Client("fffiloni/LTX-Video", hf_token=hf_token)
                    
                    result = client.predict(
                        input_image=handle_file(temp_filename),
                        prompt=prompt,
                        negative_prompt="worst quality, blurry, low resolution, static, glitch",
                        api_name="/predict"
                    )
                    
                    if result:
                        st.markdown("<h3 style='color: #00ffcc; font-size:16px;'>🎬 Synthesized Core Video:</h3>", unsafe_allow_html=True)
                        video_path = result if isinstance(result, str) else result
                        
                        if os.path.exists(video_path):
                            with open(video_path, "rb") as video_file:
                                st.video(video_file.read())
                                
                            st.success("Rendering Finished Successfully!")
                        else:
                            st.error("Error finalizing output streams into file buffer.")
                    
                    if os.path.exists(temp_filename):
                        os.remove(temp_filename)
                        
                except Exception as e:
                    st.error(f"Vortex Core Interruption: {e}")

# Footer Branding
st.markdown("<div class='footer'>Powered by Vortex AI Studio Engine • Studio Quality Free Tier</div>", unsafe_allow_html=True)

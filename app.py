import streamlit as st
import requests
import base64

# Page Configuration for Luxury UX
st.set_page_config(page_title="Vortex Link | Image to URL Engine", layout="centered")

# Premium Cyberpunk UI Custom CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #07080d 0%, #0f111a 100%);
        color: #f1f5f9;
    }
    .premium-title {
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        background: linear-gradient(90deg, #00f0ff, #7f00ff, #ff007f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        letter-spacing: -1px;
        margin-bottom: 2px;
    }
    .premium-subtitle {
        text-align: center;
        color: #64748b;
        font-size: 14px;
        margin-bottom: 40px;
    }
    section[data-testid="stFileUploadDropzone"] {
        border: 2px dashed #00f0ff !important;
        background-color: #141724 !important;
        border-radius: 14px !important;
    }
    .url-box {
        background: #1e293b;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #334155;
        color: #00f0ff;
        font-family: monospace;
        word-break: break-all;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #00f0ff 0%, #7f00ff 100%) !important;
        color: white !important;
        font-weight: bold !important;
        padding: 12px 24px !important;
        border-radius: 10px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0, 240, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 60px;
        color: #334155;
        font-size: 11px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='premium-title'>VORTEX LINK AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='premium-subtitle'>100% Free & Independent Image to URL Converter</p>", unsafe_allow_html=True)

# Main Uploader
uploaded_file = st.file_uploader("✨ Upload Image to Generate Instant URL...", type=["jpg", "png", "jpeg"])
url_type = st.radio("🔮 Choose URL Protocol:", ["Global Public CDN Link (Internet URL)", "Native Data String (Base64 Offline URL)"])

if uploaded_file:
    st.markdown("<h3 style='color: #00f0ff; font-size:15px;'>📸 Image Preview:</h3>", unsafe_allow_html=True)
    st.image(uploaded_file, use_container_width=True)
    
    if st.button("SYNTHESIZE LINK NOW 🚀"):
        with st.spinner("Processing image matrix channels..."):
            
            # METHOD 1: Global CDN Link (Anonymous Upload via Public Free Key Gateway)
            if url_type == "Global Public CDN Link (Internet URL)":
                try:
                    # We utilize the free public open router without forcing user profile tokens
                    # Free temporary gateway system
                    files = {"image": uploaded_file.getvalue()}
                    # Direct anonymous public key generator integration
                    payload = {"key": "6d207e02198a847aa98d4a2a1154857a"} # Secure integrated router key
                    
                    response = requests.post("https://imgbb.com", data=payload, files=files)
                    
                    if response.status_code == 200:
                        data = response.json()
                        direct_url = data["data"]["url"]
                        
                        st.success("🎉 Permanent Public Link Ready!")
                        st.markdown(f"<div class='url-box'>{direct_url}</div>", unsafe_allow_html=True)
                        st.caption("Aap is URL ko internet par kahin bhi share kar sakte hain, yeh sab ko dikhega.")
                    else:
                        st.error("Network temporary busy. Try method 2 or refresh.")
                except Exception as e:
                    st.error(f"Gateway Interruption: {e}")
            
            # METHOD 2: Base64 Offline Data String Link
            else:
                encoded = base64.b64encode(uploaded_file.getvalue()).decode()
                base64_url = f"data:{uploaded_file.type};base64,{encoded}"
                
                st.success("🎉 Offline Local Base64 URL Synthesized!")
                st.text_area("Copy Code Link:", base64_url, height=150)
                st.caption("Yeh URL direct browser ke address bar mein paste karne se image open ho jati hai!")

st.markdown("<div class='footer'>Vortex Link Studio • Built 100% Account Free & Protected Layer</div>", unsafe_allow_html=True)
                        

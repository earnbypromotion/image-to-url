import streamlit as st
import base64

# Premium Page Config
st.set_page_config(
    page_title="Vortex Core AI | Independent Video Engine", 
    layout="centered"
)

# Premium Cyberpunk UI Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #090a0f 0%, #121520 100%);
        color: #e2e8f0;
    }
    .premium-title {
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        background: linear-gradient(90deg, #ff007f, #7f00ff, #00f0ff);
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
        margin-bottom: 30px;
    }
    section[data-testid="stFileUploadDropzone"] {
        border: 2px dashed #7f00ff !important;
        background-color: #161925 !important;
        border-radius: 14px !important;
    }
    .footer {
        text-align: center;
        margin-top: 60px;
        color: #475569;
        font-size: 11px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='premium-title'>VORTEX CORE AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='premium-subtitle'>100% Independent Native Image-to-Video Synthesizer</p>", unsafe_allow_html=True)

# Main Inputs
uploaded_file = st.file_uploader("✨ Upload your image (No Token / No Key Required)...", type=["jpg", "png", "jpeg"])
motion_style = st.selectbox("🔮 Select Cinematic Motion Style:", ["Slow Zoom-In", "Cinematic Pan Right", "Ethereal Vertigo Effect", "Cyberpunk Glitch Transition"])

if uploaded_file:
    # Convert image to bytes to injection into JavaScript engine
    file_bytes = uploaded_file.read()
    b64_image = base64.b64encode(file_bytes).decode()
    
    st.markdown("<h3 style='color: #7f00ff; font-size:15px;'>📸 Source Visualization:</h3>", unsafe_allow_html=True)
    st.image(uploaded_file, use_container_width=True)
    
    # Process Button
    if st.button("SYNTHESIZE NATIVE VIDEO 🚀"):
        with st.spinner("Compiling native canvas frames... Rendering animation loops..."):
            
            # JavaScript Advanced Engine injected directly into the user browser 
            # This generates a real downloadable video loop without calling any external API!
            js_video_generator = f"""
            <div style="background: #161925; padding: 20px; border-radius: 14px; border: 1px solid #334155; text-align: center;">
                <h4 style="color: #00f0ff; margin-bottom: 15px; font-size: 16px;">🎬 Generated Core Stream Ready</h4>
                <canvas id="vortexCanvas" style="max-width: 100%; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.5); display: none;"></canvas>
                <video id="outputVideo" controls autoplay loop style="max-width: 100%; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.5);"></video>
                <br><br>
                <a id="downloadBtn" style="background: linear-gradient(90deg, #ff007f, #7f00ff); color: white; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: bold; display: inline-block; box-shadow: 0 4px 12px rgba(127,0,255,0.3);">Download Video 📥</a>
            </div>

            <script>
                var img = new Image();
                img.src = "data:image/jpeg;base64,{b64_image}";
                img.onload = function() {{
                    var canvas = document.getElementById('vortexCanvas');
                    var ctx = canvas.getContext('2d');
                    canvas.width = img.width > 800 ? 800 : img.width;
                    canvas.height = img.height > 600 ? 600 : img.height;
                    
                    var stream = canvas.captureStream(30); // 30 FPS native capture
                    var mediaRecorder = new MediaRecorder(stream, {{ mimeType: 'video/webm;codecs=vp9' }});
                    var chunks = [];
                    
                    mediaRecorder.ondataavailable = function(e) {{ chunks.push(e.data); }};
                    mediaRecorder.onstop = function() {{
                        var blob = new Blob(chunks, {{ 'type' : 'video/mp4' }});
                        var videoURL = URL.createObjectURL(blob);
                        document.getElementById('outputVideo').src = videoURL;
                        document.getElementById('downloadBtn').href = videoURL;
                        document.getElementById('downloadBtn').download = "vortex_motion_video.mp4";
                    }};
                    
                    mediaRecorder.start();
                    
                    var frame = 0;
                    var motionType = "{motion_style}";
                    
                    function animate() {{
                        ctx.clearRect(0, 0, canvas.width, canvas.height);
                        
                        if(motionType === "Slow Zoom-In") {{
                            var scale = 1 + (frame * 0.001);
                            var nw = canvas.width * scale;
                            var nh = canvas.height * scale;
                            var nx = (canvas.width - nw) / 2;
                            var ny = (canvas.height - nh) / 2;
                            ctx.drawImage(img, nx, ny, nw, nh);
                        }} else if(motionType === "Cinematic Pan Right") {{
                            var shift = (frame * 0.4) % (canvas.width * 0.05);
                            ctx.drawImage(img, -shift, 0, canvas.width + 50, canvas.height);
                        }} else if(motionType === "Ethereal Vertigo Effect") {{
                            ctx.save();
                            ctx.translate(canvas.width/2, canvas.height/2);
                            ctx.rotate(frame * 0.002);
                            var scale = 1 + Math.sin(frame * 0.02) * 0.03;
                            ctx.scale(scale, scale);
                            ctx.drawImage(img, -canvas.width/2, -canvas.height/2, canvas.width, canvas.height);
                            ctx.restore();
                        }} else {{
                            // Cyberpunk Glitch Style
                            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
                            if(frame % 15 === 0) {{
                                ctx.fillStyle = "rgba(0, 240, 255, 0.15)";
                                ctx.fillRect(Math.random()*canvas.width, 0, Math.random()*50, canvas.height);
                            }}
                        }}
                        
                        frame++;
                        if(frame < 90) {{ // 3 seconds video (30fps * 3 = 90 frames)
                            requestAnimationFrame(animate);
                        }} else {{
                            mediaRecorder.stop();
                        }}
                    }}
                    animate();
                }};
            </script>
            """
            st.components.v1.html(js_video_generator, height=480)

st.markdown("<div class='footer'>100% Secure & Private Native Processing Layer • No External API Connections</div>", unsafe_allow_html=True)
            

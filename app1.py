import streamlit as st
import joblib
import numpy as np

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Solar Power Generation Predictor",
    page_icon="☀️",
    layout="centered"
)

# ================== LOAD MODEL ==================
model = joblib.load(r"C:\Users\Shrushti\Desktop\solar1\solar_pipeline.pkl")

# ================== CUSTOM CSS ==================
st.markdown("""
<style>

/* Sky blue background */
.stApp {
    background: linear-gradient(to bottom, #87CEEB, #E0F6FF);
}

/* Main white card */
.block-container {
    background-color: rgba(255, 255, 255, 0.95);
    padding: 2.5rem 2rem;
    border-radius: 20px;
    box-shadow: 0px 8px 22px rgba(0, 0, 0, 0.18);
}

/* Title */
.app-title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #0D47A1;
    margin-bottom: 6px;
}

/* Subtitle */
.app-subtitle {
    text-align: center;
    font-size: 16px;
    color: #444;
    margin-bottom: 20px;
}

/* Result box */
.result-box {
    background-color: #e8f5e9;
    padding: 22px;
    border-radius: 14px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    color: #2e7d32;
    margin-top: 20px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
}

</style>
""", unsafe_allow_html=True)

# ================== HEADER ==================
st.markdown("<div class='app-title'>☀️ Solar Power Generation Predictor</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='app-subtitle'>Predict solar energy output using environmental conditions</div>",
    unsafe_allow_html=True
)

st.divider()

# ================== INPUT SECTION ==================
st.subheader("🔧 Enter Environmental Parameters")

col1, col2 = st.columns(2)

with col1:
    distance_to_solar_noon = st.slider(
        "Distance to Solar Noon (hours)",
        0.0, 6.0, 1.0, 0.1,
        help="Lower value means the sun is closer to its highest point."
    )

    average_wind_speed = st.slider(
        "Average Wind Speed (m/s)",
        0.0, 15.0, 3.0, 0.1,
        help="Moderate wind improves panel efficiency."
    )

    humidity = st.slider(
        "Humidity (%)",
        0.0, 100.0, 50.0, 1.0,
        help="Higher humidity reduces solar radiation."
    )

with col2:
    sky_cover = st.slider(
        "Sky Cover (%)",
        0.0, 100.0, 20.0, 1.0,
        help="Cloud coverage blocks sunlight."
    )

    average_pressure = st.slider(
        "Average Pressure (hPa)",
        900.0, 1100.0, 1013.0, 1.0,
        help="Normal atmospheric pressure supports stable weather."
    )

st.divider()

# ================== PREDICTION ==================
if st.button("🚀 Predict Power Generation", use_container_width=True):

    input_features = np.array([[ 
        distance_to_solar_noon,
        average_wind_speed,
        humidity,
        sky_cover,
        average_pressure
    ]])

    prediction = model.predict(input_features)[0]

    st.markdown(
        f"""
        <div class='result-box'>
            🔋 Predicted Solar Power Generation <br><br>
            {prediction:.2f} kWh
        </div>
        """,
        unsafe_allow_html=True
    )

# ================== FOOTER ==================
st.write("")
st.caption("📊 Machine Learning Model | Streamlit Dashboard")

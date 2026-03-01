import streamlit as st

st.set_page_config(
    page_title="C&A Presence Pro",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- SESSION NAVIGATION ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- LUXURY CSS ----------------
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background-color: #F5EFE4;
}

header {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stSidebar"] {display: none;}

* {
    font-family: 'Georgia', serif;
    color: #1C1C1C;
}

/* Navbar */
.navbar {
    position: sticky;
    top: 0;
    background-color: #F5EFE4;
    padding: 18px 0;
    border-bottom: 1px solid #E2D6C2;
    text-align: center;
    font-weight: 600;
    letter-spacing: 1px;
}

/* Hero */
.main-title {
    font-size: 64px;
    font-weight: 900;
    text-align: center;
    margin-top: 80px;
}

.sub-title {
    font-size: 22px;
    text-align: center;
    margin-bottom: 25px;
    color: #B08A2E;
    font-weight: 700;
}

/* Button Styling */
div.stButton > button {
    background-color: black;
    color: white;
    padding: 14px 36px;
    border-radius: 6px;
    font-weight: 600;
    border: none;
}

div.stButton > button:hover {
    background-color: #333;
    color: white;
}

/* Section Title */
.section-title {
    font-size: 38px;
    font-weight: 800;
    margin-top: 90px;
    margin-bottom: 30px;
    text-align: center;
}

/* Cards */
.card {
    background-color: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.05);
    margin-bottom: 25px;
}

.contact-box {
    text-align: center;
    font-size: 20px;
    line-height: 2;
}

</style>
""", unsafe_allow_html=True)

# ================= HOME PAGE =================
if st.session_state.page == "home":

    st.markdown('<div class="navbar">C&A Presence Pro | Premium Google Maps & Local SEO Agency</div>', unsafe_allow_html=True)

    # Hero
    st.markdown('<div class="main-title">C&A Presence Pro</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Strategic Google Visibility for Local Businesses</div>', unsafe_allow_html=True)

    # Centered Button
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Read Our Insights", use_container_width=True):
            st.session_state.page = "blog"

    # Services
    st.markdown('<div class="section-title">Our Services</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card"><h3>Google Business Profile Optimization</h3>Complete listing setup, keyword placement & ranking strategy.</div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h3>Local SEO Strategy</h3>Structured city-level SEO to dominate search results.</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h3>Google Maps Top 3 Ranking</h3>Advanced optimization for map visibility & calls.</div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h3>Review & Reputation System</h3>Strategic review growth & trust-building framework.</div>', unsafe_allow_html=True)

    # Why Choose Us
    st.markdown('<div class="section-title">Why Choose Us</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    ✔ Google Certified Expertise <br><br>
    ✔ Strong Artificial Engineering Background<br><br>
    ✔ Deep Digital Market Understanding<br><br>
    ✔ Passionate About Scaling Local Businesses
    </div>
    """, unsafe_allow_html=True)

    # Founders
    st.markdown('<div class="section-title">Meet Founders</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/chaitanya_new.jpg", width=220)
        st.markdown("""
        **Chaitanya**  
        Strategic Growth Director  

        🎓 AIR under 1000 JEE Advance  
        📜 Google Business Optimization Certified  
        📊 Specialization: Data Analytics  
        💡 Expertise: Consumer Psychology
        """)

    with col2:
        st.image("images/Ansh.jpg", width=220)
        st.markdown("""
        **Ansh**  
        SEO Specialist  

        🎓 Google Certified Digital Marketing Expert  
        🚀 Focus: From Local to Brand Growth
        """)

    # Contact
    st.markdown('<div class="section-title">Contact Us</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card contact-box">
    📍 Serving: Ambala & Yamunanagar<br><br>
    📞 <a href="tel:+918307762064">Call Ansh - 8307762064</a><br>
    📞 <a href="tel:+917082429133">Call Chaitanya - 7082429133</a><br><br>
    💬 WhatsApp Available for Strategy Consultation
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<center>© 2026 C&A Presence Pro | All Rights Reserved</center>", unsafe_allow_html=True)


# ================= BLOG PAGE =================
elif st.session_state.page == "blog":

    st.markdown("<h1 style='text-align:center;'>Our Insights</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("← Back to Home"):
            st.session_state.page = "home"

    st.markdown("""
    <div class="card">
    <h3>How Local Businesses Rank on Google</h3>
    Discover advanced SEO strategies that increase map visibility,
    generate calls and dominate local search results.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>Google Business Profile Optimization Guide</h3>
    Learn how to structure your listing to attract more high-intent customers.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>SEO vs Google Ads – Strategic Comparison</h3>
    Understand when to invest in long-term SEO and when ads give faster ROI.
    </div>
    """, unsafe_allow_html=True)

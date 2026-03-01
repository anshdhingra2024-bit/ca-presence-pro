import streamlit as st

st.set_page_config(
    page_title="C&A Presence Pro",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LUXURY CSS ----------------
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background-color: #F5EFE4;
}

header {visibility: hidden;}
footer {visibility: hidden;}

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
    font-size: 72px;
    font-weight: 900;
    text-align: center;
    margin-top: 90px;
}

.sub-title {
    font-size: 24px;
    text-align: center;
    margin-bottom: 30px;
    color: #B08A2E;
    font-weight: 700;
}

/* Buttons */
.cta-wrapper {
    text-align: center;
    margin-top: 30px;
}

.cta-btn {
    display: inline-block;
    margin: 8px;
    padding: 14px 40px;
    background-color: black;
    color: white !important;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
}

.cta-btn:hover {
    background-color: #333;
}

/* Section Title */
.section-title {
    font-size: 40px;
    font-weight: 800;
    margin-top: 100px;
    margin-bottom: 30px;
    text-align: center;
}

/* Cards */
.card {
    background-color: white;
    padding: 35px;
    border-radius: 18px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.05);
    margin-bottom: 30px;
}

/* Founder */
.founder-img {
    width: 220px;
    height: 220px;
    object-fit: cover;
    border-radius: 50%;
    margin-bottom: 15px;
}

.contact-box {
    text-align: center;
    font-size: 20px;
    line-height: 2;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ----------------
st.markdown('<div class="navbar">C&A Presence Pro | Premium Google Maps & Local SEO Agency</div>', unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown('<div class="main-title">C&A Presence Pro</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Strategic Google Visibility for Local Businesses</div>', unsafe_allow_html=True)


# ---------------- SERVICES ----------------
st.markdown('<div class="section-title">Our Services</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><h3>Google Business Profile Optimization</h3>Complete listing setup, keyword placement & ranking strategy.</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Local SEO Strategy</h3>Structured city-level SEO to dominate search results.</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>Google Maps Top 3 Ranking</h3>Advanced optimization for map visibility & calls.</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Review & Reputation System</h3>Strategic review growth & trust-building framework.</div>', unsafe_allow_html=True)

# ---------------- WHY CHOOSE US ----------------
st.markdown('<div class="section-title">Why Choose Us</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
✔ Google Certified Expertise <br><br>
✔ Strong Artificial Engineering Background<br><br>
✔ Understand Digital Market  <br><br>
✔ Passionate About Helping Local Businesses Scale Digitally
</div>
""", unsafe_allow_html=True)

# ---------------- OPTIMIZATION IMPACT ----------------
st.markdown('<div class="section-title">What Changes After Optimization?</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
• Higher Google Maps Visibility<br>
• Increased Calls & Direction Requests<br>
• Better Profile Authority & Engagement<br>
• Structured Review Growth<br>
• Local to Brand
</div>
""", unsafe_allow_html=True)

# ---------------- FOUNDERS ----------------
st.markdown('<div class="section-title">Meet Founders</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image("images/chaitanya_new.jpg",width=200)
    st.markdown("""
    **Chaitanya**  
    Strategic Growth Director  

    🎓 AIR under 1000 Jee Advance  
    📜 Google Business Optimization Certified  
    📊 Specialization: Data Analytics 
    💡 Experience: Understanding Psychology
    """)

with col2:
    st.image("images/Ansh.jpg", width=250)
    st.markdown("""
    **Ansh**  
     SEO Specialist  

    🎓 passionate Problem Solver 
    📜 Google Certified Digital Marketer Expert 
    🚀 Focus: From Local to Brand
    """)
# ---------------- CERTIFICATIONS ----------------
st.markdown("<div class='section-title'>Our Certifications</div>", unsafe_allow_html=True)

st.markdown("### 🎓 Ansh Certifications")
cert_col1, cert_col2 = st.columns(2)

with cert_col1:
    st.image("images/ansh_google_ads_search.png", width=500)
st.markdown("[🔗 Verify Certificate](https://skillshop.credential.net/78dc7f4a-bff3-4c10-b144-311214947346#acc.B8MuhEXc)")
with cert_col2:
    st.image("images/ansh_cert2.png", width=500)

st.markdown("[🔗 Verify Certificate](https://skillshop.credential.net/ae24f46b-5d3f-4c87-aa67-7c1d1d46ddb0?utm_source=whatsapp&utm_medium=social)")

# ---------------- CONTACT ----------------
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

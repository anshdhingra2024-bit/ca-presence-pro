import streamlit as st

st.set_page_config(page_title="Insights | Elevate Digital", layout="wide")

# Hide default UI
st.markdown("""
<style>
header {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stSidebar"] {display: none;}

.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: gray;
    margin-bottom: 40px;
}

.blog-card {
    background-color: #111111;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 25px;
    transition: 0.3s;
}

.blog-card:hover {
    transform: scale(1.02);
    background-color: #1a1a1a;
}

.blog-title {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 10px;
}

.blog-desc {
    font-size: 15px;
    color: #cccccc;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Our Insights</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Expert Knowledge on Google Visibility & Local Growth</div>', unsafe_allow_html=True)

# Blog Posts
st.markdown("""
<div class="blog-card">
    <div class="blog-title">How Local Businesses Can Rank on Google in 2026</div>
    <div class="blog-desc">
    Discover proven SEO strategies that help local businesses dominate search results
    and generate consistent leads without wasting ad budget.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="blog-card">
    <div class="blog-title">Google My Business Optimization Guide</div>
    <div class="blog-desc">
    Learn how to fully optimize your Google Business Profile to attract more customers
    and increase trust in your brand.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="blog-card">
    <div class="blog-title">SEO vs Google Ads – What Should You Choose?</div>
    <div class="blog-desc">
    Understand when to invest in SEO and when paid ads are the smarter strategy
    for faster growth.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("© 2026 Elevate Digital | All Rights Reserved")

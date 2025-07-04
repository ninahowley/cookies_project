import streamlit as st
import db_methods as db
import methods as m
import pandas as pd

st.html("""<style>
[data-testid="stSidebar"]> div:first-child{
background-image: url("https://thumbs.dreamstime.com/b/chocolate-chip-cookies-crumbs-forming-vertical-frame-white-background-scattered-create-visually-appealing-clean-surface-352442146.jpg");
background-size: cover;
}
</style>""")

st.header(":cookie: Share Your Thoughts")

st.subheader("We appreciate your feedback!")
st.link_button("Super Easy Feedback Form", "https://forms.gle/fAFRDY1KVoqiAGceA")

import streamlit as st

def initialize_session_state():
    if 'image' not in st.session_state:
        st.session_state.image = None
        st.session_state.processed_image = None
    if 'mm_per_pixel' not in st.session_state:
        st.session_state.mm_per_pixel = 95.5 / 576

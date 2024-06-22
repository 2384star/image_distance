import streamlit as st
from streamlit_drawable_canvas import st_canvas

def display_image():
    st.markdown(
        """
        <style>
        .image-container {
            display: flex;
            justify-content: center;
        }
        .canvas-container {
            display: flex;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container():
        st.image(st.session_state.image, caption="Uploaded Image.", use_column_width=False)
        width, height = st.session_state.image.size
        st.write(f"이미지 크기: {width} x {height} 픽셀")
        st.write("2개의 점을 선택해주세요.")

def display_canvas(image):
    canvas_width, canvas_height = image.size
    with st.container():
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=2,
            stroke_color="#000",
            background_image=image,
            update_streamlit=True,
            height=canvas_height,
            width=canvas_width,
            drawing_mode="point",
            point_display_radius=3,
            key="canvas",
            display_toolbar=True,
        )
    return canvas_result

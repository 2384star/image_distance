import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import io
from distance import calculate_distances, calculate_real_distances
from image_processing import process_image

from session_state import initialize_session_state
from UI_config import display_image, display_canvas

# 페이지 레이아웃 설정
st.set_page_config(layout="wide")

# Streamlit 제목 설정
st.title("이미지 거리 구하기")

# 이미지 파일 업로드 및 안내
uploaded_file = st.file_uploader("이미지를 선택해주세요", type=["jpg", "jpeg", "png"], key="unique_key")

# 세션 상태 초기화
initialize_session_state()

# 파일 업로드 처리
if uploaded_file is not None:
    if st.button("이미지 불러오기"):
        st.session_state.image = Image.open(uploaded_file)

# 이미지를 불러오거나 이전에 불러온 이미지가 있을 때 표시
if st.session_state.image is not None:
    display_image()
    canvas_result = display_canvas(st.session_state.image)

    if canvas_result.json_data is not None:
        points = canvas_result.json_data["objects"]
        if len(points) == 2:
            x1, y1 = points[0]["left"], points[0]["top"]
            x2, y2 = points[1]["left"], points[1]["top"]

            distance, x_distance, y_distance = calculate_distances(x1, y1, x2, y2)
            real_distance, real_x_distance, real_y_distance = calculate_real_distances(distance, x_distance, y_distance, st.session_state.mm_per_pixel)

            st.write(f"두 점 사이의 거리: {distance:.2f} 픽셀")
            st.write(f"x좌표 거리: {x_distance:.2f} 픽셀")
            st.write(f"y좌표 거리: {y_distance:.2f} 픽셀")

            if st.button("실제 크기로 변환"):
                st.write("### 변환 전")
                data_before = {
                    "두 점 사이의 거리": f"{distance:.2f} 픽셀",
                    "x좌표 거리": f"{x_distance:.2f} 픽셀",
                    "y좌표 거리": f"{y_distance:.2f} 픽셀"
                }
                st.table(data_before)

                st.write("### 변환 후")
                data_after = {
                    "두 점 사이의 거리": f"{real_distance:.2f} mm",
                    "x좌표 거리": f"{real_x_distance:.2f} mm",
                    "y좌표 거리": f"{real_y_distance:.2f} mm"
                }
                st.table(data_after)

                processed_image = process_image(st.session_state.image, x1, y1, x2, y2, real_distance)
                st.session_state.processed_image = processed_image

                st.image(processed_image, caption="Processed Image.", use_column_width=False)

                download = io.BytesIO()
                processed_image.save(download, format="PNG")
                download.seek(0)
                st.download_button(
                    label="이미지 다운로드",
                    data=download,
                    file_name="processed_image.png",
                    mime="image/png"
                )

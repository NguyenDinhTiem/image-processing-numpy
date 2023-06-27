import streamlit as st
import numpy as np
import cv2
from rembg import remove
import os
def main():
    st.title("Siêu Ứng Dụng Xịn Nhất Thế Giới 😍")
    # Lựa chọn chức năng biến đổi
    st.sidebar.subheader("Chức năng biến đổi")
    transformation = st.sidebar.selectbox(
        "Chọn chức năng",
        ("Xóa nền", "Phóng to", "Thu nhỏ", "Lật ảnh ngang", "Lật ảnh dọc")
    )
    # Tải lên hình ảnh
    uploaded_file = st.file_uploader("Chọn một hình ảnh", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Đọc hình ảnh và hiển thị
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        st.image(image, caption='Hình ảnh đã tải lên')

        # Áp dụng chức năng biến đổi
        transformed_image = apply_transformation(image, transformation)

        # Hiển thị hình ảnh sau khi biến đổi
        st.subheader("Hình ảnh sau khi biến đổi")
        st.image(transformed_image, caption='Hình ảnh đã biến đổi')

        # Lưu kết quả thành file ảnh
        save_path = "result.png"
     
        save_image(transformation, transformed_image, save_path)
        
        # Tải xuống file ảnh
        with open(save_path, "rb") as file:
            btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="result.png",
                    mime="image/png"
                )
def apply_transformation(image, transformation):
    if transformation == "Xóa nền":
        transformed_image = remove(image)
    elif transformation == "Phóng to":
        transformed_image = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    elif transformation == "Thu nhỏ":
        fxy = st.slider('Lựa chọn mức thu nhỏ?', 0.0, 1.0, 0.25)
        transformed_image = cv2.resize(image, None, fx=fxy, fy=fxy, interpolation=cv2.INTER_LINEAR)
    elif transformation == "Lật ảnh ngang":
        transformed_image = cv2.flip(image, 1)
    elif transformation == "Lật ảnh dọc":
        transformed_image = cv2.flip(image, 0)
    else:
        transformed_image = image
    return transformed_image

def save_image(transformation, image, save_path):
    if transformation == "Xóa nền":
        cv2.imwrite(save_path, image)
    else:
        cv2.imwrite(save_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

if __name__ == '__main__':
    main()

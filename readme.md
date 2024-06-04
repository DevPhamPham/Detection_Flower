# Phát hiện Hoa Mai và Hoa Đào sử dụng YOLOv8

Dự án này sử dụng YOLOv8, một mô hình phát hiện vật thể mạnh mẽ và nhanh chóng, để huấn luyện một hệ thống có khả năng nhận diện và phân biệt giữa hoa mai và hoa đào trong ảnh.

## Tổng quan

* **Mục tiêu:** Xây dựng một mô hình phát hiện vật thể chính xác, có thể xác định vị trí và phân loại hoa mai và hoa đào trong các điều kiện khác nhau.
* **Mô hình:** YOLOv8 (phiên bản cụ thể: YOLOv8s)
* **Dữ liệu:** Tập dữ liệu ảnh hoa mai và hoa đào được chú thích cẩn thận (định dạng YOLO).
* **Ngôn ngữ:** Python
* **Framework:** Ultralytics YOLOv8

## Cài đặt

1. **Clone dự án:**
   ```bash
   git clone https://github.com/DevPhamPham/Detection_Flower.git
   cd Detection_Flower
   ```

2. **Tạo môi trường ảo (khuyến nghị):**
   ```bash
      python -m venv venv
      source venv/bin/activate  # Trên Windows: venv\Scripts\activate
   ```

2. **Cài đặt các thư viện cần thiết:**
   ```bash
      pip install -r requirements.txt
   ```

## Config

- config.yaml
- google_colab_config.yaml for gg colab

## Video test

[Video test](predict.mp4)

<video width="auto" height="auto" controls>
  <source src="predict.mp4" type="video/mp4">
  Trình duyệt của bạn không hỗ trợ thẻ video.
</video>

## Video Predict

[Video Predict](predict_out.mp4.mp4)

<video width="auto" height="auto" controls>
  <source src="predict_out.mp4" type="video/mp4">
  Trình duyệt của bạn không hỗ trợ thẻ video.
</video>

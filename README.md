I made a CNN model to check the handwritten digit
# Digit Classification

## Giới thiệu
Dự án Digit Classification là một ứng dụng web cho phép người dùng tải lên hình ảnh của một chữ số và nhận dự đoán về chữ số đó bằng cách sử dụng mô hình học sâu. Ứng dụng được xây dựng bằng Flask và sử dụng TensorFlow để thực hiện dự đoán.

## Công nghệ sử dụng
- **Flask**: Framework web cho Python.
- **TensorFlow**: Thư viện học sâu để xây dựng và triển khai mô hình học máy.
- **OpenCV**: Thư viện xử lý hình ảnh.
- **Bootstrap**: Thư viện CSS để tạo giao diện người dùng đẹp mắt.

## Cài đặt

### Yêu cầu
- Python 3.x
- pip (trình quản lý gói Python)

### Cài đặt các thư viện cần thiết
Bạn có thể cài đặt các thư viện cần thiết bằng cách sử dụng pip. Chạy lệnh sau trong terminal:
```bash
pip install flask tensorflow opencv-python
```

### Tải mô hình
Đảm bảo rằng bạn đã có mô hình `mnist_model.h5` trong thư mục gốc của dự án.

## Chạy ứng dụng
Để chạy ứng dụng, bạn có thể sử dụng lệnh sau:

```bash
python app.py
```

Sau khi ứng dụng chạy, bạn có thể truy cập vào địa chỉ `http://127.0.0.1:5000/` trên trình duyệt web của mình.

## Sử dụng
1. Tải lên một hình ảnh của một chữ số bằng cách nhấn nút "Upload".
2. Ứng dụng sẽ hiển thị hình ảnh đã tải lên và dự đoán chữ số tương ứng.

## Ghi chú
- Đảm bảo rằng hình ảnh tải lên có định dạng phù hợp (PNG, JPG).
- Ứng dụng có tính năng xóa canvas để người dùng có thể vẽ lại nếu cần.

## Tài liệu tham khảo
- [Flask Documentation](https://flask.palletsprojects.com/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [OpenCV Documentation](https://opencv.org/)

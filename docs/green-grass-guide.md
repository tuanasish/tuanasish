# 🌿 Hướng dẫn sử dụng Tool "Làm Xanh Cỏ" (Green Grass)

Tool này giúp anh tự động tạo các commit trong quá khứ để lấp đầy các ô trống trên biểu đồ đóng góp (Contribution Graph) của GitHub.

## ⚠️ Lưu ý quan trọng
- GitHub có thể phát hiện nếu anh lạm dụng quá nhiều (VD: 1000 commits/ngày).
- Nên dùng ở mức độ vừa phải (1-5 commits/ngày) để trông tự nhiên nhất.
- Tool này tạo commit bằng cách thay đổi file `CONTRIBUTION.md`.

## 🛠️ Cách sử dụng

### Bước 1: Cài đặt Python
Đảm bảo máy anh đã cài Python. Anh có thể kiểm tra bằng lệnh:
```bash
python --version
```

### Bước 2: Chạy Tool
Mở terminal (PowerShell hoặc CMD) tại thư mục dự án và chạy:
```bash
python tools/green_grass.py
```

### Bước 3: Đẩy lên GitHub
Sau khi script chạy xong, các ô cỏ sẽ chỉ xanh trên máy anh. Để hiện trên GitHub, anh cần push:
```bash
git push origin main --force
```

## ⚙️ Tùy chỉnh (Chỉnh sửa file `green_grass.py`)
Anh có thể mở file `tools/green_grass.py` và sửa các dòng:
- `days=30`: Số ngày anh muốn phủ xanh (VD: 365 để phủ cả năm).
- `commits_per_day_range=(1, 5)`: Số lượng commit ngẫu nhiên mỗi ngày.

Chúc anh có một chiếc đồ thị "xanh mướt"! 🥂✨

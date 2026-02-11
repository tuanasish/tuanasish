# 🏆 Hướng dẫn "Cày" Trophy & Xanh cỏ GitHub

Để có nhiều cúp hạng cao (S, SS) và bảng đóng góp (contributions) luôn xanh mướt, cách nhanh nhất là tạo các **commit tự động**.

## ⚠️ Lưu ý quan trọng
- Cách này chỉ giúp Profile trông "đẹp" và "chăm chỉ" hơn về mặt số liệu.
- Các nhà tuyển dụng kỹ tính có thể xem lịch sử commit và phát hiện ra đây là commit ảo. 
- Chỉ nên dùng để trang trí Profile cho vui!

---

## Cách thực hiện (Dùng Script)

Em đã viết cho anh một đoạn script nhỏ (Batch file cho Windows). Anh chỉ cần chạy nó, nó sẽ tự tạo ra 100-200 commit "nháp" trong vài giây.

### Bước 1: Tạo file script
Trong thư mục `profile readme`, tạo một file tên là `farm.bat` và dán nội dung này vào:

```batch
@echo off
set /p count="Nhap so luong commit muon cay (vi du 100): "
for /l %%x in (1, 1, %count%) do (
   echo commit so %%x >> farm_log.txt
   git add farm_log.txt
   git commit -m "chore: updating logs %%x"
)
echo --- Xong! Gio hay push len Github ---
pause
```

### Bước 2: Chạy và Push
1. Click đúp vào file `farm.bat`.
2. Nhập số lượng commit bạn muốn (đừng tham quá, mỗi lần tầm 50-100 là đẹp).
3. Sau khi chạy xong, anh gõ lệnh này ở terminal để đẩy lên:
   ```bash
   git push origin main
   ```

### Bước 3: Kiểm tra cúp
- Đợi 5-10 phút để GitHub cập nhật chỉ số.
- Quay lại trang cá nhân, anh sẽ thấy cúp **Commits** của mình có thể nhảy từ Rank C lên Rank A hoặc S ngay lập tức!

---
**Tip:** Nếu muốn "xanh cỏ" cả năm trong quá khứ, người ta thường dùng các tool như `git-faker`, nhưng nó hơi phức tạp. Cách trên là đơn giản và an toàn nhất để tăng số lượng commit!

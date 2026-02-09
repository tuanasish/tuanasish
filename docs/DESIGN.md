# 🎨 DESIGN: Professional Github Profile README - Vu Anh Tuan

**Ngày tạo:** 2026-02-09
**Dựa trên:** [/BRIEF.md](file:///C:/Users/Vu%20Anh%20Tuan/Downloads/CanDeleted/profile%20readme/docs/BRIEF.md)

---

## 1. Cấu Trúc Dữ Liệu & Nội Dung (Cấu trúc Table)

README sẽ được tổ chức theo các khối "Sheet" (section) chuyên biệt để dễ quản lý và hiển thị đẹp trên cả di động/máy tính.

### 📦 SƠ ĐỒ LƯU TRỮ (Sections):
- **Hero Unit:** Title, Banner, typing animation.
- **Bio Data:** text-based introduction.
- **Skills Matrix:** Grid display of technology icons.
- **Portfolio Highlights:** Project cards with image thumbnails.
- **Dynamic Stats:** Iframe-like images for live GitHub activity.

---

## 2. Thiết Kế Màn Hình (Layout Flow)

Chúng ta sẽ sử dụng hệ thống bảng (Table) của GitHub Markdown để tạo lưới (Grid) thay vì dùng CSS Grid (do README bị giới hạn CSS).

### 📱 DANH SÁCH KHỐI GIAO DIỆN:

| # | Khối | Mô tả | Công nghệ |
|---|-----|----------|-------------|
| 1 | **Banner Header** | Hình ảnh gradient nghệ thuật với tên | `generate_image` |
| 2 | **Intro Typing** | "Hi, I'm a <Fullstack Dev>" | Markdown + Badges |
| 3 | **Tech Grid** | Lưới các icon bo góc, màu sắc | SimpleIcons SVG |
| 4 | **Project Card** | Card ngang dành cho dự án Chợ Quê | GitHub Markdown Table |
| 5 | **Stats Cards** | Thẻ thống kê commit, ngôn ngữ | Github README Stats |

---

## 3. Luồng Hoạt Động (User Journey)

### 🚶 HÀNH TRÌNH NGƯỜI XEM (Visitor Journey):
1. **Ấn tượng đầu:** Thấy Banner rực rỡ và typing animation → Định danh được ngay level Fullstack.
2. **Kỹ năng:** Lướt qua grid Icons → Thấy sự đa dạng (Flutter, Next.js, Supabase).
3. **Thực chứng:** Dừng lại ở section dự án "Chợ Quê" → Thấy hình ảnh app thực tế.
4. **Kết nối:** Bấm vào các Social Badges ở cuối trang để liên hệ.

---

## 4. Quy Tắc Kiểm Tra (Acceptance Criteria)

### 📋 CHECKLIST: README Hoàn Thiện

✅ **Về Hiển Thị:**
- [ ] Banner không bị méo/vỡ trên màn hình rộng.
- [ ] Các icon công nghệ thẳng hàng (Grid 4xN).
- [ ] Dark mode & Light mode đều dễ đọc (Sử dụng SVG trong suốt).

✅ **Về Kỹ Thuật:**
- [ ] Toàn bộ link (Social, Repo Chợ Quê) đều dẫn đến trang đích đúng.
- [ ] Stats Cards hiển thị dữ liệu live của tài khoản `@tuanasish`.
- [ ] Tốc độ load trang không bị chậm do ảnh quá lớn (Banner cần tối ưu dung lượng).

✅ **Về Nội Dung:**
- [ ] Bio súc tích, chuyên nghiệp.
- [ ] Làm bật được vai trò "Full-stack Developer".

---

## 🧪 TEST CASES: Kiểm Tra Cuối Cùng

- **TC-01:** Mở trên Mobile (App GitHub) -> Kiểm tra xem Table có bị scroll ngang quá nhiều không.
- **TC-02:** Click vào Icon LinkedIn -> Verify profile cá nhân hiện ra.
- **TC-03:** Đổi theme trình duyệt sang Dark Mode -> Verify stats cards tự động đổi màu.

---
*Tạo bởi Minh - Kiến trúc sư giải pháp (AWF 2.1)*

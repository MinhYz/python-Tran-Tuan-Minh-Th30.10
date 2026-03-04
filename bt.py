 import os

class ThiSinh:
    """Lớp đại diện cho một thí sinh"""
    def __init__(self, ma_hs, ho_ten, khoi_thi, diem_thi):
        self.ma_hs = ma_hs
        self.ho_ten = ho_ten
        self.khoi_thi = khoi_thi.upper()
        self.diem_thi = diem_thi
        # Tự động tính toán kết quả: Đậu nếu điểm từ 15 trở lên
        self.ket_qua = "Đậu" if diem_thi >= 15 else "Trượt"

    def __str__(self):
        return f"| {self.ma_hs:<10} | {self.ho_ten:<20} | {self.khoi_thi:<8} | {self.diem_thi:<8} | {self.ket_qua:<8} |"

class HeThongTuyenSinh:
    """Lớp điều khiển các chức năng quản lý"""
    def __init__(self):
        self.danh_sach = []

    # 1. Thêm thí sinh (Yêu cầu 1 & 4)
    def them_moi(self):
        print("\n--- THÊM THÍ SINH MỚI ---")
        ma = input("Nhập mã hồ sơ: ")
        # Kiểm tra trùng mã hồ sơ
        if any(ts.ma_hs == ma for ts in self.danh_sach):
            print("❌ Lỗi: Mã hồ sơ này đã tồn tại trong hệ thống!")
            return

        ten = input("Nhập họ tên: ")
        khoi = input("Nhập khối thi (A00/B00): ")
        try:
            diem = float(input("Nhập điểm thi: "))
            ts_moi = ThiSinh(ma, ten, khoi, diem)
            self.danh_sach.append(ts_moi)
            print("✅ Đã thêm thí sinh thành công.")
        except ValueError:
            print("❌ Lỗi: Điểm thi phải là con số.")

    # 2. Tìm kiếm theo mã (Yêu cầu 2)
    def tim_kiem(self):
        ma = input("\nNhập mã hồ sơ cần tìm: ")
        for ts in self.danh_sach:
            if ts.ma_hs == ma:
                print("\n--- KẾT QUẢ TÌM KIẾM ---")
                self.in_tieu_de()
                print(ts)
                return
        print("❌ Không tìm thấy thí sinh nào có mã này.")

    # 3. Sắp xếp theo kết quả (Yêu cầu 3)
    def sap_xep(self):
        # Sắp xếp theo kết quả (Đậu đứng trước Trượt)
        self.danh_sach.sort(key=lambda x: x.ket_qua)
        print("✅ Đã sắp xếp danh sách theo kết quả thi.")
        self.hien_thi_tat_ca()

    # 4. Sửa hoặc Xóa (Yêu cầu 4)
    def sua_thong_tin(self):
        ma = input("\nNhập mã hồ sơ cần sửa: ")
        for ts in self.danh_sach:
            if ts.ma_hs == ma:
                print(f"Đang sửa thông tin cho: {ts.ho_ten}")
                ts.ho_ten = input("Nhập tên mới: ")
                ts.khoi_thi = input("Nhập khối mới (A00/B00): ").upper()
                try:
                    ts.diem_thi = float(input("Nhập điểm thi mới: "))
                    ts.ket_qua = "Đậu" if ts.diem_thi >= 15 else "Trượt"
                    print("✅ Cập nhật hoàn tất.")
                except ValueError:
                    print("❌ Lỗi: Điểm không hợp lệ. Hủy cập nhật điểm.")
                return
        print("❌ Không tìm thấy thí sinh để sửa.")

    def xoa_thong_tin(self):
        ma = input("\nNhập mã hồ sơ cần xóa: ")
        original_size = len(self.danh_sach)
        self.danh_sach = [ts for ts in self.danh_sach if ts.ma_hs != ma]
        if len(self.danh_sach) < original_size:
            print("✅ Đã xóa thí sinh thành công.")
        else:
            print("❌ Không tìm thấy mã hồ sơ để xóa.")

    # 5. Xuất theo khối và kết quả (Yêu cầu 5)
    def xuat_theo_loc(self):
        khoi = input("\nNhập khối muốn xuất (A00/B00): ").upper()
        kq = input("Nhập kết quả muốn xuất (Đậu/Trượt): ")
        print(f"\n--- DANH SÁCH THÍ SINH KHỐI {khoi} - KẾT QUẢ: {kq} ---")
        self.in_tieu_de()
        count = 0
        for ts in self.danh_sach:
            if ts.khoi_thi == khoi and ts.ket_qua == kq:
                print(ts)
                count += 1
        if count == 0:
            print("   (Không có dữ liệu phù hợp)")

    def in_tieu_de(self):
        print("-" * 68)
        print(f"| {'Mã HS':<10} | {'Họ Tên':<20} | {'Khối':<8} | {'Điểm':<8} | {'Kết quả':<8} |")
        print("-" * 68)

    def hien_thi_tat_ca(self):
        if not self.danh_sach:
            print("\n⚠️ Danh sách hiện tại đang trống.")
            return
        print("\n--- TOÀN BỘ DANH SÁCH THÍ SINH ---")
        self.in_tieu_de()
        for ts in self.danh_sach:
            print(ts)
        print("-" * 68)

def main():
    ql = HeThongTuyenSinh()
    
    while True:
        print("\n========= QUẢN LÝ TUYỂN SINH =========")
        print("1. Nhập thông tin thí sinh")
        print("2. Tìm kiếm theo Mã hồ sơ")
        print("3. Sắp xếp theo Kết quả thi")
        print("4. Thêm thí sinh")
        print("5. Sửa thông tin thí sinh")
        print("6. Xóa thí sinh")
        print("7. Xuất theo Khối thi & Kết quả")
        print("8. Hiển thị toàn bộ danh sách")
        print("0. Thoát chương trình")
        
        chon = input("\nLựa chọn của bạn: ")
        
        if chon == '1' or chon == '4': ql.them_moi()
        elif chon == '2': ql.tim_kiem()
        elif chon == '3': ql.sap_xep()
        elif chon == '5': ql.sua_thong_tin()
        elif chon == '6': ql.xoa_thong_tin()
        elif chon == '7': ql.xuat_theo_loc()
        elif chon == '8': ql.hien_thi_tat_ca()
        elif chon == '0':
            print("Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()

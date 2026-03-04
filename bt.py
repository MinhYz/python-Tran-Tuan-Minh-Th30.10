import datetime
from array import array

# ==========================================
# NHÓM 1: XỬ LÝ CHUỖI (BÀI 1 - 7)
# ==========================================
def nhom_bai_string():
    print("\n--- MENU BÀI TẬP CHUỖI ---")
    print("1. Kiểm tra đối xứng")
    print("2. Đảo ngược chuỗi")
    print("3. Tìm ký tự hoa Min/Max")
    print("4. Đếm hoa/thường")
    print("5. Chèn xâu")
    print("6. Chuẩn hóa họ tên")
    print("7. Thống kê từ")
    
    chon = input("Chọn bài: ")
    
    if chon == '1':
        chuoi = input("Nhập vào một xâu: ")
        if chuoi == chuoi[::-1]:
            print("=> Kết quả: Đây là xâu đối xứng.")
        else:
            print("=> Kết quả: Không phải xâu đối xứng.")
            
    elif chon == '2':
        xau_nhap = input("Nhập xâu: ")
        dao_nguoc = ""
        for i in range(len(xau_nhap) - 1, -1, -1):
            dao_nguoc += xau_nhap[i]
        print("Xâu sau khi đảo:", dao_nguoc)

    elif chon == '6':
        ho_ten = input("Nhập họ tên cần chuẩn hóa: ")
        cac_tu = ho_ten.strip().split()
        ket_qua = " ".join(t.capitalize() for t in cac_tu)
        print("Họ tên sạch đẹp:", ket_qua)

    # ... (Các bài 3,4,5,7 làm tương tự với tên biến thuần Việt)

# ==========================================
# NHÓM 2: THỜI GIAN & DANH SÁCH (BÀI 8 - 15)
# ==========================================
def nhom_bai_date_list():
    print("\n--- MENU DATE & LIST ---")
    print("8. Tính tuổi & số ngày đã sống")
    print("11. Phân loại chẵn lẻ")
    print("13. Quản lý điểm sinh viên")
    
    chon = input("Chọn bài: ")

    if chon == '8':
        nhap_ngay = input("Ngày sinh của bạn (dd/mm/yyyy): ")
        ngay_sinh = datetime.datetime.strptime(nhap_ngay, "%d/%m/%Y")
        bay_gio = datetime.datetime.now()
        
        tuoi_hien_tai = bay_gio.year - ngay_sinh.year
        tong_ngay = (bay_gio - ngay_sinh).days
        
        print(f"Tuổi: {tuoi_hien_tai}")
        print(f"Số ngày đã trôi qua: {tong_ngay}")
        print("Hệ thống:", bay_gio.strftime("%d/%m/%Y %H:%M:%S"))

    elif chon == '11':
        n = int(input("Nhập số lượng phần tử: "))
        ds_so = []
        for i in range(n):
            ds_so.append(int(input(f"Nhập số thứ {i+1}: ")))
        
        chan = [x for x in ds_so if x % 2 == 0]
        le = [x for x in ds_so if x % 2 != 0]
        
        print("Mảng chẵn:", chan, "- Tổng:", sum(chan))
        print("Mảng lẻ:", le, "- Tổng:", sum(le))

# ==========================================
# NHÓM 3: DICTIONARY & TUYỂN SINH (BÀI 19 - 22)
# ==========================================
def quan_ly_tuyen_sinh():
    # Bài 22: Hệ thống quản lý thí sinh
    danh_sach_ts = []
    while True:
        print("\n--- QUẢN LÝ TUYỂN SINH ---")
        print("1. Thêm thí sinh")
        print("2. Tìm kiếm theo mã")
        print("3. Hiển thị danh sách")
        print("0. Quay lại")
        
        lenh = input("Chọn lệnh: ")
        if lenh == '0': break
        
        if lenh == '1':
            ma = input("Mã hồ sơ: ")
            ten = input("Họ tên: ")
            khoi = input("Khối thi (A00/B00): ")
            d1 = float(input("Điểm môn 1: "))
            d2 = float(input("Điểm môn 2: "))
            d3 = float(input("Điểm môn 3: "))
            tong = d1 + d2 + d3
            ket_qua = "Đậu" if tong >= 15 else "Trượt"
            
            thi_sinh = {
                "ma": ma, "ten": ten, "khoi": khoi, 
                "diem": tong, "kq": ket_qua
            }
            danh_sach_ts.append(thi_sinh)
            print("Đã thêm thành công!")
            
        elif lenh == '3':
            print("-" * 40)
            for ts in danh_sach_ts:
                print(f"[{ts['ma']}] {ts['ten']} - Khối: {ts['khoi']} - Tổng: {ts['diem']} - KQ: {ts['kq']}")

# ==========================================
# CHƯƠNG TRÌNH CHÍNH (MAIN MENU)
# ==========================================
def main():
    while True:
        print("\n" + "=".center(40, "="))
        print(" BÀI TẬP THỰC HÀNH CHƯƠNG 3 ".center(40, " "))
        print("=".center(40, "="))
        print("1. Nhóm bài về Xâu (String)")
        print("2. Nhóm bài về Ngày & List")
        print("3. Nhóm bài về Tuple, Set, Array")
        print("4. Hệ thống Quản lý Tuyển sinh (Bài 22)")
        print("0. Thoát chương trình")
        print("-" * 40)
        
        lua_chon = input("Bạn muốn xem nhóm bài nào? ")
        
        if lua_chon == '0':
            print("Đang thoát... Tạm biệt!")
            break
        elif lua_chon == '1':
            nhom_bai_string()
        elif lua_chon == '2':
            nhom_bai_date_list()
        elif lua_chon == '4':
            quan_ly_tuyen_sinh()
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()

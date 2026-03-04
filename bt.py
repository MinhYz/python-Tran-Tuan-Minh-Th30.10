import datetime
from array import array

# =================================================================
# FILE THỰC HÀNH CHƯƠNG 3 - TỔNG HỢP 22 BÀI TẬP
# Sinh viên: [Tên của bạn]
# =================================================================

def main():
    # Khởi tạo một số biến lưu trữ dữ liệu cho các bài quản lý
    du_lieu_bay = []      # Bài 12
    ds_lop_hoc = []       # Bài 13
    ds_tuyen_sinh = []    # Bài 22

    while True:
        print("\n" + "="*50)
        print("         MENU THỰC HÀNH CHƯƠNG 3 (COLLECTION)       ")
        print("="*50)
        print("1-7.   Nhóm bài tập về String (Chuỗi)")
        print("8-9.   Nhóm bài tập về Date - Time")
        print("10-13. Nhóm bài tập về List (Danh sách)")
        print("14-15. Nhóm bài tập về Tuple")
        print("16.    Nhóm bài tập về Set")
        print("17-18. Nhóm bài tập về Array (Mảng)")
        print("19-22. Nhóm bài tập về Dictionary")
        print("0.     Thoát chương trình")
        print("-" * 50)
        
        lua_chon = input("Nhập số bài bạn muốn chạy (1-22) hoặc 0 để thoát: ")

        if lua_chon == '0':
            print("Kết thúc chương trình. Tạm biệt!")
            break

        # --- NHÓM BÀI STRING (1-7) ---
        elif lua_chon == '1':
            print("\n[Bài 1] Kiểm tra xâu đối xứng")
            s = input("Nhập xâu: ")
            if s == s[::-1]:
                print("=> Đây là xâu đối xứng")
            else:
                print("=> Không phải xâu đối xứng")

        elif lua_chon == '2':
            print("\n[Bài 2] Đảo ngược xâu (Không dùng slice)")
            s = input("Nhập xâu: ")
            xau_dao = ""
            for i in range(len(s) - 1, -1, -1):
                xau_dao += s[i]
            print("=> Xâu đảo ngược:", xau_dao)

        elif lua_chon == '3':
            print("\n[Bài 3] Tìm chữ hoa nhỏ nhất và lớn nhất")
            s = input("Nhập xâu: ")
            ds_hoa = [ch for ch in s if 'A' <= ch <= 'Z']
            if ds_hoa:
                print(f"=> Chữ hoa nhỏ nhất: {min(ds_hoa)}")
                print(f"=> Chữ hoa lớn nhất: {max(ds_hoa)}")
            else:
                print("=> Không có ký tự hoa trong xâu")

        elif lua_chon == '4':
            print("\n[Bài 4] Đếm ký tự hoa và thường")
            s = input("Nhập xâu: ")
            hoa = sum(1 for c in s if c.isupper())
            thuong = sum(1 for c in s if c.islower())
            print(f"=> Số ký tự hoa: {hoa}")
            print(f"=> Số ký tự thường: {thuong}")

        elif lua_chon == '5':
            print("\n[Bài 5] Chèn xâu s2 vào s1 tại vị trí k")
            s1 = input("Nhập xâu thứ nhất: ")
            s2 = input("Nhập xâu thứ hai: ")
            k = int(input("Nhập vị trí k: "))
            if 0 <= k <= len(s1):
                kq = s1[:k] + s2 + s1[k:]
                print("=> Kết quả sau khi chèn:", kq)
            else:
                print("=> Vị trí k không hợp lệ")

        elif lua_chon == '6':
            print("\n[Bài 6] Chuẩn hóa họ tên")
            hoten = input("Nhập họ tên: ")
            ds_tu = hoten.strip().split()
            kq = " ".join(tu.capitalize() for tu in ds_tu)
            print("=> Họ tên chuẩn hóa:", kq)

        elif lua_chon == '7':
            print("\n[Bài 7] Thống kê chuỗi")
            s = input("Nhập chuỗi: ")
            ds_tu = s.split()
            print("- Số ký tự:", len(s))
            print("- Số từ:", len(ds_tu))
            print("- In mỗi từ trên 1 dòng:")
            for t in ds_tu: print(f"  + {t}")
            chuan_hoa = " ".join(t.capitalize() for t in ds_tu)
            print("- Chuẩn hóa nối lại:", chuan_hoa)

        # --- NHÓM BÀI DATE-TIME (8-9) ---
        elif lua_chon == '8':
            print("\n[Bài 8] Tính tuổi và thời gian trôi qua")
            ns_str = input("Nhập ngày sinh (dd/mm/yyyy): ")
            ns = datetime.datetime.strptime(ns_str, "%d/%m/%Y")
            today = datetime.datetime.today()
            tuoi = today.year - ns.year
            print(f"=> Tuổi hiện tại: {tuoi}")
            print(f"=> Tổng số ngày đã sống: {(today - ns).days} ngày")
            print("=> Hệ thống hiện tại:", today.strftime("%d/%m/%Y %H:%M:%S"))

        elif lua_chon == '9':
            print("\n[Bài 9] Quản lý ngày sinh sinh viên")
            ten = input("Nhập họ tên: ")
            ns_str = input("Nhập ngày sinh (dd/mm/yyyy): ")
            ns = datetime.datetime.strptime(ns_str, "%d/%m/%Y")
            
            ten_chuan = " ".join(t.capitalize() for t in ten.strip().split())
            print(f"=> Họ tên: {ten_chuan}")
            print(f"=> Ngày: {ns.day}, Tháng: {ns.month}, Năm: {ns.year}")
            
            nam_nhuan = (ns.year % 4 == 0 and ns.year % 100 != 0) or (ns.year % 400 == 0)
            print(f"=> Năm nhuận: {'Có' if nam_nhuan else 'Không'}")
            thu = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
            print(f"=> Sinh vào: {thu[ns.weekday()]}")

        # --- NHÓM BÀI LIST (10-13) ---
        elif lua_chon == '10':
            print("\n[Bài 10] Nhập số thực đến khi gặp 0")
            day_so = []
            while True:
                n = float(input("Nhập số (0 để dừng): "))
                if n == 0: break
                day_so.append(n)
            print("=> Dãy số vừa nhập:", day_so)

        elif lua_chon == '11':
            print("\n[Bài 11] Phân loại chẵn lẻ")
            n = int(input("Nhập số lượng phần tử n: "))
            L = [int(input(f"Nhập phần tử {i+1}: ")) for i in range(n)]
            chan = [x for x in L if x % 2 == 0]
            le = [x for x in L if x % 2 != 0]
            print(f"=> Danh sách chẵn: {chan} (Tổng: {sum(chan)})")
            print(f"=> Danh sách lẻ: {le} (Tổng: {sum(le)})")

        elif lua_chon == '12':
            print("\n[Bài 12] Quản lý đặt vé máy bay")
            ten_kh = input("Tên khách: ")
            diem_di = input("Điểm đi: ")
            diem_den = input("Điểm đến: ")
            gia = float(input("Giá tiền: "))
            du_lieu_bay.append({"ten": ten_kh, "di": diem_di, "den": diem_den, "gia": gia})
            print("=> Danh sách hiện tại:")
            for i, v in enumerate(du_lieu_bay): print(f"{i+1}. {v}")

        elif lua_chon == '13':
            print("\n[Bài 13] Quản lý lớp học")
            sl_sv = int(input("Số lượng SV cần thêm: "))
            for _ in range(sl_sv):
                ma = input("Mã SV: ")
                ten = input("Tên: ")
                diem = [float(x) for x in input("Nhập dãy điểm (cách nhau dấu cách): ").split()]
                ds_lop_hoc.append({"ma": ma, "ten": ten, "diem": diem, "dtb": sum(diem)/len(diem)})
            
            # Sắp xếp giảm dần theo DTB
            ds_lop_hoc.sort(key=lambda x: x['dtb'], reverse=True)
            print("=> Danh sách SV (Sắp xếp theo DTB giảm dần):")
            for sv in ds_lop_hoc:
                print(f"{sv['ma']} - {sv['ten']} - DTB: {sv['dtb']:.2f}")

        # --- NHÓM BÀI TUPLE, SET, ARRAY (14-18) ---
        elif lua_chon == '14':
            print("\n[Bài 14] Tuple 9 loài hoa")
            hoa = ("Lan", "Cúc", "Trúc", "Mai", "Hồng", "Huệ", "Đào", "Sen", "Súng")
            f1, f2 = hoa[:5], hoa[5:]
            print("F1:", f1)
            print("F2:", f2)
            for h in hoa: print(f"Hoa {h} có độ dài tên: {len(h)}")

        elif lua_chon == '15':
            print("\n[Bài 15] Tính tổng và tích Tuple")
            tup = tuple(int(x) for x in input("Nhập các số nguyên (cách nhau dấu cách): ").split())
            tich = 1
            for x in tup: tich *= x
            print(f"=> Tổng: {sum(tup)}, Tích: {tich}")

        elif lua_chon == '16':
            print("\n[Bài 16] Set học sinh lớp A và B")
            A = set(input("HS lớp A (cách nhau dấu phẩy): ").split(','))
            B = set(input("HS lớp B (cách nhau dấu phẩy): ").split(','))
            print("=> Học cả hai lớp:", A & B)
            print("=> Chỉ học lớp A:", A - B)
            print("=> Học ít nhất một lớp:", A | B)

        elif lua_chon == '17':
            print("\n[Bài 17] Array số nguyên")
            n = int(input("Nhập n: "))
            mang = array('i', [int(input(f"Số {i+1}: ")) for i in range(n)])
            print("=> Các phần tử:", mang.tolist())
            print(f"=> Tổng: {sum(mang)}, Trung bình: {sum(mang)/len(mang)}")

        elif lua_chon == '18':
            print("\n[Bài 18] Tách mảng âm dương")
            n = int(input("Nhập n: "))
            goc = array('f', [float(input(f"Số {i+1}: ")) for i in range(n)])
            am = array('f', [x for x in goc if x < 0])
            duong = array('f', [x for x in goc if x >= 0])
            print("=> Mảng gốc:", goc.tolist())
            print("=> Mảng âm:", am.tolist())
            print("=> Mảng dương/0:", duong.tolist())

        # --- NHÓM BÀI DICTIONARY (19-22) ---
        elif lua_chon == '19':
            students = [
                {"ma": "S1", "ten": "An", "tuoi": 21, "tp": "Hà Nội"},
                {"ma": "S2", "ten": "Ba", "tuoi": 19, "tp": "Hà Nội"},
                {"ma": "S3", "ten": "Cường", "tuoi": 22, "tp": "HCM"}
            ]
            print("=> SV tuổi >= 20:", [s['ten'] for s in students if s['tuoi'] >= 20])
            print("=> SV ở Hà Nội:", [s['ten'] for s in students if s['tp'] == "Hà Nội"])

        elif lua_chon == '20':
            print("\n[Bài 20] Sản phẩm mua nhiều nhất")
            khach = {"Nam": ["Táo", "Cam"], "Lan": ["Táo", "Ổi"], "Minh": ["Táo"]}
            thong_ke = {}
            for sp_list in khach.values():
                for sp in sp_list: thong_ke[sp] = thong_ke.get(sp, 0) + 1
            max_sp = max(thong_ke, key=thong_ke.get)
            print(f"=> Sản phẩm mua nhiều nhất là: {max_sp}")

        elif lua_chon == '21':
            lich = {"Thứ 2": ["Học Python", "Gặp thầy"], "Thứ 3": ["Làm bài tập"]}
            ngay = input("Nhập thứ cần xem: ")
            print(f"=> Công việc: {lich.get(ngay, 'Không có lịch')}")

        elif lua_chon == '22':
            print("\n[Bài 22] Quản lý tuyển sinh Đại học")
            # Logic đơn giản cho bài nộp: Thêm một người để test
            ma_hs = input("Mã hồ sơ: ")
            ten_ts = input("Họ tên: ")
            khoi = input("Khối (A00/B00): ")
            diem = float(input("Tổng điểm: "))
            kq = "Đậu" if diem >= 15 else "Trượt"
            ds_tuyen_sinh.append({"ma": ma_hs, "ten": ten_ts, "khoi": khoi, "diem": diem, "kq": kq})
            print("=> Đã lưu thí sinh. Danh sách hiện có:")
            for t in ds_tuyen_sinh: print(t)

        else:
            print("=> Lựa chọn không hợp lệ, vui lòng chọn lại từ 0-22.")

if __name__ == "__main__":
    main()

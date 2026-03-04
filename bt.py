import datetime
from array import array

# =================================================================
# BÀI THỰC HÀNH CHƯƠNG 3 - TỔNG HỢP TOÀN BỘ 22 BÀI
# =================================================================

# --- NHÓM 1: XỬ LÝ CHUỖI (BÀI 1 - 7) ---
def nhom_string():
    while True:
        print("\n--- BÀI TẬP CHUỖI (1-7) ---")
        print("1. Đối xứng | 2. Đảo ngược | 3. Hoa Min/Max | 4. Đếm hoa/thường")
        print("5. Chèn xâu | 6. Chuẩn hóa tên | 7. Thống kê chuỗi | 0. Quay lại")
        chon = input("Chọn bài: ")
        
        if chon == '0': break
        elif chon == '1':
            x = input("Nhập xâu: ")
            print("Kết quả:", "Đối xứng" if x == x[::-1] else "Không đối xứng")
        elif chon == '2':
            s = input("Nhập xâu: ")
            dao = ""
            for i in range(len(s)-1, -1, -1): dao += s[i]
            print("Xâu đảo:", dao)
        elif chon == '3':
            s = input("Nhập xâu: ")
            hoa = [c for c in s if 'A' <= c <= 'Z']
            if hoa: print(f"Min: {min(hoa)}, Max: {max(hoa)}")
            else: print("Không có chữ hoa")
        elif chon == '4':
            s = input("Nhập xâu: ")
            h = sum(1 for c in s if c.isupper())
            t = sum(1 for c in s if c.islower())
            print(f"Hoa: {h}, Thường: {t}")
        elif chon == '5':
            s1, s2 = input("Xâu 1: "), input("Xâu 2: ")
            k = int(input("Vị trí k: "))
            print("Kết quả:", s1[:k] + s2 + s1[k:])
        elif chon == '6':
            t = input("Nhập họ tên: ")
            print("Chuẩn hóa:", " ".join(w.capitalize() for w in t.strip().split()))
        elif chon == '7':
            s = input("Nhập chuỗi: ")
            ds = s.split()
            print(f"Số ký tự: {len(s)}, Số từ: {len(ds)}")
            for w in ds: print("-", w)

# --- NHÓM 2: DATE - TIME (BÀI 8 - 9) ---
def nhom_datetime():
    print("\n--- BÀI TẬP DATE-TIME (8-9) ---")
    nhap = input("Nhập ngày sinh (dd/mm/yyyy): ")
    ns = datetime.datetime.strptime(nhap, "%d/%m/%Y")
    nay = datetime.datetime.now()
    
    # Bài 8
    print(f"Tuổi: {nay.year - ns.year}")
    print(f"Số ngày đã qua: {(nay - ns).days}")
    print("Hệ thống:", nay.strftime("%d/%m/%Y %H:%M:%S"))
    
    # Bài 9
    chuan_ten = " ".join(w.capitalize() for w in input("Họ tên SV: ").strip().split())
    print(f"SV: {chuan_ten} | Sinh ngày: {ns.day}, Tháng: {ns.month}, Năm: {ns.year}")
    nhuan = (ns.year % 4 == 0 and ns.year % 100 != 0) or (ns.year % 400 == 0)
    print("Năm nhuận:", "Có" if nhuan else "Không")
    thu = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"]
    print("Thứ trong tuần:", thu[ns.weekday()])

# --- NHÓM 3: TUPLE - SET - ARRAY (BÀI 14 - 18) ---
def nhom_tuple_set_array():
    while True:
        print("\n--- BÀI TẬP TUPLE-SET-ARRAY (14-18) ---")
        print("14. Tuple Hoa | 15. Tuple Số | 16. Set Lớp | 17. Mảng Nguyên | 18. Mảng Thực | 0. Quay lại")
        chon = input("Chọn bài: ")
        
        if chon == '0': break
        elif chon == '14':
            hoa = ("Hồng", "Lan", "Huệ", "Cúc", "Mai", "Đào", "Sen", "Súng", "Quỳnh")
            f1, f2 = hoa[:5], hoa[5:]
            print("F1:", f1, "\nĐộ dài:", [len(h) for h in f1])
            print("F2:", f2, "\nĐộ dài:", [len(h) for h in f2])
        elif chon == '15':
            tp = tuple(int(x) for x in input("Nhập dãy số: ").split())
            tich = 1
            for x in tp: tich *= x
            print(f"Tổng: {sum(tp)}, Tích: {tich}")
        elif chon == '16':
            a = set(input("Lớp A: ").split(','))
            b = set(input("Lớp B: ").split(','))
            print("Giao:", a & b, "\nChỉ A:", a - b, "\nHợp:", a | b)
        elif chon == '17':
            n = int(input("n = "))
            arr = array('i', [int(input(f"Số {i+1}: ")) for i in range(n)])
            print("Mảng:", arr.tolist(), "Tổng:", sum(arr), "TB:", sum(arr)/n)
        elif chon == '18':
            n = int(input("n = "))
            goc = array('f', [float(input(f"Số {i+1}: ")) for i in range(n)])
            am = array('f', [x for x in goc if x < 0])
            duong = array('f', [x for x in goc if x >= 0])
            print(f"Gốc: {goc.tolist()}\nÂm: {am.tolist()}\nDương: {duong.tolist()}")

# --- NHÓM 4: LIST & DICTIONARY (BÀI 10-13, 19-22) ---
def nhom_list_dict():
    # Bài 22: Quản lý tuyển sinh (Tối giản cho đúng vibe thực hành)
    ds_ts = []
    while True:
        print("\n--- QUẢN LÝ & DICTIONARY (19-22) ---")
        print("19. Filter SV | 20. Mua nhiều nhất | 22. Tuyển sinh | 0. Quay lại")
        chon = input("Chọn bài: ")
        if chon == '0': break
        elif chon == '19':
            sv = [{"ma": "1", "ten": "An", "tuoi": 20, "tp": "Hà Nội"}, {"ma": "2", "ten": "Ba", "tuoi": 18, "tp": "Huế"}]
            print("Tuổi >= 20:", [s['ten'] for s in sv if s['tuoi'] >= 20])
            print("Ở Hà Nội:", [s['ten'] for s in sv if s['tp'] == "Hà Nội"])
        elif chon == '20':
            mua = {"A": ["Táo", "Cam"], "B": ["Táo"]}
            tk = {}
            for l in mua.values():
                for i in l: tk[i] = tk.get(i, 0) + 1
            print("Mua nhiều nhất:", max(tk, key=tk.get))
        elif chon == '22':
            m = input("Mã: "); t = input("Tên: "); k = input("Khối: "); d = float(input("Điểm: "))
            ds_ts.append({"ma": m, "ten": t, "khoi": k, "diem": d, "kq": "Đậu" if d >= 15 else "Trượt"})
            print("Danh sách:", ds_ts)

# --- CHƯƠNG TRÌNH CHÍNH ---
def menu_chinh():
    while True:
        print("\n" + "=".center(50, "="))
        print(" BÀI TẬP THỰC HÀNH CHƯƠNG 3 ".center(50, " "))
        print("=".center(50, "="))
        print("1. Nhóm String (Bài 1-7)")
        print("2. Nhóm Date-Time (Bài 8-9)")
        print("3. Nhóm List (Bài 10-13)")
        print("4. Nhóm Tuple - Set - Array (Bài 14-18)")
        print("5. Nhóm Dictionary (Bài 19-22)")
        print("0. Thoát")
        
        chon = input("Nhập lựa chọn của bạn: ")
        if chon == '0': break
        elif chon == '1': nhom_string()
        elif chon == '2': nhom_datetime()
        elif chon == '3': # Gom tạm vào chung với List
            print("Bài 11: Nhập n số, tách chẵn lẻ")
            n = int(input("n = "))
            l = [int(input()) for _ in range(n)]
            print("Chẵn:", [x for x in l if x%2==0], "Lẻ:", [x for x in l if x%2!=0])
        elif chon == '4': nhom_tuple_set_array()
        elif chon == '5': nhom_list_dict()

if __name__ == "__main__":
    menu_chinh()

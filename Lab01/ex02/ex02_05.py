giolamviec = float(input("Nhap so gio lam viec: "))
luonggio = float(input("Nhap thu lao so gio lam viec: "))
giotieuchuan = 44
#max tim gia tri lon nhat
giovuotchuan = max (0, giolamviec - giotieuchuan)
luong= giotieuchuan * luonggio + giovuotchuan * luonggio * 1.5
print ("Luong cua ban la: ", luong)

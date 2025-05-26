print ("Nhap cac dong van ban:  (Nhap 'done' de ket thuc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\n \chuyen cac dong da nhap thanh chu in hoa: ")
for line in lines:
    print (line.upper())
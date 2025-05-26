j = []
#range la ham dung de tao ra day so theo quy tac xac dinh 
for i in range (1999,3201):
    if (i % 7 ==0) and (i % 5 !=0):
        #.append la phuong thuc them 1 ptu vao cuoi danh sach
        j.append(str(i))
#.join la dung de noi cac phan tu trong j thanh 1 chuoi 
print("," .join(j))


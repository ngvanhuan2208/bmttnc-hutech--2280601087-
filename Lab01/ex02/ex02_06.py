intput_str = input ("Nhap 2 so X, Y: ")
#split(,) dung de tach 1 chuoi thanh cac phan tu 
dimensisons = [int(x) for x in intput_str.split(',')]
rowNum = dimensisons[0]
colNum = dimensisons[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum): 
        multilist[row][col] = row * col
print (multilist) 

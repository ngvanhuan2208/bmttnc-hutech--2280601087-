def daonguocchuoi(chuoi):
    #::-1 cat chuoi de dao nguoc 
    return chuoi[::-1]
input_str = input("Nhap chuoi can dao nguoc: ")
print("Chuoi dao nguoc: ", daonguocchuoi(input_str))
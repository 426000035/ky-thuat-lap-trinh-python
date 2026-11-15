def bai01():
    #n,m=3,5

    #Nhap gia tri n, m
    n=int(input("Nhap n: "))
    m=int(input("Nhap m: "))
   
    if(n>0 and m>0): #Kiem tra gia tri n, m
        dem=0 # dung de tinh tong so *   
        for i in range(n):
            for j in range(m):
                print('*',end=' ')
                dem=dem+1
            print()
        print("Tong so * la: ",dem)
    else:
        print('Khong hop le')

def bai02():
    h = int(input("Nhap h: "))
    if(h>0):
        for i in range(h, 0, -1):
            for j in range(i):
                print('*', end=' ')
            print()
    else:
        print('Khong hop le')

def bai03():
    a=int(input("Nhap a:"))
    b=int(input("Nhap b:"))
    k=int(input("Nhap k:"))

    if(2 <= a <= b <= 9 and 1 <= k <= 10):
        for i in range(a, b+1):
            for j in range(1, k+1):
                print(f"{i} x {j} = {i * j}")
    else:
        print('khong hop le')

#Nhập n và chế độ c. 
#Với n dương, chế độ 1 in j ở từng ô; 
#chế độ 2 in i ở từng ô. Nếu n không dương hoặc c khác 1 và 2, 
#chỉ in “Khong hop le”. Giữ nguyên hai vòng lặp; dùng if để chọn giá trị in
def bai04():
    #n = 3
    n=int(input('Nhap n: '))
    c=int(input('Nhap che do, chon 1 hoac 2: '))
    if(c==1 or c==2) and n>0:
        if(c==1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    print(j, end=' ')
                print()
        else:
                    for i in range(1, n + 1):
                        for j in range(1, n + 1):
                            print(i, end=' ')
                        print()
    else:
        print('Khong hop le')

#Nhập n, m là số lượt ngoài và số lượt trong, cho phép bằng 0. 
# Với n, m không âm, 
# in các cặp (i, j) theo mẫu rồi in tổng. 
# Nếu một giá trị âm, chỉ in “Khong hop le”.
def bai05():
    dem = 0
    n = int(input('Nhap n: '))
    m = int(input('Nhap m: '))

    if n >= 0 and m >= 0:
        i = 1
        while i <= n:
            for j in range(1, m + 1):
                print(i, j)
                dem += 1
            i += 1
        print(dem)
    else:
        print('Khong hop le')


def main():
    #bai01()
    #bai02()
    #bai03()
    #bai04()
    bai05()
    
if __name__=="__main__":
    main()

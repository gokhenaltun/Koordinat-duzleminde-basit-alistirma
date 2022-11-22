
x_1, y_1 = map(float,input("A noktası koordinatı: ").split())
x_2, y_2 = map(float,input("B noktası koordinatı: ").split())
x_3, y_3 = map(float,input("C noktası koordinatı: ").split())
x_4, y_4 = map(float,input("Bulunduğun noktanın koordinatı: ").split())
bx = x_2-x_1     
by = y_2-y_1     
cx = x_3-x_1
cy = y_3-y_1
x = x_4-x_1
y = y_4-y_1
d = bx*cy-cx*by
WA = (x*(by-cy)+y*(cx-bx)+bx*cy-cx*by)
WB = (x*cy-y*cx)
WC = (y*bx-x*by)
    
if((0< WA < 1) and (0< WB < 1) and (0< WC < 1)):
        print("A B C noktalarının Oluşturduğu Alanın içindesin.")
else:
        print("A B C noktalarının Oluşturduğu Alanın dışındasın.")
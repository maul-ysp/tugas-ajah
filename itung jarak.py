import math

x1, y1 = input("Masukkan x1, y1 (pisahkan dengan koma): ").split(",")
x1, y1 = float(x1), float(y1)

x2, y2 = input("Masukkan x2, y2 (pisahkan dengan koma): ").split(",")
x2, y2 = float(x2), float(y2)

jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Jarak:", jarak)

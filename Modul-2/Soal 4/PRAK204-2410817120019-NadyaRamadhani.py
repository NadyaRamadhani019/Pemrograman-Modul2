#input output pertama
jarijari = float(input())
tinggi = float(input())
volume = 22 / 7 * (jarijari**2) * tinggi
luas = 2 * 22 / 7 * jarijari * (jarijari + tinggi)
keliling = 2 * 22 / 7 * jarijari
print(f"Volume = {volume:.2f}")
print(f"Luas = {luas:.2f}")
print(f"Keliling = {keliling:.2f}")

print("")

#input output kedua
jarijari, tinggi = map(float, input().split())
volume = 22 / 7 * (jarijari**2) * tinggi
luas = 2 * 22 / 7 * jarijari * (jarijari + tinggi)
keliling = 2 * 22 / 7 * jarijari
print(f"Volume = {volume:.2f}")
print(f"Luas = {luas:.2f}")
print(f"Keliling = {keliling:.2f}")
#input output pertama
a, b, i, j, x, y = map(float, input().split())
hasil = (a-b) * (i/j) - (x+y)
print(f"{hasil:.3f}")

print("")

#input output kedua
a, b = map(float, input().split())
i, j = map(float, input().split())
x, y = map(float, input().split())
hasil = (a-b) * (i/j) - (x+y)
print(f"{hasil:.3f}")
def sr(a, b, c):
    return (a + b + c) / 3
n = int(input("Введите число: "))
if n % 2 == 0 and n % 3 == 0:
    print("Делится на 2 и на 3.")
elif n % 2 == 0:
    print("Делится на 2.")
elif n % 3 == 0:
    print("Делится на 3.")
else:
    print("Не делится ни на 2, ни на 3.")

n = int(input("Введите N: "))
x = abs(n)
s = 0
while x > 0:
    s += x % 10
    x //= 10
print(f"Сумма цифр: {s}")
print("Проверка функции:")
print(f"sr(3, 6, 9) = {sr(3, 6, 9):.2f}")
print(f"sr(1, 2, 4) = {sr(1, 2, 4):.2f}")
print(f"sr(-5, 0, 5) = {sr(-5, 0, 5):.2f}")
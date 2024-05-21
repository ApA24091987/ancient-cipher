def find_password(n):
    result = ''
    for i in range(1, n):
        for j in range(i, n+1):
            if (i + j) % n == 0:
                result += str(i) + str(j)

    return result

n = int(input("введите число от 3 до 20: "))
if 3 <= n <= 20:
    print(find_password(n))
else:
    print("Некорректное значение. Введите число от 3 до 20.")
#ответ число 11.
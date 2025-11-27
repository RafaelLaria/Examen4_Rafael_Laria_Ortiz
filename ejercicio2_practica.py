def cuenta_regresiva(n):
    if n == 0:
        return n
    print(n)
    cuenta_regresiva(n-1)

print(cuenta_regresiva(5))
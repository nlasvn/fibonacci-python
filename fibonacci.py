def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 1
    return fib(num - 1) + fib(num - 2)


def print_fib():
    num = int(input("Digite um número para o cálculo de fibonacci: "))
    print(f"O fibonacci de {num} é: {fib(num)}")


print_fib()

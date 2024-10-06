def fib(num):
    if num <= 1:
        return num
    return fib(num - 1) + fib(num - 2)


def print_fib():
    num = int(input("Digite um número para o cálculo de fibonacci: "))
    print(f"O fibonacci de {num} é: {fib(num)}")


print_fib()

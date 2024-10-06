def fib(num):
    sum_fib = 0
    acc_even = 0
    acc_odd = 0

    for i in range(num + 1):
        if 0 < i < 3:
            acc_even = 1
        else:
            if i % 2 == 0:
                acc_even = sum_fib
            else:
                acc_odd = sum_fib
        sum_fib = acc_even + acc_odd

    return sum_fib


def print_fib():
    num = int(input("Digite um número para o cálculo de fibonacci: "))
    print(f"O fibonacci de {num} é: {fib(num)}")


print_fib()

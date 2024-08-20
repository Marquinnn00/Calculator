def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero!"

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def main():
    print("Bem-vindo à calculadora!")
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        choice = input("Digite o número da operação (ou 'sair' para encerrar): ").strip()

        if choice == 'sair':
            print("Saindo da calculadora. Até logo!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Digite o primeiro número: ")
            num2 = get_number("Digite o segundo número: ")

            if choice == '1':
                print(f"Resultado: {add(num1, num2)}")
            elif choice == '2':
                print(f"Resultado: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Resultado: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Resultado: {divide(num1, num2)}")
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()


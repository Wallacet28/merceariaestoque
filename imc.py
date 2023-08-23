def imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Qual é o seu peso (em kg)? "))
altura = float(input("Qual é a sua altura (em metros)? "))

resultado = imc(peso, altura)
print("Seu IMC é: {:.2f}".format(resultado))

if resultado < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= resultado < 25:
    print("Você está com o peso normal.")
elif 25 <= resultado < 30:
    print("Você está com sobrepeso.")
elif 30 <= resultado < 35:
    print("Você está com obesidade grau I.")
elif 35 <= resultado < 40:
    print("Você está com obesidade grau II (severa).")
else:
    print("Você está com obesidade grau III (mórbida).")
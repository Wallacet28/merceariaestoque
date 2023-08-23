import pandas as pd

# Criar um dataframe com as colunas 'Nome', 'Matéria' e 'Nota'
notas = pd.DataFrame(columns=['Nome', 'Matéria', 'Nota'])

# Adicionar dados ao dataframe
notas = notas.append({'Nome': 'João', 'Matéria': 'Matemática', 'Nota': 9.0}, ignore_index=True)
notas = notas.append({'Nome': 'João', 'Matéria': 'Português', 'Nota': 8.5}, ignore_index=True)
notas = notas.append({'Nome': 'Maria', 'Matéria': 'Matemática', 'Nota': 7.0}, ignore_index=True)
notas = notas.append({'Nome': 'Maria', 'Matéria': 'Português', 'Nota': 9.0}, ignore_index=True)

# Exibir as notas
print(notas)


#implementação 2

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    situacao = "Aprovado"
elif media >= 4:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("Aluno:", nome)
print("Média:", media)
print("Situação:", situacao)

#outra implementação
alunos = []

for i in range(3):
    nome = input("Insira o nome do aluno: ")
    notas = []
    for j in range(12):
        nota = float(input(f"Insira a nota da matéria {j+1}: "))
        notas.append(nota)
    aluno = {"nome": nome, "notas": notas}
    alunos.append(aluno)

for aluno in alunos:
    nome = aluno["nome"]
    notas = aluno["notas"]
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 4:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print("")
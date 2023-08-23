import pandas as pd

# Dados dos alimentos
data = {'Alimento': ['Arroz', 'Feijão', 'Frango'],
        'Proteínas (g)': [6.8, 9.0, 31.0],
        'Gorduras (g)': [0.7, 1.1, 3.6],
        'Carboidratos (g)': [77.0, 23.0, 0.0]}

# Criando um DataFrame a partir dos dados
alimentos = pd.DataFrame(data)

# Perguntando ao usuário a quantidade de cada alimento em porções
porcao_arroz = float(input("Quantas porções de arroz você deseja consumir? "))
porcao_feijao = float(input("Quantas porções de feijão você deseja consumir? "))
porcao_frango = float(input("Quantas porções de frango você deseja consumir? "))

# Calculando a quantidade de proteínas, gorduras e carboidratos
proteinas = porcao_arroz * alimentos.at[0, 'Proteínas (g)'] + \
            porcao_feijao * alimentos.at[1, 'Proteínas (g)'] + \
            porcao_frango * alimentos.at[2, 'Proteínas (g)']

gorduras = porcao_arroz * alimentos.at[0, 'Gorduras (g)'] + \
           porcao_feijao * alimentos.at[1, 'Gorduras (g)'] + \
           porcao_frango * alimentos.at[2, 'Gorduras (g)']

carboidratos = porcao_arroz * alimentos.at[0, 'Carboidratos (g)'] + \
               porcao_feijao * alimentos.at[1, 'Carboidratos (g)'] + \
               porcao_frango * alimentos.at[2, 'Carboidratos (g)']

# Mostrando os resultados
print("Ingestão total de calorias: {:.1f} kcal".format(calorias))
print("Ingestão total de proteínas: {:.1f} g".format(proteinas))
print("Ingestão total de gorduras: {:.1f} g".format(gorduras))
print("Ingestão total de carboidratos: {:.1f} g".format(carboidratos))
import pandas as pd

# Definir os alimentos
alimentos = pd.DataFrame({'Alimento': ['Arroz', 'Feijão', 'Frango'],
                         'Calorias (kcal)': [130, 150, 220],
                         'Proteínas (g)': [2.5, 9, 35],
                         'Gorduras (g)': [1, 2, 8],
                         'Carboidratos (g)': [29, 25, 0]})

# Solicitar a quantidade de cada alimento em porções
porcao_arroz = float(input("Quantas porções de arroz você deseja consumir? "))
porcao_feijao = float(input("Quantas porções de feijão você deseja consumir? "))
porcao_frango = float(input("Quantas porções de frango você deseja consumir? "))

# Calcular a ingestão total de calorias
calorias = porcao_arroz * alimentos.at[0, 'Calorias (kcal)'] + \
           porcao_feijao * alimentos.at[1, 'Calorias (kcal)'] + \
           porcao_frango * alimentos.at[2, 'Calorias (kcal)']

# Calcular a ingestão total de proteínas
proteinas = porcao_arroz * alimentos.at[0, 'Proteínas (g)'] + \
            porcao_feijao * alimentos.at[1, 'Proteínas (g)'] + \
            porcao_frango * alimentos.at[2, 'Proteínas (g)']

# Calcular a ingestão total de gorduras
gorduras = porcao_arroz * alimentos.at[0, 'Gorduras (g)'] + \
           porcao_feijao * alimentos.at[1, 'Gorduras (g)'] + \
           porcao_frango * alimentos.at[2, 'Gorduras (g)']

# Calcular a ingestão total de carboidratos
carboidratos = porcao_arroz * alimentos.at[0, 'Carboidratos (g)'] + \
               porcao_feijao * alimentos.at[1, 'Carboidratos (g)'] + \
               porcao_frango * alimentos.at[2, 'Carboidratos (g)']

# Exibir o resultado
print("Ingestão total de calorias: ", calorias, "kcal")
print("Ingestão total de proteínas: ", proteinas, "g")
print("Ingestão total de gorduras: ", gorduras, "g")
print("Ingestão total de carboidratos: ", carboidratos,"g")
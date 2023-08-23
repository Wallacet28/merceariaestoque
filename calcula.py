

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

kivy.require('2.0.0')


def calcular_imc_valor(peso, altura):
    imc = peso / altura ** 2
    return imc


def definir_categoria_peso(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidade'


def calcular_taxa_metabolica_basal(peso, altura):
    bmr = 88.36 + (13.4 * peso) + (4.8 * altura * 100) - (5.7 * 30)  # 30 é a idade padrão para o cálculo
    return bmr


def calcular_calorias_diarias(peso, altura, categoria):
    bmr = calcular_taxa_metabolica_basal(peso, altura)
    if categoria == 'Abaixo do peso':
        factor = 1.6
    elif categoria == 'Peso normal':
        factor = 1.4
    elif categoria == 'Sobrepeso':
        factor = 1.2
    else:
        factor = 1.0
    calorias_diarias = bmr * factor
    return int(calorias_diarias)


class CalculadoraIMC(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dieta_label = None
        self.calcular_btn = None
        self.categoria_label = None
        self.resultado_label = None
        self.altura_input = None
        self.peso_input = None

    def build(self):
        layout = GridLayout(cols=2, spacing=10, padding=40)

        # Adicionando um Label e Input para o peso em kg
        layout.add_widget(Label(text='Peso (kg):'))
        self.peso_input = TextInput(multiline=False, size_hint=(.8, None), height=30)
        layout.add_widget(self.peso_input)

        # Adicionando um Label e Input para a altura em cm
        layout.add_widget(Label(text='Altura (cm):'))
        self.altura_input = TextInput(multiline=False, size_hint=(.8, None), height=30)
        layout.add_widget(self.altura_input)

        # Adicionando um Label para o resultado
        layout.add_widget(Label(text='Seu IMC:', size_hint=(.2, None), height=30))
        self.resultado_label = Label(text='', size_hint=(.8, None), height=30)
        layout.add_widget(self.resultado_label)

        # Adicionando um Label para mostrar a categoria de peso
        layout.add_widget(Label(text='Categoria de peso:', size_hint=(.2, None), height=30))
        self.categoria_label = Label(text='', size_hint=(.8, None), height=30)
        layout.add_widget(self.categoria_label)

        # Adicionando um botão para calcular o IMC
        self.calcular_btn = Button(text='Calcular', on_press=self.calcular_imc, size_hint=(.2, None), height=30)
        layout.add_widget(self.calcular_btn)

        # Adicionando um Label para mostrar a quantidade de calorias diárias recomendadas
        layout.add_widget(Label(text='Calorias diárias recomendadas:', size_hint=(.2, None), height=30))
        self.dieta_label = Label(text='', size_hint=(.8, None), height=30)
        layout.add_widget(self.dieta_label)

        return layout

    def calcular_imc(self):
        peso = float(self.peso_input.text)
        altura = float(self.altura_input.text) / 100  # Convertendo cm para m
        imc = calcular_imc_valor(peso, altura)
        categoria = definir_categoria_peso(imc)
        calorias_diarias = calcular_calorias_diarias(peso, altura, categoria)
        self.resultado_label.text = f'{imc:.2f}'
        self.categoria_label.text = categoria
        self.dieta_label.text = f'{calorias_diarias} calorias'


if __name__ == "__main__":
    CalculadoraIMC().run()
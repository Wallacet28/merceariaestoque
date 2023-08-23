
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CalculadoraAlimentos(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Define as cores usadas no design
        cor_principal = [0.11, 0.46, 0.97, 1]
        cor_secundaria = [0.98, 0.89, 0.51, 1]

        # Define os widgets da interface
        self.label_titulo = Label(text='Calculadora de Alimentos Saudáveis',
                                  font_size=30,
                                  color=cor_principal)
        self.label_restricao = Label(text='Restrição Calórica (kcal):',
                                     font_size=20,
                                     color=cor_principal)
        self.text_input_restricao = TextInput(multiline=False)
        self.label_alimento = Label(text='Nome do Alimento:',
                                    font_size=20,
                                    color=cor_principal)
        self.text_input_alimento = TextInput(multiline=False)
        self.label_calorias = Label(text='Calorias do Alimento (kcal):',
                                    font_size=20,
                                    color=cor_principal)
        self.text_input_calorias = TextInput(multiline=False)
        self.botao_calcular = Button(text='Calcular',
                                     background_color=cor_secundaria,
                                     color=cor_principal,
                                     font_size=20)
        self.label_resultado = Label(text='',
                                     font_size=20,
                                     color=cor_principal)

        # Adiciona os widgets ao layout
        self.add_widget(self.label_titulo)
        self.add_widget(self.label_restricao)
        self.add_widget(self.text_input_restricao)
        self.add_widget(self.label_alimento)
        self.add_widget(self.text_input_alimento)
        self.add_widget(self.label_calorias)
        self.add_widget(self.text_input_calorias)
        self.add_widget(self.botao_calcular)
        self.add_widget(self.label_resultado)

        # Associa a função de cálculo ao botão
        self.botao_calcular.bind(on_press=self.calcular_alimento)

    def calcular_alimento(self, *args):
        # Obtém os valores dos widgets de entrada
        restricao = float(self.text_input_restricao.text)
        alimento = self.text_input_alimento.text
        calorias = float(self.text_input_calorias.text)

        # Realiza o cálculo das porções do alimento
        porcoes = restricao / calorias
        resultado = f'{alimento} - {porcoes:.2f} porções'

        # Atualiza o label com o resultado
        self.label_resultado.text = resultado


class MyApp(App):

    def build(self):
        return CalculadoraAlimentos()


if __name__ == '__main__':
    MyApp().run()
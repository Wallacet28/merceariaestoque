from tkinter import Button

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class CalculadoraAlimentos(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'

        self.add_widget(Label(text='CALCULADORA DE ALIMENTOS', font_size=30, size_hint=(1, 0.3)))

        self.add_widget(Label(text='Insira a quantidade de calorias:'))
        self.calories_input = TextInput(multiline=False, input_type='number', input_filter='float')
        self.add_widget(self.calories_input)

        self.add_widget(Label(text='Insira a quantidade de carboidratos (em gramas):'))
        self.carbs_input = TextInput(multiline=False, input_type='number', input_filter='float')
        self.add_widget(self.carbs_input)

        self.add_widget(Label(text='Insira a quantidade de proteínas (em gramas):'))
        self.protein_input = TextInput(multiline=False, input_type='number', input_filter='float')
        self.add_widget(self.protein_input)

        self.add_widget(Label(text='Insira a quantidade de gorduras (em gramas):'))
        self.fat_input = TextInput(multiline=False, input_type='number', input_filter='float')
        self.add_widget(self.fat_input)

        self.result_label = Label(text='', font_size=20)
        self.add_widget(self.result_label)

        calculate_button = Button(text='Calcular')
        calculate_button.bind(on_press=self.calcular_alimentos)
        self.add_widget(calculate_button)

    def calcular_alimentos(self):
        try:
            calories = float(self.calories_input.text)
            carbs = float(self.carbs_input.text)
            protein = float(self.protein_input.text)
            fat = float(self.fat_input.text)

            total_grams = carbs + protein + fat
            carb_percent = carbs / total_grams * 100
            protein_percent = protein / total_grams * 100
            fat_percent = fat / total_grams * 100

            result_string = f'Carboidratos: {carb_percent:.2f}%\n'
            result_string += f'Proteínas: {protein_percent:.2f}%\n'
            result_string += f'Gorduras: {fat_percent:.2f}%'

            self.result_label.text = result_string
        except ValueError:
            self.result_label.text = 'Por favor, insira valores numéricos em todas as caixas de entrada.'


class MyApp(App):
    def build(self):
        return CalculadoraAlimentos()


if __name__ == '__main__':
    MyApp().run()
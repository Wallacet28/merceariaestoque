import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

kivy.require('2.0.0')


def get_imc_category(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Sobrepeso'
    elif imc < 35:
        return 'Obesidade grau 1'
    elif imc < 40:
        return 'Obesidade grau 2'
    else:
        return 'Obesidade grau 3'


class IMCCalculatorApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.calculate_btn = None
        self.height_input = None
        self.result_label = None
        self.weight_input = TextInput(multiline=False, size_hint=(.8, None), height=30)
        self.weight_input = None

    def build(self):
        layout = GridLayout(cols=2, spacing=10, padding=40)

        # Adding Label and Input for weight in kilograms
        layout.add_widget(Label(text='Peso (kg):'))
        layout.add_widget(self.weight_input)

        # Adding Label and Input for height in centimeters
        layout.add_widget(Label(text='Altura (cm):'))
        self.height_input = TextInput(multiline=False, size_hint=(.8, None), height=30)
        layout.add_widget(self.height_input)

        # Adding Label to show the result
        layout.add_widget(Label(text='Seu IMC:', size_hint=(.2, None), height=30))
        self.result_label = Label(text='', size_hint=(.8, None), height=30)
        layout.add_widget(self.result_label)

        # Adding Button to calculate the result
        self.calculate_btn = Button(text='Calcular IMC', on_press=self.calculate_imc, size_hint=(.2, None), height=30)
        layout.add_widget(self.calculate_btn)

        return layout

    def calculate_imc(self):
        weight = float(self.weight_input.text)
        assert isinstance(self.height_input.text, object)
        height = float(self.height_input.text) / 100  # converting cm to m
        imc = weight / (height ** 2)
        result_text = f'Seu IMC é {imc:.2f} ({get_imc_category(imc)})'
        self.result_label.text = result_text


if __name__ == '__main__':
    IMCCalculatorApp().run()

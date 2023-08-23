import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

kivy.require('2.0.0')


class HairSalonApp(App):

    def build(self):
        layout = GridLayout(cols=2, spacing=10, padding=40)

        # Adding Labels and Inputs for customer's name and appointment time
        layout.add_widget(Label(text='Nome do cliente:'))
        self.customer_name = TextInput(multiline=False, size_hint=(.8, None), height=30)
        layout.add_widget(self.customer_name)

        layout.add_widget(Label(text='Hora do agendamento:'))
        self.appointment_time = TextInput(multiline=False, size_hint=(.8, None), height=30)
        layout.add_widget(self.appointment_time)

        # Adding Labels and Buttons for different hair services
        layout.add_widget(Label(text='Serviços de cabelo:'))
        self.haircut_btn = Button(text='Corte de cabelo', on_press=self.haircut_selected, size_hint=(.8, None),
                                  height=30)
        layout.add_widget(self.haircut_btn)
        self.color_btn = Button(text='Coloração de cabelo', on_press=self.color_selected, size_hint=(.8, None),
                                height=30)
        layout.add_widget(self.color_btn)
        self.styling_btn = Button(text='Estilo de cabelo', on_press=self.styling_selected, size_hint=(.8, None),
                                  height=30)
        layout.add_widget(self.styling_btn)
        self.special_btn = Button(text='Serviços especiais', on_press=self.special_selected, size_hint=(.8, None),
                                  height=30)
        layout.add_widget(self.special_btn)

        # Adding Label to show the selected service
        layout.add_widget(Label(text='Serviço selecionado:', size_hint=(.2, None), height=30))
        self.selected_service = Label(text='', size_hint=(.8, None), height=30)
        layout.add_widget(self.selected_service)

        # Adding Button to confirm the appointment
        self.confirm_btn = Button(text='Confirmar', on_press=self.confirm_appointment, size_hint=(.2, None), height=30)
        layout.add_widget(self.confirm_btn)

        return layout

    def haircut_selected(self, instance):
        self.selected_service.text = 'Corte de cabelo selecionado'

    def color_selected(self, instance):
        self.selected_service.text = 'Coloração de cabelo selecionada'

    def styling_selected(self, instance):
        self.selected_service.text = 'Estilo de cabelo selecionado'

    def special_selected(self, instance):
        self.selected_service.text = 'Serviço especial selecionado'

    def confirm_appointment(self, instance):
        # Here you could add code to save the appointment to a database or send it to the salon's email
        appointment_details = f"Agendamento confirmado para {self.customer_name.text} às {self.appointment_time.text} para o serviço de {self.selected_service.text}"
        print(appointment_details)


if __name__ == '__main__':
    HairSalonApp().run()
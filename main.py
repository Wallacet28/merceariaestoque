from kivy.app import App
import kivy.uix.boxlayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class RegisterApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status = None
        self.email = None
        self.password = None
        self.username = None

    def build(self):
        self.username = TextInput(hint_text="Username")
        self.password = TextInput(hint_text="Password", password=True)
        self.email = TextInput(hint_text="Email")
        self.status = Label(text="")

        layout = kivy.uix.boxlayout.BoxLayout(orientation='vertical')
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.email)

        button = Button(text="Submit")
        button.bind(on_press=self.submit)
        layout.add_widget(button)
        layout.add_widget(self.status)

        return layout

    def submit(self):
        if self.username.text == "" or self.password.text == "" or self.email.text == "":
            self.status.text = "Please enter all fields"
        else:
            print("Username:", self.username.text)
            print("Password:", self.password.text)
            print("Email:", self.email.text)
            self.status.text = "Successful Registration"


if __name__ == '__main__':
    RegisterApp().run()


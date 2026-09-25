import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        self.secret = random.randint(1, 20)
        self.attempts = 0
        layout = BoxLayout(orientation="vertical")
        self.result_label = Label(text="Guess a number between 1 and 20")
        self.attempts_label = Label(text="Attempts: 0")
        self.input = TextInput(hint_text="Enter a number (1-20)", multiline=False)
        check_btn = Button(text="Check")
        check_btn.bind(on_press=self.check_guess)
        new_game_btn = Button(text="New Game")
        new_game_btn.bind(on_press=self.new_game)
        layout.add_widget(self.result_label)
        layout.add_widget(self.attempts_label)
        layout.add_widget(self.input)
        layout.add_widget(check_btn)
        layout.add_widget(new_game_btn)
        return layout

    def check_guess(self, instance):
        guess = int(self.input.text)
        self.attempts += 1
        self.attempts_label.text = "Attempts: " + str(self.attempts)
        if guess == self.secret:
            self.result_label.text = "Correct! You win in " + str(self.attempts) + " tries!"
        elif guess > self.secret:
            self.result_label.text = "Too high, try again"
        else:
            self.result_label.text = "Too low, try again"

    def new_game(self, instance):
        self.secret = random.randint(1, 20)
        self.attempts = 0
        self.attempts_label.text = "Attempts: 0"
        self.result_label.text = "Guess a number between 1 and 20"
        self.input.text = ""

MyApp().run()

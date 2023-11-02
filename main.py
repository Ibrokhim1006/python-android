import kivy

kivy.require("1.11.1")  # Kivy versiyasini kiritish

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text="Hi, Android!")


if __name__ == "__main__":
    MyApp().run()

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import kivy
kivy.require('1.10.1')

class MyApp(App):
    def build (self):

        fl = FloatLayout(size = (300, 300))
        fl.add_widget(Button(
        text = "this is my button",
        on_press = self.btn_press,
        background_color = [1, 0, 0, 1],
        size_hint = (.5, .25)));
        return fl

    def btn_press(self, instance):
        print('button pressed')
        instance.text = 'ready'

MyApp().run()

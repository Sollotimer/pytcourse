from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.gridlayout import GridLayout
import kivy
kivy.require('1.10.1')

class MyApp(App):
    def build (self):

        #fl = FloatLayout(size = (300, 300))
        bl = GridLayout(cols = 1, rows = 2, padding = [70], spacing = 30)
        bl.add_widget(Button(text = "this is my button", on_press = self.btn_press, background_color = [1, 0, 0, 1], size_hint = (.56, .25)))
        bl.add_widget(Button(text = "sec button", on_press = self.btn_press_but2, background_color = [0, 1, 0, 1], size_hint = (.22, .52)))
        return bl

    def btn_press(self, instance):
        print('button pressed')
        instance.text = 'ready'

    def btn_press_but2(seld, instance):
        instance.background_color = [1, 0, 0, 1]
MyApp().run()

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import kivy
kivy.require('1.10.1')

class MyApp(App):
    def build (self):
        #al = AnchorLayout(anchor_x = 'left', anchor_y = 'top')
        #fl = FloatLayout(size = (100, 300))
        #bl = GridLayout(cols = 1, rows = 2, padding = [70], spacing = 30)
        al = GridLayout(cols = 2, rows = 2, padding = [70], spacing = 30)
        bl = BoxLayout()
        bl.add_widget(Button(text = "this is my button", on_press = self.btn_press, background_color = [1, 0, 0, 1]))
        bl.add_widget(Button(text = "sec button", on_press = self.btn_press_but2, background_color = [0, 1, 0, 1]))
        al.add_widget(bl)
        al.add_widget( TextInput())
        al.add_widget( TextInput())
        al.add_widget( Button(text = "enter"))
        return al
        #fl.add_widget(bl)
        #return fl

    def btn_press(self, instance):
        print('button pressed')
        instance.text = 'ready'

    def btn_press_but2(seld, instance):
        instance.background_color = [1, 0, 0, 1]
MyApp().run()

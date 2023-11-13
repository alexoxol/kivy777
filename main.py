from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget

# Определяем наши окна
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('kv_MultipleWindows.kv')

class MyApp(App):
    def build(self):
        return kv

MyApp().run()

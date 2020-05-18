import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.clock import Clock

list = ["Transport", "F&B", "Learning"]

class MainWindow(Screen):
    def btn(self):
        show_popup()

    def update(self, dt):
        for i in range(len(list)):
            button = Button(text="B:" + list[i])
            self.add_widget(button)


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class Pop(FloatLayout):
    pass


kv = Builder.load_file("multi.kv")


class MyMainApp(App):
    def build(self):
        return kv



def show_popup():
    show = Pop()
    popupWindow = Popup(title="Popup window", content=show, size=(400,400), size_hint=(None, None))
    popupWindow.open()


if __name__ == "__main__":
    MyMainApp().run()
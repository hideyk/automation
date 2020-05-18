import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
import re


class Pop(FloatLayout):
    def __init__(self, **kwargs):
        super(Pop, self).__init__(**kwargs)
        self.text = "Hey there"


class FloatInput(TextInput):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        # Expense buttons
        self.expense_list = ["Transport", "F&B", "Learning"]
        self.expenses = GridLayout()
        self.expenses.cols = len(self.expense_list)
        for i in range(len(self.expense_list)):
            self.expenses.add_widget(Button(text=self.expense_list[i]))
        self.add_widget(self.expenses)

        # Value input
        self.inputs = GridLayout(size_hint=(0.3, 0.1))
        self.inputs.cols = 2
        self.inputs.add_widget(Label(text="Enter value:"))
        self.value = FloatInput(multiline=False)
        self.inputs.add_widget(self.value)
        self.add_widget(self.inputs)

        self.submit = Button(text="Submit", font_size=20)
        show = Pop()
        self.popup_window = Popup(title="Confirm submission?", content=show, size=(400,400), size_hint=(None, None))
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        value = self.value.text
        print(value)
        self.popup_window.open()
        self.value.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()

# self.inside.add_widget(Label(text="First name: "))
# self.firstName = TextInput(multiline=False)
# self.inside.add_widget(self.firstName)
#
# self.inside.add_widget(Label(text="Last name: "))
# self.lastName = TextInput(multiline=False)
# self.inside.add_widget(self.lastName)
#
# self.inside.add_widget(Label(text="Email: "))
# self.email = TextInput(multiline=False)
# self.inside.add_widget(self.email)
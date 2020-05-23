from expensetracker.project.DBConnector import PGConnection
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup


class Pop(GridLayout):
    def __init__(self, **kwargs):
        super(Pop, self).__init__(**kwargs)
        self.rows = 1
        self.cols = 2
        self.cnfmBtn = Button(text="Submit", background_color=(0.1, 0.7, 0.1, 1))
        self.cnclBtn = Button(text="Cancel", background_color=(0.7, 0.1, 0.1, 1))
        self.add_widget(self.cnfmBtn)
        self.add_widget(self.cnclBtn)


class NewCatScreen(Screen):
    def __init__(self, **kwargs):
        super(NewCatScreen, self).__init__(**kwargs)
        self.DB = PGConnection()
        self.expense_list = self.DB.get_expenses()
        self.revenue_list = self.DB.get_revenues()
        self.maingrid = GridLayout()
        self.maingrid.rows = 4
        self.maingrid.cols = 1

        # Colour
        self.expensesText = (1, 1, 1, 1)
        self.expensesBG = (0.04, 0.12, 0.4, 1)
        self.revenueText = (1, 1, 1, 1)
        self.revenueBG = (0.6, 0, 0, 1)
        self.changeBtnBG = (0.5, 0.5, 0.5, 1)

        def submita(self, instance):
            pass

        def switch_main(instance):
            self.manager.transition.direction = 'right'
            self.manager.current = "mainscreen"

        def submit_cat(instance):
            value = self.catInput.text
            print(value)
            showPopup = Pop()
            self.popup_window = Popup(title="Confirm submission?", content=showPopup, size=(300, 100),
                                      size_hint=(None, None))
            showPopup.cnclBtn.bind(on_release=self.popup_window.dismiss)
            # showPopup.cnfmBtn.bind(on_release=self.submita)
            self.popup_window.open()


        # Change to revenue
        self.catBox = GridLayout(size_hint=(0.3, 0.1))
        self.catBox.cols = 2
        self.catText = Label(text="New category:")
        self.catInput = TextInput(multiline=False)
        self.catBox.add_widget(self.catText)
        self.catBox.add_widget(self.catInput)

        # Category switch
        self.changeFlow = GridLayout(size_hint=(0.3, 0.1))
        self.changeFlow.cols = 1
        self.switchLabel = Label(text="Type:")
        self.switch = Switch(active=False)
        self.changeFlow.add_widget(self.switchLabel)
        self.changeFlow.add_widget(self.switch)

        # Submit button
        self.submitBtn = GridLayout(size_hint=(0.3, 1))
        self.submitBtn.rows = 1
        submit_btn = Button(text="Submit", background_color=(1, 1, 1, 1))
        submit_btn.bind(on_release=submit_cat)
        self.submitBtn.add_widget(submit_btn)

        # Back to main menu
        self.backBtn = GridLayout(size_hint=(0.3, 1))
        self.backBtn.rows = 1
        new_category_btn = Button(pos_hint={'top': 0.5}, text="Back", background_color=(1, 1, 1, 1))
        new_category_btn.bind(on_release=switch_main)
        self.backBtn.add_widget(new_category_btn)

        self.maingrid.add_widget(self.catBox)
        self.maingrid.add_widget(self.changeFlow)
        self.maingrid.add_widget(self.submitBtn)
        self.maingrid.add_widget(self.backBtn)
        self.add_widget(self.maingrid)
from expensetracker.project.DBConnector import PGConnection
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class SubcatScreen(Screen):

    def __init__(self, **kwargs):
        super(SubcatScreen, self).__init__(**kwargs)
        self.DB = PGConnection()
        self.expense_list = self.DB.get_expenses()
        self.revenue_list = self.DB.get_revenues()
        self.maingrid = GridLayout()
        self.maingrid.rows = 3
        self.maingrid.cols = 1
        self.category = ""

        self.changeBtn = GridLayout(size_hint=(0.3, 1))
        self.changeBtn.rows = 1
        add_revenue_btn = Button(text="Add revenue", size_hint=(0.3, 0.3))
        # add_revenue_btn.bind(on_release=call_revenue)
        self.changeBtn.add_widget(add_revenue_btn)

        # Change to expense
        add_expense_btn = Button(text="Add expense", size_hint=(0.3, 0.3))
        # add_expense_btn.bind(on_release=call_expense)

        # Add another category
        self.button = GridLayout(size_hint=(0.3, 1))
        self.button.rows = 1
        self.button.add_widget(
            Button(pos_hint={'top': 0.5}, text="Add another category?", background_color=(1, 1, 1, 1)))

        self.maingrid.add_widget(self.changeBtn)
        self.maingrid.add_widget(self.button)
        self.add_widget(self.maingrid)
        print("hello")
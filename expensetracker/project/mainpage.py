from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from expensetracker.project.DBConnector import PGConnection
from expensetracker.project.subcatpage import SubcatScreen
from expensetracker.project.newcatpage import NewCatScreen
import math


class MainScreen(Screen):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.DB = PGConnection()
        self.expense_list = self.DB.get_expenses()
        self.revenue_list = self.DB.get_revenues()
        self.maingrid = GridLayout()
        self.maingrid.rows = 3
        self.maingrid.cols = 1
        global category


        # Colour
        self.expensesText = (1, 1, 1, 1)
        self.expensesBG = (0.04, 0.12, 0.4, 1)
        self.revenueText = (1, 1, 1, 1)
        self.revenueBG = (0.6, 0, 0, 1)
        self.changeBtnBG = (0.5, 0.5, 0.5, 1)

        def switch_subcat(instance):
            global category
            category = instance.text
            self.subcatscreen = SubcatScreen(name="subcatscreen")
            self.subcatscreen.category = category
            self.manager.add_widget(self.subcatscreen)
            self.manager.transition.direction = 'left'
            self.manager.current = "subcatscreen"

        def switch_newcat(instance):
            self.newcatscreen = NewCatScreen(name="newcatscreen")
            self.manager.add_widget(self.newcatscreen)
            self.manager.transition.direction = 'left'
            self.manager.current = "newcatscreen"

        # Expenses
        self.expenses = GridLayout(size_hint=(0.4, 5))
        self.expensecount = len(self.expense_list)
        self.expenses.rows = math.ceil(self.expensecount/3)
        self.expenses.cols = self.expensecount if self.expensecount < 3 else 3
        for i in range(self.expensecount):
            expense_button = Button(text=self.expense_list[i], color=self.expensesText, background_color=self.expensesBG)
            expense_button.bind(on_press=switch_subcat)
            self.expenses.add_widget(expense_button)

        # Revenue
        self.revenue = GridLayout(size_hint=(0.4, 5))
        self.revenuecount = len(self.revenue_list)
        self.revenue.rows = math.ceil(self.revenuecount / 3)
        self.revenue.cols = self.revenuecount if self.revenuecount < 3 else 3
        for i in range(self.revenuecount):
            revenue_button = Button(text=self.revenue_list[i], color=self.revenueText, background_color=self.revenueBG)
            revenue_button.bind(on_press=switch_subcat)
            self.revenue.add_widget(revenue_button)


        def call_revenue(instance):
            self.changeBtn.clear_widgets()
            self.changeBtn.add_widget(add_expense_btn)
            self.maingrid.clear_widgets()
            self.maingrid.add_widget(self.revenue)
            self.maingrid.add_widget(self.changeBtn)
            self.maingrid.add_widget(self.button)

        def call_expense(instance):
            self.changeBtn.clear_widgets()
            self.changeBtn.add_widget(add_revenue_btn)
            self.maingrid.clear_widgets()
            self.maingrid.add_widget(self.expenses)
            self.maingrid.add_widget(self.changeBtn)
            self.maingrid.add_widget(self.button)


        # Change to revenue
        self.changeBtn = GridLayout(size_hint=(0.3, 1))
        self.changeBtn.rows = 1
        add_revenue_btn = Button(text="Switch to revenue", size_hint=(0.3, 0.3))
        add_revenue_btn.bind(on_release=call_revenue)
        self.changeBtn.add_widget(add_revenue_btn)

        # Change to expense
        add_expense_btn = Button(text="Switch to expense", size_hint=(0.3, 0.3))
        add_expense_btn.bind(on_release=call_expense)

        # Add another category
        self.button = GridLayout(size_hint=(0.3, 1))
        self.button.rows = 1
        new_category_btn = Button(pos_hint={'top': 0.5}, text="Add another category?", background_color=(1, 1, 1, 1))
        new_category_btn.bind(on_release=switch_newcat)
        self.button.add_widget(new_category_btn)

        self.maingrid.add_widget(self.expenses)
        self.maingrid.add_widget(self.changeBtn)
        self.maingrid.add_widget(self.button)
        self.add_widget(self.maingrid)


class MainScreenApp(App):
    def build(self):
        self.title = "Expense tracker"
        return MainScreen()


if __name__ == "__main__":
    MainScreenApp().run()

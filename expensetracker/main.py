from expensetracker.project.DBConnector import PGConnection
from expensetracker.project.mainpage import MainScreen

from kivy.uix.screenmanager import ScreenManager
from kivy.app import App


class AppScreen(ScreenManager):
    def __init__(self, **kwargs):
        super(AppScreen, self).__init__(**kwargs)
        self.category = ""
        self.mainscreen = MainScreen(name="mainscreen")
        self.add_widget(self.mainscreen)


class MainScreenApp(App):
    def build(self):
        self.title = "Expense tracker"
        return AppScreen()


if __name__ == "__main__":
    MainScreenApp().run()
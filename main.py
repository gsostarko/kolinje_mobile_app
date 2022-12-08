from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.toast import toast

# CUSTOM LIBRARIES
from database import DatabaseManagement

Window.size = (330 ,732)


    

class KolinjeApp(MDApp):
    global screen_manager
    screen_manager = ScreenManager()

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.title = "KolinjeApp"

        screen_manager.add_widget(Builder.load_file('login.kv'))
        screen_manager.add_widget(Builder.load_file('register.kv'))

        return screen_manager 

    def NewUserRegistration(self):
        #Calling specific screen
        registration_screen = self.root.get_screen('RegisterScreen')
        username = registration_screen.ids.username.text
        email = registration_screen.ids.email.text
        password = registration_screen.ids.password.text
        password_confirmation = registration_screen.ids.password_confirmation.text
        if password == password_confirmation:
            DatabaseManagement.NewUserRegistration(username = username, password = password, email = email)
            toast(f"korisnik {username} je uspješno registriran.")
            screen_manager.current = "LoginScreen"

            #Fields Clearing
            registration_screen.ids.username.text = ''
            registration_screen.ids.email.text = ''
            registration_screen.ids.password.text = ''
            registration_screen.ids.password_confirmation.text = ''

        else:
            toast("Došlo je do greške")

    def UserLogin(self):
        login_screen = self.root.get_screen('LoginScreen')
        username = login_screen.ids.username.text
        password = login_screen.ids.password.text


    def ChangeScreen(self, screen_name):
        screen_manager.current = str(screen_name)


if __name__ == "__main__":
    KolinjeApp().run()
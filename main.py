from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.toast import toast
from kivy.clock import Clock

# CUSTOM LIBRARIES
from database import DatabaseManagement, DatabaseQuery

Window.size = (330 ,732)


    

class KolinjeApp(MDApp):
    global screen_manager
    screen_manager = ScreenManager()

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.title = "KolinjeApp"

        screen_manager.add_widget(Builder.load_file('splash.kv'))
        screen_manager.add_widget(Builder.load_file('login.kv'))
        screen_manager.add_widget(Builder.load_file('register.kv'))
        screen_manager.add_widget(Builder.load_file('main.kv'))
        screen_manager.add_widget(Builder.load_file('recepies.kv'))

        return screen_manager 

    

    def NewUserRegistration(self):
        #Calling specific screen
        registration_screen = self.root.get_screen('RegisterScreen')
        username = registration_screen.ids.username.text
        email = registration_screen.ids.email.text
        password = registration_screen.ids.password.text
        password_confirmation = registration_screen.ids.password_confirmation.text
       
        if password !='' and password_confirmation != '' and username !='' and email != '':
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
                toast("Lozinke se moraju podudarati")
        else:
            toast('Molim vas popunite sva polja')

    def UserLogin(self):
        global current_user 
        login_screen = self.root.get_screen('LoginScreen')
        username = login_screen.ids.username.text
        password = login_screen.ids.password.text
        data = DatabaseQuery.LoginQuery(username,password)
        if data[0] == True: 
            screen_manager.current = str('MainScreen')
            current_user = data[1]

            login_screen.ids.username.text = ''
            login_screen.ids.password.text = ''
            toast(f'Uspješno ste se prijavili kao {current_user}')
        else:
            toast('Korisnik ne postoji i/ili je pogrešna lozinka')

    def ChangeScreen(self, screen_name):
        screen_manager.current = str(screen_name)


    def on_start(self):
        splash = self.root.get_screen('Splash')
        Clock.schedule_once(self.change_splash, 5)
        for i in range(5):
            animate = Animation(size_hint=(0.9,0.9))
            animate += Animation(size_hint=(1,1))
            animate += Animation(size_hint=(0.9,0.9))
            animate += Animation(size_hint=(1,1))
            animate += Animation(size_hint=(0.9,0.9))
            animate += Animation(size_hint=(1,1))
        animate.start(splash.ids.logo_img)
    def change_splash(self, x):
        screen_manager.current = "LoginScreen"

if __name__ == "__main__":
    KolinjeApp().run()
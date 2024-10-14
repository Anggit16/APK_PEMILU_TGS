from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class TestLogin(Screen):
    pass

    def do_login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        
        
        if username == "admin" and password == "12345":
            self.manager.current = 'menu'
            self.show_popup("Login Berhasil", "Selamat Datang")
        else:
            self.show_popup("Login Gagalll", "Username atau Password Salah!!!")
        
        
        
    def show_popup(self, title, message):
        popup_content = Label(text=message)
        popup = Popup(title=title, content=popup_content, size_hint=(None, None), size=(300, 200))
        popup.open()

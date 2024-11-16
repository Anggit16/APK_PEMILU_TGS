from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class PemilihanRt(Screen):
    def next_page(self):
        self.manager.current = 'pemilihanrt'
        self.show_popup("Success", "Anda Berhasil Memilih")
        return
    
    
    def show_popup(self, title, message):
        popup_content = Label(text=message)
        popup = Popup(title=title, content=popup_content, size_hint=(None, None), size=(300, 200))
        popup.open()
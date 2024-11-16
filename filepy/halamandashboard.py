from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

class TestDashboard(Screen):
    def logout_popup(self):
        # Membuat popup
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Teks konfirmasi
        popup_label = Label(text="Apakah kamu ingin Logout?")

        # Membuat tombol Ya dan Tidak
        button_layout = BoxLayout(spacing=20)
        yes_button = Button(text="Ya", size_hint=(0.5, 1))
        no_button = Button(text="Tidak", size_hint=(0.5, 1))

        # Mengatur aksi tombol
        yes_button.bind(on_press=self.logout)
        no_button.bind(on_press=self.logoutNo)

        # Menambahkan tombol ke layout
        button_layout.add_widget(yes_button)
        button_layout.add_widget(no_button)

        # Menambahkan teks dan tombol ke popup layout
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(button_layout)

        # Membuat dan menampilkan popup
        self.popup = Popup(title="Logout Confirmation",
                           content=popup_layout,
                           size_hint=(None, None),
                           size=(300, 200))
        self.popup.open()

    def logout(self, instance):
        # Menutup popup
        self.popup.dismiss()

        # Mengalihkan layar kembali ke halaman login
        App.get_running_app().root.current = 'login'  # Pastikan ID layar login adalah 'login_screen'

    def logoutNo(self,instance):
        # Menutup popup
        self.popup.dismiss()        

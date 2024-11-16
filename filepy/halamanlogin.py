from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import Database

class TestLogin(Screen):
    def do_login(self):
        nama = self.ids.nama_input.text
        pw = self.ids.pw_input.text

        # Cek login untuk admin secara langsung
        if nama == "admin" and pw == "12345":
            self.manager.current = 'menu'
            self.show_popup("Login Berhasil", "Selamat Datang, Admin")
            return

        # Login untuk pengguna biasa menggunakan data dari Firebase
        if nama and pw:
            try:
                # Ambil data pengguna berdasarkan username dari Firebase
                print(f"Trying to fetch data for username: {nama}")
                user_data = Database.get_product_by_name(nama)  # Mengakses metode get_product_by_name di Database

                if user_data:
                    stored_password = user_data.get('pw')
                    print(f"Stored password: {stored_password}")
                    print(f"Entered password: {pw}")

                    if stored_password == pw:
                        print("Password matched")
                        self.show_popup("Sukses", "Login berhasil!")
                        self.manager.current = 'dashboard'
                    else:
                        print("Password did not match")
                        self.show_popup("Error", "Nama atau password salah.")
                else:
                    print("User data not found")
                    self.show_popup("Error", "Nama atau password salah.")
            except Exception as e:
                self.show_popup("Error", f"Terjadi kesalahan: {str(e)}")
        else:
            self.show_popup("Error", "Nama dan password harus diisi.")

    def show_popup(self, title, message):
        popup_content = Label(text=message)
        popup = Popup(title=title, content=popup_content, size_hint=(None, None), size=(300, 200))
        popup.open()

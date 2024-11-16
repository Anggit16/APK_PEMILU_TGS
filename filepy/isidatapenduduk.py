import pyrebase
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class DataPenduduk:
# class ProductItem(BoxLayout):
    def __init__(self, product_id, product_data, delete_callback, edit_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 120
        self.padding = 5
        self.spacing = 10

        # Save product id and data
        self.product_id = product_id
        self.product_data = product_data

        # Create info layout
        info_layout = BoxLayout(orientation='vertical', size_hint_x=0.7)
        
        # Product info label
        name = product_data.get('nama', 'No Name')
        nik = product_data.get('nik', 0)
        pw = product_data.get('pw', 0)
        
        info_label = Label(
            text=f"Nama: {name}\nNIK: {nik}\nPassword: {pw}",
            size_hint_y=None,
            height=100,
            halign='left',
            valign='middle',
            color=(0, 0, 0, 1)
        )
        info_label.bind(size=info_label.setter('text_size'))
        info_layout.add_widget(info_label)

        # Button layout
        button_layout = BoxLayout(orientation='vertical', size_hint_x=0.3, spacing=5)
        
        edit_btn = Button(text='Edit', size_hint_y=0.5, background_color=(0.3, 0.5, 0.9, 1))
        edit_btn.bind(on_press=lambda x: edit_callback(product_id, product_data))
        
        delete_btn = Button(text='Hapus', size_hint_y=0.5, background_color=(0.9, 0.3, 0.3, 1))
        delete_btn.bind(on_press=lambda x: delete_callback(product_id))

        button_layout.add_widget(edit_btn)
        button_layout.add_widget(delete_btn)

        self.add_widget(info_layout)
        self.add_widget(button_layout)


class Penduduk(Screen):
    container = ObjectProperty(None)  # Container untuk menampilkan daftar penduduk

    def on_enter(self):
        # Ketika memasuki layar ini, ambil data penduduk dan tampilkan
        self.display_all_datapenduduk()

    def display_all_datapenduduk(self):
        # Hapus data sebelumnya di container
        self.container.clear_widgets()

        # Dapatkan semua data penduduk dari Firebase
        all_data = DataPenduduk.get_all_datapenduduk()
        for data in all_data:
            # Buat Label untuk setiap data penduduk dan tambahkan ke container
            penduduk_label = Label(
                text=f"Nama: {data['nama']}\nNIK: {data['nik']}\nPassword: {data['password']}",
                size_hint_y=None,
                height=100,
                halign='left',
                valign='middle'
            )
            self.container.add_widget(penduduk_label)


class IsiDataPenduduk(Screen):
    nama_input = ObjectProperty(None)
    nik_input = ObjectProperty(None)
    pw_input = ObjectProperty(None)

    def add_datapenduduk(self):
        datapenduduk_data = {
            'nama': self.ids.nama_input.text.strip(),
            'nik': self.ids.nik_input.text.strip(),
            'password': self.ids.pw_input.text.strip(),
        }

        if datapenduduk_data['nama'] and datapenduduk_data['nik'] and datapenduduk_data['password']:
            DataPenduduk.add_datapenduduk(datapenduduk_data)

            # Menampilkan pesan sukses
            popup = Popup(title='Sukses', content=Label(text='Data penduduk berhasil ditambahkan!'), size_hint=(None, None), size=(400, 200))
            popup.open()

            # Bersihkan input setelah data ditambahkan
            self.ids.nama_input.text = ""
            self.ids.nik_input.text = ""
            self.ids.pw_input.text = ""
        else:
            popup = Popup(title='Error', content=Label(text='Semua field harus diisi!'), size_hint=(None, None), size=(400, 200))
            popup.open()
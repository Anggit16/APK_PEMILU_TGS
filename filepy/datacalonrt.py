from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.filechooser import FileChooserIconView
from database import Database
from storage import StorageManager

class DataCalonrtItem(BoxLayout):
    def __init__(self, calonrt_id, calonrt_data, delete_callback, edit_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 200
        self.padding = 5
        self.spacing = 10
        

        # Save calonrw id and data
        self.calonrt_id = calonrt_id
        self.calonrt_data = calonrt_data
        
        # Create image layout
        image_layout = BoxLayout(size_hint_x=0.3, padding=5)
        image_url = calonrt_data.get('image_url', None)
        if image_url:
            calonrt_image = AsyncImage(
                source=image_url,
                allow_stretch=True,
                keep_ratio=True
            )
            image_layout.add_widget(calonrt_image)
        else:
            image_layout.add_widget(
                Label(
                    text='No Image',
                    color=(0, 0, 0, 1)  # Set color to black
                )
            )

        # Create info layout
        info_layout = BoxLayout(orientation='vertical', size_hint_x=0.7)
        
        # Product info label
        name = calonrt_data.get('nama', 'No Name')
        vm = calonrt_data.get('vm', 'No Visi')
        
        info_label = Label(
            text=f"Nama: {name}\nVisiMisi: {vm}",
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
        edit_btn.bind(on_press=lambda x: edit_callback(calonrt_id, calonrt_data))
        
        delete_btn = Button(text='Hapus', size_hint_y=0.5, background_color=(0.9, 0.3, 0.3, 1))
        delete_btn.bind(on_press=lambda x: delete_callback(calonrt_id))

        button_layout.add_widget(edit_btn)
        button_layout.add_widget(delete_btn)

        self.add_widget(image_layout)
        self.add_widget(info_layout)
        self.add_widget(button_layout)
        
    def show_popup(self, title, content):
        popup = Popup(
            title=title,
            content=Label(text=content, color=(0, 0, 0, 1)),  # Set color to black
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()

class DataCalonrtList(Screen):
    container = ObjectProperty(None)
    
    def on_enter(self):
        self.load_calonrts()
    
    def load_calonrts(self):
        self.container.clear_widgets()
        calonrts = Database.get_all_calonrts()
        
        if calonrts:
            for calonrt_id, calonrt_data in calonrts:
                calonrt_item = DataCalonrtItem(
                    calonrt_id,
                    calonrt_data,
                    self.delete_calonrt,
                    self.edit_calonrt
                )
                self.container.add_widget(calonrt_item)
        else:
            self.container.add_widget(
                Label(
                    text="Tidak ada produk tersedia",
                    size_hint_y=None,
                    height=100
                )
            )
    
    def show_add_calonrt(self):
        self.manager.current = 'add_dataclnrt'

    def edit_calonrt(self, calonrt_id, calonrt_data):
        edit_screen = self.manager.get_screen('edit_dataclnrt')
        edit_screen.set_calonrt(calonrt_id, calonrt_data)
        self.manager.current = 'edit_dataclnrt'

    def delete_calonrt(self, calonrt_id):
        confirm_popup = Popup(
            title='Konfirmasi',
            size_hint=(None, None),
            size=(300, 200)
        )
        
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text='Apakah Anda yakin ingin\nmenghapus produk ini?'))
        
        buttons = BoxLayout(size_hint_y=None, height=40, spacing=10)
        
        cancel_btn = Button(text='Batal')
        cancel_btn.bind(on_press=confirm_popup.dismiss)
        
        def confirm_delete(instance):
            try:
                # Get product data to delete image if exists
                calonrts = Database.get_all_calonrts()
                calonrt_data = next((data for pid, data in calonrts if pid == calonrt_id), None)
                
                if calonrt_data and 'image_path' in calonrt_data:
                    StorageManager.delete_image(calonrt_data['image_path'])
                
                Database.delete_calonrt(calonrt_id)
                self.load_calonrts()
                confirm_popup.dismiss()
                self.show_popup('Sukses', 'Produk berhasil dihapus!')
            except Exception as e:
                confirm_popup.dismiss()
                self.show_popup('Error', f'Gagal menghapus produk: {str(e)}')
        
        confirm_btn = Button(text='Hapus', background_color=(0.9, 0.3, 0.3, 1))
        confirm_btn.bind(on_press=confirm_delete)
        
        buttons.add_widget(cancel_btn)
        buttons.add_widget(confirm_btn)
        
        content.add_widget(buttons)
        confirm_popup.content = content
        confirm_popup.open()

    def show_popup(self, title, content):
        popup = Popup(
            title=title,
            content=Label(text=content),
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()

class AddDataCalonrt(Screen):
    name_input = ObjectProperty(None)
    vm_input = ObjectProperty(None)
    image_foto = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_image = None
        
    def choose_image(self):
        popup = ImageChooserPopup(callback=self.on_image_selected)
        popup.open()
        
    def on_image_selected(self, file_path):
        self.selected_image = file_path
        self.image_foto.source = file_path
    
    def clear_image(self):
        self.selected_image = None
        self.image_foto.source = ''
    
    def add_calonrt(self):
        nama = self.name_input.text.strip()
        vm = self.vm_input.text.strip()
        
        if nama and vm:
            try:
               # Upload image if selected
                image_url = None
                image_path = None
                if self.selected_image:
                    result = StorageManager.upload_image(self.selected_image)
                    if result["status"] == "success":
                        image_url = result["url"]
                        image_path = result["path"]
                        
                # create datacalonrw
                calonrt_data = {
                    'nama': nama,
                    'vm': vm,
                    'image_url': image_url,
                    'image_path': image_path
                } 
                
                Database.add_calonrt(calonrt_data)
                self.name_input.text = ''
                self.vm_input.text = ''
                self.selected_image = None
                self.image_foto.source = ''
                
                self.show_popup('Sukses', 'Produk berhasil ditambahkan!')
                self.manager.current = 'dataclnrt'
            except ValueError:
                self.show_popup('Error', 'nik harus berupa angka!')
            except Exception as e:
                self.show_popup('Error', f'Terjadi kesalahan: {str(e)}')
        else:
            self.show_popup('Error', 'Semua field harus diisi!')
    
    def show_popup(self, title, content):
        popup = Popup(
            title=title,
            content=Label(text=content),
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()
    
    def cancel(self):
        self.manager.current = 'dataclnrt'

class EditDataCalonrt(Screen):
    name_input = ObjectProperty(None)
    vm_input = ObjectProperty(None)
    image_foto = ObjectProperty(None)
    calonrw_id = StringProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_image = None
        self.current_image_path = None

    def on_enter(self):
        if hasattr(self, 'calonrt_data'):
            self.name_input.text = str(self.calonrt_data.get('nama', ''))
            self.vm_input.text = str(self.calonrt_data.get('vm', ''))
            self.current_image_path = self.calonrt_data.get('image_path', None)
            if self.calonrt_data.get('image_url'):
                self.image_preview.source = self.calonrt_data['image_url']

    def choose_image(self):
        popup = ImageChooserPopup(callback=self.on_image_selected)
        popup.open()
    
    def on_image_selected(self, file_path):
        self.selected_image = file_path
        self.image_foto.source = file_path
        
    def clear_image(self):
        self.selected_image = None
        self.image_foto.source = ''
        if self.current_image_path:
            StorageManager.delete_image(self.current_image_path)
            self.current_image_path = None
            
    def set_calonrt(self, calonrt_id, calonrt_data):
        self.calonrt_id = calonrt_id
        self.calonrt_data = calonrt_data

    def update_calonrt(self):
        nama = self.name_input.text.strip()
        vm = self.vm_input.text.strip()
        
        if nama and vm:
            try:
                image_url = self.calonrt_data.get('image_url')
                image_path = self.current_image_path
                
                if self.selected_image:
                    result = StorageManager.update_image(
                        self.current_image_path,
                        self.selected_image
                    )
                    if result["status"] == "success":
                        image_url = result["url"]
                        image_path = result["path"]
                
                calonrt_data = {
                    'nama': nama,
                    'vm': vm,
                    'image_url': image_url,
                    'image_path': image_path
                    
                }
                
                Database.update_calonrt(self.calonrt_id, calonrt_data)
                self.show_popup('Sukses', 'Produk berhasil diupdate!')
                self.manager.current = 'dataclnrt'
            except ValueError:
                self.show_popup('Error', 'nik  harus berupa angka!')
            except Exception as e:
                self.show_popup('Error', f'Terjadi kesalahan: {str(e)}')
        else:
            self.show_popup('Error', 'Semua field harus diisi!')

    def show_popup(self, title, content):
        popup = Popup(
            title=title,
            content=Label(text=content),
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()

    def cancel(self):
        self.manager.current = 'dataclnrt'
        
        
class ImageChooserPopup(Popup):
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Pilih Gambar'
        self.size_hint = (0.9, 0.9)
        self.callback = callback
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.file_chooser = FileChooserIconView(
            filters=['*.png', '*.jpg', '*.jpeg'],
            path='.')
        layout.add_widget(self.file_chooser)
        
        button_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        
        cancel_btn = Button(text='Batal')
        cancel_btn.bind(on_press=self.dismiss)
        
        select_btn = Button(text='Pilih', background_color=(0.3, 0.5, 0.9, 1))
        select_btn.bind(on_press=self.select_image)
        
        button_layout.add_widget(cancel_btn)
        button_layout.add_widget(select_btn)
        
        layout.add_widget(button_layout)
        self.content = layout
        
    def select_image(self, instance):
        if self.file_chooser.selection:
            self.callback(self.file_chooser.selection[0])
            self.dismiss()

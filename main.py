import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from filepy.halamanlogin import TestLogin
# admin
from filepy.halamanmenu import TestMenu
from filepy.tambahcalon import TestCalon
# from filepy.isidatacalonrt import TestCalonrt
# from filepy.isidatacalonrw import TestCalonrw
from filepy.datacalonrw import DataCalonrwItem, DataCalonrwList, AddDataCalonrw, EditDataCalonrw
from filepy.datacalonrt import DataCalonrtItem, DataCalonrtList, AddDataCalonrt, EditDataCalonrt
from filepy.calonrw1 import TestCalonrw1
from filepy.calonrt1 import TestCalonrt1
from filepy.datapenduduk import DataPenduduk
from filepy.isidatapenduduk import IsiDataPenduduk, Penduduk
from filepy.pemilihanhasilad import HasilAd
from filepy.hasilrwad import HasilrwAd
from filepy.hasilrtad import HasilrtAd
from filepy.tes import ProductItem, ProductList, EditProduct, AddProduct
# user
from filepy.halamandashboard import TestDashboard
from filepy.pemilihanrw import PemilihanRw
from filepy.pemilihanrt import PemilihanRt
from filepy.profile import Profile
from filepy.pemilihanhasilus import HasilUs
from filepy.hasilrtus import Hasil
from filepy.hasilrwus import Hasil2

from kivy.lang import Builder
from kivy.core.window import Window

class MyScreenManager(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        Window.size = (370, 782)
        Window.clearcolor = (1, 1, 1, 1)
        kv_path = os.path.join(os.path.dirname(__file__), 'filekv')
        Builder.load_file(os.path.join(kv_path, 'halamanlogin.kv'))
        # admin kv
        Builder.load_file(os.path.join(kv_path, 'halamanmenu.kv'))
        Builder.load_file(os.path.join(kv_path, 'tambahcalon.kv'))
        # Builder.load_file(os.path.join(kv_path, 'isidatacalonrt.kv'))
        # Builder.load_file(os.path.join(kv_path, 'isidatacalonrw.kv'))
        Builder.load_file(os.path.join(kv_path, 'datacalonrw.kv'))
        Builder.load_file(os.path.join(kv_path, 'datacalonrt.kv'))
        Builder.load_file(os.path.join(kv_path, 'calonrw1.kv'))
        Builder.load_file(os.path.join(kv_path, 'calonrt1.kv'))
        Builder.load_file(os.path.join(kv_path, 'datapenduduk.kv'))
        Builder.load_file(os.path.join(kv_path, 'isidatapenduduk.kv'))
        Builder.load_file(os.path.join(kv_path, 'pemilihanhasilad.kv'))
        Builder.load_file(os.path.join(kv_path, 'hasilrwad.kv'))
        Builder.load_file(os.path.join(kv_path, 'hasilrtad.kv'))
        Builder.load_file(os.path.join(kv_path, 'tes.kv'))
        # user kv
        Builder.load_file(os.path.join(kv_path, 'halamandashboard.kv'))
        Builder.load_file(os.path.join(kv_path, 'pemilihanrw.kv'))
        Builder.load_file(os.path.join(kv_path, 'pemilihanrt.kv'))
        Builder.load_file(os.path.join(kv_path, 'profile.kv'))
        Builder.load_file(os.path.join(kv_path, 'pemilihanhasilus.kv'))
        Builder.load_file(os.path.join(kv_path, 'hasilrtus.kv'))
        Builder.load_file(os.path.join(kv_path, 'hasilrwus.kv'))
        
        smanager = MyScreenManager()
        smanager.add_widget(TestLogin(name='login'))
        # admin
        smanager.add_widget(TestMenu(name='menu'))
        smanager.add_widget(TestCalon(name='tambahcln'))
        # smanager.add_widget(TestCalonrt(name='dataclnrt'))
        smanager.add_widget(DataCalonrtList(name='dataclnrt'))
        smanager.add_widget(AddDataCalonrt(name='add_dataclnrt'))
        smanager.add_widget(EditDataCalonrt(name='edit_dataclnrt'))
        # smanager.add_widget(TestCalonrw(name='dataclnrw'))
        smanager.add_widget(DataCalonrwList(name='dataclnrw'))
        smanager.add_widget(AddDataCalonrw(name='add_dataclnrw'))
        smanager.add_widget(EditDataCalonrw(name='edit_dataclnrw'))
        # smanager.add_widget(TestDatarw(name='datarw'))
        # smanager.add_widget(TestDatart(name='datart'))
        smanager.add_widget(TestCalonrw1(name='calonrw1'))
        smanager.add_widget(TestCalonrt1(name='calonrt1'))
        # smanager.add_widget(DataPenduduk(name='datapenduduk'))
        # smanager.add_widget(IsiDataPenduduk(name='isidatapenduduk'))
        # smanager.add_widget(Penduduk(name='penduduk'))
        smanager.add_widget(HasilAd(name='hasilad'))
        smanager.add_widget(HasilrwAd(name='hasilrwad'))
        smanager.add_widget(HasilrtAd(name='hasilrtad'))
        smanager.add_widget(ProductList(name='product_list'))
        smanager.add_widget(AddProduct(name='add_product'))
        smanager.add_widget(EditProduct(name='edit_product'))
        # user
        smanager.add_widget(TestDashboard(name='dashboard'))
        smanager.add_widget(PemilihanRw(name='pemilihanrw'))
        smanager.add_widget(PemilihanRt(name='pemilihanrt'))
        smanager.add_widget(Profile(name='profile'))
        smanager.add_widget(HasilUs(name='hasil'))
        smanager.add_widget(Hasil(name='hasilrtus'))
        smanager.add_widget(Hasil2(name='hasilrwus'))
        
        smanager.current = 'login' #untuk menjadikan halaman tampil pertama
        return smanager
if __name__ == '__main__':
    MyApp().run()
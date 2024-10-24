import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from filepy.halamanlogin import TestLogin
from filepy.halamanmenu import TestMenu
from filepy.tambahcalon import TestCalon
from filepy.isidatacalonrt import TestCalonrt
from filepy.isidatacalonrw import TestCalonrw
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
        Builder.load_file(os.path.join(kv_path, 'halamanmenu.kv'))
        Builder.load_file(os.path.join(kv_path, 'tambahcalon.kv'))
        Builder.load_file(os.path.join(kv_path, 'isidatacalonrt.kv'))
        Builder.load_file(os.path.join(kv_path, 'isidatacalonrw.kv'))
        smanager = MyScreenManager()
        smanager.add_widget(TestLogin(name='login'))
        smanager.add_widget(TestMenu(name='menu'))
        smanager.add_widget(TestCalon(name='tambahcln'))
        smanager.add_widget(TestCalonrt(name='dataclnrt'))
        smanager.add_widget(TestCalonrw(name='dataclnrw'))
        smanager.current = 'login' #untuk menjadikan halaman tampil pertama
        return smanager
if __name__ == '__main__':
    MyApp().run()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import kivy
from kivy.app import App
from kivy.app import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
 
kivy.require('1.8.0')
 
__version__ = "0.1"
 
class PaginaInicial(Screen):
    pass
 
class LabelConfig(Screen):
    pass

class Introducao(Screen):
    pass

class A02(Screen):
    pass

class A03(Screen):
    pass

class A04(Screen):
    pass

class A05(Screen):
    pass

class A06(Screen):
    pass

class A07(Screen):
    pass

class A08(Screen):
    pass

class ScreenManagement(ScreenManager):
    
    def switch_to_introducao(self):
        self.current = 'introducao'
    
    def switch_to_A02(self):
        self.current = 'A02'

    def switch_to_A03(self):
        self.current = 'A03'
         
    def switch_to_A04(self):
        self.current = 'A04'

    def switch_to_A05(self):
        self.current = 'A05'

    def switch_to_A06(self):
        self.current = 'A06'

    def switch_to_A07(self):
        self.current = 'A07'

    def switch_to_A08(self):
        self.current = 'A08'
    
    def switch_to_paginaInicial(self):
        self.current = 'paginaInicial'
 
class kivyWizardApp(App):
    
    def build(self):
        self.root = ScreenManagement()
        return self.root
 
if __name__ == '__main__':
    kivyWizardApp().run()
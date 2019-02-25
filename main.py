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

class DesSust(Screen):
    pass

class DeSa(Screen):
    pass

class Autores(Screen):
    pass

class Final(Screen):
    pass

class Quiz(Screen):
    pass

class Sobre(Screen):
    pass

class ScreenManagement(ScreenManager):
    
    def switch_to_introducao(self):
        self.current = 'introducao'
    
    def switch_to_DesSust(self):
        self.current = 'DesSust'

    def switch_to_DeSa(self):
        self.current = 'DeSa'
         
    def switch_to_Autores(self):
        self.current = 'Autores'

    def switch_to_Final(self):
        self.current = 'Final'

    def switch_to_Quiz(self):
        self.current = 'Quiz'

    def switch_to_Sobre(self):
        self.current = 'Sobre'
    
    def switch_to_paginaInicial(self):
        self.current = 'paginaInicial'
 
class kivyWizardApp(App):
    
    def build(self):
        self.root = ScreenManagement()
        return self.root
 
if __name__ == '__main__':
    kivyWizardApp().run()
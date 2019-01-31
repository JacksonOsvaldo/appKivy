#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Importações e tratamento de exceções

#try:
import kivy
from kivy.app import App as app
from kivy.uix.boxlayout import BoxLayout as bl
from kivy.uix.button import Button as btn
from kivy.uix.label import Label as lb

# except:
# 	import kivy
# 	kivy.require('1.0.1')

# 	from kivy.app import App as app
# 	from kivy.uix.boxlayout import BoxLayout as bl
# 	from kivy.uix.button import Button as btn
# 	from kivy.uix.label import Label as lb

#Herdando atributos do Layout do tipo Box
class FirstLayout(bl):
	pass
 
#Escrevendo o App
class App(app):
	def build(self):
		layout1 = FirstLayout(orientation='vertical')
		layout1.add_widget(btn(text='Introdução'))
		layout1.add_widget(btn(text='O que é desenvolvimento sustentável?'))
		layout1.add_widget(btn(text='Desenvolvimento sustentável na Amazônia'))
		layout1.add_widget(btn(text='Principais referências sobre o assunto'))
		layout1.add_widget(btn(text='Considerações Finais'))
		layout1.add_widget(btn(text='Quiz'))
		layout1.add_widget(btn(text='Sobre'))
		return layout1

# Executando a aplicação
if __name__ == '__main__':
	App().run()

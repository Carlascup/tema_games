'''
import kivy
kivy.require('1.0.6')
'''
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.text.markup import MarkupLabel

class MyApp(App):
	
	def build(self):
		return Label(text='Python is [b]coming!!![/b]', markup = True, font_size = '50sp')
		
if __name__=='__main__':
	MyApp().run()

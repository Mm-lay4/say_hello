from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from pygments.styles.dracula import background


class SayHello(App):
	user: TextInput
	layout: GridLayout
	greeting: Label
	button:Button

	def build(self):
		self.layout = GridLayout()
		self.layout.cols = 1
		self.layout.size_hint= (0.5 , 0.5)
		self.layout.pos_hint = {"center_x": 0.5, "center_y": 0.5}
		self.layout.add_widget(Image(source = './cat.jpeg'))

		self.greeting = Label(
			text = "What's your name?",
			color = "#00FFCE"
		)
		self.layout.add_widget(self.greeting)

		self.user = TextInput(
			multiline = False,
			hint_text = "Give me your name",
			size_hint= (1, None),
			height = 80,
			padding_y = (20, 20),

		)
		self.layout.add_widget(self.user)

		self.button = Button(
			text = "GREET",
			size_hint = (1, None),
			height = 60,
			bold = True,
			background_color = "#00FFCE"
		)
		self.button.bind(on_press = self.callback)
		self.layout.add_widget(self.button)

		return self.layout

	def callback(self, instance):
		self.greeting.text = "Hello " + self.user.text + "!"


if __name__ == '__main__':
	SayHello().run()

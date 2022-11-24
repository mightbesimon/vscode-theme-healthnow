'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from lifehacks.metaclasses import enum
from lifehacks.colour import Colour, hsla
from lifehacks.colour.palette import Mariana


################################################################
#######                     palette                      #######
################################################################
@enum
class HealthNow:
	LIGHT_0   = hsla(189, 28, 81)
	LIGHT_1   = hsla(141, 90, 95)
	RED       = hsla( 12, 99, 75)
	CORAL     = RED.clone()
	ORANGE    = hsla( 18, 99, 85)
	YELLOW    = ORANGE.clone()
	MINT      = hsla(159, 61, 45)
	TEAL      = hsla(148, 70, 55)
	BLUE      = hsla(177, 99, 33)
	PURPLE    = hsla(163, 29, 61)


################################################################
#######                      class                       #######
################################################################
class ThemeReference:

	def __init__(self, filename:str) -> None:
		self.filename:str = filename
		self.themes:list[enum[Colour]] = []

	def use_theme(self, theme:enum[Colour]) -> 'ThemeReference':
		self.themes = [theme] + self.themes
		return self

	def export_color_theme(self, filename:str) -> 'ThemeReference':
		with open(self.filename, 'r') as file:
			content = file.read()

		content = (content
			.replace(': ', ':')
			.replace('\t', '' )
			.replace('\n', '' )
		)

		for theme in self.themes:
			for name, colour in theme:
				content = content.replace(name, colour.to_hex())

		with open(filename, 'w') as file:
			file.write(content)

		return self


################################################################
#######                 MAIN STARTS HERE                 #######
################################################################
if __name__ == '__main__':\
(
	ThemeReference(filename='themes/healthnow-reference.json')
		.use_theme(Mariana)
		.use_theme(HealthNow)
		.export_color_theme(filename='themes/healthnow-color-theme.json')
)

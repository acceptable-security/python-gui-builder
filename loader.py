import os, gui
import xml.etree.ElementTree as ET
from Tkinter import *
import tkMessageBox


class NonexistantFileError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class InvalidGUILineError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class GUILoader():
	def __init__(self, gui_file,script_file=None):
		self.functions = {}
		self.script_file = script_file
		if os.path.exists(self.script_file):
			exec open(self.script_file).read()

		self.loaded = False
		self.elements = {"buttons": [],
						 "text-input": [],
						 "image": []}
		
		self.window_size = (0,0)
		self.window_name = "Custom Window"

		if not os.path.exists(gui_file):
			raise NonexistantFileError("GUI File doesn't exist")
		self.dom_tree = ET.parse(gui_file)

	def loadToMem(self):
		root = self.dom_tree.getroot()
		if root.tag != "window":
			raise InvalidGUILineError("First object must be a window object")

		window_attribs = root.attrib
		
		try:
			window_size = window_attribs['size']
			window_size = window_size.split(' ')
			self.window_size = (int(window_size[0]),int(window_size[1]))
		except:
			raise InvalidGUILineError("Window size not specified")

		try:
			self.window_name = window_attribs['name']
		except:
			pass

		for button in root.iter('button'):
			attrib = button.attrib
			butt = [attrib["text"],(int(attrib["position"].split(' ')[0]),int(attrib["position"].split(' ')[1])), attrib["side"]]
			
			try:
				alert = attrib["alert"]
				

			except:
				try:
					butt.append(self.functions[attrib["function"]])
				except:
					pass

			self.elements["buttons"].append(butt)


		self.loaded = True

	def startGUI(self):
		if self.loaded == False:
			return False
		else:
			root = Tk() 
			self.app = gui.BuiltApplication(master=root, loader=self)
			self.app.mainloop()
			root.destroy()


loader = GUILoader("test.gui", "test.guiscript")
loader.loadToMem()
loader.startGUI()
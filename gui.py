from Tkinter import *

class BuiltApplication(Frame):
	def createWidgets(self):
		win_size = self.loader.window_size
		self.master.geometry("%dx%d+0+0" % (win_size[0], win_size[1]))
		self.master.title(self.loader.window_name)
		#self.frame = Frame(self, relief=RAISED, borderwidth=1)
		#self.frame.pack(fill=BOTH, expand=1)

		for button in self.loader.elements["buttons"]:
			tkbtn = Button(self)#, relief=RAISED)
			x = button[1][0]
			y = button[1][1]
			tkbtn["text"] = button[0]
			#tkbtn.place(x=x,y=y)
			
			if len(button) >= 4:
				print "cmd"
				tkbtn["command"] = button[3]

			tkbtn.pack({"side": button[2], "padx": x, "pady": y})#side=button[2], padx=x,pady=y)

			self.buttons.append(tkbtn)

	def __init__(self, master=None, loader=None):
		Frame.__init__(self, master)
		self.pack(fill=BOTH, expand=1)
		self.buttons = []
		self.loader = loader
		if self.loader != None:
			self.createWidgets()
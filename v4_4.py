import tkinter
from tkinter import ttk
#import matplotlib
#import matplotlib.pyplot as plt
#matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class entercanvas(tkinter.Canvas):
	def __init__(self, parent, w, h, errorlabel):
		super().__init__(parent, width = w, height = h, bg = 'white')
		self.errorlabel = errorlabel
		self.hscale = 3
		self.wscale = 3
		self.width = w  
		self.height = h 
		self.bounds = {"lower": h-h//11, "upper": h//11, "left": w//11, "right": w-w//11} 
		self.latestx = None
		self.latesty = None
		self.drawcoords(self.wscale, self.hscale)
		self.points = {x: h//2 for x in range(w//11, w-w//11 + 1)}
		self.create_rectangle(w//20, h//2, w-w//20 + 1, h//2, outline="red", fill="red")

		def canvasClick(event):
			x = event.x
			y = event.y  
			if not w//11-5<=x<=w-w//11+5 or not h//11-5<=y<=h-h//11+5:
				return("Out of bounds!")
			elif w//11-5<=x<w//11:
				x = w//11
			elif w-w//11<x<=w-w//11+5:
				x = w-w//11
			if h//11-5<=y<h//11:
				y = h//11
			elif h-h//11<y<=h-h//11+5:
				y = h-h//11
			if self.latestx != None:
				if self.latestx>x:
					self.create_rectangle(x-1,0,self.latestx+1,self.height,fill="white",outline="white")
				elif self.latestx<x:
					self.create_rectangle(self.latestx-1,0,x+1,self.height,fill="white",outline="white")
			self.create_rectangle(x,0,x,self.height,fill="white",outline="white")
			self.drawcoords(3, self.hscale)
			if self.latestx != None:
				if self.latestx>x:
					for i in range (x,self.latestx+1):
						if y==self.latesty:
							j=y  
						else:
							j = ((self.latesty-y)*(i-x))//(self.latestx-x)+y
						self.points.update({i:j})
						self.create_rectangle(i, j, i, j, outline="red", fill="red")
				elif self.latestx<x:
					for i in range(self.latestx-1, x+1):
						if y==self.latesty:
							j=y  
						else:
							j = ((y-self.latesty)*(i-self.latestx))//(x-self.latestx)+self.latesty
						self.points.update({i:j})
						self.create_rectangle(i, j, i, j, outline="red", fill="red")
			self.create_rectangle(x,y,x,y, outline="red", fill="red")
			self.points.update({x:y})
			self.latestx=x  
			self.latesty=y
			
			for i in self.points.keys():
				if self.points[i]==0 or self.points[i]==h//2:
					self.create_rectangle(i,h//2,i,h//2,outline="red", fill="red")

			return(x,y)

		def ReleaseButton(event):
			self.latestx = None
			self.latesty = None

		self.bind('<B1-Motion>', lambda x: self.errorlabel.reconfig(canvasClick(x)))
		self.bind('<ButtonRelease-1>', ReleaseButton)


	def drawcoords(self, wscale, hscale):
		w = self.width
		h = self.height

		self.create_line(w//2, h//20, w//2, h-h//20)
		self.create_line(w//2, h//20, w//2+w//50, h//20+h//50)
		self.create_line(w//2, h//20, w//2-w//50, h//20+h//50)
		self.create_line(w-w//20, h//2, w//20, h//2)
		self.create_line(w-w//20, h//2, w-w//20-w//50, h//2+h//50)
		self.create_line(w-w//20, h//2, w-w//20-w//50, h//2-h//50)
		self.create_text(w//2-w//50, h//2+h//50, text="0")

		if hscale==3:
			self.create_line(w//2-w//50, h//11, w//2+w//50, h//11)
			self.create_text(w//2+w//30, h//11, text="3")
			self.create_line(w//2-w//50, (5*h)//22, w//2+w//50, (5*h)//22)
			self.create_text(w//2+w//30, (5*h)//22, text="2")
			self.create_line(w//2-w//50, (8*h)//22, w//2+w//50, (8*h)//22)
			self.create_text(w//2+w//30, (8*h)//22, text="1")

			self.create_line(w//2-w//50, h-h//11, w//2+w//50, h-h//11)
			self.create_text(w//2+w//30, h-h//11, text="-3")
			self.create_line(w//2-w//50, h-(5*h)//22, w//2+w//50, h-(5*h)//22)
			self.create_text(w//2+w//30, h-(5*h)//22, text="-2")
			self.create_line(w//2-w//50, h-(8*h)//22, w//2+w//50, h-(8*h)//22)
			self.create_text(w//2+w//30, h-(8*h)//22, text="-1")

		else:
			i = hscale
			while i >= -hscale:
				if i!=0:
					self.create_line(w//2-w//50, h//11-(i-hscale)*9*h//22//hscale, w//2+w//50, h//11-(i-hscale)*9*h//22//hscale)
					self.create_text(w//2+w//30, h//11-(i-hscale)*9*h//22//hscale, text=str(i))
				i = i-(hscale/4)

		if wscale==3:
			self.create_line(w-w//11, h//2-h//50, w-w//11, h//2+h//50)
			self.create_text(w-w//11, h//2+h//30, text="3")
			self.create_line(w-(5*w)//22, h//2-h//50, w-(5*w)//22, h//2+h//50)
			self.create_text(w-(5*w)//22, h//2+h//30, text="2")
			self.create_line(w-(8*w)//22, h//2-h//50, w-(8*w)//22, h//2+h//50)
			self.create_text(w-(8*w)//22, h//2+h//30, text="1")

			self.create_line(w//11, h//2-h//50, w//11, h//2+h//50)
			self.create_text(w//11, h//2+h//30, text="-3")
			self.create_line((5*w)//22, h//2-h//50, (5*w)//22, h//2+h//50)
			self.create_text((5*w)//22, h//2+h//30, text="-2")
			self.create_line((8*w)//22, h//2-h//50, (8*w)//22, h//2+h//50)
			self.create_text((8*w)//22, h//2+h//30, text="-1")

		else:
			i = -wscale
			while i<=wscale:
				if i!=0:
					self.create_line(w//11+(i+wscale)*9*w//22//wscale, h//2-h//50, w//11+(i+wscale)*9*w//22//wscale, h//2+h//50)
					self.create_text(w//11+(i+wscale)*9*w//22//wscale, h//2+h//30, text=str(i))
				i = i+wscale/4

		return()

	def eraseall(self):
		try:
			self.hscale = int(float(yscale.get()))
			yscale.set(str(self.hscale))
		except ValueError:
			errorWindow = tkinter.Tk()
			errorLabel = tkinter.Label(errorWindow, text = f'Error: cannot set scale on Y-axis to {yscale.get()}: not a number')
			errorLabel.grid(row = 0, column = 0)
			errorButton = tkinter.Button(errorWindow, text = 'OK', command = errorWindow.destroy)
			errorButton.grid(row = 1, column = 0)
			return()
		try:
			self.wscale = int(float(xscale.get()))
			xscale.set(str(self.wscale))
		except ValueError:
			errorWindow = tkinter.Tk()
			errorLabel = tkinter.Label(errorWindow, text = f'Error: cannot set scale on X-axis to {xscale.get()}: not a number')
			errorLabel.grid(row = 0, column = 0)
			errorButton = tkinter.Button(errorWindow, text = 'OK', command = errorWindow.destroy)
			errorButton.grid(row = 1, column = 0)
			return()
		self.create_rectangle(0,0,self.width,self.height,outline="white",fill="white")
		self.drawcoords(self.wscale,self.hscale)
		self.latestx=None
		self.latesty=None
		w,h = self.width,self.height
		self.points = {x: h//2 for x in range(w//11, w-w//11 + 1)}
		self.create_rectangle(w//20, h//2-1, w-w//20 + 1, h//2, outline="red", fill="red")
		return()


class errorlabel(tkinter.Label):
	def __init__(self, parent):
		super().__init__(parent, text = "")
	def reconfig(self, txt):
		if txt=="Out of bounds!":
			self.config(bg = "red")
			self.config(text = txt)
		else:
			self.config(text="")
			self.config(bg = window.cget("bg"))

def placeholder():
	func = to_real_coords(canvas1)
	if degree1_entry.get() != '0':
		func = regular_smoothing(func, int(degree1_entry.get()))
	if degree2_entry.get() != '0':
		func = mean_smoothing(func, int(degree2_entry.get()))
	if degree3_entry.get() != '0':
		func = partically_smart_smoothing(func, int(degree3_entry.get()))
	if int(param_var2.get()):
		func = Fourier(func)
	ax.cla()
	ax.plot([p[0] for p in func], [p[1] for p in func])
	canvas2.draw()
	return()

def convert(points):
	out = dict()
	i = canvas1.bounds["left"]
	while i<=canvas1.bounds["right"]:
		if i in points.keys():
			out.update({i-canvas1.bounds["left"]-canvas1.width//2:canvas1.height//2 - (points[i]-canvas1.bounds["upper"])})
		else:
			out.update({i-canvas1.bounds["left"]-canvas1.width//2:None})
		i+=1
	return(out)

def on_yscale_change(*args):
	canvas1.eraseall()

def on_infty_change(*args):
	if at_infty.get()=="negpower":
		n = at_infty_entry.get()
		if n=="" or n=="0":
			errorWindow = tkinter.Tk()
			if n=="":
				n = "no"
			else:
				n += " as"
			errorLabel = tkinter.Label(errorWindow, text = f'Error: cannot set behavior at infinity to t\u207B\u207F with {n} value of n')
			errorLabel.grid(row = 0, column = 0)
			errorButton = tkinter.Button(errorWindow, text = 'OK', command = errorWindow.destroy)
			errorButton.grid(row = 1, column = 0)
			at_infty.set("0")
			return()
		try:
			n = int(float(n))
			at_infty_power.set(str(n))
			#at_infty_entry.update()
		except ValueError:
			errorWindow = tkinter.Tk()
			errorLabel = tkinter.Label(errorWindow, text = 'Error: cannot set behavior at infinity to t\u207B\u207F, invalid value of n - not a number')
			errorLabel.grid(row = 0, column = 0)
			errorButton = tkinter.Button(errorWindow, text = 'OK', command = errorWindow.destroy)
			errorButton.grid(row = 1, column = 0)
			at_infty.set("0")
			return()
		return()





def to_real_coords(canvas):  #передать canvas1
	w, h = canvas.width, canvas.height
	WW, HH = canvas.wscale, canvas.hscale
	func = [(point * (WW - (-WW)) / (w * 18 // 20) + (-WW) - (w // 20) * (WW - (-WW)) / (w * 18 / 20), -(canvas.points[point] * (HH - (-HH)) / (h * 18 // 20) + (-HH) - (h // 20) * (HH - (-HH)) / (h * 18 / 20)) ) for point in canvas.points]
	return func



def sealing(func, n):
	for t in range(n):
		func = binary_sealing(func)
	return func


def binary_sealing(func):
	dist = func[1][0] - func[0][0]
	diff = [func[t + 1][1] - func[t][1] for t in range(len(func) - 1)]
	diff2 = [diff[t + 1] - diff[t] for t in range(len(diff) - 1)]
	seal_diff2 = [diff2[t] + (diff2[t+1] - diff2[t]) / (1 + ((dist ** 2 + diff2[t+1] ** 2) / (dist ** 2 + diff2[t] ** 2)) ** (1/2))  for t in range(len(diff2) - 1)]
	seal_diff = []
	for t in range(1, len(diff) - 1):
		seal_diff.append(diff[t] - seal_diff2[t-1] / 4)
		seal_diff.append(diff[t] + seal_diff2[t-1] / 4)
	seal_diff = [diff[0] * (4/3) + seal_diff[0] * (-1/3), diff[0] * (2/3) + seal_diff[0] * (1/3)] + seal_diff 
	seal_diff.append(diff[-1] * (2/3) + seal_diff[-1] * (1/3))
	seal_diff.append(diff[-1] * (4/3) + seal_diff[-2] * (-1/3))
	cur_x = func[0][0]
	cur_y = func[0][1]
	seal_func = [func[0]]
	for t in range(len(seal_diff)):
		cur_x += dist / 2
		cur_y += seal_diff[t] / 2
		seal_func.append((cur_x, cur_y))
	return seal_func


def thinning(func, n):
	return [func[t] for t in range(0, len(func), n)]


def regular_smoothing(func, n): #n логарифм размаха, МАКСИМУМЫ И РАЗРЫВЫ ПОСЛЕ РАЗРЕЖЕНИЯ НЕ ПРИТУПЛЯЮТСЯ, оптимальное значение n для нашего размера холста -- 4.
	return sealing(thinning(func, 2 ** n), n)


def mean_smoothing(func, n):
	y = [func[t][1] for t in range(len(func))]
	y = [y[0]] * n + y + [y[-1]] * n
	mean = [sum(y[t - n:t + n + 1])/(2 * n + 1) for t in range(n, len(y) - n + 1)]
	return [(func[t][0], mean[t]) for t in range(len(func))]


def partically_smart_smoothing(func, n): #n логарифм размаха
	A = [1, 1]
	m = len(A)
	for i in range(n):
		B = [0 for t in range(2 * m - 1)]
		for k in range(m):
			for t in range(m):
				B[k + t] += A[t]
		A = B
		m = len(A)
	n = 2 ** (n - 1)
	y = [func[t][1] for t in range(len(func))]
	y = [y[0]] * n + y + [y[-1]] * n
	mean = [sum([y[k + t] * A[n + t] for t in range(-n, n + 1)]) / (4 * n) for k in range(n, len(y) - n)]
	return [(func[t][0], mean[t]) for t in range(len(func))]


from scipy.interpolate import UnivariateSpline


def spline(func):
	return [(func[t][0], (UnivariateSpline([p[0] for p in func], [p[1] for p in func])([p[0] for p in func]))[t]) for t in range(func)]


def anti_regular_smoothing(func, n): #n логарифм
	return thinning(spline(sealing(func, n)), 2 ** n)





from collections import defaultdict
from numpy.fft import fft


def Fourier(func):
	funcy = defaultdict(float)
	for i in range(len(func)):
		funcy[func[i][0]] = func[i][1]
	fury = fft(*funcy)




l = 480
window = tkinter.Tk()
window.wm_title("FOURIERTRANSFORM")

label1 = tkinter.Label(window, text="Draw your function")
label1.grid(row = 0, column = 0, columnspan = 2)
label2 = errorlabel(window)
canvas1 = entercanvas(window, l, l, label2)

canvas1.grid(row = 1, column = 0, columnspan = 2)
label2.grid(row = 2, column = 0, columnspan = 2)

canvas1.create_rectangle(440,440,441,441)
canvas1.create_rectangle(40,440,40,440)

erasebutton = tkinter.Button(window, text="Clear canvas", command = canvas1.eraseall)
erasebutton.grid(row = 3, column = 0)

gobutton = tkinter.Button(window, text = "Go!", command = placeholder)
gobutton.grid(row = 3, column = 1)

fig = Figure()
ax = fig.add_subplot()
canvas2 = FigureCanvasTkAgg(fig, master = window)
canvas2.get_tk_widget().grid(row = 1, column = 3)

frame = tkinter.Frame(window)
frame.grid(row = 1, column = 2)

scale_label = tkinter.Label(frame, text = "Scale on the axes\n(will be rounded to integer)", bg = "light blue")
scale_label.grid(row = 0, column = 0, columnspan = 2)

yscale = tkinter.StringVar(value = "3")
y_scale_label = tkinter.Label(frame, text = "Scale on Y-axis:")
y_scale_entry = tkinter.Entry(frame, textvariable = yscale, width = 5)

y_scale_label.grid(row = 1, column = 0, sticky="E")
y_scale_entry.grid(row = 1, column = 1, sticky = "W")

xscale = tkinter.StringVar(value = "3")
x_scale_label = tkinter.Label(frame, text = "Scale on X-axis:")
x_scale_entry = tkinter.Entry(frame, textvariable = xscale, width = 5)

x_scale_label.grid(row = 2, column = 0, sticky="E")
x_scale_entry.grid(row = 2, column = 1, sticky = "W")

rescale_button = tkinter.Button(frame, text = "Redraw with new scale\n(this will clear canvas)", command = canvas1.eraseall)
rescale_button.grid(row = 3, column = 0, columnspan = 2)


degree_label = tkinter.Label(frame, text = "Сглаживание", bg = "light blue")
degree_label.grid(row = 4, column = 0, columnspan = 2)

degree1_power = tkinter.StringVar(value = '0')
degree1_entrylabel = tkinter.Label(frame, text="Логарифм размаха интерполяционного сглаживания")
degree1_entry = tkinter.Entry(frame, width = 5, textvariable = degree1_power)
degree1_entrylabel.grid(row = 17, column = 0, sticky="E")
degree1_entry.grid(row = 17, column = 1, sticky = "W")

degree2_power = tkinter.StringVar(value = '0')
degree2_entrylabel = tkinter.Label(frame, text="Размах сглаживания усреднением")
degree2_entry = tkinter.Entry(frame, width = 5, textvariable = degree2_power)
degree2_entrylabel.grid(row = 18, column = 0, sticky="E")
degree2_entry.grid(row = 18, column = 1, sticky = "W")

degree3_power = tkinter.StringVar(value = '0')
degree3_entrylabel = tkinter.Label(frame, text="Логарифм размаха сглаживания умным усреднением")
degree3_entry = tkinter.Entry(frame, width = 5, textvariable = degree3_power)
degree3_entrylabel.grid(row = 19, column = 0, sticky="E")
degree3_entry.grid(row = 19, column = 1, sticky = "W")

param_var1 = tkinter.IntVar()
param1 = tkinter.Checkbutton(frame, variable = param_var1, text = 'Сглаживание сплайном?')
param1.grid(row = 20, column= 0, columnspan = 2)


param_var2 = tkinter.IntVar()
param2 = tkinter.Checkbutton(frame, variable = param_var2, text = 'Применить преобразование Фурье?')
param2.grid(row = 22, column= 0, columnspan = 2)



window.mainloop()

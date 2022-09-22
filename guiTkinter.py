import tkinter as tk
from serialPort import *

root = tk.Tk()
root.title("CLI DGS-1210-28/ME")

def button_click(number):
	if (number <= 24): 
		ser.write(b"cable diagnostic port %d\r" % number)
		#print(ser.read(ser.inWaiting()).decode('ascii')) # использую отдельное окно консоли с minicom	
	if (number >= 25 and number <= 28 ):
		ser.write(b"show ports %d\r" % number)
		#print(ser.read(ser.inWaiting()).decode('ascii'))
		sleep(0.5)
		ser.write(b"q")
 


button_1 = tk.Button(root, text = ' 1', padx = 39, pady = 20, command = lambda: button_click(1)).grid(sticky = tk.W + tk.E, row = 0, column = 0)
button_2 = tk.Button(root, text = ' 2', padx = 39, pady = 20, command = lambda: button_click(2)).grid(sticky = tk.W + tk.E, row = 1, column = 0)
button_3 = tk.Button(root, text = ' 3', padx = 39, pady = 20, command = lambda: button_click(3)).grid(sticky = tk.W + tk.E, row = 0, column = 1)
button_4 = tk.Button(root, text = ' 4', padx = 39, pady = 20, command = lambda: button_click(4)).grid(sticky = tk.W + tk.E, row = 1, column = 1)

button_5 = tk.Button(root, text = ' 5', padx = 39, pady = 20, command = lambda: button_click(5)).grid(sticky = tk.W + tk.E, row = 0, column = 2)
button_6 = tk.Button(root, text = ' 6', padx = 39, pady = 20, command = lambda: button_click(6)).grid(sticky = tk.W + tk.E, row = 1, column = 2)
button_7 = tk.Button(root, text = ' 7', padx = 39, pady = 20, command = lambda: button_click(7)).grid(sticky = tk.W + tk.E, row = 0, column = 3)
button_8 = tk.Button(root, text = ' 8', padx = 39, pady = 20, command = lambda: button_click(8)).grid(sticky = tk.W + tk.E, row = 1, column = 3)

button_9  = tk.Button(root, text = ' 9', padx = 39, pady = 20, command = lambda: button_click(9)).grid(sticky = tk.W + tk.E, row = 0, column = 4)
button_10 = tk.Button(root, text = '10', padx = 39, pady = 20, command = lambda: button_click(10)).grid(sticky = tk.W + tk.E, row = 1, column = 4)
button_11 = tk.Button(root, text = '11', padx = 39, pady = 20, command = lambda: button_click(11)).grid(sticky = tk.W + tk.E, row = 0, column = 5)
button_12 = tk.Button(root, text = '12', padx = 39, pady = 20, command = lambda: button_click(12)).grid(sticky = tk.W + tk.E, row = 1, column = 5)

button_13 = tk.Button(root, text = '13', padx = 39, pady = 20, command = lambda: button_click(13)).grid(sticky = tk.W + tk.E, row = 0, column = 6)
button_14 = tk.Button(root, text = '14', padx = 39, pady = 20, command = lambda: button_click(14)).grid(sticky = tk.W + tk.E, row = 1, column = 6)
button_15 = tk.Button(root, text = '15', padx = 39, pady = 20, command = lambda: button_click(15)).grid(sticky = tk.W + tk.E, row = 0, column = 7)
button_16 = tk.Button(root, text = '16', padx = 39, pady = 20, command = lambda: button_click(16)).grid(sticky = tk.W + tk.E, row = 1, column = 7)

button_17 = tk.Button(root, text = '17', padx = 39, pady = 20, command = lambda: button_click(17)).grid(sticky = tk.W + tk.E, row = 0, column = 8)
button_18 = tk.Button(root, text = '18', padx = 39, pady = 20, command = lambda: button_click(18)).grid(sticky = tk.W + tk.E, row = 1, column = 8)
button_19 = tk.Button(root, text = '19', padx = 39, pady = 20, command = lambda: button_click(19)).grid(sticky = tk.W + tk.E, row = 0, column = 9)
button_20 = tk.Button(root, text = '20', padx = 39, pady = 20, command = lambda: button_click(20)).grid(sticky = tk.W + tk.E, row = 1, column = 9)

button_21 = tk.Button(root, text = '21', padx = 39, pady = 20, command = lambda: button_click(21)).grid(sticky = tk.W + tk.E, row = 0, column = 10)
button_22 = tk.Button(root, text = '22', padx = 39, pady = 20, command = lambda: button_click(22)).grid(sticky = tk.W + tk.E, row = 1, column = 10)
button_23 = tk.Button(root, text = '23', padx = 39, pady = 20, command = lambda: button_click(23)).grid(sticky = tk.W + tk.E, row = 0, column = 11)
button_24 = tk.Button(root, text = '24', padx = 39, pady = 20, command = lambda: button_click(24)).grid(sticky = tk.W + tk.E, row = 1, column = 11)

button_25 = tk.Button(root, text = 'SFP25', padx = 39, pady = 20, command = lambda: button_click(25)).grid(sticky = tk.W + tk.E, row = 0, column = 12)
button_26 = tk.Button(root, text = 'SFP26', padx = 39, pady = 20, command = lambda: button_click(26)).grid(sticky = tk.W + tk.E, row = 1, column = 12)
button_27 = tk.Button(root, text = 'SFP27', padx = 39, pady = 20, command = lambda: button_click(27)).grid(sticky = tk.W + tk.E, row = 0, column = 13)
button_28 = tk.Button(root, text = 'SFP28', padx = 39, pady = 20, command = lambda: button_click(28)).grid(sticky = tk.W + tk.E, row = 1, column = 13)

#Ben Ryan
#Miller Rabin primality check
#program uses a tkinter gui for input of numbers to check, and display of result

import random
import tkinter
from tkinter import *
tk = tkinter.Tk()

numBox = None
ansBox = None

#sets up gui
def setupDisplay():
	global numBox, ansBox
	
	tk.title("Primality Check")
	tk.resizable(0,0)
	
	numBox = Text(tk, height=1, width=15)
	numBox.grid(row=0, column=0)
	
	Button(tk, text=">> Check >>", command=execute, height=1, width=15).grid(row=0, column=1)
	
	ansBox = Text(tk, height=1, width=15)
	ansBox.config(state='disabled')
	ansBox.grid(row=0, column=2)
	
def checkPrimality(n, t):	
	#special condition 1 to exlcude 2 from further processing
	if n == 2:
		return "Prime"
		
	#special condition to exclude even numbers from further processing
	if n % 2 == 0:
		return "Composite"

	k = 0
	q = n-1
	
	#finding k and q based on n-1
	while q%2 == 0:
		q>>= 1
		k+=1

	#ensure k and q are stored as ints
	k = int(k)
	q = int(q)

	#ensure (n-1 = (2^k)*q) is satisified with the found values before continuing
	try:
		assert(pow(2,k)*q == n - 1)
	except:
		return("Assertion Error")
	
	#loop t times
	for i in range(t):
		#choose random integer from 2 to n-1, inclusive
		a = random.randint(2,n-1)
		
		result = "Composite"
		
		ans = pow(a,q,n)
	
		#if a^q mod n = 1, inconclusive
		if ans == 1:
			result = "Inconclusive"
	
		#loop from 0 to k-1
		for j in range(k):
			ans = pow(a, (2**j)*q, n)
			
			#if a^((2^j)*q) mod n = n - 1, inconclusive
			if ans == n-1:
				result = "Inconclusive"
		
		
		#if final result is composite then return as it is definitely not prime
		#otherwise continue the loop
		if result == "Composite":
			return "Composite"
		
	return "Probably Prime"

#use to update the answer box with the result
def updateDisplay(msg):
	ansBox.config(state='normal')
	ansBox.delete('1.0', END)
	ansBox.insert(INSERT, msg)
	ansBox.config(state='disabled')

#runs when check button is pressed
def execute():
	#get contents of user input box without the end line 
	num = numBox.get('1.0', END)
	num = num[0:len(num)-1]
		
	#initial error check before checking, must be a digit and must be greater than 1
	if num.isdigit() == True and int(num) > 1:		
		#check primality of number entered, loop 20 times
		result = checkPrimality(int(num), 20)
		
		#dispaly result
		updateDisplay(result)
	else:
		updateDisplay("Error")
		
setupDisplay()
tk.mainloop()
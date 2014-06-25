"""
This module contains the library of braille 
arrays which can be parsed by Braille.py, 
and will include methods which allow the
user to customize their braille arrays,
including the ability to add new braille 
systems. 
"""
from tkinter import *
# TODO: 
# - Figure out why display isn't working right ~~PRIORITY
# - FIX numbers modifier
# - Create error handling for import
# - Add custom braille creator
# - Clean this crap up!

letters = {'a' : [1, 0,
                  0, 0,
                  0, 0],
          
          'b' : [1, 0,
                 1, 0,
                 0, 0],
          
          'c' : [1, 1,
                 0, 0,
                 0, 0],
          
          'd' : [1, 1,
                 0, 1,
                 0, 0],
          
          'e' : [1, 0,
                 0, 1,
                 0, 0],

          'f' : [1, 1,
                 1, 0,
                 0, 0],

          'g' : [1, 1,
                 1, 1,
                 0, 0],

          'h' : [1, 0,
                 1, 1,
                 0, 0],

          'i' : [0, 1,
                 1, 0,
                 0, 0],

          'j' : [0, 1,
                 1, 1,
                 0, 0],

          'k' : [1, 0,
                 0, 0,
                 1, 0],

          'l' : [1, 0,
                 1, 0,
                 1, 0],

          'm' : [1, 1,
                 0, 0,
                 1, 0],

          'n' : [1, 1,
                 0, 1,
                 1, 0],

          'o' : [1, 0,
                 0, 1,
                 1, 0],

          'p' : [1, 1,
                 1, 0,
                 1, 0],

          'q' : [1, 1,
                 1, 1,
                 1, 0],

          'r' : [1, 0,
                 1, 1,
                 1, 0],

          's' : [0, 1,
                 1, 0,
                 1, 0],
          
          't' : [0, 1,
                 1, 1,
                 1, 0],

          'u' : [1, 0,
                 0, 0,
                 1, 1],

          'v' : [1, 0,
                 1, 0,
                 1, 1],

          'w' : [0, 1,
                 1, 1,
                 0, 1],

          'x' : [1, 1,
                 0, 0,
                 1, 1],

          'y' : [1, 1,
                 0, 1,
                 1, 1],

          'z' : [1, 0,
                 0, 1,
                 1, 1]}

# MODE stores the numerical mode. The default mode is 0, for the literary code.
# MODE 1 is the Nemeth, or mathematical code. 
MODE = 0

numbers = {1 : letters['a'],
		   2 : letters['b'],
		   3 : letters['c'],
		   4 : letters['d'],
		   5 : letters['e'],
		   6 : letters['f'],
		   7 : letters['g'],
		   8 : letters['h'],
		   9 : letters['i'],
		   0 : letters['j']}

# This function converts the "numbers" dictionary between Nemeth and Literary modes 
def toggleMode():
	global MODE, numbers

	if MODE == 0:
		for i in numbers:
			numbers[i].insert(0, 0)
			numbers[i].insert(0, 0)
			numbers[i].pop(-1)
			numbers[i].pop(-1)

			MODE = 1
		print("Mode switched to Nemeth")
		return "Mode switched to Nemeth"

	elif MODE == 1:
		numbers = {1 : letters['a'],
		           2 : letters['b'],
		           3 : letters['c'],
		           4 : letters['d'],
	        	   5 : letters['e'],
	        	   6 : letters['f'],
	        	   7 : letters['g'],
	        	   8 : letters['h'],
	        	   9 : letters['i'],
	        	   0 : letters['j']}
		MODE = 0
		print("Mode switched to Literary")
		return "Mode switched to Literary"

	else:
		print("Error: Invalid mode")
		return "Error: Invalid mode"

# Uncomment to run toggleMode in console

#toggleMode()
#wait = input("Press Enter to continue. . .")
###################################################################################
# This section contains diagnostic functions. They are indexed below with a short # 
# description for each.                                                           #
#                                                                                 # 
# - checkLib: This function checks to make sure all letters are assigned to a     #
#             braille array of length 6,and that they are comprised of only "on"  #
#             or "off" values.                                                    #
#                                                                                 #
# - checkMode: This function returns and prints the mode ID (0 for Literary,      #
#              1 for Nemeth) along with a string informing which mode it is in    #
###################################################################################

def checkLib():
    count = 0
    letcheck = []
    invcheck = []
    finalcheck = [0, 0]
    for i in letters:
        # Checks if letters have length of 6
        if len(letters[i]) != 6:
            count += 1
            letcheck.append(i)
        # Checks if letters use any values other than 1 or 0    
        for j in letters[i]:
            if j != 0 and j != 1:
                invcheck.append(i)

    # Informs user of errors
    if len(letcheck) == 0:
        print("All letters have the correct number of pips!")

    else:
        print("Letters wrong size: ", letcheck)
        finalcheck[0] = 1
    
    
    if len(invcheck) == 0:
        print("All letters are valid!")

    else:
        print("Invalid letters: ", invcheck)
        finalcheck[1] = 1

    if finalcheck == [0, 0]:
        print("Library looks good for now!")

    # This is a workaround for there being no exclusive or in Python. Read this line as:
    #     elif finalcheck == [1, 0] xor finalcheck == [0, 1]
    elif (finalcheck == [1, 0] and finalchek != [0, 1]) or (finalcheck == [0, 1] and finalcheck != [1, 0]):
        print("Check the above letters and correct any mistakes.")

    elif finalcheck == [1, 1]:
        print("Check the above letters and correct any mistakes. Some of the letters might have multiple issues!")

    else:
        print("Error: finalcheck broke!") 

# Uncomment to run checkLib in console
#checkLib()
#wait = input("Press Enter to continue. . .")

###################################################################################	

def checkMode():
	global MODE

	if MODE == 0:
		print("Current Mode: Literary")
		return 0, "Current Mode: Literary"

	elif MODE == 1:
		print("Current Mode: Nemeth")
		return 1, "Current Mode: Nemeth"

	else:
		print("Error: Invalid mode")
		return "Error: Invalid mode"

# Uncomment to run checkLib in console
#checkMode()
#wait = input("Press Enter to continue. . .")



#class libBraille(object):
#    pass




# DEBUGGING

"""
print("This should read: \n\"Mode switched to Nemeth\"")
toggleMode()
wait = input("Press Enter to continue. . .")

print("This should read: \n\"Current mode: Nemeth\"")
checkMode()
wait = input("Press Enter to continue. . .")

print("This should read: \n\"Mode switched to Literary\"")
toggleMode()
wait = input("Press Enter to continue. . .")

print("This should read: \n\"Current mode: Literary\"")
checkMode()
wait = input("Press Enter to continue. . .")
"""
#i = True
#while i == True:
#	wait = input("Press Enter to exit; I don't do anything yet!")
#	i = False

HEIGHT = 400
WIDTH = 225
gui = Tk()
#class Pip():
#    def __init__():

pips = ["black", "black", "black", "black", "black", "black"]

# DEBUGGING
#pips = ["white", "blue", "red", "yellow", "green", "pink"]

def displayBraille(char):
    global letters, numbers, pips

    #char.lower()

    if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
        for i in numbers:
            for j in numbers[i]:
                if numbers[i][j] == 1:
                    pips[j] = "white"
                else:
                    pips[j] = "black"

#    elif type(char) == 'str' and char in letters:
#        for i in letters:
#            for j in letters[i]:
#                if letters[i][j] == 1:
#                    pips[j] = "white"
#    else:
#        print("Error: invalid character")

    else:  
        for i in letters:
            for j in letters[i]:
                if letters[i][j] == 1:
                    pips[j] = "white"
                else:
                    pips[j] = "black"




disp = Canvas(gui, height = HEIGHT, width = WIDTH, bg = "black")

displayBraille('h')

#pip0
disp.create_oval(WIDTH / 3, HEIGHT / 4, WIDTH / 3 + 10, HEIGHT / 4 + 10, fill = pips[0])

#pip1
disp.create_oval((WIDTH / 3) * 2, HEIGHT / 4, ((WIDTH / 3) * 2) + 10, HEIGHT / 4 + 10, fill = pips[1])

#pip2
disp.create_oval(WIDTH / 3, (HEIGHT / 4) * 2, WIDTH / 3 + 10, ((HEIGHT / 4) * 2) + 10, fill = pips[2])

#pip3
disp.create_oval((WIDTH / 3) * 2, (HEIGHT / 4) * 2, ((WIDTH / 3) * 2) + 10, ((HEIGHT / 4) * 2) + 10, fill = pips[3])

#pip4
disp.create_oval(WIDTH / 3, (HEIGHT / 4) * 3, WIDTH / 3 + 10, ((HEIGHT / 4) * 3) + 10, fill = pips[4])

#pip5
disp.create_oval((WIDTH / 3) * 2, (HEIGHT / 4) * 3, ((WIDTH / 3) * 2) + 10, ((HEIGHT / 4) * 3) + 10, fill = pips[5])
disp.pack()

#DEBUGGING
print(pips)

gui.mainloop()

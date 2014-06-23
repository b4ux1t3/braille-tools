"""
This module contains the library of braille 
arrays which can be parsed by Braille.py, 
and will include methods which allow the
user to customize their braille arrays,
including the ability to add new braille 
systems. 
"""
# TODO: 
# - Add numbers modifier
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

# This function checks to make sure all letters are assigned to a braille array of length 6,
# and that they are comprised of only "on" or "off" values.
def checkLib():
    count = 0
    letcheck = []
    invcheck = []
    finalcheck = [0, 0]
    for i in letters:
        # Checks if letters have length of 6
        if len(letters[i]) != 6:
            count += 1
            list.append(i)
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
        print("Invalid letters: ", incheck)
        finalcheck[1] = 1

    if finalcheck == [0, 0]:
        print("Library looks good for now!")
    elif finalcheck == [1, 0] or finalcheck == [0, 1]:
        print("Check the above letters and correct any mistakes.")
    elif finalcheck == [1, 1]:
        print("Check the above letters and correct any mistakes. Some of the letters might have multiple issues!")
    else:
        print("Error: finalcheck broke!") 


# Uncomment to run checkLib in console
#checkLib()
#wait = input()

#class libBraille(object):
#    pass

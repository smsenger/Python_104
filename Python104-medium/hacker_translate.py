

# Translate a string into leetspeak. They key is as follows:
# A = 4
# E = 3
# G = 6
# I = 1
# O = 0
# S = 5
# T = 7 

#start with the text to translate and make the code all uppercase
trans = 'This is the beggining of the paragraph. Actually, I will just write two sentences to test out the code.'.upper()


def hacker_speak(text):

    for letter in text:         #Iterate through the string
        if letter == 'A':       #name letter to change
            print('4', end='')  #print the corresponding nubmers, using end='' to continue on same line
        elif letter == 'E':
            print('3', end='') 
        elif letter == 'G':
            print('6', end='')
        elif letter == 'I':
            print('1', end='')
        elif letter == 'O':
            print('0', end='')
        elif letter == 'S':
            print('5', end='')
        elif letter == 'T':
            print('7', end='')
        else:
            print(letter, end='')
        
hacker_speak(trans)            #call the function with string variable name as argument




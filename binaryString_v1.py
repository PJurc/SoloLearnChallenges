#   "Valid Binary String"
# Write a program to check if the user input
# is a valid binary string or not.
# Challenge by Swapnil Srivastava.

s = input("Enter text to check if it is a binary string: ")
if len(s) == 0: #if no input, quit the program
    print("Please enter text.")
    quit()
c = True #set to True initially
for i in range(len(s)): #iterate through string 's'
    if(s[i] != '0' and s[i] != '1'): #if a char that is not a 0 or 1 is found
        c = False #change value to false
        break #terminate the loop. Unecessary, but saves processing resources

print(c)

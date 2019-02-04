#   "ASCII Converter"
# Write a program, which takes a text as input
# and converts it to ASCII decimal numbers.
# Challenge by Shudarshan Rai.

s = input("Enter text to be converted: ")

for i in range(len(s)): #iterate through string 's'.
    print((int(ord(s[i]))), end=" ") #convert to unicode string, then to int, separate by spaces.

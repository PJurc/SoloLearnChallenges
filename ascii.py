def ascii(s):
    """
    Converts a string to
    ASCII values
    """
    sa = " " #a new string to store ASCII
    for i in range(len(s)):
        sa += str(ord(s[i])) + " " #convert text to ASCII, convert that to string, add a space and add the result to sa
    return sa #return the new string

s = input("Enter text to be converted: ") #input
sa = ascii(s) #assign sa to the function's returned value
print(sa) #print the ASCII string
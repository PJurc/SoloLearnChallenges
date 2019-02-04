#include <stdio.h>
#include <string.h>

/*  "ASCII Converter"
Write a program, which takes a text as input
and converts it to ASCII decimal numbers.
Challenge by Shudarshan Rai.
*/
int main (void)
{
char s[100];
printf("Enter text to be converted to ASCII: \n");
gets(s); //Get the string

for(int i = 0; i < strlen(s); i++) //Iterate through string 's'
{
    printf("%i ", s[i]); //Print the int values of each char. (ASCII)
}
return 0;
}


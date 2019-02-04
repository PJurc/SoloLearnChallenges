#include <stdio.h>
#include <string.h>

/*  "Valid Binary String"
Write a program to check if the user input
is a valid binary string or not.
Challenge by Swapnil Srivastava. */

int main(void)
{
    char s[100];
    char* c = "true";
    printf("Enter text to check if it is a binary string: \n");
    gets(s);
    if(strlen(s) == 0){
        fprintf(stderr, "Please enter text. \n");
        return 1;
    }

    for(int i = 0; i < strlen(s); i++){
        if(s[i] != '0' && s[i] != '1'){
            c = "false";
            break;
        }
    }
    printf("%s", c);
    return 0;
}

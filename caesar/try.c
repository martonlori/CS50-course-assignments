#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
int digitchecker(string input);
string decypher (string plaintext, string key);
int main (int argc, string argv[])
{
    string plaintext;
    if (argc != 2)
    {
        printf("Error: Incorrect number of cmd line arguments. Correct usage: ./caesar key \n");
        return 1;
    }
    if (argc == 2 && !digitchecker(argv[1]))
    {
        printf("Error: key is not a decimal number. Correct usage: ./caesar key\n");
        return 1;
    }
    if (argc == 2 && digitchecker(argv[1]))
    {
        plaintext = get_string("plaintext:\n");
        string key = argv[1];
    string cyphertext = decypher(plaintext, key);
    printf("cyphertext: %s\n", cyphertext);
  return 0;
    }
    
}
int digitchecker(string input)
{
   for (int i = 0; i < strlen(input); i++)
    {
        if (!isdigit(input[i]))
        {
            return 0;
        }
    }
    return 1;
}
string decypher (string plaintext, string key)
{
    int key_int = atoi(key);
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (isalpha(plaintext[i]))
        {
            if (isupper(plaintext[i]))
            {
                plaintext[i] = ((plaintext[i] - 'A' + key_int) %26 ) + 'A';
            }
            else if (islower(plaintext[i]))
            {
                plaintext[i] = ((plaintext[i] - 'a' + key_int) %26 ) + 'a';
            }
        }
    }
    return plaintext;
}
// current state: plaintext's characters to be rotated 'key' times
//

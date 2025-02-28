#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int digitchecker(string text);
float avgletters(string text);
float avgsentences(string text);
int main(void)
{
    // get text as input
    string text;
    int n;
    do
    {
        text = get_string("Text: ");
    }
    while (digitchecker(text) == 1);
    float index = avgletters(text) * 0.0588 - 0.296 * avgsentences(text) - 15.8;
    index = round(index);

    if (index < 16 && index > 0)
    {
        printf("Grade %i\n", (int) index);
    }
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
}
// make a funciton, that checks if any digit of the input of text is a digit
int digitchecker(string text)
{
    for (int i = 0; i < strlen(text); i++)
    {
        if (isdigit(text[i]))
        {
            return 1;
        }
    }
    return 0;
}
// implement a function that checks the average letters per 100 words
float avgletters(string text)
{
    float x = strlen(text); // x is the number of (just) letters in the text
    for (int n = 0; n < strlen(text); n++)
    {
        if (isspace(text[n]) || ispunct(text[n]))
        {
            x = x - 1;
        }
    }

    float y = 0; // y is the number of words in the text
    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i]))
        {
            y = y + 1;
        }
    }
    y = y + 1;

    float L = (x / y) * 100;
    return L;
}

// implement a function that checks the average number of sentences per 100
// words
float avgsentences(string text)
{
    float y = 0; // y is the number of words in the text
    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i]))
        {
            y = y + 1;
        }
    }
    y = y + 1;

    float x = 0; // x is the number of sentences in the text
    for (int n = 0; n < strlen(text); n++)
    {
        if (text[n] == '.' || text[n] == '?' || text[n] == '!')
        {
            x = x + 1;
        }
    }
    float S = x / y * 100;
    return S;
}

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int digitcheck(string);
int score1st(string word);
int score2nd(string word);
int scores[26] = {0};
int main(void)
{
    scores['A' - 'A'] = 1;
    scores['B' - 'A'] = 3;
    scores['C' - 'A'] = 3;
    scores['D' - 'A'] = 2;
    scores['E' - 'A'] = 1;
    scores['F' - 'A'] = 4;
    scores['G' - 'A'] = 2;
    scores['H' - 'A'] = 4;
    scores['I' - 'A'] = 1;
    scores['J' - 'A'] = 8;
    scores['K' - 'A'] = 5;
    scores['L' - 'A'] = 1;
    scores['M' - 'A'] = 3;
    scores['N' - 'A'] = 1;
    scores['O' - 'A'] = 1;
    scores['P' - 'A'] = 3;
    scores['Q' - 'A'] = 10;
    scores['R' - 'A'] = 1;
    scores['S' - 'A'] = 1;
    scores['T' - 'A'] = 1;
    scores['U' - 'A'] = 1;
    scores['V' - 'A'] = 4;
    scores['W' - 'A'] = 4;
    scores['X' - 'A'] = 8;
    scores['Y' - 'A'] = 4;
    scores['Z' - 'A'] = 10;
    string player1, player2;
    int score1, score2;

    // Promt user for a word, but only accept characters, not digits
    do
    {
        player1 = get_string("Player 1: ");
    }
    while (digitcheck(player1) == 1);
    score1 = score1st(player1);

    do
    {
        player2 = get_string("Player 2: ");
    }
    while (digitcheck(player2) == 1);
    score2 = score2nd(player2);

    if (score1 == score2)
    {
        printf("Tie!\n");
    }
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
}
// implement a digit-checker function
int digitcheck(string word)
{
    for (int i = 0; i < strlen(word); i++)
    {
        if (isdigit(word[i]))
        {
            return 1;
        }
    }
    return 0;
}
// implement a score checker function
int score1st(string word)
{
    int score1;
    score1 = 0;
    for (int n = 0; n < strlen(word); n++)
    {
        word[n] = toupper(word[n]);
        score1 = score1 + scores[word[n] - 'A'];
    }
    return score1;
}
int score2nd(string word)
{
    int score2;
    score2 = 0;
    for (int n = 0; n < strlen(word); n++)
    {
        word[n] = toupper(word[n]);
        score2 = score2 + scores[word[n] - 'A'];
    }
    return score2;
}

// Implements a dictionary's functionality

#include "dictionary.h"
#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
int wordcounter;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hashed_value = hash(word);
    node *cursor = table[hashed_value];
    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function - idea: using the % to handle the rest?
    if (strlen(word) > 3)
    {
        int value = (7 * (toupper(word[0]) - 'A') + 5 * (toupper(word[1]) - 'A') +
                     3 * (toupper(word[2]) - 'A') + 2 * (toupper(word[3]) - 'A')) %
                    N;
        return value;
    }
    if (strlen(word) == 3)
    {
        int value = (7 * (toupper(word[0]) - 'A') + 5 * (toupper(word[1]) - 'A') +
                     3 * (toupper(word[2]) - 'A')) %
                    N;
        return value;
    }
    if (strlen(word) == 2)
    {
        int value = (7 * (toupper(word[0]) - 'A') + 5 * (toupper(word[1]) - 'A')) % N;
        return value;
    }
    if (strlen(word) == 1)
    {
        int value = 7 * (toupper(word[0]) - 'A');
        return value;
    }
    else
    {
        return 0;
    }
}

// Loads dictionary into memory, returning true if successful, else false - idea: implement here a
// checker that counts how many words were loaded
bool load(const char *dictionary)
{
    // TODO
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        printf("Error when reading into file\n");
        return 0;
    }
    char buffer[46];
    wordcounter = 0;
    while (fscanf(dict, "%s", buffer) != EOF)
    {
        node *p = malloc(sizeof(node));
        if (p == NULL)
        {
            return 0;
        }
        strcpy(p->word, buffer);
        int index = hash(p->word);
        p->next = table[index];
        table[index] = p;
        wordcounter++;
    }
    if (fclose(dict) != 0)
    {
        return false;
    }
    else
    {
        return true;
    }
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO

    if (wordcounter != 0)
    {
        return wordcounter;
    }
    else
    {
        return 0;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        node *temp = table[i];
        while (cursor != NULL)
        {
            temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}

#include <cs50.h>
#include <stdio.h>

void print_row(int spaces, int bricks);
int main(void)
{
    int i;
    int n;
    do
    {
        i = get_int("Height:");
    }
    while (i < 1);
    for (n = 0; n < i; n++)
    {
        print_row(i - (n + 1), n + 1);
    }
}
void print_row(int spaces, int bricks)
{
    for (int n = 0; n < spaces; n++)
    {
        printf(" ");
    }
    for (int n = 0; n < bricks; n++)
    {
        printf("#");
    }
    printf("\n");
}

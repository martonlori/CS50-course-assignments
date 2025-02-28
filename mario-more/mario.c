#include <cs50.h>
#include <stdio.h>
void print_row(int spaces, int bricks);
int main(void)
{
    int h;
    int n;
    do
        h = get_int("Height:");
    while (h < 1 || h > 8); // Asks for imput, only accepts numbers between 1 and 8. h=height of pyramid
    for (n = 0; n < h; n++)
    {
        print_row(h - (n + 1), n + 1);
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
    printf("  ");
    for (int n = 0; n < bricks; n++)
    {
        printf("#");
    }

    printf("\n");
}

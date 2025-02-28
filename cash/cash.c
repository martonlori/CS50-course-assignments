#include <cs50.h>
#include <stdio.h>

int cents;
int quarters = 25;
int dimes = 10;
int nickels = 5;
int pennies = 1;
int change;
int no_apropenz;
int maradek;
int maradek2;
int maradek3;
int maradek4;
int main(void)
{
    do
    {
        cents = get_int("Change owed:");
    }
    while (cents < 0);
    for (; cents >= quarters; cents -= quarters)
    {
        no_apropenz++;
    }
    maradek = cents;
    for (; maradek >= dimes; maradek -= dimes)
    {
        no_apropenz++;
    }
    maradek2 = maradek;
    for (; maradek2 >= nickels; maradek2 -= nickels)
    {
        no_apropenz++;
    }
    maradek3 = maradek2;
    for (; maradek3 >= pennies; maradek3 -= pennies)
    {
        no_apropenz++;
    }

    printf("%d\n", no_apropenz);
}

#include <cs50.h>
#include <stdio.h>
long ccnumber;
long firstsecond;
long simplify(void);
int counter;
int y;
int main(void)
{
    do
    {
        ccnumber = get_long("Number: ");
    }
    while (ccnumber < 0);
    firstsecond = ccnumber;
    for (counter = 2; ccnumber > 100; counter++)
    {
        ccnumber = simplify();
    }

    if (ccnumber == 34 || ccnumber == 37)
    {
        if (counter == 15)
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }

    else if (50 < ccnumber && ccnumber < 56)
    {
        if (counter == 16)
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else if (39 < ccnumber && ccnumber < 50)
    {
        if (counter == 13 || counter == 16)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
long simplify(void)
{
    firstsecond = ccnumber / 10;
    return firstsecond;
}

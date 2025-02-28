#include <cs50.h>
#include <stdio.h>
long ccnumber;
long firstsecond;
long simplify(void);
int simplenumber;
int main(void)
{
    do
    {
        ccnumber = get_long("Number: ");
    }
    while (ccnumber < 0);
    firstsecond = ccnumber;
    for (; ccnumber > 100;)
    {
        ccnumber = simplify();
    }

    if (ccnumber == 34 || ccnumber == 37)
    {
        printf("AMEX\n");
    }
    else if (50 < ccnumber && ccnumber < 56)
    {
        printf("MASTERCARD\n");
    }
    else if (39 < ccnumber && ccnumber < 50)
    {
        printf("VISA\n");
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

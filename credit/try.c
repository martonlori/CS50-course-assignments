#include <cs50.h>
#include <stdio.h>
#include <math.h>
long ccnumber;
long firstsecond;
long simplify (void);
long originalnumber;
int main (void)
{
    do
    {
        ccnumber = get_long("Number: ");
        originalnumber = ccnumber;
    }
    while ( ccnumber < 0);
firstsecond = ccnumber;
    for (; ccnumber > 100;)
    {
            ccnumber = simplify ();
    }

    if ((ccnumber == 34 || ccnumber == 37))
    {
        if ((originalnumber >= (pow(10,15)) && originalnumber < ((pow(10,15)) + (pow(10,15)))))
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");
        }

    }
    else if ((50 < ccnumber && ccnumber < 56))
    {
        if ((originalnumber >= (pow(10,16)) && originalnumber < ((pow(10,16)) + (pow(10,16)))))
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }

    }
    else if ((39 < ccnumber && ccnumber < 50))
    {
        if (((originalnumber >= (pow(10,16)) && originalnumber < ((pow(10,16)) + (pow(10,16)))) || (originalnumber >= (pow(10,13)) && originalnumber < ((pow(10,13)) + (pow(10,13))))))
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

long simplify (void)
{

       firstsecond = ccnumber / 10;
       return firstsecond;
}


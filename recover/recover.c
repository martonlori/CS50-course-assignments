#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Open memory card
    FILE *carddata = fopen("card.raw", "r");
    char filename[8];
    if (carddata == NULL)
    {
        printf("Error when opening the file\n");
        return 1;
    }
    else if (argc != 2)
    {
        printf("Error:more than 2 cmd line arguments\n");
        return 1;
    }
    FILE *file = NULL;
    uint8_t buffer[512];
    int counter = 0;
    while ((fread(buffer, 512, 1, carddata)) != 0)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (file != NULL)
            {
                fclose(file);
            }
            sprintf(filename, "%03d.jpg", counter);
            file = fopen(filename, "wb");
            counter++;
        }
        if (file != NULL)
        {
            fwrite(buffer, 512, 1, file);
        }
    }
    if (file != NULL)
    {
        fclose(file);
    }
    fclose(carddata);
}

// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file

        char buffer[HEADER_SIZE];
        FILE *a;
        FILE *b;
        a = fopen(argv[1], "r");
        b = fopen(argv[2], "w");
        if (input != NULL && output != NULL)
        {
            fread(buffer, HEADER_SIZE, 1, a);
            fwrite(buffer, HEADER_SIZE, 1, b);
        }
        else
        {
            return 1;
        }

        fclose(a);
        fclose(b);

    // TODO: Read samples from input file and write updated data to output file

    int16_t buffer;
    FILE *a;
    FILE *b;
    a = fopen(argv[1], "r");
    b = fopen(argv[2], "w");
     while (fread(&buffer, sizeof(int16_t), 1, a) != 0)
    {
        float dummy = buffer * factor;
         if (dummy > 32767)
        {
            buffer = 32767;
        }
        else if (dummy >= -32768 && dummy <= 32767)
        {
            buffer = round(dummy);
        }
        else if (dummy < -32768)
        {
            buffer = -32768;
        }
        fwrite(&buffer, sizeof(int16_t), 1, b);

    }

    fclose(a);
    fclose(b);



    // Close files
    fclose(input);
    fclose(output);
}

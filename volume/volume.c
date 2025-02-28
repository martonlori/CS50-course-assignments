// Modifies the volume of an audio file

#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

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
    if (a != NULL && b != NULL)
    {
        if (fread(buffer, HEADER_SIZE, 1, a) != 1)
        {
            return 1;
        }
        if (fwrite(buffer, HEADER_SIZE, 1, b) != 1)
        {
            return 1;
        }
    }
    else
    {
        return 1;
    }

    // TODO: Read samples from input file and write updated data to output file

    int16_t buffer1;

    if (a != NULL && b != NULL)
    {
        while (fread(&buffer1, sizeof(int16_t), 1, a) != 0)
        {
            double result = buffer1 * factor;
            if (result > 32767)
            {
                buffer1 = 32767;
            }
            else if (result < -32768)
            {
                buffer1 = -32768;
            }
            else
            {
                buffer1 = result;
            }
            fwrite(&buffer1, sizeof(int16_t), 1, b);
        }
    }

    // Close files
    fclose(input);
    fclose(output);
}

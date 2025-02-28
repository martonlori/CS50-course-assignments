#include "helpers.h"
#include <math.h>

// Convert image to grayscale: loop through the pixels, calculate average, round, set RGB to average
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            double d_average =
                (((image[i][j].rgbtBlue) + (image[i][j].rgbtRed) + (image[i][j].rgbtGreen)) / 3.0);
            int i_average = round(d_average);
            image[i][j].rgbtBlue = i_average;
            image[i][j].rgbtRed = i_average;
            image[i][j].rgbtGreen = i_average;
        }
    }
    return;
}

// Convert image to sepia: loop through the pixels, calculate the sepiaRGBs with the form, round
// them, cap them at 255
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            double d_sepiaR = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            int i_sepiaR = round(d_sepiaR);
            i_sepiaR = (i_sepiaR > 255) ? 255 : i_sepiaR;
            double d_sepiaG = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            int i_sepiaG = round(d_sepiaG);
            i_sepiaG = (i_sepiaG > 255) ? 255 : i_sepiaG;
            double d_sepiaB = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;
            int i_sepiaB = round(d_sepiaB);
            i_sepiaB = (i_sepiaB > 255) ? 255 : i_sepiaB;
            image[i][j].rgbtRed = i_sepiaR;
            image[i][j].rgbtBlue = i_sepiaB;
            image[i][j].rgbtGreen = i_sepiaG;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (j < width / 2.0)
            {
                RGBTRIPLE temp = image[i][j];
                image[i][j] = image[i][width - 1 - j];
                image[i][width - 1 - j] = temp;
            }
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE blurred[height][width];
    int counter = 0;
    int sumR = 0;
    int sumG = 0;
    int sumB = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            sumR = 0;
            sumG = 0;
            sumB = 0;
            counter = 0;
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                if ((j + k) < width && (j + k) >= 0 && (i + l) < height && (i + l) >= 0)
                {
                    sumR = sumR + image[i + l][j + k].rgbtRed;
                    sumG = sumG + image[i + l][j + k].rgbtGreen;
                    sumB = sumB + image[i + l][j + k].rgbtBlue;
                    counter++;
                }
                }
            }
            int blurryR = round((float) sumR / counter);
            blurred[i][j].rgbtRed = blurryR;
            int blurryG = round((float) sumG / counter);
            blurred[i][j].rgbtGreen = blurryG;
            int blurryB = round((float) sumB / counter);
            blurred[i][j].rgbtBlue = blurryB;
        }
    }
    for (int o = 0; o < height; o++)
    {
        for (int s = 0; s < width; s++)
        {
            image[o][s] = blurred[o][s];
        }
    }
    return;
}

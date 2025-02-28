from cs50 import get_string

# structure:
# 1.Get input from user
# 2.Create a variable that holds the number of words in text (W)
# 3.Create variable, that holds average number of letters in text in 100 words (L). L = letters / words * 100
# 4.Create variable that holds average number of sentences in text in 100 words (S). S = sentences / words * 100
# 5.Coleman-Liau index: 0.0588 * L - 0.296 * S - 15.8
# 6.Cap output: min.: Before Grade 1, max.: Grade 16+
# 7.Output: Grade X (result of formula == X), X is rounded to the nearest integer

text = get_string("Text: ")

word_counter = 1
letter_counter = 0
sentence_counter = 0

for char in text:
    if char == " ":
        word_counter += 1
    if char.isalpha():
        letter_counter += 1
    if char == "." or char == "?" or char == "!":
        sentence_counter += 1

W = word_counter
L = letter_counter / W * 100
S = sentence_counter / W * 100

index = round(0.0588 * L - 0.296 * S - 15.8)

if index >= 16:
    print("Grade 16+")
elif index >= 1:
    print("Grade " + str(index))
elif index < 1:
    print("Before Grade 1")

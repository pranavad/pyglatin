from tkinter.filedialog import askopenfilename
import time
input("Press Enter to select file to be translated")
filename = askopenfilename()
original = open(filename)
original = original.read()
str_list = original.split()


def pyglatin():

    lis = []
    yes_no = input("Do you want to output the translation in this file? (Enter Yes or no to output in another file)").lower()
    if yes_no == "yes" or yes_no == "yeah" or yes_no == "y":

        output_file_write = open(filename,"w")
        print("Translated to " + filename)
    else:
        input("Press Enter to select output file")
        output_file = askopenfilename()
        output_file_write = open(output_file,"w")
        print("Translated to " + output_file)
    for word in str_list:
        start_mark = ""
        if word[0] == "\"" or word[0] == "'":
            start_mark = word[0]
            word = word[1:]


        first_letter = word[0]
        word = word[1:]
        end_mark = ""
        if len(word) > 1:
            if word[-1] == "." or word[-1] == ";" or word[-1] == "," or word[-1] == "'" or word[-1] == "\"" or word[-1] == "!" or word[-1] == "?":
                end_mark = word[-1]
                word = word[0:-2]
        letters = "aeiouAEIOU".split()
        for i in letters:
            if first_letter == i:
                word = start_mark + first_letter + word + "yay" + end_mark
                lis.append(word)
                break
            elif i != first_letter:
                word = start_mark + word + first_letter + "ay" + end_mark
                lis.append(word)
                break
    final_doc = " ".join(lis)
    output_file_write.write(final_doc)
def de_pyg():
    lis = []
    yes_no = input("Do you want to output the translation in this file? (Enter Yes or no to output in another file)").lower()
    if yes_no == "yes" or yes_no == "yeah" or yes_no == "y":

        output_file_write = open(filename,"w")
        print("Translated to " + filename)
    else:
        input("Press Enter to select output file")
        output_file = askopenfilename()
        output_file_write = open(output_file,"w")
        print("Translated to " + output_file)
    for i in str_list:
        end_mark = ""
        start_mark = ""
        if word[-1] == "\'" or word[-1]== ":" or word[-1]== ";" or word[-1]== "\"" or word[-1]== "." or word[-1]== "," or word[-1]== "'":
            end_mark = i[-1]
            i = word[:-3]
        else:
            word = word[:-2]
        if len(i) > 1:
            first_letter = i[-1]
            word = word[:-1]

            if word[0] == "\"" or word[0] == "'":
                start_mark = i[0]
                word = word[1:]

            lis.append(start_mark + first_letter + word + end_mark)
        else:
            lis.append(i)
    final_doc = " ".join(lis)
    output_file_write.write(final_doc)

translation = input("Do you want to encrypt or decrypt? \n(Enter encrypt for encryption or decrypt for decryption)\n>>>").lower()
print("WARNING - If you try to decrypt an already decrypted file, its contents will be lost. Don't say I didn't warn you")
if translation == "encrypt":
    pyglatin()
elif translation == "decrypt":
    de_pyg()
else:
    print("Try again with valid input (encrypt or decrypt)")

time.sleep(5)

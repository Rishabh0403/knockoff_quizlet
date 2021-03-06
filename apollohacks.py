from tkinter import *
import random
import csv

x = r"C:\Users\pande\Desktop\ApolloHacksData.csv"
data = csv.reader(open(x, encoding='utf-8-sig'))
list = []
for line in data:
    list.append(tuple(line))
print(list)

window = Tk()
window.title("Flashcard App")
window.geometry("600x600")

# getting the words from the csv file
words = list

# get count of word list
count = len(words)

def next():
    global hinter, hint_count
    #clear screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    #reset hints
    hinter = ""
    hint_count = 0
    #create random selection
    global random_word
    random_word = random.randint(0, count-1)
    #update label with word
    spanish_word.config(text=words[random_word][0])
def answer():
    if my_entry.get().capitalize() == words[random_word][1]:
        answer_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][1]}")
    else:
        answer_label.config(text=f"Incorrect! {words[random_word][0]} is not {my_entry.get().capitalize()}")

# keeps track of hint
hinter = ""
hint_count = 0
def hint():
    global hint_count, hinter
    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count += 1



spanish_word = Label(window, text="", font=("Helvetica", 36))
spanish_word.pack(pady=50)

answer_label = Label(window, text="")
answer_label.pack(pady=20)

my_entry = Entry(window, font=("Helvetica", 18))
my_entry.pack(pady=20)

# making buttons

button_frame = Frame(window)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=1)

next_button = Button(button_frame, text="Next", command = next)
next_button.grid(row=0, column=2, padx=20)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=0, padx=20)

# making hint label
hint_label = Label(window, text="")
hint_label.pack(pady=20)

# run next function when program starts
next()
window.mainloop()

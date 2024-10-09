from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- GENERATE A NEW WORD ------------------------------- #
try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('data/french_words.csv')

vocab = df.to_dict(orient="records")
random_vocab= {}
to_learn = []

def next_word():
    global random_vocab, vocab, to_learn
    try:
        random_vocab = random.choice(vocab)
        canvas.itemconfig(card_title, text = 'French', fill='black')
        canvas.itemconfig(card_word, text=random_vocab['French'], fill='black')
        canvas.itemconfig(card_background, image=card_front_image)
        vocab.remove(random_vocab)
    except IndexError:
        messagebox.showinfo(message="Good Job!")
        data = pd.DataFrame(to_learn)
        data.to_csv('data/words_to_learn.csv', index=False)

def flip_card():
    global vocab, to_learn
    canvas.itemconfig(card_title, text = 'English', fill='white')
    canvas.itemconfig(card_word, text = random_vocab['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)
    window.after(2000, func=flip_back)

    # add the unknown vocab
    vocab.append(random_vocab)
    to_learn.append(random_vocab)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)


def flip_back():
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=random_vocab['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_image)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

# canvas setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file = 'images/card_back.png')
card_background = canvas.create_image(400,263,image=card_front_image)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))
canvas.grid(column=0,row=0, columnspan=2)

# create the buttons
check_image = PhotoImage(file='images/right.png')
button_known = Button(image=check_image, command = next_word, highlightbackground=BACKGROUND_COLOR)
button_known.grid(column=1,row=1)

cross_image = PhotoImage(file='images/wrong.png')
button_unknown = Button(image=cross_image, command = flip_card, highlightbackground=BACKGROUND_COLOR)
button_unknown.grid(column=0, row=1)

next_word()

window.mainloop()


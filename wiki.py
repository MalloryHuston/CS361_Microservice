# Title: Wikipedia Scraper
# Class: CS 361 - Software Engineering I
# Author: Mallory Huston
# Description: A wikipedia scraper microservice that pulls up any information of a
#              category of your choosing.

from tkinter import *
import wikipedia as wiki

root = Tk()
root.title('Game Development Guide - Category Wikipedia')
root.geometry("700x675")


# Clear
def clear():
    my_entry.delete(0, END)
    my_text.delete(0.0, END)


# Search
def search():
    data = wiki.page(my_entry.get())
    # Clear screen
    clear()
    # Output Wikipedia Results to Textbox
    my_text.insert(0.0, data.content)
    

# Write to File
def writeFile():
    fileName = input("Article name: ") + ".txt"
    file = open(fileName, 'a+')
    file.write(my_text.get("1.0", 'end-1c') + '\n')
    file.close()


my_label_frame = LabelFrame(root, text="Search Category")
my_label_frame.pack(pady=20)

# Create entry box
my_entry = Entry(my_label_frame, font=("Helvetica", 18), width=47)
my_entry.pack(pady=20, padx=20)

# Create text box frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create vertical scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create horizontal scrollbar
hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

# Create text box
my_text = Text(my_frame, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

# Configure scrollbars
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# Button Frame
button_frame = Frame(root)
button_frame.pack(pady=10)

# Buttons
search_button = Button(button_frame, text="Lookup", font=("Helvetica", 32), fg="#3a3a3a", command=search)
search_button.grid(row=0, column=0, padx=20)

clear_button = Button(button_frame, text="Clear", font=("Helvetica", 32), fg="#3a3a3a", command=clear)
clear_button.grid(row=0, column=1)

write_button = Button(button_frame, text="Write to File", font=("Helvetica", 32), fg="#3a3a3a", command=writeFile)
write_button.grid(row=0, column=2)

root.mainloop()

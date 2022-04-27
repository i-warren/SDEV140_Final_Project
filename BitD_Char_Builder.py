from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Character Creator")

# adding favicon
root.iconbitmap('images/favicon.ico')

# add image
my_img = ImageTk.PhotoImage(Image.open('images/BitD_banner.png'))
my_label = Label(image=my_img)
my_label.grid(column=0, row=0, columnspan=14)

# make exit button
button_quit = Button(root, text="Exit", command=root.quit, padx=40, bg="#25262b", fg="#f2f2f2")
button_quit.grid(row=1, column=1, columnspan=2)

# make create character button
    #CREATE COMMAND
button_create = Button(root, text="Create", command=root.quit, padx=35, bg="#25262b", fg="#f2f2f2")
button_create.grid(row=1, column=6,columnspan=2)

# make load character button
    #CREATE COMMAND
button_load = Button(root, text="Load", command=root.quit, padx=35, bg="#25262b", fg="#f2f2f2")
button_load.grid(row=1, column=11,columnspan=2)


root.mainloop()
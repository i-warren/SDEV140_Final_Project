import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font as tkfont


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self['bg'] = '#0d0d0d'

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.grid()
        # side = "top", fill = "both", expand = True
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        # title
        self.title("BitD Character Creator")

        # adding favicon
        self.iconbitmap('images/favicon.ico')

        self.frames = {}
        for F in (StartPage, CreatePage, LoadPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()




class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self['bg'] = '#0d0d0d'

        global bitdbanner
        bitdbanner = ImageTk.PhotoImage(Image.open('images/BitD_banner.png'))
        my_label = tk.Label(self, image=bitdbanner, bg='#0d0d0d')
        my_label.grid(column=0, row=0, columnspan=14)

        # make exit button
        button_quit = tk.Button(self, text="Exit", padx=40, bg="#25262b", fg="#f2f2f2")
        button_quit.config(command=self.quit)
        button_quit.grid(row=1, column=1, columnspan=2)

        # create character button
        button_create = tk.Button(self, text="Create", padx=35, bg="#25262b", fg="#f2f2f2")
        button_create.config(command=lambda: controller.show_frame("CreatePage"))
        button_create.grid(row=1, column=6, columnspan=2)

        # load character button
        button_load = tk.Button(self, text="Load", padx=35, bg="#25262b", fg="#f2f2f2")
        button_load.config(command=lambda: controller.show_frame("LoadPage"))
        button_load.grid(row=1, column=11, columnspan=2)




class CreatePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self['bg'] = '#0d0d0d'

        global bitddark
        bitddark = ImageTk.PhotoImage(Image.open('images/BitD_dark.png'))
        my_label = tk.Label(self, image=bitddark, bg='#0d0d0d')
        my_label.grid(column=0, row=0, columnspan=14)


        # make exit button
        button_quit = tk.Button(self, text="Exit", padx=40, bg="#25262b", fg="#f2f2f2")
        button_quit.config(command=self.quit)
        button_quit.grid(row=1, column=1, columnspan=2)

        # create character button
        button_create = tk.Button(self, text="Create", padx=35, bg="#25262b", fg="#f2f2f2")
        button_create.config(command=lambda: controller.show_frame("CreatePage"))
        button_create.grid(row=1, column=6, columnspan=2)

        # load character button
        button_load = tk.Button(self, text="Load", padx=35, bg="#25262b", fg="#f2f2f2")
        button_load.config(command=lambda: controller.show_frame("LoadPage"))
        button_load.grid(row=1, column=11, columnspan=2)


class LoadPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self['bg'] = '#0d0d0d'




        bgimg = tk.Label(self, image=bitddark, bg='#0d0d0d')
        bgimg.place(x = 0, y = 0)

        e = tk.Entry(bgimg, width=35, borderwidth=5)
        e.place(x=200, y=200)

        # make exit button
        button_quit = tk.Button(self, text="Exit", padx=40, bg="#25262b", fg="#f2f2f2")
        button_quit.config(command=self.quit)
        # button_quit.place(x=100, y=100)
        button_quit.grid(row=1, column=1, columnspan=2)

        # create character button
        button_create = tk.Button(self, text="Create", padx=35, bg="#25262b", fg="#f2f2f2")
        button_create.config(command=lambda: controller.show_frame("CreatePage"))
        button_create.grid(row=1, column=6, columnspan=2)

        # load character button
        button_load = tk.Button(self, text="Load", padx=35, bg="#25262b", fg="#f2f2f2")
        button_load.config(command=lambda: controller.show_frame("LoadPage"))
        button_load.grid(row=1, column=11, columnspan=2)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
#
# class WindowOrganize:
#     @staticmethod
#     # def center_window_on_screen():
#     #     """
#     #     This centres the window when it is not maximised.  It
#     #     uses the screen and window height and width variables
#     #     defined in the program below.
#     #     :return: Nothing
#     #     """
#     #     x_cord = int((screen_width / 2) - (width / 2))
#     #     y_cord = int((screen_height / 2) - (height / 2))
#     #     root.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))
#
#     @staticmethod
#     def change_to_main():
#         """
#         This function swaps from the create
#         frame to the main frame.
#         :return: Nothing
#         """
#         BitDBuilder(root).grid()
#         CreateChar(root).forget()
#
#     @staticmethod
#     def change_to_create():
#         """
#         This function swaps from the work
#         frame to the quiz frame.
#         :return: Nothing
#         """
#         CreateChar(root).grid()
#         BitDBuilder(root).forget()
#
#
#
# class BitDBuilder(tk.Frame):
#     def __init__(self, parent, *args, **kwargs):
#         tk.Frame.__init__(self, parent, *args, **kwargs)
#         self.parent = parent
#
#         # !!!!CREATE CHARACTER BUTTON FUNCTION!!!!
#         def createchar():
#             pass
#
#         # !!!!CREATE LOAD CHARACTER FUNCTION!!!!!
#         def loadchar():
#             pass
#
#
#         global bitdbanner
#         bitdbanner = ImageTk.PhotoImage(Image.open('images/BitD_banner.png'))
#         my_label = tk.Label(image=bitdbanner)
#         my_label.grid(column=0, row=0, columnspan=14)
#
#         # make exit button
#         button_quit = tk.Button(root, text="Exit", padx=40, bg="#25262b", fg="#f2f2f2")
#         button_quit.config(command=root.quit)
#         button_quit.grid(row=1, column=1, columnspan=2)
#
#         # create character button
#         button_create = tk.Button(root, text="Create", command=createchar, padx=35, bg="#25262b", fg="#f2f2f2")
#         button_create.config(command=WindowOrganize.change_to_create)
#         button_create.grid(row=1, column=6, columnspan=2)
#
#         # load character button
#         button_load = tk.Button(root, text="Load", command=loadchar, padx=35, bg="#25262b", fg="#f2f2f2")
#         button_load.grid(row=1, column=11, columnspan=2)
#
#
# class CreateChar(tk.Frame):
#     def __init__(self, parent, *args, **kwargs):
#         tk.Frame.__init__(self, parent, *args, **kwargs)
#         self.parent = parent
#
#         global bitdbanner
#         bitdbanner = ImageTk.PhotoImage(Image.open('images/BitD_banner.png'))
#         my_label = tk.Label(image=bitdbanner)
#         my_label.grid(column=0, row=0, columnspan=14)
#
#         # make exit button
#         button_quit = tk.Button(root, text="Exit", command=root.quit, padx=40, bg="#25262b", fg="#f2f2f2")
#         button_quit.grid(row=1, column=1, columnspan=2)
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     BitDBuilder(root).grid()
#
#
#     # title
#     root.title("Character Creator")
#
#     # adding favicon
#     root.iconbitmap('images/favicon.ico')
#     root.mainloop()

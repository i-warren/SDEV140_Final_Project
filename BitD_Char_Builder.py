import tkinter as tk
import csv
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import font as tkfont


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self['bg'] = '#0d0d0d'
        self.geometry("1200x650")
        self.resizable(False, False)
        self.wm_attributes("-transparentcolor", 'grey')

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where frames are stacked
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.grid()


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


        # >>>>>>>>>>>>>>>>>>>>>>>>>>>> MAIN FRAME
        startfrm = tk.Frame(self, height=559, width=1200, bg="#0d0d0d")
        startfrm.grid(row=0, column=1, columnspan=14)

        global bitdbanner
        bitdbanner = ImageTk.PhotoImage(Image.open('images/BitD_banner.png'))
        bg = tk.Label(startfrm, image=bitdbanner, bg='#0d0d0d')
        bg.grid(row=0, column=0, columnspan=14)

        # explabel = tk.Label(bg, text="Select a Class to Create and Clic")


        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> NAV FRAME

        navfrm = tk.Frame(self, width=1200, height=85, bg="#0d0d0d", borderwidth=0, highlightthickness=0)
        navfrm.grid(row=1, column=0, columnspan=14)

        # make exit button
        button_quit = tk.Button(startfrm, text="Exit", padx=40, pady=10, bg="#25262b", fg="#f2f2f2")
        button_quit.config(command=self.quit)
        # button_quit.place(x=100, y=100)
        button_quit.grid(row=1, column=0, columnspan=2)

        # make main button
        button_quit = tk.Button(startfrm, text="Main", padx=40, pady=10, bg="#25262b", fg="#f2f2f2")
        button_quit.config(state="disabled", command=lambda: controller.show_frame("StartPage"))
        # button_quit.place(x=100, y=100)
        button_quit.grid(row=1, column=4, columnspan=2)

        # create character button
        button_create = tk.Button(startfrm, text="Create", padx=35, pady=10, bg="#25262b", fg="#f2f2f2")
        button_create.config(command=lambda: controller.show_frame("CreatePage"))
        button_create.grid(row=1, column=8, columnspan=2)

        # load character button
        button_load = tk.Button(startfrm, text="Load", padx=35, pady=10, bg="#25262b", fg="#f2f2f2")
        button_load.config(command=lambda: controller.show_frame("LoadPage"))
        button_load.grid(row=1, column=12, columnspan=2)




class CreatePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self['bg'] = '#0d0d0d'

        # >>>>>>>>>>>>>>>>>>>>> Main Frame

        infofrm = tk.Frame(self, height=559, width=1200, bg="#F25C05")
        infofrm.grid(row=0, column=0, columnspan=7)

        global bitddrk
        bitddrk = ImageTk.PhotoImage(Image.open('images/BitD_dark.png'))
        bg = tk.Label(infofrm, image=bitddrk, bg='#0d0d0d', borderwidth=0, highlightthickness=0)
        bg.grid(column=0, row=0, sticky="e")

        # name section
        nameframe = tk.Frame(bg, width=235, height=50)
        nameframe.place(x=75, y=25)
        nameframe.pack_propagate(False)
        namelabel = tk.Label(nameframe, text="Name", fg="#f25c05", bg="#25262b", font=("Helvetica 14 bold"))
        namelabel.pack(fill=tk.X)
        nameentry = tk.Entry(nameframe, font=("Helvetica 14"))
        nameentry.pack(fill=tk.X)

        # Alias Section
        aliasframe = tk.Frame(bg, width=235, height=50)
        aliasframe.place(x=325, y=25)
        aliasframe.pack_propagate(False)
        aliaslabel = tk.Label(aliasframe, text="Alias", fg="#f25c05", bg="#25262b", font=("Helvetica 14 bold"))
        aliaslabel.pack(fill=tk.X)
        aliasentry = tk.Entry(aliasframe, font=("Helvetica 14"))
        aliasentry.pack(fill=tk.X)

        # Look Section
        lookframe = tk.Frame(bg, width=485, height=50)
        lookframe.place(x=75, y=100)
        lookframe.pack_propagate(False)
        looklabel = tk.Label(lookframe, text="Describe Your Look", fg="#f25c05", bg="#25262b",
                             font=("Helvetica 14 bold"))
        looklabel.pack(fill=tk.X)
        lookentry = tk.Entry(lookframe, font=("Helvetica 14"))
        lookentry.pack(fill=tk.X)

        # Heiritage secion
        heirframe = tk.Frame(bg, width=235, height=50)
        heirframe.place(x=75, y=175)
        heirframe.pack_propagate(False)
        heirlabel = tk.Label(heirframe, text="Heiritage", fg="#f25c05", bg="#25262b", font=("Helvetica 14 bold"))
        heirlabel.pack(fill=tk.X)
        # !!!!!!!! MAKE DROPDOWN!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        heirentry = tk.Entry(heirframe, font=("Helvetica 14"))
        heirentry.pack(fill=tk.X)

        # Background Section
        backframe = tk.Frame(bg, width=235, height=50)
        backframe.place(x=325, y=175)
        backframe.pack_propagate(False)
        backlabel = tk.Label(backframe, text="Background", fg="#f25c05", bg="#25262b", font=("Helvetica 14 bold"))
        backlabel.pack(fill=tk.X)
        # !!!!!!MAKE DROPDOWN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        backentry = tk.Entry(backframe, font=("Helvetica 14"))
        backentry.pack(fill=tk.X)

        # Vice Section
        # Create Vice Frame
        viceframe = tk.Frame(bg, width=485, height=125, bg="#25262b")
        viceframe.place(x=75, y=250)
        viceframe.grid_propagate(False)
        vicelabel = tk.Label(viceframe, padx=15, pady=4, text="Vice", fg="#f25c05", bg="#25262b",
                             font=("Helvetica 14 bold"))
        vicelabel.grid(column=0, row=0)

        # list of vices
        vicelist = ("Faith", "Gambling", "Luxury", "Obligation", "Pleasure", "Stupor", "Weird")

        # vice radiobuttons
        # Create variable for radio buttons
        v1 = tk.IntVar()
        v1.set(1)

        # first row radiobuttons
        for i in range(1, 4):
            tk.Radiobutton(viceframe, text=f"{vicelist[i - 1]}", padx=17, variable=v1, value=i, selectcolor="#0d0d0d",
                           fg="#f2f2f2", bg="#25262b", font=("Helvetica 12")).grid(row=0, column=i)

        # second row radiobutons
        for i in range(4, 8):
            tk.Radiobutton(viceframe, text=f"{vicelist[i - 1]}", padx=17, variable=v1, value=i, selectcolor="#0d0d0d",
                           fg="#f2f2f2", bg="#25262b", font=("Helvetica 12")).grid(row=1, column=(i - 4))

        # create vice details label and entry box
        viceplabel = tk.Label(viceframe, padx=15, pady=4, text="Details and Purveyor", fg="#f25c05", bg="#25262b",
                              font=("Helvetica 14 bold"))
        viceplabel.grid(row=2, column=0, columnspan=4)
        vicepentry = tk.Entry(viceframe, font=("Helvetica 14"))
        vicepentry.grid(row=3, column=0, columnspan=4, sticky=tk.EW)

        # ----PLAYBOOK SELECTION SECTION----
        archselframe = tk.Frame(bg, width=485, height=125, bg="#25262b")
        archselframe.place(x=75, y=400)

        # Create Label
        archsellabel = tk.Label(archselframe, padx=160, pady=4, text="Select A Playbook", fg="#f25c05", bg="#25262b",
                              font=("Helvetica 14 bold"))
        archsellabel.grid(column= 0, row=0, columnspan=4)

        # sets variable type for playbook selection radio buttons
        p1 = tk.IntVar()
        p1.set(1)

        # list of playbooks
        # playbooklist = ("Cutter", "Gambling", "Luxury", "Obligation", "Pleasure", "Stupor", "Weird")

        # dictionary of playbooks and row in reference csv file
        global playdict
        playdict = {"cutter": 1, "hound": 2, "leech": 3, "lurk": 4, "slide": 5, "spider": 6, "whisper": 7}

        #create capitalized list from dictionary
        playbooknames = list(playdict.keys())
        for i in range(len(playbooknames)):
            playbooknames[i] = playbooknames[i].capitalize()

        # Select button function
        def playclick(value):
            """Function takes in value from radio button and configures
            radio buttons of abilities and ally sections"""
            updateability(value)
            updatefriend(value)

        def updateability(value):
            global playbook
            if value == 1:
                playbook = "cutter"
            elif value ==2:
                playbook = "hound"
            elif value == 3:
                playbook = "leech"
            elif value == 4:
                playbook = "lurk"
            elif value == 5:
                playbook = "slide"
            elif value == 6:
                playbook = "spider"
            elif value == 7:
                playbook = "whisper"

            specabilities = specability(playbook)

            s1.config(text=f"{(specabilities[0])}")
            s2.config(text=f"{(specabilities[1])}")
            s3.config(text=f"{(specabilities[2])}")
            s4.config(text=f"{(specabilities[3])}")
            s5.config(text=f"{(specabilities[4])}")
            s6.config(text=f"{(specabilities[5])}")
            s7.config(text=f"{(specabilities[6])}")
            s8.config(text=f"{(specabilities[7])}")

        def updatefriend(value):
            if value == 1:
                playbook = "cutter"
            elif value ==2:
                playbook = "hound"
            elif value == 3:
                playbook = "leech"
            elif value == 4:
                playbook = "lurk"
            elif value == 5:
                playbook = "slide"
            elif value == 6:
                playbook = "spider"
            elif value == 7:
                playbook = "whisper"

            friends = friendfoe(playbook)

            fr1.config(text=f"   {(friends[0])}")
            fr2.config(text=f"   {(friends[1])}")
            fr3.config(text=f"   {(friends[2])}")
            fr4.config(text=f"   {(friends[3])}")
            fr5.config(text=f"   {(friends[4])}")





        # first row radiobuttons
        for i in range(1, 5):
            tk.Radiobutton(archselframe, text=f"{(playbooknames[i - 1])}", padx=17, variable=p1, value=i, selectcolor="#0d0d0d", fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"), command=lambda: playclick(p1.get())).grid(row=1, column=i-1)

        # second row radiobuttons
        for i in range(5, 8):
            tk.Radiobutton(archselframe, text=f"{(playbooknames[i - 1])}", padx=17, variable=p1, value=i, selectcolor="#0d0d0d", fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"), command=lambda: playclick(p1.get())).grid(row=2, column=i - 5, columnspan=2)



        # ----SPECIAL ABILITY SECTION----

        def read_cell(x, play):
            """function takes in a value for the csv column and the archetype
            to return a value from a specific cell in the reference csv"""

            y = playdict[play]

            with open('.dat/BitDClasses.csv', 'r') as f:
                reader = csv.reader(f)
                y_count = 0

                for n in reader:
                    if y_count == y:
                        cell = n[x]
                        return cell
                    y_count += 1

        def specability(play):
            """Propagates a list of a classes special abilitiesplay is passed
            through to read_cell and values returned appended to the list"""

            abilitylist = []
            for i in range(1, 9):
                abilitylist.append(read_cell(i, play))
                abilities = tuple(abilitylist)
            return abilities


        def friendfoe(play):
            """Propagates a list of a playbooks friends and rivals. play is passed
            through to read_cell and values returned appended to the list"""

            friendlist = []
            for i in range(17, 22):
                friendlist.append(read_cell(i, play))
                friends = tuple(friendlist)
            return friends


        # create list from selected playbook
        specabilities = specability("cutter")

        # Create Special Ability Frame
        specfrm = tk.Frame(bg, width=317, height=260, bg="#25262b")
        specfrm.place(x=598, y=25)
        specfrm.pack_propagate(False)

        # sets variable type for ability selection radio buttons
        s = tk.IntVar()
        s.set(1)

        # Creates label and radiobuttons
        # label
        speclabel = tk.Label(specfrm,text="Pick A Special Ability", fg="#f25c05", bg="#25262b", font=("Helvetica 14 bold"))
        speclabel.pack()

        # radiobuttons
        s1 = tk.Radiobutton(specfrm, text=f"{(specabilities[0])}", padx=17, variable=s, value=1, selectcolor="#0d0d0d", fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        s2 = tk.Radiobutton(specfrm, text=f"{(specabilities[1])}", padx=17, variable=s, value=2, selectcolor="#0d0d0d", fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        s3 = tk.Radiobutton(specfrm, text=f"{(specabilities[2])}", padx=17, variable=s, value=3, selectcolor="#0d0d0d", fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        s4 = tk.Radiobutton(specfrm, text=f"{(specabilities[3])}", padx=17, variable=s, value=4, selectcolor="#0d0d0d", fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        s5 = tk.Radiobutton(specfrm, text=f"{(specabilities[4])}", padx=17, variable=s, value=5, selectcolor="#0d0d0d", fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        s6 = tk.Radiobutton(specfrm, text=f"{(specabilities[5])}", padx=17, variable=s, value=6, selectcolor="#0d0d0d", fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        s7 = tk.Radiobutton(specfrm, text=f"{(specabilities[6])}", padx=17, variable=s, value=7, selectcolor="#0d0d0d", fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        s8 = tk.Radiobutton(specfrm, text=f"{(specabilities[7])}", padx=17, variable=s, value=8, selectcolor="#0d0d0d", fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))

        s1.pack(anchor=tk.W)
        s2.pack(anchor=tk.W)
        s3.pack(anchor=tk.W)
        s4.pack(anchor=tk.W)
        s5.pack(anchor=tk.W)
        s6.pack(anchor=tk.W)
        s7.pack(anchor=tk.W)
        s8.pack(anchor=tk.W)


        # ----FRIEND/RIVAL SECTION----
        # create list from selected playbook
        friends = friendfoe("cutter")



        # Create Friend/Rival Frame
        frndfrm = tk.Frame(bg, width=317, height=225, bg="#25262b")
        frndfrm.place(x=598, y=325)
        frndfrm.grid_propagate(False)

        #  Create top Label
        frndlabel = tk.Label(frndfrm, padx=75, text="Pick One Each", fg="#f25c05", bg="#25262b", font=("Helvetica 14 bold"))
        frndlabel.grid(column=0, row=0, columnspan=2)

        # Create Button Labels
        fbuttonlabel = tk.Label(frndfrm, padx=10, text="Friend", fg="#f25c05", bg="#25262b", anchor=tk.W, font=("Helvetica 14 bold"))
        fbuttonlabel.grid(column=0, row=1, sticky=tk.W)
        rbuttonlabel = tk.Label(frndfrm, padx=10, text="Rival", fg="#f25c05", bg="#25262b",justify=tk.RIGHT, anchor=tk.E, font=("Helvetica 14 bold"))
        rbuttonlabel.grid(column=1, row=1, sticky=tk.E)

        # sets variable type for friend selection radio buttons
        fr = tk.IntVar()
        fr.set(1)

        # sets variable type for friend selection radio buttons
        r = tk.IntVar()
        r.set(1)

        # Create friend radiobuttons
        fr1 = tk.Radiobutton(frndfrm, text=f"   {(friends[0])}", padx=10, variable=fr, value=1, selectcolor="#0d0d0d",
                            fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        fr2 = tk.Radiobutton(frndfrm, text=f"   {(friends[1])}", padx=10, variable=fr, value=2, selectcolor="#0d0d0d",
                            fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        fr3 = tk.Radiobutton(frndfrm, text=f"   {(friends[2])}", padx=10, variable=fr, value=3, selectcolor="#0d0d0d",
                            fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        fr4 = tk.Radiobutton(frndfrm, text=f"   {(friends[3])}", padx=10, variable=fr, value=4, selectcolor="#0d0d0d",
                            fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        fr5 = tk.Radiobutton(frndfrm, text=f"   {(friends[4])}", padx=10, variable=fr, value=5, selectcolor="#0d0d0d",
                            fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))


        fr1.grid(column=0,row=2, sticky=tk.W)
        fr2.grid(column=0,row=3, sticky=tk.W)
        fr3.grid(column=0,row=4, sticky=tk.W)
        fr4.grid(column=0,row=5, sticky=tk.W)
        fr5.grid(column=0,row=6, sticky=tk.W)

        # Create rival radiobuttons
        r1 = tk.Radiobutton(frndfrm, text=f"", padx=17, variable=r, value=1, selectcolor="#0d0d0d",
                             fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        r2 = tk.Radiobutton(frndfrm, text=f"", padx=17, variable=r, value=2, selectcolor="#0d0d0d",
                             fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        r3 = tk.Radiobutton(frndfrm, text=f"", padx=17, variable=r, value=3, selectcolor="#0d0d0d",
                             fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        r4 = tk.Radiobutton(frndfrm, text=f"", padx=17, variable=r, value=4, selectcolor="#0d0d0d",
                             fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
        r5 = tk.Radiobutton(frndfrm, text=f"", padx=17, variable=r, value=5, selectcolor="#0d0d0d",
                             fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))

        r1.grid(column=1, row=2, sticky=tk.E)
        r2.grid(column=1, row=3, sticky=tk.E)
        r3.grid(column=1, row=4, sticky=tk.E)
        r4.grid(column=1, row=5, sticky=tk.E)
        r5.grid(column=1, row=6, sticky=tk.E)


        # ----ACTION RATING SECTION----

        # Create Action Frame
        actfrm = tk.Frame(bg, width=198, height=125, bg="#25262b")
        actfrm.place(x=935, y=25)

        # >>>>>>>>>>>>>>>>>>>>> Nav Frame <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # Create Navigation Frame
        navfrm = tk.Frame(self, width=1200, height=85, bg="#0d0d0d", borderwidth=0, highlightthickness=0)
        navfrm.grid(row=1, column=0, columnspan=14)

        # creates invisible spacer so that buttons display as intended
        spacfrm = tk.Frame(navfrm, width=1200, height=1, bg="#0d0d0d")
        spacfrm.grid(row=0, column=0, columnspan=14)

        # open button
        def opnfile():
            global file_image
            self.filename = filedialog.askopenfilename(
                initialdir="",
                title="Select A File",
                filetypes=(("png files", "*.png"), ("all files", "*.*")))
            # !!! ADD FILETYPE CHECK

            # !!! CREATE>>>CALL NEW FRAME WITH DATA FROM FILE

            # CODE FROM PRACTICE-FOR REFERENCE ONLY
            # fileLabel = tk.Label(self, text=self.filename).pack()
            # file_image = ImageTk.PhotoImage(Image.open(self.filename))
            # fileLabel = Label(image=my_image).pack()



        # open file button
        filbtn = tk.Button(navfrm, text="Open File", command=opnfile, padx=27, pady=10, bg="#25262b", fg="#F25C05")
        filbtn.grid(row=1, column=6, columnspan=2)

        # make exit button
        button_quit = tk.Button(navfrm, text="Exit", padx=40, pady=10, bg="#25262b", fg="#f2f2f2")
        button_quit.config(command=self.quit)
        button_quit.grid(row=2, column=0, columnspan=2, )

        # make main button
        button_quit = tk.Button(navfrm, text="Main", padx=40, pady=10, bg="#25262b", fg="#f2f2f2")
        button_quit.config(command=lambda: controller.show_frame("StartPage"))
        button_quit.grid(row=2, column=4, columnspan=2)

        # create character button
        button_create = tk.Button(navfrm, text="Create", padx=35, pady=10, bg="#25262b", fg="#f2f2f2")
        button_create.config(state="disabled", command=lambda: controller.show_frame("CreatePage"))
        button_create.grid(row=2, column=8, columnspan=2)

        # load character button
        button_load = tk.Button(navfrm, text="Load", padx=35, pady=10, bg="#25262b", fg="#f2f2f2")
        button_load.config(command=lambda: controller.show_frame("LoadPage"))
        button_load.grid(row=2, column=12, columnspan=2)

        namelabel = tk.Label(infofrm, text="Name", bg="#25262b", fg="#F25C05")
        nameentry = tk.Entry(infofrm, width= 35)
 # !!!!!!!!!!!!!!!!!ADD TO FRAME

class LoadPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self['bg'] = '#0d0d0d'

        infofrm = tk.Frame(self, height=559, width=1200, bg="#F25C05")
        infofrm.grid(row=0, column=0, columnspan=7)

        # displayfrm = tk.Frame(self, height=559, width=600, bg="#222222", borderwidth=0, highlightthickness=0)
        # displayfrm.grid(row=0, column=7, columnspan=7)

        navfrm = tk.Frame(self, width=1200, height=85, bg="#0d0d0d", borderwidth=0, highlightthickness=0)
        navfrm.grid(row=1, column=0, columnspan=14)

        spacfrm = tk.Frame(navfrm, width=1200, height=1, bg="#0d0d0d")
        spacfrm.grid(row=0, column=0, columnspan=14)

        bg = tk.Label(infofrm, image=bitddrk, bg='#0d0d0d', borderwidth=0, highlightthickness=0)
        bg.grid(column=0, row=0, sticky="e")

        # bgimgR = tk.Label(displayfrm, image=bitddarkR, bg='#0d0d0d', borderwidth=0, highlightthickness=0)
        # bgimgR.grid(column=0, row=0, sticky="w")





        # open file method
        def opnfile():
            global file_image
            self.filename = filedialog.askopenfilename(
                initialdir="",
                title="Select A File",
                filetypes=(("png files", "*.png"), ("all files", "*.*")))
            # !!! ADD FILETYPE CHECK


            # !!! CREATE>>>CALL NEW FRAME WITH DATA FROM FILE

            # CODE FROM PRACTICE-FOR REFERENCE ONLY
            # fileLabel = tk.Label(self, text=self.filename).pack()
            # file_image = ImageTk.PhotoImage(Image.open(self.filename))
            # fileLabel = Label(image=my_image).pack()


        # open file button
        filbtn = tk.Button(navfrm, text="Open File", command=opnfile, padx=27, pady=10, bg="#25262b", fg="#F25C05")
        filbtn.grid(row=1, column=6, columnspan=2)

        # make exit button
        button_quit = tk.Button(navfrm, text="Exit", padx=40, pady=10, bg="#25262b", fg="#f2f2f2")
        button_quit.config(command=self.quit)
        # button_quit.place(x=100, y=100)
        button_quit.grid(row=2, column=0, columnspan=2,)

        # make main button
        button_quit = tk.Button(navfrm, text="Main", padx=40, pady=10, bg="#25262b", fg="#f2f2f2")
        button_quit.config(command=lambda: controller.show_frame("StartPage"))
        # button_quit.place(x=100, y=100)
        button_quit.grid(row=2, column=4, columnspan=2)

        # create character button
        button_create = tk.Button(navfrm, text="Create", padx=35, pady=10, bg="#25262b", fg="#f2f2f2")
        button_create.config(command=lambda: controller.show_frame("CreatePage"))
        button_create.grid(row=2, column=8, columnspan=2)

        # load character button
        button_load = tk.Button(navfrm, text="Load", padx=35, pady=10, bg="#25262b", fg="#f2f2f2")
        button_load.config(state="disabled", command=lambda: controller.show_frame("LoadPage"))
        button_load.grid(row=2, column=12, columnspan=2)

        displbl = tk.Label(bg, text="Click on\'Open File\' to select a character file \n ??? files only", bg="#25262b", fg="#f2f2f2")
        displbl.place(x=290, y=500,anchor="center")


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

import tkinter as tk
import csv
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import font as tkfont


root = tk.Tk()
root["bg"] = "#0d0d0d"
root.geometry("1200x650")
root.resizable(False, False)
root.title("BitD Character Creator")
root.iconbitmap('images/favicon.ico')


# >>>>>>>>>>>>>> Main Frame <<<<<<<<<<<<<<<<<<<<<
startfrm = tk.Frame(root, height=559, width=1200, bg="#0d0d0d")
startfrm.grid(row=0, column=0, columnspan=14)

global bitdbanner
bitdbanner = ImageTk.PhotoImage(Image.open('images/BitD_banner.png'))
bg = tk.Label(startfrm, image=bitdbanner, bg='#0d0d0d')
bg.grid(row=0, column=0, columnspan=14)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!THIS IS IN 2 LOCATIONS
def savfile():
    formats = [('Comma Separated values', '*.csv'), ]
    global file_name

    fields = ["name", "alias", "look", "heiritage", "background", "vice", "details", "playbook", "specAbility",
              "friend", "rival", "action1", "action2", "action3", "action4", "action5", "action6", "action7"]

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!NEED TO CREATE FUNCTIONS TO GRAB DATA
    # namecsv = "Tanis"
    # aliascsv = "the well endowed"
    # lookcsv = "well dressed"
    # heiritagecsv = "Rimmgarder"
    # backgroundcsv = "Military"
    # vicecsv = "the leaf"
    # vicedetailscsv = "All day everyday, the guy down the street"
    # playbookcsv = "cutter"
    # specAbilitycsv = 0
    # friendcsv = 2
    # rivalcsv = 4
    # action1csv = "hunt1"
    # action2csv = "hunt2"
    # action3csv = "prowl1"
    # action4csv = "skirmish1"
    # action5csv = "skrmish2"
    # action6csv = "command1"
    # action7csv = "consort1"
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!NEED TO CREATE FUNCTIONS TO GRAB DATA

    rows = [namecsv, aliascsv, lookcsv, heiritagecsv, backgroundcsv, vicecsv, vicedetailscsv, playbookcsv,
            specAbilitycsv, friendcsv, rivalcsv, action1csv, action2csv, action3csv, action4csv, action5csv, action6csv,
            action7csv]

    with open(filedialog.asksaveasfilename(parent=root, filetypes=formats, defaultextension=".csv", title="Save As..."),
              'w', newline='', encoding='utf-8') as fp:
        csvwriter = csv.writer(fp)
        csvwriter.writerow(fields)
        csvwriter.writerow(rows)


def openload():

    ldwindow = tk.Toplevel(root)
    ldwindow["bg"] = "#0d0d0d"
    ldwindow.geometry("1200x650")
    ldwindow.resizable(False, False)
    ldwindow.title("BitD Character Creator-Load")
    ldwindow.iconbitmap('images/favicon.ico')
    # global file_image
    # filename = filedialog.askopenfilename(initialdir="", title="Select A File", filetypes=[("CSV files", "*.csv")])

    def openmain():
        try:
            ldwindow.withdraw()
        finally:
            root.deiconify()

    infofrm = tk.Frame(ldwindow, height=559, width=1200, bg="#F25C05")
    infofrm.grid(row=0, column=0, columnspan=14)

    global bitddrk
    bitddrk = ImageTk.PhotoImage(Image.open('images/BitD_dark.png'))

    global bgload
    bgload = tk.Label(infofrm, image=bitddrk, bg='#0d0d0d', borderwidth=0, highlightthickness=0)
    bgload.grid(column=0, row=0)

    navfrm = tk.Frame(ldwindow, width=1200, height=85, bg="#0d0d0d", borderwidth=0, highlightthickness=0)
    navfrm.grid(row=1, column=0, columnspan=14)

    # creates invisible spacer so that buttons display as intended
    spacfrm = tk.Frame(navfrm, width=1200, height=1, bg="#0d0d0d")
    spacfrm.grid(row=0, column=0, columnspan=14)

    # make exit button
    button_quit = tk.Button(navfrm, text="Exit", padx=40, pady=10, bg="#25262b", fg="#f2f2f2")
    button_quit.config(command=root.quit)
    button_quit.grid(row=2, column=3, columnspan=2, )

    # make main button
    button_quit = tk.Button(navfrm, text="Main", padx=40, pady=10, bg="#25262b", fg="#f2f2f2")
    button_quit.config(command=openmain)
    button_quit.grid(row=2, column=6, columnspan=2)

    # load character button
    button_load = tk.Button(navfrm, text="Load", padx=35, pady=10, bg="#25262b", fg="#f2f2f2", disabledforeground="#f25c05")
    button_load.config(state="disabled")
    button_load.grid(row=2, column=9, columnspan=2)


def opencreate():
    root.withdraw()

    crwindow = tk.Toplevel(root)
    crwindow["bg"] = "#0d0d0d"
    crwindow.geometry("1200x650")
    crwindow.resizable(False, False)
    crwindow.title("BitD Character Creator")
    crwindow.iconbitmap('images/favicon.ico')

    def openmain():
        try:
            crwindow.withdraw()
        finally:
            root.deiconify()


    infofrm = tk.Frame(crwindow, height=559, width=1200, bg="#F25C05")
    infofrm.grid(row=0, column=0, columnspan=7)

    global bitddrk
    bitddrk = ImageTk.PhotoImage(Image.open('images/BitD_dark.png'))
    global bgcreate
    bgcreate = tk.Label(infofrm, image=bitddrk, bg='#0d0d0d', borderwidth=0, highlightthickness=0)
    bgcreate.grid(column=0, row=0, sticky="e")


    # name section
    nameframe = tk.Frame(bgcreate, width=235, height=50)
    nameframe.place(x=75, y=25)
    nameframe.pack_propagate(False)
    namelabel = tk.Label(nameframe, text="Name", fg="#f25c05", bg="#25262b", font=("Helvetica 14 bold"))
    namelabel.pack(fill=tk.X)
    nameentry = tk.Entry(nameframe, font=("Helvetica 14"))
    nameentry.pack(fill=tk.X)

    # Alias Section
    aliasframe = tk.Frame(bgcreate, width=235, height=50)
    aliasframe.place(x=325, y=25)
    aliasframe.pack_propagate(False)
    aliaslabel = tk.Label(aliasframe, text="Alias", fg="#f25c05", bg="#25262b", font=("Helvetica 14 bold"))
    aliaslabel.pack(fill=tk.X)
    aliasentry = tk.Entry(aliasframe, font=("Helvetica 14"))
    aliasentry.pack(fill=tk.X)

    # Look Section
    lookframe = tk.Frame(bgcreate, width=485, height=50)
    lookframe.place(x=75, y=100)
    lookframe.pack_propagate(False)
    looklabel = tk.Label(lookframe, text="Describe Your Look", fg="#f25c05", bg="#25262b",
                         font=("Helvetica 14 bold"))
    looklabel.pack(fill=tk.X)
    lookentry = tk.Entry(lookframe, font=("Helvetica 14"))
    lookentry.pack(fill=tk.X)

    # Heiritage secion
    heirframe = tk.Frame(bgcreate, width=235, height=50)
    heirframe.place(x=75, y=175)
    heirframe.pack_propagate(False)
    heirlabel = tk.Label(heirframe, text="Heiritage", fg="#f25c05", bg="#25262b", font=("Helvetica 14 bold"))
    heirlabel.pack(fill=tk.X)
    # !!!!!!!! MAKE DROPDOWN!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    heirentry = tk.Entry(heirframe, font=("Helvetica 14"))
    heirentry.pack(fill=tk.X)

    # Background Section
    backframe = tk.Frame(bgcreate, width=235, height=50)
    backframe.place(x=325, y=175)
    backframe.pack_propagate(False)
    backlabel = tk.Label(backframe, text="Background", fg="#f25c05", bg="#25262b", font=("Helvetica 14 bold"))
    backlabel.pack(fill=tk.X)
    # !!!!!!MAKE DROPDOWN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    backentry = tk.Entry(backframe, font=("Helvetica 14"))
    backentry.pack(fill=tk.X)

    # Vice Section
    # Create Vice Frame
    viceframe = tk.Frame(bgcreate, width=485, height=125, bg="#25262b")
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

    # >>>>>>>>>>>>>>>>>>> PLAYBOOK SELECTION SECTION <<<<<<<<<<<<<<<<<<<<<<<<

    # dictionary of playbooks and row in reference csv file
    global playdict
    playdict = {"cutter": 1, "hound": 2, "leech": 3, "lurk": 4, "slide": 5, "spider": 6, "whisper": 7}

    # create capitalized list from dictionary
    playbooknames = list(playdict.keys())
    for i in range(len(playbooknames)):
        playbooknames[i] = playbooknames[i].capitalize()

    # Select button functions
    def playclick(value):
        """Function takes in value from radio button and configures
        radio buttons of abilities and ally sections"""
        updateability(value)
        updatefriend(value)
        updateactions(value)

    def updateability(value):
        global playbook
        if value == 1:
            playbook = "cutter"
        elif value == 2:
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
        elif value == 2:
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

    def updateactions(value):
        try:
            for i in actionckbxlist:
                i.deselect()
            for index, element in enumerate(actionckbxlist):
                if index % 4 == 0:
                    element.config(state="normal")
        finally:
            if value == 1:
                playbook = "cutter"
                skirmishbox1.select()
                skirmishbox1.config(state="disabled")
                skirmishbox2.select()
                commandbox1.select()
                commandbox1.config(state="disabled")
                commandbox2.config(state="normal")
            elif value == 2:
                playbook = "hound"
                huntbox1.select()
                huntbox1.config(state="disabled")
                huntbox2.select()
                surveybox1.select()
                surveybox1.config(state="disabled")
            elif value == 3:
                playbook = "leech"
                tinkerbox1.select()
                tinkerbox1.config(state="disabled")
                tinkerbox2.select()
                wreckbox1.select()
                wreckbox1.config(state="disabled")
            elif value == 4:
                playbook = "lurk"
                prowlbox1.select()
                prowlbox1.config(state="disabled")
                prowlbox2.select()
                finessebox1.select()
                finessebox1.config(state="disabled")
            elif value == 5:
                playbook = "slide"
                swaybox1.select()
                swaybox1.config(state="disabled")
                swaybox2.select()
                consortbox1.select()
                consortbox1.config(state="disabled")
            elif value == 6:
                playbook = "spider"
                consortbox1.select()
                consortbox1.config(state="disabled")
                consortbox2.select()
                studybox1.select()
                studybox1.config(state="disabled")
            elif value == 7:
                playbook = "whisper"
                attunebox1.select()
                attunebox1.config(state="disabled")
                attunebox2.select()
                studybox1.select()
                studybox1.config(state="disabled")

    # Create Playbook Selection Frame
    archselframe = tk.Frame(bgcreate, width=485, height=125, bg="#25262b")
    archselframe.place(x=75, y=400)

    # Create Label
    archsellabel = tk.Label(archselframe, padx=160, pady=4, text="Select A Playbook", fg="#f25c05", bg="#25262b",
                            font=("Helvetica 14 bold"))
    archsellabel.grid(column=0, row=0, columnspan=4)

    # sets variable type for playbook selection radio buttons
    p1 = tk.IntVar()
    p1.set(1)

    # first row radiobuttons
    for i in range(1, 5):
        tk.Radiobutton(archselframe, text=f"{(playbooknames[i - 1])}", padx=17, variable=p1, value=i,
                       selectcolor="#0d0d0d", fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"),
                       command=lambda: playclick(p1.get())).grid(row=1, column=i - 1)

    # second row radiobuttons
    for i in range(5, 8):
        tk.Radiobutton(archselframe, text=f"{(playbooknames[i - 1])}", padx=17, variable=p1, value=i,
                       selectcolor="#0d0d0d", fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"),
                       command=lambda: playclick(p1.get())).grid(row=2, column=i - 5, columnspan=2)

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
        """Propagates a list of a playbook's special abilities for reference by the program. play is passed
        through to read_cell and values returned appended to the list"""

        abilitylist = []
        for i in range(1, 9):
            abilitylist.append(read_cell(i, play))
            abilities = tuple(abilitylist)
        return abilities

    def friendfoe(play):
        """Propagates a list of a playbooks friends and rivals for reference by program. play is passed
        through to read_cell and values returned appended to the list"""

        friendlist = []
        for i in range(17, 22):
            friendlist.append(read_cell(i, play))
            friends = tuple(friendlist)
        return friends

    # create list from selected playbook
    specabilities = specability("cutter")

    # Create Special Ability Frame
    specfrm = tk.Frame(bgcreate, width=317, height=275, bg="#25262b")
    specfrm.place(x=598, y=25)
    specfrm.pack_propagate(False)

    # sets variable type for ability selection radio buttons
    s = tk.IntVar()
    s.set(1)

    # Creates label and radiobuttons
    # label
    speclabel = tk.Label(specfrm, text="Pick A Special Ability", fg="#f25c05", bg="#25262b", font=("Helvetica 14 bold"))
    speclabel.pack()

    # radiobuttons
    s1 = tk.Radiobutton(specfrm, text=f"{(specabilities[0])}", padx=17, variable=s, value=1, selectcolor="#0d0d0d",
                        fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
    s2 = tk.Radiobutton(specfrm, text=f"{(specabilities[1])}", padx=17, variable=s, value=2, selectcolor="#0d0d0d",
                        fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
    s3 = tk.Radiobutton(specfrm, text=f"{(specabilities[2])}", padx=17, variable=s, value=3, selectcolor="#0d0d0d",
                        fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
    s4 = tk.Radiobutton(specfrm, text=f"{(specabilities[3])}", padx=17, variable=s, value=4, selectcolor="#0d0d0d",
                        fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
    s5 = tk.Radiobutton(specfrm, text=f"{(specabilities[4])}", padx=17, variable=s, value=5, selectcolor="#0d0d0d",
                        fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
    s6 = tk.Radiobutton(specfrm, text=f"{(specabilities[5])}", padx=17, variable=s, value=6, selectcolor="#0d0d0d",
                        fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
    s7 = tk.Radiobutton(specfrm, text=f"{(specabilities[6])}", padx=17, variable=s, value=7, selectcolor="#0d0d0d",
                        fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))
    s8 = tk.Radiobutton(specfrm, text=f"{(specabilities[7])}", padx=17, variable=s, value=8, selectcolor="#0d0d0d",
                        fg="#f2f2f2", bg="#25262b", font=("Helvetica 12"))

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
    frndfrm = tk.Frame(bgcreate, width=317, height=225, bg="#25262b")
    frndfrm.place(x=598, y=315)
    frndfrm.grid_propagate(False)

    #  Create top Label
    frndlabel = tk.Label(frndfrm, padx=75, text="Pick One Each", fg="#f25c05", bg="#25262b", font=("Helvetica 14 bold"))
    frndlabel.grid(column=0, row=0, columnspan=2)

    # Create Button Labels
    fbuttonlabel = tk.Label(frndfrm, padx=10, text="Friend", fg="#f25c05", bg="#25262b", anchor=tk.W,
                            font=("Helvetica 14 bold"))
    fbuttonlabel.grid(column=0, row=1, sticky=tk.W)
    rbuttonlabel = tk.Label(frndfrm, padx=10, text="Rival", fg="#f25c05", bg="#25262b", justify=tk.RIGHT, anchor=tk.E,
                            font=("Helvetica 14 bold"))
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

    fr1.grid(column=0, row=2, sticky=tk.W)
    fr2.grid(column=0, row=3, sticky=tk.W)
    fr3.grid(column=0, row=4, sticky=tk.W)
    fr4.grid(column=0, row=5, sticky=tk.W)
    fr5.grid(column=0, row=6, sticky=tk.W)

    # Create rival radiobuttons
    r1 = tk.Radiobutton(frndfrm, text=f"", padx=17, variable=r, value=1, selectcolor="#0d0d0d", fg="#f2f2f2",
                        bg="#25262b", font=("Helvetica 12"))
    r2 = tk.Radiobutton(frndfrm, text=f"", padx=17, variable=r, value=2, selectcolor="#0d0d0d", fg="#f2f2f2",
                        bg="#25262b", font=("Helvetica 12"))
    r3 = tk.Radiobutton(frndfrm, text=f"", padx=17, variable=r, value=3, selectcolor="#0d0d0d", fg="#f2f2f2",
                        bg="#25262b", font=("Helvetica 12"))
    r4 = tk.Radiobutton(frndfrm, text=f"", padx=17, variable=r, value=4, selectcolor="#0d0d0d", fg="#f2f2f2",
                        bg="#25262b", font=("Helvetica 12"))
    r5 = tk.Radiobutton(frndfrm, text=f"", padx=17, variable=r, value=5, selectcolor="#0d0d0d", fg="#f2f2f2",
                        bg="#25262b", font=("Helvetica 12"))

    r1.grid(column=1, row=2, sticky=tk.E)
    r2.grid(column=1, row=3, sticky=tk.E)
    r3.grid(column=1, row=4, sticky=tk.E)
    r4.grid(column=1, row=5, sticky=tk.E)
    r5.grid(column=1, row=6, sticky=tk.E)

    # ----ACTION RATING SECTION----

    # Create Action Checkbox Variables- These store the rank of each action
    # Insight Action Variables


    # Create Action Rating Frames
    actionsfrm = tk.Frame(bgcreate, width=198, height=450, bg="#25262b")
    actionsfrm.place(x=935, y=25)
    actionsfrm.grid_propagate(False)

    hunt1 = tk.IntVar()
    hunt2 = tk.IntVar()
    hunt3 = tk.IntVar()
    hunt4 = tk.IntVar()

    study1 = tk.IntVar()
    study2 = tk.IntVar()
    study3 = tk.IntVar()
    study4 = tk.IntVar()

    survey1 = tk.IntVar()
    survey2 = tk.IntVar()
    survey3 = tk.IntVar()
    survey4 = tk.IntVar()

    tinker1 = tk.IntVar()
    tinker2 = tk.IntVar()
    tinker3 = tk.IntVar()
    tinker4 = tk.IntVar()

    # Prowess Action Variables
    finesse1 = tk.IntVar()
    finesse2 = tk.IntVar()
    finesse3 = tk.IntVar()
    finesse4 = tk.IntVar()

    prowl1 = tk.IntVar()
    prowl2 = tk.IntVar()
    prowl3 = tk.IntVar()
    prowl4 = tk.IntVar()

    skirmish1 = tk.IntVar()
    skirmish2 = tk.IntVar()
    skirmish3 = tk.IntVar()
    skirmish4 = tk.IntVar()

    wreck1 = tk.IntVar()
    wreck2 = tk.IntVar()
    wreck3 = tk.IntVar()
    wreck4 = tk.IntVar()

    # Resolve Action Variables
    attune1 = tk.IntVar()
    attune2 = tk.IntVar()
    attune3 = tk.IntVar()
    attune4 = tk.IntVar()

    command1 = tk.IntVar()
    command2 = tk.IntVar()
    command3 = tk.IntVar()
    command4 = tk.IntVar()

    consort1 = tk.IntVar()
    consort2 = tk.IntVar()
    consort3 = tk.IntVar()
    consort4 = tk.IntVar()

    sway1 = tk.IntVar()
    sway2 = tk.IntVar()
    sway3 = tk.IntVar()
    sway4 = tk.IntVar()

    def actionclick(nextbtn, var):
        value = var.get()
        if value >= 1:
            nextbtn.config(state="normal")
        elif value<1:
            nextbtn.config(state="disabled")


    # Create Actions label
    actionslabel = tk.Label(actionsfrm, text="Assign Four\nAction Ranks", padx=35, fg="#f25c05", bg="#25262b",
                            anchor=tk.W, font=("Helvetica 14 bold"))
    actionslabel.grid(column=0, columnspan=4, row=0)

    # Create Insight Label
    insightlabel = tk.Label(actionsfrm, text="Insight", padx=35, fg="#f2f2f2", bg="#25262b", font=("Helvetica 12 bold"))
    insightlabel.grid(column=0, columnspan=4, row=1)
    # Create Insight Division Checkboxes
    # Huntboxes
    huntbox1 = tk.Checkbutton(actionsfrm, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d", font=("Helvetica 11"), variable= hunt1, command=lambda: actionclick(huntbox2, hunt1))
    huntbox1.grid(column=0, row=2)
    huntbox2 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                              font=("Helvetica 11"), command=actionclick, variable=hunt2)
    huntbox2.place(x=40, y=75)
    huntbox3 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                              font=("Helvetica 11"), variable=hunt3)
    huntbox3.place(x=60, y=75)
    huntbox4 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                              font=("Helvetica 11"), variable=hunt4)
    huntbox4.place(x=80, y=75)
    huntlabel = tk.Label(actionsfrm, text="Hunt", fg="#f2f2f2", bg="#25262b", font=("Helvetica 11 bold"))
    huntlabel.place(x=120, y=76)

    # Studyboxes
    studybox1 = tk.Checkbutton(actionsfrm, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d", font=("Helvetica 11"),
                               variable=study1, command=lambda: actionclick(studybox2, study1))
    studybox1.grid(column=0, row=3)
    studybox2 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                               font=("Helvetica 11"), variable=study2)
    studybox2.place(x=40, y=102)
    studybox3 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                               font=("Helvetica 11"), variable=study3)
    studybox3.place(x=60, y=102)
    studybox4 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                               font=("Helvetica 11"), variable=study4)
    studybox4.place(x=80, y=102)
    studylabel = tk.Label(actionsfrm, text="Study", fg="#f2f2f2", bg="#25262b", font=("Helvetica 11 bold"))
    studylabel.place(x=120, y=103)

    # Surveyboxes
    surveybox1 = tk.Checkbutton(actionsfrm, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d", font=("Helvetica 11"),
                                variable=survey1, command=lambda: actionclick(surveybox2, survey1))
    surveybox1.grid(column=0, row=4)
    surveybox2 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                font=("Helvetica 11"), variable=survey2)
    surveybox2.place(x=40, y=129)
    surveybox3 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                font=("Helvetica 11"), variable=survey3)
    surveybox3.place(x=60, y=129)
    surveybox4 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                font=("Helvetica 11"), variable=survey4)
    surveybox4.place(x=80, y=129)
    surveylabel = tk.Label(actionsfrm, text="Survey", fg="#f2f2f2", bg="#25262b", font=("Helvetica 11 bold"))
    surveylabel.place(x=120, y=130)

    # Tinkerboxes
    tinkerbox1 = tk.Checkbutton(actionsfrm, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d", font=("Helvetica 11"),
                                variable=tinker1, command=lambda: actionclick(tinkerbox2, tinker1))
    tinkerbox1.grid(column=0, row=5)
    tinkerbox2 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                font=("Helvetica 11"), variable=tinker2)
    tinkerbox2.place(x=40, y=156)
    tinkerbox3 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                font=("Helvetica 11"), variable=tinker3)
    tinkerbox3.place(x=60, y=156)
    tinkerbox4 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                font=("Helvetica 11"), variable=tinker4)
    tinkerbox4.place(x=80, y=156)
    tinkerlabel = tk.Label(actionsfrm, text="Tinker", fg="#f2f2f2", bg="#25262b", font=("Helvetica 11 bold"))
    tinkerlabel.place(x=120, y=157)

    # Create Prowess Label
    prowesslabel = tk.Label(actionsfrm, text="Prowess", padx=35, fg="#f2f2f2", bg="#25262b", font=("Helvetica 12 bold"))
    prowesslabel.grid(column=0, columnspan=4, row=6)
    # Create Prowess Division Checkboxes
    # Finesseboxes
    finessebox1 = tk.Checkbutton(actionsfrm, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d", font=("Helvetica 11"),
                                 variable=finesse1, command=lambda: actionclick(finessebox2, finesse1))
    finessebox1.grid(column=0, row=7)
    finessebox2 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                 font=("Helvetica 11"), variable=finesse2)
    finessebox2.place(x=40, y=208)
    finessebox3 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                 font=("Helvetica 11"), variable=finesse3)
    finessebox3.place(x=60, y=208)
    finessebox4 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                 font=("Helvetica 11"), variable=finesse4)
    finessebox4.place(x=80, y=208)
    finesselabel = tk.Label(actionsfrm, text="Finesse", fg="#f2f2f2", bg="#25262b", font=("Helvetica 11 bold"))
    finesselabel.place(x=120, y=209)

    # Prowlboxes
    prowlbox1 = tk.Checkbutton(actionsfrm, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d", font=("Helvetica 11"),
                               variable=prowl1, command=lambda: actionclick(prowlbox2, prowl1))
    prowlbox1.grid(column=0, row=8)
    prowlbox2 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                               font=("Helvetica 11"), variable=prowl2)
    prowlbox2.place(x=40, y=235)
    prowlbox3 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                               font=("Helvetica 11"), variable=prowl3)
    prowlbox3.place(x=60, y=235)
    prowlbox4 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                               font=("Helvetica 11"), variable=prowl4)
    prowlbox4.place(x=80, y=235)
    prowllabel = tk.Label(actionsfrm, text="Prowl", fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", font=("Helvetica 11 bold"))
    prowllabel.place(x=120, y=235)

    # Skirmishboxes
    skirmishbox1 = tk.Checkbutton(actionsfrm, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d", font=("Helvetica 11"),
                                  variable=skirmish1, command=lambda: actionclick(skirmishbox2, skirmish1))
    skirmishbox1.grid(column=0, row=9)
    skirmishbox2 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                  font=("Helvetica 11"), variable=skirmish2)
    skirmishbox2.place(x=40, y=262)
    skirmishbox3 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                  font=("Helvetica 11"), variable=skirmish3)
    skirmishbox3.place(x=60, y=262)
    skirmishbox4 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                  font=("Helvetica 11"), variable=skirmish4)
    skirmishbox4.place(x=80, y=262)
    skirmishlabel = tk.Label(actionsfrm, text="Skirmish", fg="#f2f2f2", bg="#25262b", font=("Helvetica 11 bold"))
    skirmishlabel.place(x=120, y=263)

    # Wreckboxes
    wreckbox1 = tk.Checkbutton(actionsfrm, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d", font=("Helvetica 11"),
                               variable=wreck1, command=lambda: actionclick(wreckbox2, wreck1))
    wreckbox1.grid(column=0, row=10)
    wreckbox2 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                               font=("Helvetica 11"), variable=wreck2)
    wreckbox2.place(x=40, y=289)
    wreckbox3 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                               font=("Helvetica 11"), variable=wreck3)
    wreckbox3.place(x=60, y=289)
    wreckbox4 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                               font=("Helvetica 11"), variable=wreck4)
    wreckbox4.place(x=80, y=289)
    wrecklabel = tk.Label(actionsfrm, text="Wreck", fg="#f2f2f2", bg="#25262b", font=("Helvetica 11 bold"))
    wrecklabel.place(x=120, y=290)

    # Create Resolve Label
    resolvelabel = tk.Label(actionsfrm, text="Resolve", padx=35, fg="#f2f2f2", bg="#25262b", font=("Helvetica 12 bold"))
    resolvelabel.grid(column=0, columnspan=4, row=11)
    # Create Resolve Division Checkboxes
    # Attune Boxes
    attunebox1 = tk.Checkbutton(actionsfrm, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d", font=("Helvetica 11"),
                                variable=attune1, command=lambda: actionclick(attunebox2, attune1))
    attunebox1.grid(column=0, row=12)
    attunebox2 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                font=("Helvetica 11"), variable=attune2)
    attunebox2.place(x=40, y=341)
    attunebox3 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                font=("Helvetica 11"), variable=attune3)
    attunebox3.place(x=60, y=341)
    attunebox4 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                font=("Helvetica 11"), variable=attune4)
    attunebox4.place(x=80, y=341)
    attunelabel = tk.Label(actionsfrm, text="Attune", fg="#f2f2f2", bg="#25262b", font=("Helvetica 11 bold"))
    attunelabel.place(x=120, y=342)

    # Command Boxes
    commandbox1 = tk.Checkbutton(actionsfrm, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d", font=("Helvetica 11"), variable=command1, command=lambda: actionclick(commandbox2, command1))
    commandbox1.grid(column=0, row=13)
    commandbox2 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                 font=("Helvetica 11"), variable=command2)
    commandbox2.place(x=40, y=368)
    commandbox3 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                 font=("Helvetica 11"), variable=command3)
    commandbox3.place(x=60, y=368)
    commandbox4 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                 font=("Helvetica 11"), variable=command4)
    commandbox4.place(x=80, y=368)
    commandlabel = tk.Label(actionsfrm, text="Command", fg="#f2f2f2", bg="#25262b", font=("Helvetica 11 bold"))
    commandlabel.place(x=120, y=369)

    # Consort Boxes
    consortbox1 = tk.Checkbutton(actionsfrm, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d", font=("Helvetica 11"),
                                 variable=consort1, command=lambda: actionclick(consortbox2, consort1))
    consortbox1.grid(column=0, row=14)
    consortbox2 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                 font=("Helvetica 11"), variable=consort2)
    consortbox2.place(x=40, y=395)
    consortbox3 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                 font=("Helvetica 11"), variable=consort3)
    consortbox3.place(x=60, y=395)
    consortbox4 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                                 font=("Helvetica 11"), variable=consort4)
    consortbox4.place(x=80, y=395)
    consortlabel = tk.Label(actionsfrm, text="Consort", fg="#f2f2f2", bg="#25262b", font=("Helvetica 11 bold"))
    consortlabel.place(x=120, y=396)

    # Sway Boxes
    swaybox1 = tk.Checkbutton(actionsfrm, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d", font=("Helvetica 11"),
                              variable=sway1, command=lambda: actionclick(swaybox2, sway1))
    swaybox1.grid(column=0, row=15)
    swaybox2 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                              font=("Helvetica 11"), variable=sway2)
    swaybox2.place(x=40, y=422)
    swaybox3 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                              font=("Helvetica 11"), variable=sway3)
    swaybox3.place(x=60, y=422)
    swaybox4 = tk.Checkbutton(actionsfrm, state=tk.DISABLED, fg="#f2f2f2", bg="#25262b", disabledforeground="#f25c05", selectcolor="#0d0d0d",
                              font=("Helvetica 11"), variable=sway4)
    swaybox4.place(x=80, y=422)
    swaylabel = tk.Label(actionsfrm, text="Sway", fg="#f2f2f2", bg="#25262b", font=("Helvetica 11 bold"))
    swaylabel.place(x=120, y=423)

    actionckbxlist = [huntbox1, huntbox2, huntbox3, huntbox4, studybox1, studybox2, studybox3, studybox4, surveybox1, surveybox2, surveybox3, surveybox4, tinkerbox1,tinkerbox2, tinkerbox3, tinkerbox4, finessebox1, finessebox2, finessebox3, finessebox4, prowlbox1, prowlbox2, prowlbox3, prowlbox4, skirmishbox1, skirmishbox2, skirmishbox3, skirmishbox4, wreckbox1, wreckbox2, wreckbox3, wreckbox4, attunebox1, attunebox2, attunebox3, attunebox4, commandbox1, commandbox2, commandbox3, commandbox4, consortbox1, consortbox2, consortbox3, consortbox4, swaybox1, swaybox2, swaybox3, swaybox4]
    action1_2list = [huntbox1, huntbox2, studybox1, studybox2, surveybox1, tinkerbox1,tinkerbox2, tinkerbox3, tinkerbox4, finessebox1, finessebox2, finessebox3, finessebox4, prowlbox1, prowlbox2, prowlbox3, prowlbox4, skirmishbox1, skirmishbox2, skirmishbox3, skirmishbox4, wreckbox1, wreckbox2, wreckbox3, wreckbox4, attunebox1, attunebox2, attunebox3, attunebox4, commandbox1, commandbox2, commandbox3, commandbox4, consortbox1, consortbox2, consortbox3, consortbox4, swaybox1, swaybox2, swaybox3, swaybox4]

    # >>>>>>>>>>>>>>>>>>>>>>>>>>> Save File <<<<<<<<<<<<<<<<<<<<<

    # Save button
    def opnfile():
        global file_image
        opnfilename = filedialog.askopenfilename(initialdir="", title="Select A File",
                                                   filetypes=[("CSV files", "*.csv")])

    def savfile():
        formats = [('Comma Separated values', '*.csv'), ]
        global file_name

        fields = ["name", "alias", "look", "heiritage", "background", "vice", "details", "playbook", "specAbility",
                  "friend", "rival", "action1", "action2", "action3", "action4", "action5", "action6", "action7"]
        # !!!!!!!!!!!!!!!!!!!!!!!! These Need Proper input!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # namecsv = "Tanis"
        # aliascsv = "the well endowed"
        # lookcsv = "well dressed"
        # heiritagecsv = "Rimmgarder"
        # backgroundcsv = "Military"
        # vicecsv = "the leaf"
        # vicedetailscsv = "All day everyday, the guy down the street"
        # playbookcsv = "cutter"
        # specAbilitycsv = 0
        # friendcsv = 2
        # rivalcsv = 4
        # action1csv = "hunt1"
        # action2csv = "hunt2"
        # action3csv = "prowl1"
        # action4csv = "skirmish1"
        # action5csv = "skrmish2"
        # action6csv = "command1"
        # action7csv = "consort1"
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        rows = [namecsv, aliascsv, lookcsv, heiritagecsv, backgroundcsv, vicecsv, vicedetailscsv, playbookcsv,
                specAbilitycsv, friendcsv, rivalcsv, action1csv, action2csv, action3csv, action4csv, action5csv,
                action6csv,
                action7csv]

        with open(filedialog.asksaveasfilename(parent=root, filetypes=formats, defaultextension=".csv",
                                               title="Save As..."),
                  'w', newline='', encoding='utf-8') as fp:
            csvwriter = csv.writer(fp)
            csvwriter.writerow(fields)
            csvwriter.writerow(rows)
        # !!! ADD FILETYPE CHECK

        # !!! CREATE>>>CALL NEW FRAME WITH DATA FROM FILE

    # Save file button
    savebutton = tk.Button(bgcreate, text="Save Character", command=savfile, padx=27, pady=10, bg="#25262b",
                           fg="#F25C05")
    savebutton.place(x=965, y=495)

    # >>>>>>>>>>>>>>>>>>>>> Navigation Section <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # Create Navigation Frame
    navcfrm = tk.Frame(crwindow, width=1200, height=85, bg="#0d0d0d", borderwidth=0, highlightthickness=0)
    navcfrm.grid(row=1, column=0, columnspan=14)

    # creates invisible spacer so that buttons display as intended
    spacfrm = tk.Frame(navcfrm, width=1200, height=1, bg="#0d0d0d")
    spacfrm.grid(row=0, column=0, columnspan=14)

    # make exit button
    button_quit = tk.Button(navcfrm, text="Exit", padx=40, pady=10, bg="#25262b", fg="#f2f2f2")
    button_quit.config(command=root.quit)
    button_quit.grid(row=2, column=3, columnspan=2, )

    # make main button
    button_quit = tk.Button(navcfrm, text="Main", padx=40, pady=10, bg="#25262b", fg="#f2f2f2")
    button_quit.config(command=openmain)
    button_quit.grid(row=2, column=6, columnspan=2)

    # create character button
    button_create = tk.Button(navcfrm, text="Create", padx=35, pady=10, bg="#25262b", fg="#f2f2f2")
    button_create.config(state="disabled", disabledforeground="#f25c05")
    button_create.grid(row=2, column=9, columnspan=2)


# >>>>>>>>>>>>>>>>>>>>> Navigation Section <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Create Navigation Frame
navfrm = tk.Frame(root, width=1200, height=85, bg="#0d0d0d", borderwidth=0, highlightthickness=0)
navfrm.grid(row=1, column=0, columnspan=14)

# creates invisible spacer so that buttons display as intended
spacfrm = tk.Frame(navfrm, width=1200, height=1, bg="#0d0d0d")
spacfrm.grid(row=0, column=0, columnspan=14)

# make exit button
button_quit = tk.Button(navfrm, text="Exit", padx=40, pady=10, bg="#25262b", fg="#f2f2f2")
button_quit.config(command=root.quit)
button_quit.grid(row=2, column=0, columnspan=2, )

# make main button
button_quit = tk.Button(navfrm, text="Main", padx=40, pady=10, bg="#25262b", fg="#f2f2f2")
button_quit.config(state="disabled", disabledforeground="#f25c05")
button_quit.grid(row=2, column=4, columnspan=2)

# create character button
button_create = tk.Button(navfrm, text="Create", padx=35, pady=10, bg="#25262b", fg="#f2f2f2")
button_create.config(command=opencreate)
button_create.grid(row=2, column=8, columnspan=2)

# load character button
button_load = tk.Button(navfrm, text="Load", padx=35, pady=10, bg="#25262b", fg="#f2f2f2")
button_load.config(command=openload)
button_load.grid(row=2, column=12, columnspan=2)




if __name__ == "__main__":
    root.mainloop()

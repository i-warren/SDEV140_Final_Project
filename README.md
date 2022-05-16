BitD Character Creator
========================
This character creator is designed to be used with the ***Blades in the Dark*** tabletop roleplaying game designed by **John Harper**. https://bladesinthedark.com/
The program is designed to allow a user to easily create a character and then save the character as a csv file. Future improvements will allow a user to view the character that has been saved.

How to Use This Program
-----------------------
### Requirements
This program is written with Python 3. If you don't have **Python 3** you can download it at [here](https://www.python.org/downloads/)
This program also has the following imports
- tkinter as tk
- csv
- ImageTk, Image from PIL
- filedialog from tkinter

### Using the Program
The  program laods to a main screen from which the user can navigate to the main windows of the program
#### Nav Bars
The Navbars in the program may consist of the following buttons:
- Exit 
> Exits the Program
- Main
> Returns user to the main window
- Create
> Opens the Create Character window
- Load
> Opens the Load Character Window

### Create Character Window
This window allows the user to create a character using the rules of the ***Blades in the Dark Game***. To reference game rules on how to create characters go [here](https://bladesinthedark.com/character-creation)

#### Name
Enter your characters name

#### Alias
Enter your characters alias

#### Describe Your Look
Enter how your character appears/dresses.

#### Heiritage
Enter your characters Heiritage

#### Background
Enter your characters Background and any details about it.

#### Vice
Choose a single vice, then enter any detail and the purveyor of the vice.

#### Playbook
Choose a single playbook. This will change which **Special Abilities** and **Friends/Rivals** you can select. It will also auto populate the starting actions for the playbook.

#### Special Ability
Pick one **Special Ability**.

#### Friend/Rival
Pick one **Friend** using the buttons on the left and one **Rival** using the buttons on the right.

#### Action Ranks
Assign 4 **Action Ranks**. You may not select a rank higher than two at character creation.

#### Save Character
This will save the data from the form to a csv file to load later in the **Load Window**.

### Load Character Window
***This section is under construction currently. Please check in later.*** 




Future Improvements
-------------------
Moving forward improvements will be added as seen below
- Finish **Load Window**
- Change setup so instead of TopLevel windows program raises a frame to visible status
- Create global variables for fonts styles
- Make all aspects of Playbooks importable from CSV to easily add new playbooks
- Change Background and Heiritage to dropdown options
- Add character loadout options
- Add write to pdf feature

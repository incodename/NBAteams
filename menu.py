#Building Beautiful Command Line Interfaces with Python
from __future__ import print_function
from pyfiglet import Figlet
from clint.arguments import Args
from clint.textui import puts, colored, indent

from query import insertTeam
from query import deleteTeam
from query import updateTeam
from query import viewTeam
from query import searchTeam
import sys
import os

sys.path.insert(0, os.path.abspath('..'))
args = Args()

q = 'y'
while (q == 'y') or (q =='Y'):
    os.system('cls')

    f = Figlet(font='slant')
    d = Figlet(font='doom')
    print (f.renderText("NBA TEAMS"))

    print('>>> Introducing the 2019 NBA Team Rosters!')
    print('                                   Version 4.1.19d\n')

    puts(colored.yellow('Group 2'))
    puts(colored.clean('Eugenio, Jared Bryce B.'))
    puts(colored.clean('Cajipe,  Ralph Henrik I.'))
    puts(colored.clean('Finessa, Carl Ryan\n'))

    puts(colored.cyan('[1] - Add Team '))
    puts(colored.red('[2] - Delete Team'))
    puts(colored.green('[3] - Update Team'))
    puts(colored.yellow('[4] - View Team'))
    puts(colored.magenta('[5] - Search Team'))
    puts(colored.cyan('[6] - Exit\n'))

    choice = int(input('>>> Enter Choice: '))
    if choice == 1:
        os.system('cls')
        a = input('Enter Team Name: ')
        b = input('Enter Starting Point Guard: ')
        c = input('Enter Starting Shooting Guard: ')
        d = input('Enter Starting Small Forward: ')
        e = input('Enter Starting Power Forward: ')
        f = input('Enter Starting Center: ')
        g = input('Enter Owner: ')
        h = input('Enter Coach: ')
        insertTeam(a,b,c,d,e,f,g,h)

    elif choice == 2:
        os.system('cls')
        viewTeam()
        os.system('cls')
        teamN = input('Enter Team Name: ')
        deleteTeam(teamN)

    elif choice == 3:
        os.system('cls')
        updateTeam()

    elif choice == 4:
        os.system('cls')
        viewTeam()

    elif choice == 5:
        os.system('cls')
        searchTeam()

    elif choice == 6:
        os.system('cls')
        print (d.renderText("SEE YOU IN PLAYOFFS!"))
        sys.exit()

    else:
        os.system('cls')
        print('\nError.')

    print(' ')
    q = input('Go back to the Main Menu?[Y = Yes/X = Exit]: ')

    if q != 'y':
        os.system('cls')
        print(d.renderText("SEE YOU IN PLAYOFFS!"))
        sys.exit()

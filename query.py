from __future__ import print_function
from pyfiglet import Figlet
from clint.arguments import Args
from clint.textui import puts, colored, indent
from model import Team as tm
import peewee as p
import os
db = p.SqliteDatabase('nbateams.db')

def insertTeam(_tName,_tPG,_tSG,_tSF,_tPF,_tC,_tOwner,_tCoach):
    x = tm.insert({tm.tName:_tName,tm.tPG:_tPG,tm.tSG:_tSG,tm.tSF:_tSF,tm.tPF:_tPF,tm.tC:_tC,tm.tOwner:_tOwner,tm.tCoach:_tCoach})
    cnfrm = input('Are you sure you want to add {} to the list of teams? [Y]: '.format(_tName))
    if (cnfrm == 'y') or (cnfrm == 'Y'):
        y = x.execute()
        os.system('cls')
        viewTeam()
        puts(colored.cyan('\nThere are now a total of {} teams!\n'.format(y)))

def deleteTeam(teamN):
    x = tm.delete().where(tm.tName == teamN)
    cnfrm = input('Are you sure you want to delete {} from the list of teams? [Y]: '.format(teamN))
    if (cnfrm == 'y') or (cnfrm == 'Y'):
        y = x.execute()
        os.system('cls')
        viewTeam()
        puts(colored.cyan('\n{} team has been deleted!\n'.format(y)))


def updateTeam():
    viewTeam()
    teamN = input('Enter the name of the Team: ')
    _tName = input('Enter the name of the new Team: ')
    _tPG = input('Point Guard: ')
    _tSG = input('Shooting Guard: ')
    _tSF = input('Small Forward: ')
    _tPF = input('Power Forward: ')
    _tC = input('Center: ')
    _tOwner = input('Team Owner: ')
    _tCoach = input('Team Coach: ')

    x = tm.update({tm.tName:_tName,tm.tPG:_tPG,tm.tSG:_tSG,tm.tSF:_tSF,tm.tPF:_tPF,tm.tC:_tC,tm.tOwner:_tOwner,tm.tCoach:_tCoach}).where(tm.tName==teamN)
    cnfrm = input('Are you sure you want to replace the {} with the {}? [Y]: '.format(teamN,_tName))
    if (cnfrm == 'y') or (cnfrm == 'Y'):
        y = x.execute()
        os.system('cls')
        puts(colored.cyan('\n{} team has been updated!\n'.format(y)))
        viewTeam()

def viewTeam():
    hold = 123
    tt = 0
    tc = tm.select().count()

    while (hold == 123):
        t = tm.select().limit(5).offset(tt)
        print('{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}'.format('Team','Point Guard', 'Shooting Guard', 'Small Forward', 'Power Forward', 'Center', 'Owner', 'Coach'))
        print('-'*157)
        for team in t:
            print('{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}'.format(team.tName,team.tPG,team.tSG,team.tSF,team.tPF,team.tC,team.tOwner,team.tCoach))
        hold = input('\nNEXT[N]|END[X]: ')

        while (hold == 'n') or (hold =='N'):
            os.system('cls')
            tt = tt + 5
            t = tm.select().limit(5).offset(tt)
            print('{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}'.format('Team','Point Guard', 'Shooting Guard', 'Small Forward', 'Power Forward', 'Center', 'Owner', 'Coach'))
            print('-'*160)
            for team in t:
                print('{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}'.format(team.tName,team.tPG,team.tSG,team.tSF,team.tPF,team.tC,team.tOwner,team.tCoach))
            hold = input('\nPREV[P]|NEXT[N]|END[X]: ')

            while (hold == 'p') or (hold =='P'):
                os.system('cls')
                tt = tt - 5
                t = tm.select().limit(5).offset(tt)
                print('{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}'.format('Team','Point Guard', 'Shooting Guard', 'Small Forward', 'Power Forward', 'Center', 'Owner', 'Coach'))
                print('-'*160)
                for team in t:
                    print('{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}'.format(team.tName,team.tPG,team.tSG,team.tSF,team.tPF,team.tC,team.tOwner,team.tCoach))
                hold = input('\nPREV[P]|NEXT[N]|END[X]: ')

                if  (tt == 5) & (hold == 'p') or (hold == 'P'):
                    os.system('cls')
                    tt = 0
                    hold = 123


                elif tt < 0:
                    break




def searchTeam():
    teamN = input('Enter Team Name: ')
    t = tm.select().where(tm.tName.startswith(teamN))
    os.system('cls')
    print('{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}'.format('Team','Point Guard', 'Shooting Guard', 'Small Forward', 'Power Forward', 'Center', 'Owner', 'Coach'))
    print('-'*160)
    for team in t:
        print('{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}'.format(team.tName,team.tPG,team.tSG,team.tSF,team.tPF,team.tC,team.tOwner,team.tCoach))

    ctr = len(t)
    puts(colored.cyan('\nTotal No. of Teams: {}'.format(ctr)))

#   BTT: Version 0.2 Revival [Preview Release]
#   This release is incomplete. Only contains the Setup and could contain bugs.
#   Build Version: 4
#   Build Date: April 30, 2021
#   Made by rootinstinct, https://github.com/rootinstinct/ :) 
#   Special thanks to https://github.com/lemonheadongit/, they really helped out. (Literally redid the project 1000x better than me.)
#   Imports

import time
import os
import datetime
import random

#   Config Check and FTS

print()
print("================================")
print("|| BTT Revival 0.2 // Alpha 2 ||")
print("================================")
print("||    Made by rootinstinct    ||")
print("================================")
print("If you're experiencing any problems, be sure to leave an issue in the repository and let us know. \nRepo Link: https://github.com/rootinstinct/bettertimetable\n")
time.sleep(3)

cfgcheck = open('config.txt', 'r')
with open('config.txt', 'r') as cfgcheck:
    cfgstatus = cfgcheck.readlines()

#   First Time Setup [FTS]

if cfgstatus == ['fts0']:
    print("Starting First Time Setup...")
    time.sleep(1)
    input("First Time Setup ready, press any button to get started.\n")

#   Phase One:
#   Username

usersetup = open('username.txt', 'w')
with open('username.txt', 'w') as usersetup:
    username = input("We best get started with your name. Type out your name.\n")

#   Username Confirm

userconfirm = open('username.txt', 'w')
with open('username.txt', 'w') as userconfirm:
    print()
    print("Alright,", username)
    userconfirmin = input("Is that correct? [y/n]\n")

if userconfirmin == "n":
    userconfirmin = 1

if userconfirmin == "y":
    userconfirmin = 0

usertruewrite = open('username.txt', 'w')
if userconfirmin == 0:
    with open('username.txt', 'w') as usertruewrite:
        usertruewrite.write(username)

#   Username Confirm: Loop

while userconfirmin == 1:
    usersetup = open('username.txt', 'w')
    with open('username.txt', 'w') as usersetup:
        username = input("Alright, we go again, your name?\n")
        usersetup.write(username)
    with open('username.txt', 'r') as userconfirm:
        print("Alright,", username)
        userconfirmin = input("Is that correct? [y/n]\n")

#   Amount Of Days [AOD]

print()

aod = input("Now that we got your name sorted out, how many days of work do you have in a week? (This cannot be more than 7)\n")

aod = int(aod)

#   AOD Confirm

print()

print("Alright, you have", aod, " days in your schedule.")
aodconfirm = input("Is that correct? [y/n]\n")

if aodconfirm == "n":
    aodconfirm = 1

#   AOD Confirm: Loop

while aodconfirm == 1:
    aod = input("Let's try get it right this time (no pressure), how much days do you have per week in your schedule (1-7)\n")
    print("Alright, you have", aod, ".\n")
    aodconfirm = input("Is that correct? [y/n]\n")
    if aodconfirm == "n":
        aodconfirm = 1
    else:
        aodconfirm = 0

#   AOD Check

aod = int(aod)

if aod > 7 or aod < 1:
    input("That input was incorrect, amount of days cannot be more than 7 or less than 1. Press any button to continue.\n")
    aoderror = 1
else:
    aoderror = 0

#   AOD Check: Loop

while aoderror == 1:
    aod = input("Let's try get it right this time (no pressure), how much days do you have per week in your schedule (1-7)\n")
    aod = int(aod)
    if aod > 7 or aod < 1:
        input("That input was incorrect, amount of days cannot be more than 7 or less than 1. Press any button to continue.\n")
    else:
        aoderror = 0

#   AOD Write

aodwrite = open('aod.txt', 'w')

aod = str(aod)

if aoderror == 0:
    with open('aod.txt', 'w') as aodwrite:
        aodwrite.write(aod)

#   Amount of Subjects Per Day [AOS]

aos = input("And before we get into Subject setup, how many subjects do you have per day?\n")

aos = int(aos)

#   AOS Confirm

print("Alright, you have", aos, "subjects per day.")
aosconfirm = input("Is that correct? [y/n]")

if aosconfirm == "n":
    aosconfirm = 1

if aosconfirm == "y":
    aosconfirm = 0

#   AOS Confirm: Loop

while aosconfirm == 1:
    aos = input("Alright, let's try again. How many subjects do you have per day?\n")
    aos = int(aos)
    print("So, you have", aos, "subjects.\n")
    aosconfirmin = input("Is that correct? [y/n]")
    if aosconfirmin == "n":
        aosconfirm = 1

#   AOS Write

aoswrite = open('aos.txt', 'w')

aos = str(aos)

if aosconfirm == 0:
    with open('aos.txt', 'w') as aoswrite:
        aoswrite.write(aos)

#   End of Preview

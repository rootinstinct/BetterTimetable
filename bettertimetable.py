#   BetterTimetable: Version 0.2 Preview.
#   Configuration added! If your Timetable is not configured you should automatically be asked to go through the setup process.
#   Made by rootinstinct, https://www.github.com/rootinstinct/ :)
#   Let me know if anything is broken too. Constantly updating and squashing out bugs.
print("BetterTimetable -- Alpha 2 / 0.2")
config = open("config.txt","r") 
config2 = int(config.readline())
config.close()
config = open("config.txt", "w")
if config2 == 1:
    print("BetterTimetable setup initialized, answer a few questions and we'll get you up and running.")
    username = config.writelines(input("What is your name?"))
    subjectone_dayone = config.writelines((input("What is the first subject on Day One?")))
    subjecttwo_dayone = config.writelines((input("What is your second subject on Day One?")))
    subjectthree_dayone = config.writelines((input("What is your third subject on Day One?")))
    subjectfour_dayone = config.writelines((input("What is your fourth subject on Day One?")))
    subjectfive_dayone = config.writelines((input("What is your fifth subject on Day One?")))
            #   Day Two
    subjectone_daytwo = config.writelines((input("What is the first subject on Day Two?")))
    subjecttwo_daytwo = config.writelines((input("What is your second subject on Day Two?")))
    subjectthree_daytwo = config.writelines((input("What is your third subject on Day Two?")))
    subjectfour_daytwo = config.writelines((input("What is your fourth subject on Day Two?")))
    subjectfive_daytwo = config.writelines((input("What is your fifth subject on Day Two?")))
            #   Day Three
    subjectone_daythree = config.writelines((input("What is the first subject on Day Three?")))
    subjecttwo_daythree = config.writelines((input("What is your second subject on Day Three?")))
    subjectthree_daythree = config.writelines((input("What is your third subject on Day Three?")))
    subjectfour_daythree = config.writelines((input("What is your fourth subject on Day Three?")))
    subjectfive_daythree = config.writelines((input("What is your fifth subject on Day Three?")))
            #   Day Four
    subjectone_dayfour = config.writelines((input("What is the first subject on Day Four?")))
    subjecttwo_dayfour = config.writelines((input("What is your second subject on Day Four?")))
    subjectthree_dayfour = config.writelines((input("What is your third subject on Day Four?")))
    subjectfour_dayfour = config.writelines((input("What is your fourth subject on Day Four?")))
    subjectfive_dayfour = config.writelines((input("What is your fifth subject on Day Four?")))
            #   Day Five
    subjectone_dayfive = config.writelines((input("What is the first subject on Day Five?")))
    subjecttwo_dayfive = config.writelines((input("What is your second subject on Day Five?")))
    subjectthree_dayfive = config.writelines((input("What is your third subject on Day Five?")))
    subjectfour_dayfive = config.writelines((input("What is your fourth subject on Day Five?")))
    subjectfive_dayfive = config.writelines((input("What is your fifth subject on Day Five?")))
            #   Day Six
    subjectone_daysix = config.writelines((input("What is the first subject on Day Six?")))
    subjecttwo_daysix = config.writelines((input("What is your second subject on Day Six?")))
    subjectthree_daysix = config.writelines((input("What is your third subject on Day Six?")))
    subjectfour_daysix = config.writelines((input("What is your fourth subject on Day Six?")))
    subjectfive_daysix = config.writelines((input("What is your fifth subject on Day Six?")))
    config.write("0")
    print("Alright, thats all the setup! This is BetterTimetable.")
else:
            print("BetterTimetable configured.")
day1 = "Day 1: (Unconfigured)"
day2 = "Day 2: (Unconfigured)"
day3 = "Day 3: (Unconfigured)"
day4 = "Day 4: (Unconfigured)"
day5 = "Day 5: (Unconfigured)"
day6 = "Day 6: (Unconfigured)"
day0 = "Day 0: (Unconfigured)"
day11 = "Day One: [Subjects]\n[Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
day21 = "Day Two: [Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
day31 = "Day Three: [Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
day41 = "Day Four: [Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
day51 = "Day Five: [Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
day61 = "Day Six: [Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
day01 = "Day Zero: [Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
print()
config = input("Timetable view:\nWould you like Clear View [press 0] or the default view? [press 1] ")
open1 = open("config.txt", "r")
if day1 == "[Day 1] (Unconfigured)":
    print("Status -- Unconfigured, please change code.")
else:
    print("Select the day and we'll show you your schedule.")
day = input()
day = int(day)
if day == 1 and config == 1:
    print(day1)
else:
    print(day11)
if day == 2 and config == 1:
    print(day2)
else:
    print(day21)
if day == 3 and config == 1:
    print(day3)
else:
    print(day31)
if day == 4 and config == 1:
    print(day4)
else:
    print(day41)
if day == 5 and config == 1:
    print(day5)
else:
    print(day51)
if day == 6 and config == 1:
    print(day6)
else:
    print(day61)
if day == 0 and config == 1:
    print(day0)
else:
    print(day01)
#   Hope your timetable is better :D

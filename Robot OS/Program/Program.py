import webbrowser
import sys
from subprocess import *
from time import sleep
import time
from playsound import playsound
user = input("Enter your username:")
machine = input("Please enter a machine name for your PI:")
print('''
-----------------------------------
         |CMS  Instruction|
1. For camera view - camera view
2. For help - help.set
3. To exit - shut.in or shutdown
4. For Windows Cam view - CMS.view
5. To set a lock/passward - Lock.CMS
6. To set Auto AI Pilot - RC.set
-----------------------------------
''')
while True:
    main = input("python3/" + (user) + "/" + (machine) + ">>> ")

    if "camera view" in main:
        Popen('python client.py')
        print('''
        -------------------------------------------
                         |NOTE|
        For the camera view, a temporary
        setup is required, please follow the 
        instructions.

        1. Enter your Raspberry PI's IP address
        in the first window that popup.

        2. To operate the camera from your Windows,
        Open the CMS OS and type the command -
        CMS.view

        3. Now you will get a Live view on your
        PC, about what your PI Camera is able to see

        OR

        You can use the PI os itself for live view
        but operating from windows is easy.
        --------------------------------------------
        ''')

    elif "help.set" in main:
        Popen('Help.html')

    elif "CMS.view" in main:
        print("Available for Windows and Mac OS only.")
        sleep(5)
        Popen('python server.py')

    elif "shut.in" in main or "shutdown" in main:
        print("Shuting down...")
        playsound('preview_4.mp3')
        sys.exit()

    elif "cls" in main or "cls()" in main or "clear" in main or "clear()" in main:
        Popen('cls.bat')
        time.sleep(3)
        print("python3/" + (user) + "/" + (machine) + ">>> ")

    elif "AI.RC_setup" in main or "RC.set" in main:
        Popen('python RC_1.py')
        sleep(3)
        Popen('python RC_2.py')
        sleep(7)
        print('''
        Before, heading to the location, please fill some os the informations needed for the flight.''')
        prop = input("How many propellers are there in the plane? :")
        if "1" in prop:
            print("Ok")

        elif "2" in prop:
            print("Ok")

        else:
            print("Sorry, can't be handeled.") 

        distance = input("What is the distance? In m? :")
        battery = input("Battery Mah -")
        motor = input("Kv rating of motor - ")

        if "1200" in battery or "1100" in battery or "1300" in battery and "2000" in motor or "2100" in battery or "2200" in battery or "2250" in battery and distance <= 1000 and distance >= 0:
            print('''Ok, the flight is possible,
            recommended not to fly in manual mode
            ''') 

        else:
            print("The flight is not possible by the AI's, try  flying in manual mode, However you can fly the plane using the AI in the computer.")
            print("Moreever the conditions can cause harm to the plane tough.")
    elif "Lock.CMS" in main:
        lock = input("New passward: ")
        print("New passward set as ")
        new = input("Enter passward:")

        if lock in new:
            print("Welocme back " + (user))

        else:
            print("Try againg later...")
            sleep(5)
            playsound('preview_4.mp3')

    else:
        print((main) + " Command not recognised.")
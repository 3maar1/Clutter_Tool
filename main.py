from math import floor
import shutil
from colorama import init,Fore
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import os
import json
import time
import logging
import random
from fuzzywuzzy import fuzz

init(autoreset=True)
while True:
    print(Fore.BLUE +
    """
Welcome to
    
██████╗ ██╗      █████╗ ███╗   ██╗██╗██╗  ██╗
██╔══██╗██║     ██╔══██╗████╗  ██║██║╚██╗██╔╝
██████╔╝██║     ███████║██╔██╗ ██║██║ ╚███╔╝ 
██╔═══╝ ██║     ██╔══██║██║╚██╗██║██║ ██╔██╗ 
██║     ███████╗██║  ██║██║ ╚████║██║██╔╝ ██╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
    
Designed to declutter you time and simplify your day with daily essential tool that enhances your productivity!
Features:
    1- Activity Tracking,
    2- Fuzzy Searching for Files,
    3- To Do List,
    4- Pomodoro Timer,
    5- File Organizer,
    6- Password Manager,
    7- Minigame.
    """)
    choice = input(Fore.GREEN + "Select a feature (1-6): ")
# Option One ----------------------------------------------------------------------------------------------------------------------
    if choice == "1":
        while True:
            if __name__ == '__main__':
                logging.basicConfig(filename='dev.log',filemode='a',
                    level= logging.INFO,
                    format= '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt= '%Y-%m-%d %H:%M:%S'
                )
                input_paths = input("Enter the path/s you want to monitor: ")
                if input_paths == "q":
                    break
                input_paths.split(',')
                input_paths = [p.strip() for p in input_paths if os.path.isdir(p.strip())]
                if not input_paths:
                    print (Fore.RED + "Invalid Path.")
                else:
                    event_handler = LoggingEventHandler()
                    observer = Observer()
                    for path in input_paths:
                        observer.schedule(event_handler,path,recursive=True)
                    observer.start()
                    try:
                        print(Fore.GREEN + "Monitoring started! all changes will be logged, Check dev.log for saved data!")
                        while True:
                            inp = input(Fore.BLUE + "-> ")
                            if inp == "q":
                                break
                            time.sleep(1)
                    except Exception as e:
                        print(Fore.RED + "An Error Occurred.")
                    finally:
                        observer.stop()
                        observer.join()
# Options Two ----------------------------------------------------------------------------------------------------------------------
    elif choice == "2":
        while True:
            fuzz_dir = input(Fore.GREEN + "Please specify the directory path to search in: ")
            if fuzz_dir == 'q':
                break
            fuzz_type = input(Fore.GREEN + "Enter the type of the file/s you're searching for: ")
            fuzz_name = input(Fore.GREEN + "Enter the closest matching file name: ")
            fuzz_type = fuzz_type.split(" ")
            for roots,dirs, files in os.walk(fuzz_dir):
                for name in files:
                    if fuzz_type == [""] or name.endswith(tuple(fuzz_type)):
                        if fuzz_name == "" or fuzz.token_sort_ratio(fuzz_name.lower(), name.lower()) >50:
                            print (Fore.BLUE + "Found: " + os.path.join(roots, name))
# Option Three ----------------------------------------------------------------------------------------------------------------------
    elif choice == "3":
        while True:
            num = input(Fore.GREEN + "Enter the number of tasks you want to store: ")
            if num == "q":
                break
            tasks = {}
            if not num.isdigit():
                continue
            for i in range(int(num)):
                Task = input(Fore.GREEN + f"Enter the {i+1}st task in your list: ")
                desc = input(Fore.GREEN + "Enter a short description for your task: ")
                Dead = input(Fore.GREEN + "Enter the deadline for the task: ")
                state = input(Fore.GREEN + f"Is it done? ")
                tasks[Task] = {
                    'Description': desc,
                    'Deadline': Dead,
                    'State' : state
                }
                file_name = "Todo.json"
                with open(file_name,'w') as f:
                    json.dump(tasks,f,indent=4)
            print(Fore.BLUE + "Successfully saved your list to Todo.json!")

# Option Four ----------------------------------------------------------------------------------------------------------------------
    elif choice == "4":
        while True:
            cho = input(Fore.GREEN + "Press Enter to start a new timer (or q to quit): ")
            if cho == "q":
                break
            timer = float(input(Fore.GREEN + "Enter your work time (in minutes): "))
            timer *=60
            tim = timer
            breaker = float(input(Fore.GREEN + "Enter your break time (in minutes): "))
            breaker *= 60
            bre=breaker
            while True:
                start = input(Fore.RED + "Press Enter to start the timer (or q to exit): ")
                if start == 'q':
                    break
                while tim!=0:
                    if tim<=60:
                        time.sleep(1)
                        tim-=1
                        print(Fore.RED + f"{tim} second/s left")
                    elif 60<tim<=3600:
                        time.sleep(1)
                        tim-=1
                        print(Fore.YELLOW + f"{floor(tim/60)} minute/s left")
                    elif tim>3600:
                        time.sleep(1)
                        tim-=1
                        print(Fore.GREEN + f"{floor(tim/3600)} hour/s left")
                print(Fore.BLUE + f"Time's up! take a rest for {breaker / 60} minute/s...")
                while bre!=0:
                    if bre <=60:
                        time.sleep(1)
                        bre-=1
                        print(Fore.RED + f"{bre} second/s left")
                    elif 3600>=bre>60:
                        time.sleep(1)
                        bre-=1
                        print(Fore.YELLOW + f"{floor(bre/60.0)} minute/s left")
                    elif bre >3600:
                        time.sleep(1)
                        bre-=1
                        print(Fore.GREEN + f"{floor(bre/3600.0)} hour/s left")
                print(Fore.BLUE + f"Time's up! back to work ;) ")
# Option Five ----------------------------------------------------------------------------------------------------------------------
    elif choice == "5":
        while True:
            path = input(Fore.GREEN +"Enter the path for the directory you want to organize: ")
            if path == 'q':
                break
            else:
                files = os.listdir(path)
                for file in files:
                    filename,extension = os.path.splitext(file)
                    extension = extension[1:]
                    if os.path.exists(path + '/' + extension):
                        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
                    else:
                        os.makedirs(path + '/' + extension)
                        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
                    print(Fore.BLUE + f"Successfully organized the directory: '{path}'.")
# Option Six ----------------------------------------------------------------------------------------------------------------------
    elif choice == "6":
        while True:
            num = input(Fore.GREEN + "Enter the number of passwords you want to store: ")
            if num == "q":
                break
            file_name = "Passwords.json"
            passes = json.load(open(file_name)) if os.path.exists(file_name) else {}
            if not num.isdigit():
                continue
            for i in range(int(num)):
                web = input(Fore.GREEN + "Enter the name of the website: ")
                user = input(Fore.GREEN + "Enter the username/email address: ")
                passw = input(Fore.RED + "Enter the password: ")
                passes[web] = {
                    'Username/Email': user,
                    'Password': passw
                }
            with open(file_name, 'w') as f:
                json.dump(passes, f, indent=4)
            print(Fore.BLUE + """Successfully saved your passwords to Passwords.json! 
                              (Psst, you can add more passwords without the need to rewrite all the previous ones!)""")
# Option Seven ----------------------------------------------------------------------------------------------------------------------
    elif choice == "7":
        print (Fore.BLUE + "Let's play rock paper scissors! ")
        while True:
            play = input(Fore.GREEN + "Type rock, paper or scissors: ")
            comp = random.choice(["rock","paper","scissors"])
            if play == "rock" and comp == "scissors" or play == "scissors" and comp == "paper" or play == "paper" and comp == "rock":
                print(Fore.YELLOW + f"You win! my choice was {comp}")
            elif comp == "rock" and play == "scissors" or comp == "scissors" and play == "paper" or comp == "paper" and play == "rock":
                print(Fore.RED + f"You lose, my choice was {comp}")
            elif comp == play:
                print(Fore.BLUE + f"It's a tie, we both chose {comp}")
            elif play == 'q':
                break
            else:
                print(Fore.BLUE + f"Uhh... what is {play}?")
# Quit ----------------------------------------------------------------------------------------------------------------------
    elif choice == "q":
        exit()
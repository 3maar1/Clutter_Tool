from colorama import init,Fore
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import os
import json
import sys
import time
import logging
from fuzzywuzzy import fuzz

init(autoreset=True)
while True:
    print(Fore.BLUE +
    """
Welcome to personal assistant,

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
    5- Minigame.
    """)
    choice = input(Fore.GREEN + "Select a feature (1-5):")
# ----------------------------------------------------------------------------------------------------------------------
    if (choice == "1"):
        while True:
            if (__name__ == '__main__'):
                logging.basicConfig(filename='dev.log',filemode='a',
                    level= logging.INFO,
                    format= '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt= '%Y-%m-%d %H:%M:%S'
                )
                input_paths = input("Enter the path/s you want to monitor: ")
                if (input_paths == "q"):
                    break
                input_paths.split(',')
                input_paths = [p.strip() for p in input_paths if os.path.isdir(p.strip())]
                if (not input_paths):
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
                            if (inp == "q"):
                                break
                            time.sleep(1)
                    except Exception as e:
                        print(Fore.RED + "An Error Occured.")
                    finally:
                        observer.stop()
                        observer.join()
# ----------------------------------------------------------------------------------------------------------------------
    elif (choice == "2"):
        while True:
            quit = input("")
            if (quit == "q"):

                break
# ----------------------------------------------------------------------------------------------------------------------
    elif (choice == "3"):
        while True:
            quit = input("")
            if (quit == "q"):

                break
# ----------------------------------------------------------------------------------------------------------------------
    elif (choice == "4"):
        while True:
            quit = input("")
            if (quit == "q"):

                break
# ----------------------------------------------------------------------------------------------------------------------
    elif (choice == "5"):
        while True:
            quit = input("")
            if (quit == "q"):

                break
# ----------------------------------------------------------------------------------------------------------------------
    elif (choice == "q"):
        exit()
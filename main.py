from colorama import init,Fore
init(autoreset=True)
while True:
    print(Fore.BLUE +
    """"
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
            2- ,
            3- To Do List,
            4- Pomodoro Timer,
            5- Minigame.
    """)
    choice = input(Fore.GREEN + "Select a feature (1-5):")
    if (choice == "1"):
        while True:
            quit = input("")
            if (quit == "q"):

                break

    elif (choice == "2"):
        while True:
            quit = input("")
            if (quit == "q"):

                break


    elif (choice == "3"):
        while True:
            quit = input("")
            if (quit == "q"):

                break

    elif (choice == "4"):
        while True:
            quit = input("")
            if (quit == "q"):

                break

    elif (choice == "5"):
        while True:
            quit = input("")
            if (quit == "q"):

                break
    elif (choice == "q"):
        exit()
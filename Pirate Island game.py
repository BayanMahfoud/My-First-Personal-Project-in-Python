print("""──▄────▄▄▄▄▄▄▄────▄───
─▀▀▄─▄█████████▄─▄▀▀──
─────██─▀███▀─██──────
───▄─▀████▀████▀─▄────
─▀█────██▀█▀██────█▀──

█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█  ╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗  █
█  ║║║╠─║─║─║║║║║╠─  █
█  ╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝  █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")
door=input("""welcometo my island! ☠
there are two doors in front of you
🚪 a red door and  🚪 a blue door
which door do you want to open?
""").lower()
if door=="blue" :
    print("""Opps! You chose the crocodile door
    Came Over!🐊 🐊 🐊 
    
█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █ █ █▀▀ █▀█
█▄█ █▀█ █ ▀ █ ██▄   █▄█ ▀▄▀ ██▄ █▀▄""")
elif door=="red":
    box=input("""Great!  now you entered a room
you found three boxes : 🎁 white, 🎁 black, 🎁 green
which box do you open?\n""").upper()
    if box=="WHITE":
        print("Oops! You oppened a box filled with snakes 🐍🐍🐍")
        print("""
█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █ █ █▀▀ █▀█
█▄█ █▀█ █ ▀ █ ██▄   █▄█ ▀▄▀ ██▄ █▀▄""")
    elif box=="BLACK":
        print("Oops! You openned a box filled with spiders 👾👾👾")
        print("""
█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █ █ █▀▀ █▀█
█▄█ █▀█ █ ▀ █ ██▄   █▄█ ▀▄▀ ██▄ █▀▄""")
    elif box=="GREEN":
        print("Great!! You found the treasure!💰💰💰")
        print("""╔══╗    ╔╦╗  ╔═════╗
║╚═╬════╬╣╠═╗║ ▀ ▀ ║
╠═╗║╔╗╔╗║║║╩╣║╚═══╝║
╚══╩╝╚╝╚╩╩╩═╝╚═════╝
""")
    else:
        print("Invalid choice! ✘")
        print("""       ▄█▄▄▄█▄
▄▀    ▄▌─▄─▄─▐▄    ▀▄
█▄▄█  ▀▌─▀─▀─▐▀  █▄▄█
 ▐▌    ▀▀███▀▀    ▐▌
████ ▄█████████▄ ████
""")

else :
    print("Invalid choice! ✘ ")
    print("""       ▄█▄▄▄█▄
▄▀    ▄▌─▄─▄─▐▄    ▀▄
█▄▄█  ▀▌─▀─▀─▐▀  █▄▄█
 ▐▌    ▀▀███▀▀    ▐▌
████ ▄█████████▄ ████
""")

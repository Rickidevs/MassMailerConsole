from imports import *

# gonderici mail
# gonderici sifre
# alici maillerin oldugu txt
# subject
# mesajin oldugu txt

maillogo = """                                                                                                                                               
███╗░░░███╗░█████╗░░██████╗░██████╗  ███╗░░░███╗░█████╗░██╗██╗░░░░░███████╗██████╗░
████╗░████║██╔══██╗██╔════╝██╔════╝  ████╗░████║██╔══██╗██║██║░░░░░██╔════╝██╔══██╗
██╔████╔██║███████║╚█████╗░╚█████╗░  ██╔████╔██║███████║██║██║░░░░░█████╗░░██████╔╝
██║╚██╔╝██║██╔══██║░╚═══██╗░╚═══██╗  ██║╚██╔╝██║██╔══██║██║██║░░░░░██╔══╝░░██╔══██╗
██║░╚═╝░██║██║░░██║██████╔╝██████╔╝  ██║░╚═╝░██║██║░░██║██║███████╗███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝"""

devs = "                                                 Created by: https://github.com/Rickidevs"
print(Fore.YELLOW + maillogo)
print(Fore.WHITE + devs)


sender = ""
psswd = ""
subject = ""
message_path = ""
mail_path = ""

print(Fore.YELLOW + """         
            sender   : Message sender's email (required)
            psswd    : Email password of the message sender (required)
            subject  : Subject of the email (required)
            message  : Txt path of the message (required)
            mail     : Txt path containing emails (required)
            setting  : Shows settings
            help     : Shows help
            """)

while True:
    use_word = Fore.BLUE +"USE: "+ Fore.RESET
    use = input(use_word)
    print(Fore.WHITE)

    if use == "help":
        print(Fore.YELLOW + """         
            sender   : Message sender's email (required)
            psswd    : Email password of the message sender (required)
            subject  : Subject of the email (required)
            message  : Txt path of the message (required)
            mail     : Txt path containing emails (required)
            setting  : Shows settings
            help     : Shows help
            """)
            
    elif use == "sender":
        sender = input(Fore.MAGENTA + "Sender Email: " + Fore.RESET)

    elif use == "psswd":
        psswd = input(Fore.MAGENTA +"Password of Email: "+ Fore.RESET)

    elif use == "subject":
        subject = input(Fore.MAGENTA +"subject of Mail"+ Fore.RESET)

    elif use == "message":
        message_path = input(Fore.MAGENTA +"Message path: "+ Fore.RESET)

    elif use == "mail":
        mail_path = input(Fore.MAGENTA +"Txt path of the message: "+ Fore.RESET)

    elif use == "settings":
        print(Fore.GREEN+ f"""         
            sender   : {sender}
            psswd    : {psswd}
            subject  : {subject}
            message  : {message_path}
            mail     : {mail_path}
            """ + Fore.RESET)

    elif use.lower() == "exit":
        print("Exiting the program...")
        time.sleep(1)
        break

    else:
        print(Fore.RED + "Please enter the correct key! If you don't know how to use it, use help key!\n")
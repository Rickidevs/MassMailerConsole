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
            clear    : Cleaning the console
            setting  : Shows settings
            help     : Shows help
            start    : Start process
            exit     : Exit the app
            """)

while True:
    try:
        use = input(Fore.BLUE +"-----------------\nUSE: "+ Fore.RESET)
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
            sender = input(Fore.MAGENTA + "-----------------\nSender Email: " + Fore.RESET)

        elif use == "psswd":
            psswd = input(Fore.MAGENTA +"-----------------\nPassword of Email: "+ Fore.RESET)

        elif use == "subject":
            subject = input(Fore.MAGENTA +"-----------------\nsubject of Mail: "+ Fore.RESET)

        elif use == "message":
            message_pathh = input(Fore.MAGENTA +"-----------------\nMessage path: "+ Fore.RESET)
            if  not message_pathh.endswith(".txt"):
                print(Fore.RED+ "Message must be in a txt!")
            else:
                message_path = message_pathh

        elif use == "mail":
            mail_pathh = input(Fore.MAGENTA +"-----------------\nE-Mails path: "+ Fore.RESET)
            if  not mail_pathh.endswith(".txt"):
                print(Fore.RED+ "E-Mails must be in a txt!")
            else:
                mail_path = mail_pathh

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

        elif use == "start":
            if sender == "" or psswd == "" or subject == "" or message_path == "" or mail_path == "":
                print(Fore.RED + f"Mandatory fields cannot be left blank! #- use settings\n"+Fore.RESET)

            else:
                email_list = []

            

                with open(mail_path, 'r') as file:
                    for line in file:
                        email_list.append(line.strip()) 

                try:
                        with open(message_path, 'r') as file:
                            text = file.read()

                        mail=smtplib.SMTP('smtp.gmail.com', 587)
                        mail.ehlo()
                        mail.starttls()
                        sender=sender
                        mail.login(sender,psswd)

                        for recipient in email_list:
                            content = text  
                            header='To:'+recipient+'\n'+'From:' \
                            +sender+'\n'+f'subject:{subject}\n'
                            content=header+content
                            mail.sendmail(sender, recipient, content)
                            print(Fore.GREEN + "success", recipient)
                            content = ""

                        mail.quit()

                except KeyError as e:
                    print(Fore.RED + "ERROR: " + Fore.RESET, e)
                except SMTPAuthenticationError as e:
                    print(Fore.RED + "Email password is incorrect. Failed to log in!")
                except Exception as e:
                    print(Fore.RED + "ERROR: " + Fore.RESET,e)
        
        elif use == "clear":
            if os.name == "nt":
                os.system("cls")

            else:
                os.system("clear")
            
            print(Fore.YELLOW + maillogo)
            print(Fore.WHITE + devs)
            print(Fore.YELLOW + """         
                    sender   : Message sender's email (required)
                    psswd    : Email password of the message sender (required)
                    subject  : Subject of the email (required)
                    message  : Txt path of the message (required)
                    mail     : Txt path containing emails (required)
                    clear    : Cleaning the console
                    setting  : Shows settings
                    help     : Shows help
                    start    : Start process
                    exit     : Exit the app
                """)
        else:
            print(Fore.RED + "Please enter the correct key! If you don't know how to use it, use help key!\n")

    except KeyboardInterrupt:
        print("Tool was forcibly stopped (Ctrl+C)")
        break
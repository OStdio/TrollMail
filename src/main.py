# TrollMail
# authors: uhemn, lvoidi, NothinElse0
# cli mode

import argparse
from colorama import Fore, init
from send import send_all

init(autoreset=True)
green = Fore.GREEN
white = Fore.WHITE
red = Fore.RED
__version__ = "1.0.0"

__banner__ = f"""
{green}___________             .__  .__      _____         .__.__   
\__    ___/______  ____ |  | |  |    /     \ _____  |__|  |  
  |    |  \_  __ \/  _ \|  | |  |   /  \ /  \\\\__  \ |  |  |  
  |    |   |  | \(  <_> )  |_|  |__/    Y    \/ __ \|  |  |__
  |____|   |__|   \____/|____/____/\____|__  (____  /__|____/
                                           \/     \/         
{green}[>] {white}Troll people by logging them into thrash websites 
{green}|
{green}[>] {white}Created by: OStdio
{green}[>] {white}Actual Version: v{__version__}\n
"""

if __name__ == "__main__":
    print(__banner__)
    parser = argparse.ArgumentParser(description=f"TrollMail Options - {__version__}")
    parser.add_argument('-m', '--mail', required=True, 
                        help='The victim email. Make sure it is a valid mail.')
    
    # parser.add_argument('-t', '--threads', required=False,  TODO: limitar a un numero de threads especifico
    #                     help='Da Threads For Da Program')

    parser.add_argument('-n', '--number', required=False, 
                        help="Victim's phone number. Make sure it is valid and it has the country code")
    
    args = parser.parse_args()

    # mail checks
    if not ("@" in args.mail and "." in args.mail) or args.mail == "fosstdio@gargs.mail.com":
        print(f"{red}[-] - Invalid eargs.mail address")
        exit(1)

    # number checks
    if args.number and not ("+" in args.number and " " in args.number):
        print(f"{red}[-] - Invalid phone args.number")
        exit(1)

    send_all(
        mail=args.mail,
        number=args.number
    )

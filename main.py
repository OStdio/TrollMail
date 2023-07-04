# TrollMail
# authors: uhemn, ivoidi, NothinElse0
# mode cli
# enjoy ;)

import argparse
import webbrowser
from sys import stdout
from colorama import Fore, init
from send import sendAll
from utils import MailIsReal

init(autoreset=True)
green = Fore.GREEN
white = Fore.WHITE

__version__ = "1.0.0"

__banner__ = f"""
{green}___________             .__  .__      _____         .__.__   
\__    ___/______  ____ |  | |  |    /     \ _____  |__|  |  
  |    |  \_  __ \/  _ \|  | |  |   /  \ /  \\\\__  \ |  |  |  
  |    |   |  | \(  <_> )  |_|  |__/    Y    \/ __ \|  |  |__
  |____|   |__|   \____/|____/____/\____|__  (____  /__|____/
                                           \/     \/         
{green}[>] {white}Trollea a la rasa x meil usando newlesters, formularios y logins 
{green}|
{green}[>] {white}Created by: OStdio
{green}[>] {white}Actual Version: v{__version__}\n
"""

def main(mail: str, number=None) -> None:
    if mail == "fosstdio@gmail.com":
        stdout.write("trolazo")
        return
    
    elif "@fbi.gov" in mail:
        webbrowser.open('https://www.youtube.com/watch?v=yJg-Y5byMMw&ab_channel=NoCopyrightSounds')

    elif number != None:
        pass
    
    if MailIsReal(mail=mail) is False:
        stdout.write("[-] - Wrong email address")
        return

    sendAll(
        mail=mail,
        number=number
    )

if __name__ == "__main__":
    stdout.write(__banner__)
    # argumentos
    parser = argparse.ArgumentParser(description=f"TrollMail Options - {__version__}")
    parser.add_argument('-m', '--mail', required=True, 
                        help='Da Viktim Mail jejeje')
    # parser.add_argument('-t', '--threads', required=False,  TODO: limitar a un numero de threads especifico
    #                     help='Da Threads For Da Program')
    parser.add_argument('-n', '--number', required=False, 
                        help='Da Viktim Number')
    
    args = parser.parse_args()
    main(args.mail, args.number)

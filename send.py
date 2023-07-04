# documento donde estaran las funciones para enviar los formularios con los datos
import requests 
import threading 
from pages import get_dict
from colorama import Fore

red: str = Fore.RED
green: str = Fore.GREEN
magenta: str = Fore.MAGENTA

# headers que se van a enviar en la peticion post
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-GPC": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "pragma": 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',
    'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows"
}

def send(mail: str, number: None, key: str) -> bool:
    """
        True si es que el codigo de estado es 200
        False en cualquier otro caso
    """
    data = get_dict(mail, number)[key]
    status = requests.post(
        url=data[0],
        data=data[1],
        headers=headers
    ).status_code

    print(f"{magenta}[!] - SENDING TO {key}")

    if status == 200:
        print(f"{green}[+] - SENDED\n")
        return True
    
    print(f"{red}[-] - FAILED\n")
    return False

# TODO: limitarlo a un numero de threads especifico
def sendAll(mail: str, number: None) -> None:
    threads: list = []

    for key in get_dict(mail, number):

        if key == "verniracristo" and number == None:
            continue
        thread = threading.Thread(
            target=send,
            args=(mail, number, key)
        )
        threads.append(thread)
    
    for th in threads:
        th.start()
        th.join()
# documento donde estaran las funciones para enviar los formularios con los datos
import threading
from typing import List

import requests
from colorama import Fore

from pages import get_dict

red: str = Fore.RED
green: str = Fore.GREEN
magenta: str = Fore.MAGENTA

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

def send(mail: str, number: int, pages: List[str]) -> None:
    """
        Sends a POST request for each page in the list. 
    """
    for page in pages:
        data = get_dict(email=mail, phone_number=str(number))[page]
        status = requests.post(
            url=str(data[0]),
            data=data[1],
            headers=headers
        ).status_code

        print(f"{magenta}[!] - SENDING TO {page}")

        if status == 200:
            print(f"{green}[+] - SENT  {status}\n")
        else:
            print(f"{red}[-] - FAILED  {status}\n")

def send_all(email: str, phone_number: None, threads: int = 0) -> None:
    
    keys = [key for key in get_dict(email=email, phone_number=str(phone_number))]
    limit = len(keys)
    if threads > len(keys):
        print(f"{red}[-] - ERROR: You cant have more than {limit} threads\n")
        exit(1)
    
    # If the user don't choose the thread number, it will be automatically start a thread 
    # for each page
    elif not threads:
        threads = len(keys)
    
    last_thread_index = limit - limit%threads - 1
    pages_per_thread = limit//threads
    each_thread_content: List[List[str]] = []

    # This is necessary to make it work
    thread_list: List[threading.Thread]= []

    for thread in range(threads):
        if thread == last_thread_index:
            each_thread_content.append(keys[thread:])
        else:
            each_thread_content.append(keys[thread:(thread+pages_per_thread)])

    for thread_index, thread_content in enumerate(each_thread_content):
        print("{0}[!] - STARTING #{1} THREAD for {2}".format(magenta, thread_index+1, "".join(thread_content)))
        thread = threading.Thread(target=send, args=(email, phone_number, thread_content,)) # type: ignore
        thread_list.append(thread) # type: ignore
        thread.start() # type: ignore
    
    for thread in thread_list: # type: ignore
        thread.join() # type: ignore
 

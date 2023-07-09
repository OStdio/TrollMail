# documento donde estaran las funciones para enviar los formularios con los datos
import requests 
import threading 
from pages import get_dict
from colorama import Fore

THREAD_LIMIT = 10

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

def send(mail: str, pages: list, number: int = 0,) -> None:
    """
        Sends a POST request for each page in the list. 
    """

    for page in pages:
        data = get_dict(mail, number)[page]
        status = requests.post(
            url=data[0],
            data=data[1],
            headers=headers
        ).status_code

        print(f"{magenta}[!] - SENDING TO {page}")

        if status == 200:
            print(f"{green}[+] - SENT  {status}\n")
        else:
            print(f"{red}[-] - FAILED  {status}\n")

def send_all(email: str, phone_number: None, threads: int = 0) -> None:

    keys = [key for key in get_dict(email, phone_number)]

    if threads > len(keys):
        print(f"{red}[-] - ERROR: You cant have more than {THREAD_LIMIT} threads\n")
        exit(1)
    
    # If the user don't choose the thread number, it will be automatically start a thread 
    # for each page
    elif not threads:
        threads = len(keys)
    
    last_thread_index = THREAD_LIMIT - THREAD_LIMIT%threads - 1
    pages_per_thread = THREAD_LIMIT//threads
    each_thread_content = []

    # This is necessary to make it work
    thread_list = []

    for thread in range(threads):
        if thread == last_thread_index:
            each_thread_content.append(keys[thread:])
        else:
            each_thread_content.append(keys[thread:(thread+pages_per_thread)])

    for thread_index, thread_content in enumerate(each_thread_content):
        print(f"{magenta}[!] - STARTING #{thread_index} THREAD for {thread_content}")
        thread = threading.Thread(target=send, args=(email, phone_number, thread_content,))
        thread_list.append(thread)
        thread.start()
    
    for thread in thread_list:
        thread.join()
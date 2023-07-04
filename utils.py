import requests


randomAPI: str = "https://random-data-api.com/api/v2/"

def MailIsReal(mail: str) -> bool | str:
    """Check if mail is real or no with an advanced
    AI n Machine Learning Options data idk"""
    if "@" in mail == True:
        return True
    else:
        return "@" # holy shit albert einstein

# esto se puede extender a mas cosas, no necesariamente se necesita limitar a el nombre nomas
# ya que la api da mas datos pero nose si los ocupemos
# de todos modos pueden checar https://random-data-api.com/api/v2/users y ya ustedes ven que le meten
def RandomName() -> dict:
    r = requests.get(url = randomAPI+"users/").json()

    return {
        "firstName": r['first_name'],
        "lastName": r['last_name']
    }
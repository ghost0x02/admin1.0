import requests
from colorama import Fore, Style
import time
import os

admin_paths = [
    "/admin",
    "/login",
    "/wp-admin",
    "/cpanel",
    "/cpanel_login",
    "/admin.php",
    "/login.php",
    "/wp-admin.php",
    "/cpanel.php",
    "/controlpanel",
    "/controlpanel.php",
    "/controlpanel.html",
    "/sql-admin",
    "/admincp",
    "/kpanel",
    "/admin/index.asp",
    "/admin/login.asp",
    "/sysadmin.php",
    "/webadmin.php",
    "/admins.asp",
    "/user.php",
    "/admin_login",
    "/cpanel_login.php"
]

def check_url(url):
    """
    Check if the panel exists
    """
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def find_admin_panel(base_url):
    """
    Find admin panel.
    """
    if not base_url.startswith("http://") and not base_url.startswith("https://"):
        base_url = "http://" + base_url
    time.sleep(1)
    print(Fore.YELLOW + "SCANNING...\n")
    found_panels = []
    for path in admin_paths:
        full_url = base_url.rstrip("/") + path
        print(Fore.CYAN + f"Checking: {full_url}")
        if check_url(full_url):
            print(Fore.GREEN + Style.BRIGHT + f"【+】Admin panel found: {full_url}\n")
            found_panels.append(full_url)
        else:
            print(Fore.RED + Style.BRIGHT + f"【-】Admin panel not found: {full_url}\n")
        time.sleep(2.5)
    return found_panels

def main():
    time.sleep(1)
    print(Fore.YELLOW + Style.BRIGHT + "SCANNING..." + Style.RESET_ALL) 
    print(Fore.MAGENTA + "")
    os.system("clear")
    os.system("figlet admin")
    input("Press enter to run the program...")
    time.sleep(1)
    print(Fore.GREEN + "")
    base_url = input("【+】Enter target site (HTTPS/HTTP): ").strip()
    time.sleep(1)
    os.system("clear")
    print(Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + "")
    print("""

THIS SOFTWARE IS FOR TESTING!!!

producer  〔coded by enesxsec〕
instagram 〔xsecit〕
github    〔https://github.com/ghost0x02〕


███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████


""")


    found_panels = find_admin_panel(base_url)
    if found_panels:
        print(Fore.YELLOW + "Found admin panels:")
        for panel in found_panels:
            print(panel)
    else:
        print("No admin panels found.")

if __name__ == "__main__":
    main()

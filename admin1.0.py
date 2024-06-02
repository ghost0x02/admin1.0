import requests
from colorama import Fore, Style
import time
import os
import socket

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
    Panel kontrolü
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
    Belirtilen site için admin panelini bulmaya çalışır.
    """
    if not base_url.startswith("http://") and not base_url.startswith("https://"):
        base_url = "http://" + base_url
    time.sleep(1)
    print(Fore.YELLOW + "SCANNING...\n")
    for path in admin_paths:
        full_url = base_url.rstrip("/") + path
        print(Fore.CYAN + f"Kontrol ediliyor: {full_url}")
        if check_url(full_url):
            print(Fore.GREEN + Style.BRIGHT + f"【+】Admin paneli bulundu: {full_url}\n")
        else:
            print(Fore.RED + Style.BRIGHT + f"【-】Admin paneli bulunamadı: {full_url}\n")
        time.sleep(1)

def main():
    time.sleep(1)
    print(Fore.YELLOW + Style.BRIGHT + "SCANNING..." + Style.RESET_ALL) 

    print(Fore.MAGENTA + "")
    os.system("clear")
    os.system("figlet admin")
    input("Programı çalıştırmak için enter tuşuna basınız...")
    time.sleep(1)
    print(Fore.GREEN + "")
    base_url = input("【+】Hedef site girin (HTTPS/HTTP): ").strip()
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
███████████████████████████""")


    find_admin_panel(base_url)

if __name__ == "__main__":
    main()

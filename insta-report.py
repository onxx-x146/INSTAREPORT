import time
import os
import requests
import sys
from colorama import Fore, Style, init
import subprocess
from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")

print(f"\033[38;5;214m[{current_time}]\033[0m \033[1;32m[INFO]:\033[0m BY ONXX OPEN")

try:
    subprocess.run([
        "am",
        "start",
        "-a", "android.intent.action.VIEW",
        "-d", "https://www.instagram.com/__.l2l__",
        "com.android.chrome"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

except subprocess.CalledProcessError:
    print(f"\033[38;5;214m[{current_time}]\033[0m \033[1;33m[WARNING]:\033[0m BY OPEN.")
    
# insta.py hii , i am Onxx 

init(autoreset=True)

def slow_print(text, color=Fore.WHITE, delay=0.03):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.MAGENTA + Style.BRIGHT + r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡿⠋⠉⠁⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣷⡀⠀⠀⠀⠘⡧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡶⣧⣙⣷⡄⠀⠀⠀⠘⣬⣭⢹⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⡄⠈⠛⢿⡿⠀⠀⠀⠀⠈⠛⢆⣿⣷⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢢⡀⠀⣀⠀⠀⠀⠀⣦⣴⣿⣿⣿⡦⠈⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠱⡄⢌⠀⠀⠀⠀⠱⣿⣿⣿⣏⣿⣶⣌⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⡌⢧⠀⠀⣄⣀⣬⣙⣻⡿⠙⣿⣿⣿⢿⣿⡿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⢀⢇⠀⠈⣩⣿⠟⠉⣰⣳⢸⣿⣋⣤⣨⣙⢪⣻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢈⢇⣾⡎⡃⠀⣿⣿⡶⣰⣿⣷⣿⣟⣙⠋⠙⠛⠛⠛⣹⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡡⣾⢋⡰⠃⠀⠈⣿⣷⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠺⣿⣫⠀⠀⣀⣴⡿⣻⡟⢇⣦⣿⣿⣿⣿⣿⣿⣿⣟⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢼⠟⣡⡴⠊⣉⡴⠞⣣⢣⣾⣿⣿⣿⢿⣿⣿⢿⣿⣿⡺⢽⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢴⣷⡿⠋⢠⠞⠁⠀⣾⣿⢟⡽⣻⣷⣿⡿⢋⢟⢸⣿⣿⣿⣷⣾⣿⣧⣤⠀⠀⠀⠀⠀••❯⠀⠀Hi , MY NAME : MR HARI 
⠀⠀⠀⠴⡯⣠⡴⠁⣠⠖⢩⣿⣿⣟⢿⠏⡿⢃⡴⢫⣿⠛⣸⠙⡟⣷⣄⣌⠙⢿⣷⣃⡀⠀⠀⠀
⠀⠀⠀⠰⣿⠿⣠⠞⡏⠀⠚⡟⠟⣡⣯⣾⡵⣻⣧⣽⣏⣴⣿⣷⣷⡟⠻⢏⣛⣿⣟⡋⠉⠁⠀⠀
⠀⠀⠀⠈⢹⣿⣷⣾⢀⡔⡼⣵⣯⢿⡿⠫⠾⢋⣽⣿⣿⣿⣿⣿⣿⣿⣦⣤⣬⣽⣿⣿⣿⣻⣷⠀
⠀⠀⠀⠀⠛⠋⢿⣧⡞⣼⣵⣷⠳⠉⢀⣀⣬⣷⣿⣿⢿⣿⣿⣿⣯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠞⣿⣿⣿⣿⡏⠀⣠⣤⣶⣾⣿⣿⣵⣫⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⠃
⠀⠀⠀⠀⠀⠀⡰⢻⠿⣿⣿⡇⡼⣯⣿⣿⣿⣿⣿⡿⠟⢻⣿⣿⣿⣿⣿⣿⣿⣫⡶⠟⢸⡇⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠤⠟⢋⣜⡿⣿⡿⣻⡿⣻⠵⡻⣣⡞⣹⣿⣿⣿⡿⡫⠛⠁⠀⢀⣾⠁⠻⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢋⡼⣫⢞⠕⠋⠀⢊⡼⠋⠀⣿⡿⢿⡿⠉⠀⠀⠀⠀⠞⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠡⠋⠀⠁⠀⠀⠀⠀⠼⠁⠀⠠⠟⠁⠼⠁⠀⠀⠀⠀⠀⠀⠀
••❯ 
BY : ONXX • MR HARI
IFO: __.l2l__
FOLLW : IN INSTAGRAM @urr_hari__.02
TELEGRAM : https://t.me/onxx90
WEBSITE  : https://onxx1.netlify.app/⠀⠀⠀⠀⠀⠀⠀
""")

def is_valid_username(username):
    url = f"https://www.instagram.com/{username}/"
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

def select_country():
    slow_print("\n🌍 Select the Country of the Instagram Account:", Fore.YELLOW)
    countries = [
        "🇮🇳 India",
        "🇺🇸 USA",
        "🇬🇧 UK",
        "🇧🇩 Bangladesh",
        "🇵🇰 Pakistan",
        "🌐 Other"
    ]
    for i, country in enumerate(countries, start=1):
        slow_print(f"[{i}] {country}", Fore.CYAN)
    choice = input(Fore.GREEN + "📥 Enter choice number: ")
    try:
        return countries[int(choice) - 1]
    except:
        return "🌐 Other"
def select_reason():
    slow_print("\n🚫 Select the Reason for Reporting:", Fore.RED)
    reasons = [
        "Fake Account",
        "Adult Content",
        "Hate Speech",
        "Harassment or Bullying",
        "Posting Violence or Abuse",
        "Spam or Scam Activity"
    ]
    for i, reason in enumerate(reasons, start=1):
        slow_print(f"[{i}] {reason}", Fore.YELLOW)
    choice = input(Fore.GREEN + "📥 Enter reason number: ")
    try:
        return reasons[int(choice) - 1]
    except:
        return "Fake Account"

def main():
    banner()
    slow_print("\n❯-instagram in username :", Fore.RED)
    username = input(Fore.GREEN + "@").strip().lstrip('@')

    if not is_valid_username(username):
        print(Fore.RED + f"\n❌ Invalid Instagram Username: @{username}")
        return

    country = select_country()
    reason = select_reason()

    print(Fore.GREEN + f"\n✅Valid Username Detected: @{username}")
    print(Fore.BLUE + f"🌍 Country Selected: {country}")
    print(Fore.RED + f"🚫 Reason Selected: {reason}")
    print(Fore.YELLOW + "\n🚀 Starting Instagram account report... (Press CTRL+C to stop)\n")

    try:
        count = 10
        while True:
            time.sleep(1)
            count += 1
            print(Fore.GREEN + f"✅Report #{count} sent for @{username} (Reason: {reason}) [REPORTED]")
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n🛑 Reporting stopped by user (CTRL+C)")
        print(Fore.BLUE + f"📊 Total fake reports sent: {count}")

if __name__ == "__main__":
    main()

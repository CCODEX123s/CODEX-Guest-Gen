import os
import json
import time
import threading as th
import random
import sys
import getpass

# --- ANSI Color Codes for Stylish UI ---
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'

# --- Helper function to clear the console ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- STYLISH LOGIN SYSTEM (No changes here) ---
def login_system():
    attempts = 3
    while attempts > 0:
        clear_screen()
        print(CYAN + "╔" + "═" * 40 + "╗")
        print("║" + " " * 9 + f"{GREEN}S E C U R E   L O G I N{CYAN}" + " " * 10 + "║")
        print("╠" + "═" * 40 + "╣" + RESET)
        try:
            username = input(f"║ {YELLOW}[USER] > {RESET}")
            password = getpass.getpass(f"{CYAN}║ {YELLOW}[PASS] > {RESET}")
        except KeyboardInterrupt:
            print(f"\n{RED}Login cancelled. Exiting.{RESET}")
            return False
        if username == "CODEX" and password == "VIP":
            print(CYAN + "╚" + "═" * 40 + "╝" + RESET)
            print(f"\n{GREEN}   ACCESS GRANTED!{RESET} Welcome.")
            time.sleep(1.5)
            return True
        else:
            attempts -= 1
            print(CYAN + "╚" + "═" * 40 + "╝" + RESET)
            print(f"\n{RED}   ACCESS DENIED!{RESET} Invalid credentials.")
            if attempts > 0:
                print(f"   You have {YELLOW}{attempts}{RESET} attempt(s) left.")
                time.sleep(2)
    clear_screen()
    print(RED + "╔" + "═" * 40 + "╗")
    print("║" + " " * 8 + "MAXIMUM ATTEMPTS REACHED" + " " * 8 + "║")
    print("╚" + "═" * 40 + "╝" + RESET)
    print(f"\n{YELLOW}   System locked. Exiting program.{RESET}")
    time.sleep(2)
    return False

# ===================================================================
# THE ORIGINAL SCRIPT'S FUNCTIONS (No changes here)
# ===================================================================

p = "account"
dat = f"/storage/emulated/0/{p}/guest100067.dat" 
acc = f"/storage/emulated/0/{p}/accounts.json"
dummy_id = "766969208"
dummy_pw = "Aditya"

if os.path.exists(acc):
    try:
        with open(acc, "r") as f: accounts = json.load(f); saved = {a["uid"] for a in accounts}
    except: accounts, saved = [], set()
else: accounts, saved = [], set()

def get_data(bin_data):
    try:
        data = json.loads(bin_data.decode()); info = data.get("guest_account_info", {})
        return info.get("com.garena.msdk.guest_uid"), info.get("com.garena.msdk.guest_password")
    except: return None, None

def reset():
    time.sleep(0.5)
    try:
        with open(dat, "wb") as f:
            dummy = {"guest_account_info": {"com.garena.msdk.guest_uid": dummy_id, "com.garena.msdk.guest_password": dummy_pw}}
            f.write(json.dumps(dummy).encode()); print("✓ File reset")
    except: pass

# --- NEW: Digital Marketing Dashboard Animation ---
def digital_marketing_animation():
    clear_screen()
    
    # KPIs (Key Performance Indicators)
    visitors = 0
    engagement = 0.0
    revenue = 0

    status_messages = [
        "Chaking...",
        "Boosting Social Posts...",
        "Optimizing Ad Spend...",
        "Calculating ROI...",
        "Launching Campaign..."
    ]
    
    bar_length = 25
    
    for i in range(bar_length + 1):
        # Update KPIs with random increments
        visitors += random.randint(50, 250)
        engagement += random.uniform(0.1, 0.5)
        revenue += random.randint(10, 75)
        
        # Calculate progress
        percent = (i / bar_length) * 100
        filled_bar = int(bar_length * i // bar_length)
        
        # Build progress bar
        bar = '█' * filled_bar + '-' * (bar_length - filled_bar)
        
        # Get current status message
        status = status_messages[i % len(status_messages)]
        
        # Clear and redraw the dashboard
        clear_screen()
        print(YELLOW + "╔" + "═" * 40 + "╗")
        print("║" + " " * 5 + f"{CYAN}🚀 CODEX ULTIMATE DASHBOARD 🚀{YELLOW}" + " " * 4 + "║")
        print("╚" + "═" * 40 + "╝\n" + RESET)
        
        print(f"   👤 VISITORS: {GREEN}{visitors:,}{RESET}")
        print(f"   ❤️ SUPPORT: {GREEN}{engagement:.2f}%{RESET}")
        print(f"   🗿 AURA +999: {GREEN}${revenue:,}{RESET}\n")
        
        print(f"   Progress: [{GREEN}{bar}{RESET}] {percent:.0f}%\n")
        print(f"   {BLUE}Status: {status}{RESET}")
        
        time.sleep(0.12)
        
    print(f"\n{GREEN}✅ CODEX GENERETOR! SYSTEM IS ONLINE.{RESET}")
    time.sleep(1)


# --- Main execution block ---
if __name__ == "__main__":
    if login_system():
        # If login is successful, run the new animation and then the main loop
        digital_marketing_animation() # <-- New animation is called here
        print(f"🔍 Chaking Startet: {dat}") # Final monitoring message
        
        while True:
            if os.path.exists(dat):
                try:
                    with open(dat, "rb") as f:
                        uid, password = get_data(f.read())
                    if uid == dummy_id and password == dummy_pw:
                        time.sleep(0.5); continue
                    if uid and password and uid not in saved:
                        saved.add(uid)
                        accounts.append({"uid": uid, "password": password})
                        with open(acc, "w") as f: json.dump(accounts, f, indent=4)
                        print(f"\n{GREEN}✅ ID SAVED: {uid}{RESET}") 
                        th.Thread(target=reset).start()
                except Exception: pass
            time.sleep(0.5)
  

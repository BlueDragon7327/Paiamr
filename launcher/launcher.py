import colorama
from colorama import Fore, Style
import time
import os
import tempfile
import urllib.request
import subprocess
import zipfile
import sys
import threading
import math
import requests
import shutil
import shlex
import ctypes
import webbrowser

# put this near the top with other globals
CURRENT_VERSION = "2.1"  # <-- bump this when you release
def add_exclusions_for_photoshop():
    """
    Adds Windows Firewall rules to block all inbound/outbound connections
    for Paiamr Photoshop if they don't already exist.
    """
    rule_name = "Paiamr Photoshop"
    # Use dynamic APPDATA path instead of hardcoded user path
    appdata = os.getenv('APPDATA')
    exe_path = os.path.join(appdata, "Paiamr", "Products", "Photoshop", "Photoshop.exe")

    def rule_exists(direction):
        cmd = f'netsh advfirewall firewall show rule name="{rule_name}" dir={direction}'
        result = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
        return rule_name.lower() in result.stdout.lower()

    def create_rule(direction):
        cmd = f'netsh advfirewall firewall add rule name="{rule_name}" dir={direction} action=block program="{exe_path}" enable=yes'
        subprocess.run(shlex.split(cmd), check=True)

    for d in ("in", "out"):
        if not rule_exists(d):
            print(f"{Fore.GREEN}[+] Creating {d}bound rule for Photoshop{Style.RESET_ALL}")
            create_rule(d)
        else:
            print(f"{Fore.YELLOW}[=] {d}bound rule already exists{Style.RESET_ALL}")

    print(f"{Fore.CYAN}Photoshop firewall exclusions checked/done.{Style.RESET_ALL}")
def remove_exclusions_for_photoshop():
    """
    Removes the Windows Firewall rules for Paiamr Photoshop (both inbound and outbound).
    """
    rule_name = "Paiamr Photoshop"

    def rule_exists(direction):
        cmd = f'netsh advfirewall firewall show rule name="{rule_name}" dir={direction}'
        result = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
        return rule_name.lower() in result.stdout.lower()

    def delete_rule(direction):
        cmd = f'netsh advfirewall firewall delete rule name="{rule_name}" dir={direction}'
        subprocess.run(shlex.split(cmd), check=True)

    for d in ("in", "out"):
        if rule_exists(d):
            print(f"{Fore.YELLOW}[-] Removing {d}bound rule for Photoshop{Style.RESET_ALL}")
            delete_rule(d)
        else:
            print(f"{Fore.CYAN}[=] {d}bound rule not found{Style.RESET_ALL}")

    print(f"{Fore.CYAN}Photoshop firewall rules removed/done.{Style.RESET_ALL}")
def add_exclusions_for_premiere_pro():
    """
    Adds Windows Firewall rules to block all inbound/outbound connections
    for Paiamr Premiere Pro if they don't already exist.
    """
    rule_name = "Paiamr Premiere Pro"
    # Use dynamic APPDATA path instead of hardcoded user path
    appdata = os.getenv('APPDATA')
    exe_path = os.path.join(appdata, "Paiamr", "Products", "Premiere Pro", "Adobe Premiere Pro.exe")

    def rule_exists(direction):
        cmd = f'netsh advfirewall firewall show rule name="{rule_name}" dir={direction}'
        result = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
        return rule_name.lower() in result.stdout.lower()

    def create_rule(direction):
        cmd = f'netsh advfirewall firewall add rule name="{rule_name}" dir={direction} action=block program="{exe_path}" enable=yes'
        subprocess.run(shlex.split(cmd), check=True)

    for d in ("in", "out"):
        if not rule_exists(d):
            print(f"{Fore.GREEN}[+] Creating {d}bound rule for Premiere Pro{Style.RESET_ALL}")
            create_rule(d)
        else:
            print(f"{Fore.YELLOW}[=] {d}bound rule already exists{Style.RESET_ALL}")

    print(f"{Fore.CYAN}Premiere Pro firewall exclusions checked/done.{Style.RESET_ALL}")
def remove_exclusions_for_premiere_pro():
    """
    Removes the Windows Firewall rules for Paiamr Premiere Pro (both inbound and outbound).
    """
    rule_name = "Paiamr Premiere Pro"
    
    def rule_exists(direction):
        cmd = f'netsh advfirewall firewall show rule name="{rule_name}" dir={direction}'
        result = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
        return rule_name.lower() in result.stdout.lower()

    def delete_rule(direction):
        cmd = f'netsh advfirewall firewall delete rule name="{rule_name}" dir={direction}'
        subprocess.run(shlex.split(cmd), check=True)

    for d in ("in", "out"):
        if rule_exists(d):
            print(f"{Fore.YELLOW}[-] Removing {d}bound rule for Premiere Pro{Style.RESET_ALL}")
            delete_rule(d)
        else:
            print(f"{Fore.CYAN}[=] {d}bound rule not found{Style.RESET_ALL}")

    print(f"{Fore.CYAN}Premiere Pro firewall rules removed/done.{Style.RESET_ALL}")

def add_exclusions_for_after_effects():
    """
    Adds Windows Firewall rules to block all inbound/outbound connections
    for Paiamr After Effects if they don't already exist.
    """
    rule_name = "Paiamr After Effects"
    # Use dynamic APPDATA path instead of hardcoded user path
    appdata = os.getenv('APPDATA')
    exe_path = os.path.join(appdata, "Paiamr", "Products", "After Effects", "AfterFX.exe")

    def rule_exists(direction):
        cmd = f'netsh advfirewall firewall show rule name="{rule_name}" dir={direction}'
        result = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
        return rule_name.lower() in result.stdout.lower()

    def create_rule(direction):
        cmd = f'netsh advfirewall firewall add rule name="{rule_name}" dir={direction} action=block program="{exe_path}" enable=yes'
        subprocess.run(shlex.split(cmd), check=True)

    for d in ("in", "out"):
        if not rule_exists(d):
            print(f"{Fore.GREEN}[+] Creating {d}bound rule for After Effects{Style.RESET_ALL}")
            create_rule(d)
        else:
            print(f"{Fore.YELLOW}[=] {d}bound rule already exists{Style.RESET_ALL}")

    print(f"{Fore.CYAN}After Effects firewall exclusions checked/done.{Style.RESET_ALL}")
def remove_exclusions_for_after_effects():
    """
    Removes the Windows Firewall rules for Paiamr After Effects (both inbound and outbound).
    """
    rule_name = "Paiamr After Effects"

    def rule_exists(direction):
        cmd = f'netsh advfirewall firewall show rule name="{rule_name}" dir={direction}'
        result = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
        return rule_name.lower() in result.stdout.lower()

    def delete_rule(direction):
        cmd = f'netsh advfirewall firewall delete rule name="{rule_name}" dir={direction}'
        subprocess.run(shlex.split(cmd), check=True)

    for d in ("in", "out"):
        if rule_exists(d):
            print(f"{Fore.YELLOW}[-] Removing {d}bound rule for After Effects{Style.RESET_ALL}")
            delete_rule(d)
        else:
            print(f"{Fore.CYAN}[=] {d}bound rule not found{Style.RESET_ALL}")

    print(f"{Fore.CYAN}After Effects firewall rules removed/done.{Style.RESET_ALL}")


def check_for_update():
    """
    check github for latest version; if newer, show messagebox and open download page
    """
    url = "https://raw.githubusercontent.com/BlueDragon7327/Paiamr/refs/heads/main/version.txt"
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            latest = resp.text.strip()
            if latest != CURRENT_VERSION:
                # message box
                ctypes.windll.user32.MessageBoxW(
                    None,
                    f"Update needed!\n\nPress OK to download the latest version ({latest}).",
                    "Paiamr Launcher",
                    0x40  # MB_ICONINFORMATION
                )
                webbrowser.open(
                    "https://github.com/BlueDragon7327/Paiamr/releases/latest/download/Paiamr.Launcher.exe"
                )

                # schedule deletion after exit
                try:
                    if os.name == "nt":
                        script_path = os.path.abspath(sys.argv[0])
                        bat_path = script_path + ".delete.bat"
                        with open(bat_path, "w") as bat:
                            bat.write(f'''@echo off
ping 127.0.0.1 -n 2 >nul
del "{script_path}"
del "%~f0"
''')
                        os.startfile(bat_path)
                except Exception as e:
                    print(f"{Fore.RED}Couldn't schedule delete: {e}{Style.RESET_ALL}")

                sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}Update check failed: {e}{Style.RESET_ALL}")
# Initialize colorama for cross-platform colored text
colorama.init()

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_art():
    """Print the ASCII art for Paiamr."""
    ascii_art = (
        f"{Fore.RED} ________  ________  ___  ________  _____ ______   ________     {Style.RESET_ALL}\n"
        f"{Fore.RED}|\\   __  \\|\\   __  \\|\\  \\|\\   __  \\|\\   _ \\  _   \\|\\   __  \\    {Style.RESET_ALL}\n"
        f"{Fore.YELLOW}\\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\ \\  \\|\\  \\ \\  \\\\__\\ \\  \\ \\  \\|\\  \\   {Style.RESET_ALL}\n"
        f"{Fore.GREEN} \\ \\   ____\\ \\   __  \\ \\  \\ \\   __  \\ \\  \\\\|__| \\  \\ \\   _  _\\  {Style.RESET_ALL}\n"
        f"{Fore.CYAN}  \\ \\  \\___|\\ \\  \\ \\  \\ \\  \\ \\  \\ \\  \\ \\  \\    \\ \\  \\ \\  \\\\  \\| {Style.RESET_ALL}\n"
        f"{Fore.BLUE}   \\ \\__\\    \\ \\__\\ \\__\\ \\__\\    \\ \\__\\ \\__\\\\ _\\ {Style.RESET_ALL}\n"
        f"{Fore.MAGENTA}    \\|__|     \\|__|\\|__|\\|__|\\|__|\\|__|     \\|__|\\|__|\\|__|{Style.RESET_ALL}\n"
    )
    print(ascii_art)

def print_menu(selected_option):
    """Print the menu with the selected option highlighted."""
    clear_screen()
    print_ascii_art()
    print(f"{Fore.MAGENTA}Welcome to Paiamr! Select an option:{Style.RESET_ALL}\n")
    
    options = ["Download Products", "Launch Products", "Uninstall Products", "Exit"]
    for i, option in enumerate(options, 1):
        if i == selected_option:
            print(f"{Fore.WHITE}   {i}. {option}{Style.RESET_ALL}")
        else:
            print(f"{Fore.WHITE}   {i}. {option}{Style.RESET_ALL}")

def is_creative_cloud_installed():
    """Detect if Adobe Creative Cloud is installed."""
    if os.name == 'nt':
        # Windows typical install paths
        possible_paths = [
            r"C:\Program Files\Adobe\Adobe Creative Cloud\ACC\Creative Cloud.exe",
            r"C:\Program Files (x86)\Adobe\Adobe Creative Cloud\ACC\Creative Cloud.exe"
        ]
        return any(os.path.exists(path) for path in possible_paths)
    else:
        # macOS typical install path
        return os.path.exists("/Applications/Adobe Creative Cloud/Adobe Creative Cloud.app")

def download_and_run_cc_installer():
    """Download Creative Cloud installer and run it."""
    url = "https://prod-rel-ffc-ccm.oobesaas.adobe.com/adobe-ffc-external/core/v1/wam/download?sapCode=KCCC&productName=Creative%20Cloud&os=win&guid=c3e40293-04ce-4d08-a616-27e05c7cb624&contextParams=%7B%22component%22%3A%22cc-home%22%2C%22visitor_guid%22%3A%2269316307789845275906987015493941800587%22%2C%22campaign_id%22%3A%222024-11-kaizenStrictSignIn%22%2C%22browser%22%3A%22chrome%22%2C%22context_guid%22%3A%2280c66f91-4e80-4d59-9fd9-f29ec955119d%22%2C%22variation_id%22%3A%22control%22%2C%22experience_id%22%3A%22%22%2C%22planCodeList%22%3A%22cc_free%7Cdc_free%22%2C%22updateCCD%22%3A%22true%22%2C%22secondarySapcodeList%22%3A%22%22%2C%22Product_ID_Promoted%22%3A%22KCCC%22%2C%22userGuid%22%3A%220EF12274687895E30A495C96%40AdobeID%22%2C%22authId%22%3A%220EF12274687895E30A495C96%40AdobeID%22%2C%22contextComName%22%3A%22Organic%3ACCH%22%2C%22contextSvcName%22%3A%22NO-WAM%22%2C%22contextOrigin%22%3A%22Organic%3ACCH%22%2C%22gpv%22%3A%22adobe.com%3Adownload%3Acreative-cloud%22%2C%22AMCV_9E1005A551ED61CA0A490D45%2540AdobeOrg%22%3A%22MCMID%7C69316307789845275906987015493941800587%22%2C%22kaizenTrialDuration%22%3A7%7D&wamFeature=nuj-live&environment=prod&api_key=CCHomeWeb1"
    temp_dir = tempfile.gettempdir()
    installer_path = os.path.join(temp_dir, "CreativeCloudSetup.exe")
    try:
        print(f"{Fore.YELLOW}Downloading Creative Cloud installer...{Style.RESET_ALL}")
        urllib.request.urlretrieve(url, installer_path)
        print(f"{Fore.YELLOW}Running Creative Cloud installer...{Style.RESET_ALL}")
        subprocess.Popen([installer_path], shell=True)
    except Exception as e:
        print(f"{Fore.RED}Failed to download or run installer: {e}{Style.RESET_ALL}")

def get_products_status():
    """Check which products are installed and which are available to install."""
    appdata = os.getenv('APPDATA')
    products_dir = os.path.join(appdata, "Paiamr", "Products")
    photoshop_dir = os.path.join(products_dir, "Photoshop")
    premiere_dir = os.path.join(products_dir, "Premiere Pro")
    after_effects_dir = os.path.join(products_dir, "After Effects")
    installed = []
    available = []

    # Ensure base products directory exists
    if not os.path.exists(products_dir):
        os.makedirs(products_dir)

    # Check Photoshop
    if os.path.exists(photoshop_dir):
        installed.append("Photoshop")
    else:
        available.append("Photoshop")

    # Check Premiere Pro
    if os.path.exists(premiere_dir):
        installed.append("Premiere Pro")
    else:
        available.append("Premiere Pro")

    # Check After Effects
    if os.path.exists(after_effects_dir):
        installed.append("After Effects")
    else:
        available.append("After Effects")

    return available, installed

def download_with_progress(url, dest_path, num_threads=8):
    """Download a file using multiple threads for speed, with a progress bar."""
    # Get file size
    response = requests.head(url, allow_redirects=True)
    if 'Content-Length' not in response.headers:
        # fallback to single-threaded if server doesn't support range requests
        def reporthook(block_num, block_size, total_size):
            downloaded = block_num * block_size
            percent = int(downloaded * 100 / total_size) if total_size > 0 else 0
            bar = ('#' * (percent // 2)).ljust(50)
            sys.stdout.write(f"\r{Fore.YELLOW}Downloading: [{bar}] {percent}%{Style.RESET_ALL}")
            sys.stdout.flush()
        urllib.request.urlretrieve(url, dest_path, reporthook)
        print()
        return

    file_size = int(response.headers['Content-Length'])
    part_size = math.ceil(file_size / num_threads)
    progress = [0] * num_threads

    def download_part(idx, start, end):
        headers = {'Range': f'bytes={start}-{end}'}
        r = requests.get(url, headers=headers, stream=True)
        with open(dest_path, 'r+b') as f:
            f.seek(start)
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    progress[idx] += len(chunk)

    # Pre-allocate file
    with open(dest_path, 'wb') as f:
        f.truncate(file_size)

    threads = []
    for i in range(num_threads):
        start = i * part_size
        end = min(start + part_size - 1, file_size - 1)
        t = threading.Thread(target=download_part, args=(i, start, end))
        threads.append(t)
        t.start()

    # Progress bar
    while any(t.is_alive() for t in threads):
        downloaded = sum(progress)
        percent = int(downloaded * 100 / file_size)
        bar = ('#' * (percent // 2)).ljust(50)
        sys.stdout.write(f"\r{Fore.YELLOW}Downloading: [{bar}] {percent}%{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.1)
    for t in threads:
        t.join()
    sys.stdout.write(f"\r{Fore.YELLOW}Downloading: [{'#'*50}] 100%{Style.RESET_ALL}\n")
    sys.stdout.flush()

def extract_with_progress(zip_path, extract_to):
    """Extract a zip file with a progress bar."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        members = zip_ref.infolist()
        total = len(members)
        for i, member in enumerate(members, 1):
            zip_ref.extract(member, extract_to)
            percent = int(i * 100 / total)
            bar = ('#' * (percent // 2)).ljust(50)
            sys.stdout.write(f"\r{Fore.CYAN}Extracting:  [{bar}] {percent}%{Style.RESET_ALL}")
            sys.stdout.flush()
        print()  # Newline after progress bar

def create_start_menu_shortcut(product_name, exe_path):
    """Create a Start Menu shortcut for the product."""
    try:
        from win32com.client import Dispatch

        # Use ProgramData Start Menu for all users
        start_menu = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
        shortcut_path = os.path.join(start_menu, f"{product_name}.lnk")

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = exe_path
        shortcut.WorkingDirectory = os.path.dirname(exe_path)
        shortcut.IconLocation = exe_path
        shortcut.save()
        print(f"{Fore.GREEN}Shortcut for {product_name} created in Start Menu!{Style.RESET_ALL}")
    except ImportError:
        print(f"{Fore.RED}Shortcut creation requires 'pywin32'. Please install it with 'pip install pywin32'.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Failed to create Start Menu shortcut: {e}{Style.RESET_ALL}")

def install_product(product_name):
    """Install the given product (downloads, extracts, launches, then exits)."""
    appdata = os.getenv('APPDATA')
    products_dir = os.path.join(appdata, "Paiamr", "Products")
    product_dir = os.path.join(products_dir, product_name)
    if not os.path.exists(product_dir):
        os.makedirs(product_dir)
    if product_name == "Photoshop":
        # URLs for both parts
        part_urls = [
            "https://github.com/BlueDragon7327/Paiamr/releases/latest/download/photoshoppart1.zip",
            "https://github.com/BlueDragon7327/Paiamr/releases/latest/download/photoshoppart2.zip"
        ]
        temp_dir = tempfile.gettempdir()
        part_files = [
            os.path.join(temp_dir, "photoshoppart1.zip"),
            os.path.join(temp_dir, "photoshoppart2.zip")
        ]
        # Download both parts
        for url, part_file in zip(part_urls, part_files):
            print(f"{Fore.YELLOW}Starting download for {os.path.basename(part_file)}...{Style.RESET_ALL}")
            download_with_progress(url, part_file)
        # Extract both parts
        for part_file in part_files:
            print(f"{Fore.CYAN}Extracting {os.path.basename(part_file)}...{Style.RESET_ALL}")
            extract_with_progress(part_file, product_dir)
            os.remove(part_file)
        exe_path = os.path.join(product_dir, "Photoshop.exe")
        if os.path.exists(exe_path):
            add_exclusions_for_photoshop()
            print(f"{Fore.GREEN}Firewall bypass added for Photoshop.{Style.RESET_ALL}")
            create_start_menu_shortcut(product_name, exe_path)
            print(f"{Fore.GREEN}Launching {product_name}...{Style.RESET_ALL}")
            subprocess.Popen([exe_path], shell=True)
            print(f"{Fore.GREEN}{product_name} launched. Exiting Paiamr...{Style.RESET_ALL}")
            time.sleep(1)
            os._exit(0)
        else:
            print(f"{Fore.RED}Failed to find Photoshop.exe after extraction.{Style.RESET_ALL}")
            time.sleep(2)
    elif product_name == "Premiere Pro":
        # URLs for both parts
        part_urls = [
            "https://github.com/BlueDragon7327/Paiamr/releases/latest/download/premierepropart1.zip",
            "https://github.com/BlueDragon7327/Paiamr/releases/latest/download/premierepropart2.zip"
        ]
        temp_dir = tempfile.gettempdir()
        part_files = [
            os.path.join(temp_dir, "premierepropart1.zip"),
            os.path.join(temp_dir, "premierepropart2.zip")
        ]
        # Download both parts
        for url, part_file in zip(part_urls, part_files):
            print(f"{Fore.YELLOW}Starting download for {os.path.basename(part_file)}...{Style.RESET_ALL}")
            download_with_progress(url, part_file)
        # Extract both parts
        for part_file in part_files:
            print(f"{Fore.CYAN}Extracting {os.path.basename(part_file)}...{Style.RESET_ALL}")
            extract_with_progress(part_file, product_dir)
            os.remove(part_file)
        exe_path = os.path.join(product_dir, "Adobe Premiere Pro.exe")
        if os.path.exists(exe_path):
            add_exclusions_for_premiere_pro()
            print(f"{Fore.GREEN}Firewall bypass added for Premiere Pro.{Style.RESET_ALL}")
            create_start_menu_shortcut(product_name, exe_path)
            print(f"{Fore.GREEN}Launching {product_name}...{Style.RESET_ALL}")
            subprocess.Popen([exe_path], shell=True)
            print(f"{Fore.GREEN}{product_name} launched. Exiting Paiamr...{Style.RESET_ALL}")
            time.sleep(1)
            os._exit(0)
        else:
            print(f"{Fore.RED}Failed to find Adobe Premiere Pro.exe after extraction.{Style.RESET_ALL}")
            time.sleep(2)
    elif product_name == "After Effects":
        # URLs for both parts
        part_urls = [
            "https://github.com/BlueDragon7327/Paiamr/releases/latest/download/aftereffectspart1.zip",
            "https://github.com/BlueDragon7327/Paiamr/releases/latest/download/aftereffectspart2.zip"
        ]
        temp_dir = tempfile.gettempdir()
        part_files = [
            os.path.join(temp_dir, "aftereffectspart1.zip"),
            os.path.join(temp_dir, "aftereffectspart2.zip")
        ]
        # Download both parts
        for url, part_file in zip(part_urls, part_files):
            print(f"{Fore.YELLOW}Starting download for {os.path.basename(part_file)}...{Style.RESET_ALL}")
            download_with_progress(url, part_file)
        # Extract both parts
        for part_file in part_files:
            print(f"{Fore.CYAN}Extracting {os.path.basename(part_file)}...{Style.RESET_ALL}")
            extract_with_progress(part_file, product_dir)
            os.remove(part_file)
        exe_path = os.path.join(product_dir, "AfterFX.exe")
        if os.path.exists(exe_path):
            add_exclusions_for_after_effects()
            print(f"{Fore.GREEN}Firewall bypass added for After Effects.{Style.RESET_ALL}")
            create_start_menu_shortcut(product_name, exe_path)
            print(f"{Fore.GREEN}Launching {product_name}...{Style.RESET_ALL}")
            subprocess.Popen([exe_path], shell=True)
            print(f"{Fore.GREEN}{product_name} launched. Exiting Paiamr...{Style.RESET_ALL}")
            time.sleep(1)
            os._exit(0)
        else:
            print(f"{Fore.RED}Failed to find AfterFX.exe after extraction.{Style.RESET_ALL}")
            time.sleep(2)
    else:
        print(f"{Fore.YELLOW}{product_name} is already installed or unknown product.{Style.RESET_ALL}")
        time.sleep(2)

def uninstall_product(product_name):
    """Uninstall the given product by deleting its folder, shortcut, and firewall rules."""
    appdata = os.getenv('APPDATA')
    product_dir = os.path.join(appdata, "Paiamr", "Products", product_name)

    # Remove firewall rules if it's Photoshop
    if product_name == "Photoshop":
        remove_exclusions_for_photoshop()  # prints its own messages
    elif product_name == "Premiere Pro":
        remove_exclusions_for_premiere_pro()  # prints its own messages
    elif product_name == "After Effects":
        remove_exclusions_for_after_effects()  # prints its own messages

    # Delete shortcut if on Windows
    if os.name == 'nt':
        start_menu = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
        shortcut_path = os.path.join(start_menu, f"{product_name}.lnk")
        if os.path.exists(shortcut_path):
            os.remove(shortcut_path)
            print(f"{Fore.GREEN}Removed shortcut for {product_name}.{Style.RESET_ALL}")

    # Delete product folder
    if os.path.exists(product_dir):
        shutil.rmtree(product_dir)
        print(f"{Fore.GREEN}Deleted folder for {product_name}.{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}Folder for {product_name} not found.{Style.RESET_ALL}")


def show_download_products_menu():
    """Show menu for downloading products."""
    while True:
        available, _ = get_products_status()
        clear_screen()
        print_ascii_art()
        print(f"{Fore.MAGENTA}Available Products to Install:{Style.RESET_ALL}\n")
        if not available:
            print(f"{Fore.GREEN}All products are already installed!{Style.RESET_ALL}")
            time.sleep(2)
            return
        for idx, prod in enumerate(available, 1):
            print(f"{Fore.WHITE}{idx}. {prod}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}0. Back{Style.RESET_ALL}")
        choice = input(f"\n{Fore.CYAN}Enter your choice: {Style.RESET_ALL}")
        try:
            choice = int(choice)
            if choice == 0:
                return
            elif 1 <= choice <= len(available):
                install_product(available[choice - 1])
            else:
                print(f"{Fore.RED}Invalid choice.{Style.RESET_ALL}")
                time.sleep(1)
        except ValueError:
            print(f"{Fore.RED}Invalid input.{Style.RESET_ALL}")
            time.sleep(1)

def show_launch_products_menu():
    """Show menu for launching installed products."""
    while True:
        _, installed = get_products_status()
        clear_screen()
        print_ascii_art()
        print(f"{Fore.MAGENTA}Installed Products to Launch:{Style.RESET_ALL}\n")
        if not installed:
            print(f"{Fore.YELLOW}No products installed yet!{Style.RESET_ALL}")
            time.sleep(2)
            return
        for idx, prod in enumerate(installed, 1):
            print(f"{Fore.WHITE}{idx}. {prod}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}0. Back{Style.RESET_ALL}")
        choice = input(f"\n{Fore.CYAN}Enter your choice: {Style.RESET_ALL}")
        try:
            choice = int(choice)
            if choice == 0:
                return
            elif 1 <= choice <= len(installed):
                product = installed[choice - 1]
                appdata = os.getenv('APPDATA')
                if product == "Photoshop":
                    exe_path = os.path.join(appdata, "Paiamr", "Products", "Photoshop", "Photoshop.exe")
                    exe_name = "Photoshop.exe"
                elif product == "Premiere Pro":
                    exe_path = os.path.join(appdata, "Paiamr", "Products", "Premiere Pro", "Premiere Pro.exe")
                    exe_name = "Premiere Pro.exe"
                elif product == "After Effects":
                    exe_path = os.path.join(appdata, "Paiamr", "Products", "After Effects", "AfterFX.exe")
                    exe_name = "AfterFX.exe"
                else:
                    print(f"{Fore.YELLOW}Launching {product} (functionality to be implemented){Style.RESET_ALL}")
                    time.sleep(2)
                    continue
                if os.path.exists(exe_path):
                    print(f"{Fore.GREEN}Launching {product}...{Style.RESET_ALL}")
                    subprocess.Popen([exe_path], shell=True)
                    print(f"{Fore.GREEN}{product} launched. Exiting Paiamr...{Style.RESET_ALL}")
                    sys.stdout.flush()
                    sys.stderr.flush()
                    os._exit(1)  # Use nonzero exit code for forced exit
                else:
                    print(f"{Fore.RED}{exe_name} not found!{Style.RESET_ALL}")
                    time.sleep(2)
            else:
                print(f"{Fore.RED}Invalid choice.{Style.RESET_ALL}")
                time.sleep(1)
        except ValueError:
            print(f"{Fore.RED}Invalid input.{Style.RESET_ALL}")
            time.sleep(1)

def show_uninstall_products_menu():
    """Show menu for uninstalling installed products."""
    while True:
        _, installed = get_products_status()
        clear_screen()
        print_ascii_art()
        print(f"{Fore.MAGENTA}Installed Products to Uninstall:{Style.RESET_ALL}\n")
        if not installed:
            print(f"{Fore.YELLOW}No products installed yet!{Style.RESET_ALL}")
            time.sleep(2)
            return
        for idx, prod in enumerate(installed, 1):
            print(f"{Fore.WHITE}{idx}. {prod}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}0. Back{Style.RESET_ALL}")
        choice = input(f"\n{Fore.CYAN}Enter your choice: {Style.RESET_ALL}")
        try:
            choice = int(choice)
            if choice == 0:
                return
            elif 1 <= choice <= len(installed):
                product = installed[choice - 1]
                confirm = input(f"{Fore.YELLOW}Are you sure you want to uninstall {product}? (y/n): {Style.RESET_ALL}")
                if confirm.lower() == 'y':
                    uninstall_product(product)
                    print(f"{Fore.GREEN}Uninstall complete for {product}.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}Uninstall cancelled.{Style.RESET_ALL}")
                time.sleep(2)
            else:
                print(f"{Fore.RED}Invalid choice.{Style.RESET_ALL}")
                time.sleep(1)
        except ValueError:
            print(f"{Fore.RED}Invalid input.{Style.RESET_ALL}")
            time.sleep(1)

def is_running_as_admin():
    """Check if the script is running with admin rights."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def relaunch_as_admin():
    """Relaunch the script with admin rights."""
    if sys.version_info[0] == 3:
        params = ' '.join([f'"{arg}"' for arg in sys.argv])
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1)
        sys.exit(0)

def main():
    check_for_update()
    """Main function to run the Paiamr launcher."""
    # Request admin rights if not running as admin
    if os.name == 'nt' and not is_running_as_admin():
        print(f"{Fore.YELLOW}Requesting administrator privileges...{Style.RESET_ALL}")
        relaunch_as_admin()
        return
    # Check for Adobe Creative Cloud
    if is_creative_cloud_installed():
        print(f"{Fore.GREEN}Adobe Creative Cloud detected on this system.{Style.RESET_ALL}")
        time.sleep(2)
    else:
        download_and_run_cc_installer()
        print(f"{Fore.RED}Creative Cloud Needed, Please Finish the Installer and Restart Paiamr.{Style.RESET_ALL}")
        input(f"{Fore.CYAN}Press Enter to exit...{Style.RESET_ALL}")
        return
    selected_option = 1

    while True:
        print_menu(selected_option)
        choice = input(f"\n{Fore.CYAN}Enter your choice (1-4): {Style.RESET_ALL}")
        try:
            choice = int(choice)
            if choice in [1, 2, 3, 4]:
                selected_option = choice
                if choice == 1:
                    show_download_products_menu()
                elif choice == 2:
                    show_launch_products_menu()
                elif choice == 3:
                    show_uninstall_products_menu()
                elif choice == 4:
                    clear_screen()
                    print(f"{Fore.RED}Exiting Paiamr... Goodbye!{Style.RESET_ALL}")
                    time.sleep(1)
                    break
            else:
                print(f"{Fore.RED}Please enter a number between 1 and 4.{Style.RESET_ALL}")
                time.sleep(2)
        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
            time.sleep(2)

if __name__ == "__main__":
    main()

import pyautogui
import subprocess
import time
from bs4 import BeautifulSoup
import pygetwindow as gw
import pyperclip
import keyboard
import warnings
from bs4 import MarkupResemblesLocatorWarning
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)


def wait_and_click(image_name, max_wait=60, confidence=0.7):
    print(f" Waiting for '{image_name}'...")
    start_time = time.time()
    location = None

    while location is None and (time.time() - start_time) < max_wait:
        try:
            location = pyautogui.locateOnScreen(image_name, confidence=confidence)
            if location is None:
                time.sleep(1)
        except pyautogui.ImageNotFoundException:
            time.sleep(1)

    if location:
        x, y = pyautogui.center(location)
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.click()
        print(f" Clicked: {image_name}")
        return True
    else:
        print(f" Could not find: {image_name} in {max_wait} seconds")
        return False


def run_js_to_copy_data():
    # Focus the Chrome window
    for w in gw.getWindowsWithTitle("LinkedIn"):
        if "LinkedIn" in w.title:
            w.activate()
            time.sleep(1)
            break

    # Open DevTools
    pyautogui.hotkey("ctrl", "shift", "j")
    time.sleep(3)

    # Focus the console
    pyautogui.moveTo(900, 800, duration=0.5)  # Adjust this if console is elsewhere
    pyautogui.click()
    time.sleep(1)

    # Paste and execute JS
    js_code = """
    (function() {
        const divs = Array.from(document.querySelectorAll("div.x_ql9qN"));
        const content = divs.map(d => d.innerText).join("\\n");
        navigator.clipboard.writeText(content);
    })();
    """
    pyperclip.copy(js_code)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(4)

    # Close DevTools
    pyautogui.hotkey("ctrl", "shift", "j")
    time.sleep(1)

    # Read clipboard
    result = pyperclip.paste()
    return result.strip().splitlines()


# Step 1: Launch Chrome with LinkedIn
print("🌐 Launching Chrome...")
subprocess.Popen(['start', 'chrome', 'https://www.linkedin.com/in/anupammittal007/'], shell=True)

# Step 2: Wait and click Apollo Sidebar
wait_and_click('apollo_button.png')

# Step 3: Try to extract data without clicking
print("🔍 Trying to extract data without clicking...")
time.sleep(5)
initial_data = run_js_to_copy_data()
print(" Initial data found:", initial_data)

# Step 4: Click email button and extract
if wait_and_click('apollo_button_email.png'):
    time.sleep(9)
    print(" Extracting email...")
    email_data = run_js_to_copy_data()
    print(" Email data after click:", email_data)

# Step 5: Click phone button and extract
if wait_and_click('apollo_button_phone.png'):
    time.sleep(9)
    print(" Extracting phone...")
    phone_data = run_js_to_copy_data()
    print("\ Phone data after click:", phone_data)

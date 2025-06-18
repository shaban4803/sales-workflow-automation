from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Setup browser
options = webdriver.ChromeOptions()
options.add_argument("--remote-debugging-port=9222")  # optional if needed
driver = webdriver.Chrome(options=options)

# Open the same profile page (it may open a new tab)
driver.get('https://www.linkedin.com/in/anupammittal007/')
time.sleep(15)  # Wait for Apollo to fully inject data

# Extract visible HTML and parse
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
data = [el.text.strip() for el in soup.find_all('div', class_='x_ql9qN')]

print(" Extracted Data:", data)
driver.quit()

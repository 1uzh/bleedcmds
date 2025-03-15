from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from colorama import Fore
import time

service = Service(r"chromedriver.exe")
driver = webdriver.Chrome(service=service)

url = "https://bleed.bot/commands"
print(Fore.CYAN + "Navigating to:", url)

try:
    driver.get(url)
    time.sleep(5)

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    elements = soup.find_all('p', class_="text-xl font-semibold inline-flex items-center")
    command_list = [element.text.strip() for element in elements]

    print(Fore.MAGENTA + "Commands:")
    for command in command_list:
        print(Fore.MAGENTA + f"- {command}")

    with open("output.txt", "w") as file:
        file.write("\n".join(command_list))
    print(Fore.GREEN + "Data successfully written to 'output.txt'.")

except Exception as e:
    print(Fore.RED + "An error occurred:", str(e))

finally:

    print(Fore.YELLOW + "WebDriver closed, program will exit automatically.")
    driver.quit()
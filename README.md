![bleed](https://github.com/user-attachments/assets/73c4d242-4df2-4475-8777-20fb920d2e19)

# Bleed Command Exporter 
( or any document you want to export information out of )

# What is this?
This is a bleed commands exporter is made using python and it is super easy to use and user-friendly

# Size

![Static Badge](https://img.shields.io/badge/file%20size%20-%201.07%20kb%20-%20cyan?style=flat)

# Requirements
( included in the release , here only if you're lazy )
``` bash
pip install colorama
pip install selenium
pip install bs4
pip install time
pip install os ( optional for other projects )
```
# Usage
```python
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
```
- Great for python beginners to learn code
- Willing to do updates
- Easy to use

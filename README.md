https://www.google.com/url?sa=i&url=https%3A%2F%2Fbleed.bot%2F&psig=AOvVaw2jfM41geD4FEpVI2InEnAO&ust=1742100624800000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPC509aki4wDFQAAAAAdAAAAABAE
# Bleed Command Exporter ( or any document you want to export information out of
This command exporter is made using python and it is super easy to use and user-friendly

![Static Badge](https://img.shields.io/badge/file%20size%20-%201.07%20KB%20(%20not%20including%20ChromeDriver%20))

# Requirements ( included in the release , here only if you're lazy )
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

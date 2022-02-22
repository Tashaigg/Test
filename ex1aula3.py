from selenium.webdriver import Chrome
from time import sleep
browser = Chrome()
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser.get(url)
sleep(2)
p = browser.find_elements_by_tag_name('p')
h = browser.find_element_by_tag_name('h1')

dic = {h.text:
    {
        't1':{p[0].text},
        't2':{p[1].text},
        't3':{p[2].text},
    }
    }

print(f' o código de p.text é: {p[0].text}')
print(f' o código de p é: {p}')
print(dic)
browser.quit()

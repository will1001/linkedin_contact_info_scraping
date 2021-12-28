import time

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

link = "https://www.linkedin.com/in/prawito-hudoro/"
driver = webdriver.Chrome()


def scraping():
    email = None
    phones = None
    websites = None
    twitter = None
    output = ""
    login()
    driver.get(link)
    driver.find_elements(By.XPATH,
                         "//a[@class='ember-view link-without-visited-state cursor-pointer text-heading-small "
                         "inline-block break-words']")[
        0].click()
    time.sleep(3)
    contact_info_panel = \
        driver.find_elements(By.XPATH, "//section[@class='pv-contact-info__contact-type ci-websites']")[0]
    if contact_info_panel.is_displayed():
        content2 = driver.page_source.encode('utf-8').strip()
        soup2 = BeautifulSoup(content2, 'lxml')
        websites = soup2.findAll('section', class_='ci-websites')
        twitter = soup2.findAll('section', class_='ci-twitter')
        phones = soup2.findAll('section', class_='ci-phone')
        email = soup2.findAll('section', class_='ci-email')
        birthday = soup2.findAll('section', class_='ci-birthday')
        connected = soup2.findAll('section', class_='ci-connected')
    # i = 0
    # print(websites[0].findChildren('ul'))
    if len(websites) != 0:
        output += "Websites :"
        for website in websites[0].findChildren('ul')[0].findChildren('li'):
            link_href = website.findChildren('a')[0].get('href')
            description = website.findChildren('span')[0].text.replace('\n', '').replace(' ', '')
            output += f"\n - {link_href} {description}"
    if len(twitter) != 0:
        output += f"\ntwitter : {twitter[0].findChildren('a')[0].get('href')}"
    if len(phones) != 0:
        output += "\nPhones :"
        for phone in phones[0].findChildren('ul')[0].findChildren('li'):
            number = phone.findChildren('span')[0].text.replace('\n', '').replace(' ', '')
            number_desc = phone.findChildren('span')[1].text.replace('\n', '').replace(' ', '')
            output += f"\n - {number} {number_desc}"
    if len(email) != 0:
        email_text = email[0].findChildren('a')[0].text.replace('\n', '').replace(' ', '')
        output += f"\nemail : {email_text}"
    if len(birthday) != 0:
        birthday_text = birthday[0].findChildren('span')[0].text.replace('\n', '').replace(' ', '')
        output += f"\nbirthday : {birthday_text}"
    if len(connected) != 0:
        connected_text = connected[0].findChildren('span')[0].text.replace('\n', '').replace(' ', '')
        output += f"\nconnected : {connected_text}"

    print(output)
    driver.close()


def login():
    # data_login = {
    #     'username': 'wilirahmatm@gmail.com',
    #     'password': 'WilI281094'
    # }

    driver.get('https://www.linkedin.com/login/in')
    username_input = driver.find_elements(By.ID, "username")[0]
    password_input = driver.find_elements(By.ID, "password")[0]
    username_input.send_keys("wilirahmatm@gmail.com")
    password_input.send_keys("WilI281094")
    driver.find_elements(By.CLASS_NAME, "login__form_action_container")[0].click()

    # print(button_login.click)
    # time.sleep(10)
    # content = driver.page_source.encode('utf-8').strip()
    # soup = BeautifulSoup(content, 'lxml')
    # contact_info_button = soup.findAll('div')
    # print(contact_info_button)


if __name__ == '__main__':
    scraping()

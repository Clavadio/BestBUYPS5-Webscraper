from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import actions
from selenium.common.exceptions import NoSuchElementException    
import os
import smtplib
from email.message import EmailMessage
import time

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

browser = webdriver.Chrome(options=options, executable_path='C:\\Users\\DELL 390\Desktop\\PythonEnvironment\\env\\pythonWorkSpaces\\chromedriver.exe')
outOfStockMessage = 'PlayStation 5 consoles sold out quickly. Please check back or follow us on Twitter @BBYC_Gamers for updates.'
textXpath = '//*[@id="root"]/div/div[4]/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/p'

def sendEmail():
    EMAIL_ADDRESS = 'Your Email Address'
    EMAIL_PASS = 'Your Email Password'
    EMAIL_RECEIP = 'Recipient Email Address'
    filename = "C:\\Bestbuy.txt"

    msg = EmailMessage()
    msg['Subject'] = 'Best Buy Update?'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_RECEIP
    msg['CC'] = 'A second Gmail address' #not required
    msg.add_attachment(open(filename, "r").read(), filename ="Postings.txt")

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

        smtp.send_message(msg)
def check_exists_by_xpath():
    if browser.find_element_by_xpath(textXpath):
        return True
    else:
        return False    

def checkText(count):
    x=0
    while x==0:
        browser.get('https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184')
        time.sleep(2)
        titleDiv = browser.find_element_by_xpath(textXpath)
        isPresent = check_exists_by_xpath()
        titleText = titleDiv.text
        print(f'{count}: {titleText}')
        
        if  isPresent == False:
            testMessage = 'Quickly Best Buy PS5 is back in stock!'
            print(testMessage)
            with open("C:\\Bestbuy.txt", "w") as file:
                file.write((f'{testMessage}'))
            sendEmail()
            x+=1        
        else:
            time.sleep(2)
            count+=1 
            
i=0
checkText(i)
        
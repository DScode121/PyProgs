from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime


def classlink():
    link = ''
    thetime = datetime.datetime.now()
    if 'enter the day here' in thetime.ctime() and 'hour' in str(thetime.hour) and 'min' in str(thetime.minute):
        link = 'enter your meet link here'
    elif 'enter the day here' in thetime.ctime() and 'hour' in str(thetime.hour) and 'min' in str(thetime.minute):
        link = 'enter your meet link here'
    elif 'enter the day here' in thetime.ctime() and 'hour' in str(thetime.hour) and 'min' in str(thetime.minute):
        link = 'enter your meet link here'
    elif 'enter the day here' in thetime.ctime() and 'hour' in str(thetime.hour) and 'min' in str(thetime.minute):
        link = 'enter your meet link here'
    else:
        link = 'oops'
    return link


def Glogin(mail_address, password):
    # Login Page
    driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

    # input Gmail
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(10)

    # input Password
    driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element_by_id("passwordNext").click()
    driver.implicitly_wait(10)

    # go to google home page
    driver.get('https://google.com/')
    driver.implicitly_wait(100)


'''
THIS FUNCTION CAN BE USED TO TURN OFF YOUR MICROPHONE AND CAMERA
'''


def turnOffMicCam():
    # turn off Microphone
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.implicitly_wait(3000)

    # turn off camera
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    driver.implicitly_wait(3000)


def joinNow():
    # Join meet
    print(1)
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    print(1)


def AskToJoin():
    # Ask to Join meet
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()


# Ask to join and join now buttons have same xpaths


# assign email id and password
mail_address = 'enter your mail id'
password = 'enter your pass'

# create chrome instance
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_argument('--disable-notifications')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 2
})
driver = webdriver.Chrome(options=opt)
if __name__ == "__main__":
    '''login to Google account'''
    Glogin(mail_address, password)
    ''' go to google meet'''
    driver.get(classlink())
    '''USE THE 'turnOffMicCam()' FUNCTION HERE TO TURN OFF YOUR MIC AND CAM'''
    time.sleep(5)
    joinNow()

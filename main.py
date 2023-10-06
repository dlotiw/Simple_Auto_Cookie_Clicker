from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import time
import threading
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(options=options)
# driver.get("https://www.python.org/")
# events_el = driver.find_element(By.CSS_SELECTOR,'#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul')
# times = [t.text for t in events_el.find_elements(By.TAG_NAME,'time')]
# ev_names = [t.text for t in events_el.find_elements(By.TAG_NAME,'a')]
# events = {}
# for i in range(len(ev_names)):
#     events[i] = {'name': ev_names[i], 'time': times[i]}
# print(events)

# driver.get('https://secure-retreat-92358.herokuapp.com/')
# name = driver.find_element(By.NAME,'fName')
# lname = driver.find_element(By.NAME,'lName')
# email = driver.find_element(By.NAME,'email')
# name.send_keys('Randy')
# lname.send_keys('Random')
# email.send_keys('randy.random@rimwordgame.com')
# driver.find_element(By.TAG_NAME,'button').click()
def click_cookie(cookie):
    while True:
        cookie.click()


def auto_cookie():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.get('https://orteil.dashnet.org/cookieclicker/')
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.fc-cta-consent > p:nth-child(2)'))).click()
    driver.find_element(By.ID,'langSelect-EN').click()
    WebDriverWait(driver,10).until(EC.invisibility_of_element(element=(By.ID,'loader')))
    cookie = driver.find_element(By.ID,'bigCookie')
    t1 = threading.Thread(target=click_cookie,args=(cookie,))
    products = driver.find_elements(By.CSS_SELECTOR,'[id^=product]')
    i=0
    while True:
        try:
            if len(products[i].get_attribute('id')) > 9:
                products.pop(i)
            else:
                i+=1
        except:
            break 
    # for i in range(19):
    #     upgrades.append(driver.find_element(By.ID,f'product{i}'))
    t1.start()
    t_end = time.time() + 31*60
    while time.time() < t_end:
        for i in range(len(products)-1,0,-1):
          
            if 'unlocked enabled' in products[i].get_attribute('class'):
                products[i].click()
        try:
            possible = EC._element_if_visible(driver.find_element(By.ID,'upgrade0'))
            if 'enabled' in possible.get_attribute('class'):
                possible.click()
        except exceptions.NoSuchElementException:
            pass
    driver.quit()
            
            
                

    
    
    



if __name__ == '__main__':
    auto_cookie()




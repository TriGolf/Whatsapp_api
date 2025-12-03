from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import shutil

class Whatsapp :
    def __init__(self, service=None, headless=False) :
        if service :
            self.service = webdriver.FirefoxService(service)
        else :
            self.service = None
        
        self.options = webdriver.FirefoxOptions()
        self.options.set_preference('intl.accept_languages', 'en-GB')

        if headless :
            self.options.add_argument('--headless')

        if os.path.exists('profile') :
            self.options.profile = webdriver.FirefoxProfile('profile')

        self.driver = webdriver.Firefox(options=self.options,service=self.service)
        self.wait = WebDriverWait(self.driver,60)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://web.whatsapp.com")


        if not os.path.exists('profile') :
            input("Scannez le qr code et appuyez sur entrée (vous resterez connecté la prochaine fois)")
            try :
                shutil.copytree(src=self.driver.capabilities['moz:profile'], dst='profile')
                print("Enregistrement des infos de connexions réussie")
            except :
                print("Erreur lors de l'enregistrement des données de connexion (cela peut quand même marcher)")

        else :
            try :
                self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="x1hx0egp x6ikm8r x1odjw0f x6prxxf x1k6rcq7 x1whj5v"]'))) # Champ de recherche
            except TimeoutError :
                print("Une erreur est survenue lors de la connexion. Si vous voyez un qr code à l'écran, veuillez supprimer le dossier profile et réessayer")
        


        
    
    def go_to(self,phone) :

        if phone.lower() == "unread" :
            button = self.driver.find_element(By.XPATH,'//button[@class="xjb2p0i x1ypdohk x972fbf xcfux6l x1qhh985 xm0m39n xzqyx8i xqa96yk xvwobac x1h2y310 x1mvgj39 x6prxxf xo1l8bm x1btupbp x1yky6xw xf573un x1yrsyyn x10b6aqq x1ye3gou xn6708d"]')
            button.click()
            return
        
        self.new_chat = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[3]/div/div[4]/header/header/div/span/div/div[1]/span/button')
        self.new_chat.click()

        self.selec_contact = self.driver.find_element(By.XPATH,'//div[@class="x1hx0egp x6ikm8r x1odjw0f x6prxxf x1k6rcq7 x1whj5v"]')
        for x in range(len(phone)) :
            self.selec_contact.send_keys(phone[x])
        time.sleep(0.5)
        
        self.contact = self.driver.find_element(By.XPATH,'//div[@style="z-index: 0; transition: none; height: 72px; transform: translateY(72px);" and @role="listitem"]')
        self.contact.click()

        self.actual_contact = phone
        time.sleep(0.5)

    def send_message(self,message) :
        self.div = self.driver.find_element(By.XPATH,'//div[@class="x1hx0egp x6ikm8r x1odjw0f x1k6rcq7 x6prxxf"]')
        self.div.click()
        actions = ActionChains(self.driver)

        #pyperclip.copy(message)

        print("ecrit")
        #self.div.send_keys(self.control_key,'v')
        actions.send_keys(message).perform()
        self.div.send_keys(Keys.ENTER)
        time.sleep(1)
    
    def refresh(self) :
        self.driver.refresh()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="x1hx0egp x6ikm8r x1odjw0f x6prxxf x1k6rcq7 x1whj5v"]'))) # Champ de recherche
        self.actual_contact = None
    
    def read_last_messages(self) :
        self.messages = self.driver.find_elements(By.XPATH,'//span[@class="_ao3e selectable-text copyable-text"]')
        for x in self.messages :
            pass
        try :
            self.nb_messages = len(self.messages) - 1
            self.last_message = self.messages[self.nb_messages:]
            self.last_message = self.last_message[0]
            print(self.last_message.text)
            return self.last_message.text
        except Exception as e:
            print("Pas de message :",e)
            return None
        
    def quit(self) :
        self.driver.quit()

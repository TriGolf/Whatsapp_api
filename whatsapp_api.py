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
                self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label="Champ de recherche"]')))
            except TimeoutError :
                print("Une erreur est survenue lors de la connexion. Si vous voyez un qr code à l'écran, veuillez supprimer le dossier profile et réessayer")
        


        
    
    def go_to(self,phone) :

        if phone.lower() == "unread" :
            button = self.driver.find_element(By.XPATH,'//button[@class="xjb2p0i x1ypdohk x972fbf xcfux6l x1qhh985 xm0m39n xzqyx8i xqa96yk xvwobac x1h2y310 x1mvgj39 x6prxxf xo1l8bm x1btupbp x1yky6xw xf573un x1yrsyyn x10b6aqq x1ye3gou xn6708d"]')
            button.click()
            return
        
        self.new_chat = self.driver.find_element(By.XPATH,'//button[@class="html-button xdj266r x14z9mp xat24cr x1lziwak xexx8yu xyri2b x18d9i69 x1c1uobl x178xt8z x1lun4ml xso031l xpilrb4 x1n2onr6 x1ejq31n x18oe1m7 x1sy0etr xstzfhl x1so62im x1syfmzz x1ja2u2z x1s928wv x1j6awrg x4eaejv x1wsn0xg x1r0yslu x2q1x1w xapdjt xr6f91l x5rv0tg x1akc3lz xikp0eg x1xl5mkn x1mfml39 x1l5mzlr xgmdoj8 x1f1wgk5 x1x3ic1u xjbqb8w xuwfzo9 xy0j11r xg268so x1b4bgnk x1wb366y xtnn1bt x9v5kkp xmw7ebm xrdum7p x2lah0s x1lliihq xk8lq53 x9f619 xt8t1vi x1xc408v x129tdwq x15urzxu x1vqgdyp x100vrsf"]')
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
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="html-button xdj266r x14z9mp xat24cr x1lziwak xexx8yu xyri2b x18d9i69 x1c1uobl x178xt8z x1lun4ml xso031l xpilrb4 x1n2onr6 x1ejq31n x18oe1m7 x1sy0etr xstzfhl x1so62im x1syfmzz x1ja2u2z x1s928wv x1j6awrg x4eaejv x1wsn0xg x1r0yslu x2q1x1w xapdjt xr6f91l x5rv0tg x1akc3lz xikp0eg x1xl5mkn x1mfml39 x1l5mzlr xgmdoj8 x1f1wgk5 x1x3ic1u xjbqb8w xuwfzo9 xy0j11r xg268so x1b4bgnk x1wb366y xtnn1bt x9v5kkp xmw7ebm xrdum7p x2lah0s x1lliihq xk8lq53 x9f619 xt8t1vi x1xc408v x129tdwq x15urzxu x1vqgdyp x100vrsf"]')))
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

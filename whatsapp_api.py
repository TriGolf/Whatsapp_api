from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip

class Whatsapp :
    def __init__(self, profile, service, headless) :
        if service :
            self.service = webdriver.FirefoxService(service)
        else :
            self.service = None
        
        self.options = webdriver.FirefoxOptions()
        self.options.profile = webdriver.FirefoxProfile(profile)
        if headless :
          self.options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=self.options,service=self.service)
        self.wait = WebDriverWait(self.driver,60)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://web.whatsapp.com")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label="Champ de recherche"]')))
    
    def select(self,phone) : # Sélectionner le contact (Numéro de téléphone ou nom du contact/groupe)
        self.new_chat = self.driver.find_element(By.XPATH,'//div[@aria-label="Nouvelle discussion" and @role="button"]')
        self.new_chat.click()

        self.selec_contact = self.driver.find_element(By.XPATH,'//div[@aria-label="Champ de recherche"]')
        for x in range(len(phone)) :
            self.selec_contact.send_keys(phone[x])
        
        self.contact = self.driver.find_element(By.XPATH,'//div[@style="z-index: 0; transition: none; height: 72px; transform: translateY(72px);" and @role="listitem"]')
        self.contact.click()

        self.actual_contact = phone
        time.sleep(3)

    def send_message(self,message) : # Envoie un message au contact sélectionné auparavant
        self.div = self.driver.find_element(By.XPATH,'//div[@aria-label="Entrez un message"]')
        pyperclip.copy(message)

        print("ecrit")
        #for x in range(len(message)) :
            #self.div.send_keys(message[x])
        self.div.send_keys(Keys.CONTROL,'v')
        self.div.send_keys(Keys.ENTER)
        time.sleep(1)
    
    def refresh(self) :
        self.driver.refresh()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label="Champ de recherche"]')))
        self.actual_contact = None
    
    def read_last_messages(self) : # Retourne le dernier message du contact sélectionné (y compris vos messages)
        self.messages = self.driver.find_elements(By.XPATH,'//span[@class="_ao3e selectable-text copyable-text"]')
        for x in self.messages :
            pass
            #print(x.text)
        try :
            self.nb_messages = len(self.messages) - 1
            self.last_message = self.messages[self.nb_messages:]
            self.last_message = self.last_message[0]
            print(self.last_message.text)
            return self.last_message.text
        except Exception as e:
            print("Pas de message (peut être une erreur) :",e)
            return None

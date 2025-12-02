# Ce code connecte l'api de groq à whatsapp (un groupe ou vous même)
# Les commandes /1, /2, /3 vous permettent de changer de modèle et la commande /reset de rénitialiser la mémoire du modèle
from whatsapp_api import Whatsapp
from groq import Groq
import time

model = "mixtral-8x7b-32768"
prompt_system = "Tu est un assistant par messages whatsapp qui parle en français et s'appelle François. Tu peux donc utiliser les mises en formes proposées par whatsapp (tu peux encadrer une ligne par * pour mettre le texte en gras,` pour mettre le style \"code\", etc...). Tu ne dois pas commencer tes messages par @"
client = Groq(api_key='Votre api key')


what = Whatsapp(service='geckodriver (si besoin)',headless=True)
what.go_to('Téléphone ou nom groupe/contact') # Groupe/contact qui sera connecté à groq (mettez votre propre numéro si vous voulez le connecter à vous même)


what.send_message("Bonjour, je suis François, votre assistant virtuel.\n comment puis-je vous aider ?") # Premier message
messages=[
    {
        "role": "system",
        "content": prompt_system
    }
]

while 1 :
    last_message = what.read_last_messages()
    if last_message != None :
        if last_message.startswith("@") :
            messages.append({"role":"user","content":last_message})
            what.send_message("Je réfléchis...")
            try :
                chat_completion = client.chat.completions.create(
                    messages=messages,
                    model=model,
                )
                what.send_message(chat_completion.choices[0].message.content)
                messages.append({"role":"assistant","content":chat_completion.choices[0].message.content})
            except :
                what.send_message("Une erreur s'est produite...\nPour résoudre le problème vous pouvez essayer de rénitialiser l'historique avec /reset ou de changer de modèle avec /1,/2 ou /3")
            print("message envoye")
            
        elif last_message.startswith("/reset") :
            messages=[
                {
                "role": "system",
                "content": prompt_system
                }
            ]
            what.send_message("Historique de conversation rénitialisé")
            
        elif last_message.startswith("/") :
            if last_message == '/1' :
                model = "mixtral-8x7b-32768"
            elif last_message == '/2':
                model = "llama3-8b-8192"
            elif last_message == '/3' :
                model = "llama3-70b-8192"
            what.send_message(f"Le modèle est maintenant {model}")

        time.sleep(1)

# Whatsapp_api
Une api pour whatsapp

# Dépendances :

Sélénium et shutils
```
pip install -r requirements.txt
```


# Utilisation :
Assurez vous que le programme est dans votre répertoire puis ajoutez
```python
from whatsapp_api import Whatsapp # Bien penser à mettre whatsapp_api dans le même répertoire que votre programme
```

Pour initier le programme faites ensuite
```python
what = Whatsapp()
```

Il y a trois paramètres optionnels pour la classe Whatsapp : service, headless

Le paramètre service sert à insérer le chemin vers le geckodriver (disponible ici :https://github.com/mozilla/geckodriver/releases) si besoin (j'en ai eu besoin seulement sur mon raspberry pi)

Le paramètre headless (par défaut sur False) vous permet, s'il est mis sur True, de lancer votre code sans ouvrir de fenêtre firefox.
***Je vous conseille néanmoins de le mettre sur False pour tester et débugger votre code afin de voir ce qui se passe (et aussi de vous connecter avec votre qr code)***


Avant d'envoyer et lire les messages, vous devez sélectionner le contact :
```python
what.go_to("Numéro de téléphone ou nom de contact/groupe") # Vous pouvez tester avec la fonction recherche de whatsapp sur votre téléphone pour savoir si cela va marcher
```
Si vous mettez "unread" à la place d'un numéro de téléphone, cela ira dans les messages non lus (cette fonction est en cours de développement)

Pour lire le dernier message du contact/groupe sélectionné précedemment (y compris les votres) :
```python
message = what.read_last_messages()
```

Et pour envoyer un message (au contact sélectionné) :
```python
what.send_message("votre message")
```

Pour finir pour fermer "proprement" le programme if faut faire :
```python
what.quit()
```

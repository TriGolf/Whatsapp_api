# Whatsapp_api
Une api pour whatsapp

# Dépendances :

Sélénium et pyperclip
```
pip install selenium
pip install pyperclip
```
Sur linux, vous faudra peut être aussi installer xclip et redémarrer votre ordinateur
```
sudo apt install xclip
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

Il y a trois paramètres optionnels pour la classe Whatsapp : service, headless et control_key

Le paramètre service sert à insérer le chemin vers le geckodriver (disponible ici :https://github.com/mozilla/geckodriver/releases) si besoin (j'en ai eu besoin seulement sur mon raspberry pi

Le paramètre headless (par défaut sur False) vous permet, s'il est mis sur True, de lancer votre code sans ouvrir de fenêtre firefox.
***Je vous conseille néanmoins de le mettre sur False pour tester et débugger votre code afin de voir ce qui se passe***

Le paramètre control_key (par défaut sur "CONTROL") sert à définir la touche pour faire le controle+v (Changez à "COMMAND" si vous êtes sur mac)

Avant d'envoyer et lire les messages, vous devez sélectionner le contact :
```python
what.select("Numéro de téléphone ou nom de contact/groupe") # Vous pouvez tester avec la fonction recherche de whatsapp sur votre téléphone pour savoir si cela va marcher
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

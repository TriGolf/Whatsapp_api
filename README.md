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
import whatsapp_api
```

Pour initier le programme faites ensuite
```python
what = Whatsapp(service=None,headless=True")
```

Notez que dans certains cas il faut installer le geckodriver disponible ici : https://github.com/mozilla/geckodriver/releases et mettre son lien dans le paramètre *service*.

Le paramètre headless vous permet, s'il est mis sur True, de ne pas lançer de fenêtre.
***Je vous conseille néanmoins de le mettre sur False pour tester et débugger votre code afin de voir ce qui se passe***

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

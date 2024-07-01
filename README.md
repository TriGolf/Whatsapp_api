# Whatsapp_api
Une api pour whatsapp

# Dépendances :

Sélénium et pyperclip
```
pip install selenium
pip install pyperclip
```

# Utilisation :
Assurez vous que le programme est dans votre répertoire puis ajoutez
```python
import whatsapp_api
```

Pour initier le programme faites ensuite
```python
what = Whatsapp(service=None,profile="Path/to/firefox/profile,headless=True")
```
Notez qu'il faut créer un profile firefox avant (dans firefox tapez about:profiles, créez un profile pour whatsapp, lançez le dans une nouvelle fenêtre, allez sur web.whatsapp.com et connctez vous avec le QR code) ***Attention*** quand vous créez un nouveau profile firefox, il faut penser à remettre le profile "default" par défaut

Notez que dans certains cas il faut installer le geckodriver disponible ici : https://github.com/mozilla/geckodriver/releases et mettre son lien dans service.

Le paramètre headless vous permet, s'il est mis sur True, de ne pas lançer de fenêtre.
***Je vous conseille néanmoins de le mettre sur False pour tester et débugger votre code afin de voir ce qui se passe***

Avant d'envoyer et lire les messages, vous devez sélectionner le contact :
```python
what.select("Numéro de téléphone ou nom de contact/groupe") # Vous pouvez tester avec la fonction recherche de whatsapp sur votre téléphone pour savoir si cela va marcher
```

Pour lire le dernier message d'un contact/groupe (y compris les votres) :
```python
message = what.read_last_messages()
```

Et pour envoyer un message :
```python
what.send_message("votre message")
```

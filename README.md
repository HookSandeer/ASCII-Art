# Convertisseur ASCII-ART pour windows :

## C'est quoi ?

Le convertisseur d'image en ASCII-ART est un programme qui convertis, après redimmension, <br>
chaque pixel de l'image en une lettre plus ou moins imposante, qui reprend la couleur original du pixel.<br><br>

## Exemple :
[Image original](https://github.com/HookSandeer/ASCII-Art/blob/main/Asset/before.jpg "photo")
[Image après convertion](https://github.com/HookSandeer/ASCII-Art/blob/main/Asset/after.png "photo")
## Comment ça fonctionne ?

__Le fonctionnement du programme est très simple, voici comment procéder :__
<br>
<br>
- Lancer le programme, soit le fichier python, ou alors l'executable windows
- Choisir une image, et l'ouvrir dans le programme
    - L'image doit être au format JPEG (.jpg)
    - Si l'image est trop petite, le rendu sera petit
- Vous pouvez soit afficher l'image, soit l'enregister en format .png

## Comment l'installer ?

__Il suffit de télécharger la dernière version [ici](https://github.com/HookSandeer/ASCII-Art/releases), et de lancer l'application.__
<br>
<br>
Si vous souhaitez executer via le code python, il faut :
- Un interpreteur python sur votre machine (Téléchargeable [ici](https://www.python.org/downloads/))
- Verifier que le module Tkinter soit installer (normalement le cas sur toute les machines)
- Vérifier que le module Pillow (pour le traitement d'image) soit installer
    - Pour l'installer : ouvrir un terminal (comme powershell) et entrer la commande suivante :


```$ pip install pillow```
<br>
<br>
<br>
__Une fois les modules installés, il suffit d'executer le code python :__
<br>
- Soit via : 
    - L'explorateur de fichier : clique droit -> ouvrir avec -> python
    - Un terminal (Attention d'être dans le dossier que le script) :


```$ python ./main.py```
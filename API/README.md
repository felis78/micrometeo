## Installation de l'api sur environnement Linux/Ubuntu:

### Installer mariadb:

```
sudo apt install mariadb-server
sudo apt install libmariadb3 libmariadb-dev
```


### Installer python:

```
$ sudo apt install python3
$ sudo apt install python3.10-venv
$ sudo apt install pip3
```

### Installer l'environnement Python

1. se placer dans le dossier API:
   
```
$ cd API
```

2. créer un environnement virtuel:

```
$ python3 -m venv /venv
```

### Installation des dépendances du projet:

1. Activer l'environnement python:
   
```
$ source venv/bin/activate
```

2.Installer les dépendences:

```
$ pip3 -r requirements.txt
```

### Activation de l'api (mode dev):

```
$ python app.py
```

### Commandes supplémentaires:

Pour stopper l'api: Ctrl + C
Pour quitter désactiver l'environnement python:
```
$ deactivate
```


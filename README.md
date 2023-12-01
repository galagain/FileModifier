# File Modifier

## Problématique

L'objectif du programme "main.py" est de résoudre un problème rencontré dans un fichier CSV ou texte, illustré par l'exemple suivant (example.txt). La colonne C contient des ";" qui sont également des séparateurs.

### Exemple d'origine (example.txt) :
```
A;		B;		C;		D;		E
valeur1;	valeur2;	va;leur3;	valeur4;	valeur5
valeur6;	valeur7;	v;ale;ur8;	valeur9;	valeur10
valeur11;	valeur12;	valeur13;	valeur14;	valeur15
```

Le fichier résultant souhaité doit ressembler à ceci, sans ";" autre que pour les séparations.

### Exemple modifié :
```
A;		B;		C;		D;		E
valeur1;	valeur2;	va,leur3;	valeur4;	valeur5
valeur6;	valeur7;	v,ale,ur8;	valeur9;	valeur10
valeur11;	valeur12;	valeur13;	valeur14;	valeur15
```

## Utilisation
Le programme Python "main.py" résout ce problème en remplaçant les ";" dans une colonne spécifiée. Pour utiliser le script, les paramètres suivants doivent être spécifiés lors de l'exécution :

- file_path: Le chemin vers le fichier d'origine (exemple: "example.txt").
- separator: Le séparateur utilisé pour diviser les colonnes dans le fichier (exemple: ";").
- column: Le nom de la colonne à modifier (exemple: "C").
- replace: Le texte de remplacement à utiliser pour modifier la colonne spécifiée (exemple: ",").
- result_name: Le nom du fichier résultant après les modifications (exemple: "result.txt").

Ces paramètres peuvent être spécifiés en exécutant le script Python. Aucune librairie externe n'est nécessaire, car argparse et csv sont des librairies standard incluses par défaut dans Python.

### Exemple d'exécution :
```bash
python main.py "example.txt" --separator ";" --column "C" --replace "," --result_name result.txt
```

Dans le cas présent, les paramètres nécessaires sont les suivants.

### Exemple minimale d'exécution :
```bash
python main.py "example.txt" --column "C"
```

Le fichier main.py est fourni ci-dessus avec la documentation des paramètres et la logique de traitement du fichier.

## Version graphique

Le fichier gmain.py offre une interface graphique pour utiliser l'application sans avoir à recourir à la ligne de commande. L'interface graphique est créée exclusivement à l'aide de Tkinter.

La classe FileModifierApp() facilite l'intégration du fichier précédent dans une application graphique conviviale.

Pour utiliser cette version graphique, il est nécessaire d'installer Tkinter sur la machine où l'interpréteur Python est exécuté. Cela peut être réalisé avec pip, en utilisant la méthode suivante :

Avec pip :
```bash
pip install tk
```

Ou avec poetry :
```bash
poetry add tk
```


Pour distribuer l'application sous forme d'exécutable, les étapes suivantes sont nécessaires :

1) Installer la bibliothèque permettant de transformer le programme Python en un exécutable :

```bash
pip install pyinstaller
```

2) Créer l'exécutable avec la commande :

```bash
pyinstaller --onefile gmain.py
```

Cela générera un exécutable autonome qui peut être utilisé sur n'importe quelle machine, même celles qui ne possèdent pas d'installation Python.

L'exécutable se trouvera dans le dossier dist/ et sera nommé gmain.exe.
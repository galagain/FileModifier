import argparse
import csv


def process_file(file_path, separator, column, replace, result_name):
    """
    Modifie un fichier CSV en remplaçant les valeurs d'une colonne spécifiée.

    Ce script prend en entrée un fichier CSV (.csv) ou un fichier TEXTE (.txt)

    :param file_path: Le chemin vers le fichier d'origine (exemple: "example.txt")
    :param separator: Le séparateur utilisé pour diviser les colonnes dans le fichier (exemple: ";")
    :param column: Le nom de la colonne à modifier (exemple: "C")
    :param replace: Le texte de remplacement à utiliser pour modifier la colonne spécifiée (exemple: ",")
    :param result_name: Le nom du fichier résultant après les modifications (exemple: "result.txt")
    :return: True si le processus est terminé avec succès
    """

    # Ouvrir le fichier CSV/TXT en mode lecture ('r')
    with open(file_path, 'r') as fichier:
        # Initialiser la variable colonne à None
        colonne = None

        # Parcourir les lignes du fichier
        for ligne in fichier:
            # Diviser la ligne en utilisant le séparateur et supprimer les espaces autour
            colonne = ligne.strip().split(separator)

            # Sortir de la boucle après la première ligne (pour obtenir les en-têtes)
            break

    # Nettoyer les noms de colonnes en enlevant les caractères spéciaux
    colonne_propre = [nom_colonne.strip('\t') for nom_colonne in colonne]

    # Obtenir l'indice de la colonne spécifiée (celle qui a potentiellement des séparateurs)
    idx = colonne_propre.index(column)

    # Initialiser une liste vide pour stocker les lignes modifiées
    result = []

    # Ouvrir à nouveau le fichier CSV en mode lecture ('r')
    with open(file_path, 'r') as fichier:
        # Parcourir les lignes du fichier
        for ligne in fichier:
            # Initialiser une liste temporaire pour stocker les parties de la ligne
            temp = []

            # Diviser la ligne en utilisant le séparateur et prendre les parties avant l'indice spécifié
            temp += ligne.strip().split(separator)[:idx]

            # Ajouter la partie de la ligne entre l'indice spécifié et le reste des colonnes modifiées avec le remplacement
            temp += [replace.join(ligne.strip().split(separator)[idx:-(len(colonne) - idx) + 1])]

            # Ajouter le reste des colonnes non modifiées à la liste temporaire
            temp += ligne.strip().split(separator)[-(len(colonne) - idx) + 1:]

            # Ajouter la liste temporaire à la liste résultante
            result.append(temp)

    # Ouvrir un nouveau fichier CSV/TXT en mode écriture ('w') pour sauvegarder les résultats
    with open(result_name, 'w', newline='') as fichier_csv:
        # Créer un objet writer avec le délimiteur spécifié
        writer = csv.writer(fichier_csv, delimiter=separator)

        # Écrire chaque ligne de la liste résultante dans le nouveau fichier CSV
        for ligne in result:
            writer.writerow(ligne)

    # Afficher un message indiquant que le processus est terminé
    print("Terminé", "Le fichier " + result_name + " a été généré avec succès!")
    return True


if __name__ == "__main__":
    # Configuration de l'analyseur d'arguments en ligne de commande
    parser = argparse.ArgumentParser(
        description="Modifie un fichier CSV en remplaçant les valeurs d'une colonne spécifiée.")

    # Ajout des arguments à l'analyseur
    parser.add_argument("file_path",
                        help="Le chemin vers le fichier d'origine (exemple: 'example.txt')")
    parser.add_argument("--separator",
                        default=";",
                        help="Le séparateur utilisé pour diviser les colonnes dans le fichier (exemple: ';')")
    parser.add_argument("--column",
                        help="Le nom de la colonne à modifier (exemple: 'C')")
    parser.add_argument("--replace",
                        default=",",
                        help="Le texte de remplacement à utiliser pour modifier la colonne spécifiée (exemple: ',')")
    parser.add_argument("--result_name",
                        default="result.txt",
                        help="Le nom du fichier résultant après les modifications (exemple: 'result.txt')")

    # Analyse des arguments de la ligne de commande
    args = parser.parse_args()

    # Appel de la fonction avec les arguments de la ligne de commande
    process_file(args.file_path, args.separator, args.column, args.replace, args.result_name)

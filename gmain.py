import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Importation de la fonction process_file depuis le fichier main.py
from main import process_file


class FileModifierApp:
    def __init__(self, master):
        """
        Initialise l'application GUI pour modifier un fichier CSV/TXT.

        Paramètres :
        - master (tk.Tk) : La fenêtre principale de l'application.
        """
        self.master = master
        master.title("File Modifier")

        # Affiche un message de bienvenue
        self.intro_label = tk.Label(master,
                                    text="Bienvenue dans l'application File Modifier! \n Si une colonne contient le "
                                         "séparateur du CSV/TXT, celui-ci sera remplacé par la valeur souhaitée.")
        self.intro_label.grid(row=0, column=0, columnspan=3, pady=(20, 20))

        # Configuration des widgets pour le chemin du fichier d'entrée
        self.setup_file_input()

        # Configuration des widgets pour spécifier la colonne à modifier
        self.setup_column_input()

        # Configuration des widgets pour spécifier le séparateur
        self.setup_separator_input()

        # Configuration des widgets pour spécifier le texte de remplacement
        self.setup_replace_input()

        # Configuration des widgets pour spécifier le nom du fichier généré
        self.setup_result_name_input()

        # Bouton pour déclencher le processus de modification du fichier
        self.btn_process = tk.Button(master, text="Modifier le fichier", command=self.process_file)
        self.btn_process.grid(row=6, column=1)

    def setup_file_input(self):
        """
        Configure les widgets liés au chemin du fichier d'entrée.
        """
        self.csv_text = tk.Label(self.master, text="Chemin du fichier CSV/TXT à traiter :")
        self.csv_text.grid(row=1, column=0, sticky=tk.E)
        self.csv_file = tk.Entry(self.master)
        self.csv_file.grid(row=1, column=1)
        self.btn_browse = tk.Button(self.master, text="Parcourir", command=self.browse_file)
        self.btn_browse.grid(row=1, column=2)

    def setup_column_input(self):
        """
        Configure les widgets pour spécifier la colonne à modifier.
        """
        self.column_text = tk.Label(self.master, text="Nom de la colonne à modifier :")
        self.column_text.grid(row=2, column=0, sticky=tk.E)
        self.column = tk.Entry(self.master)
        self.column.grid(row=2, column=1)

    def setup_separator_input(self):
        """
        Configure les widgets pour spécifier le séparateur.
        """
        self.separator_text = tk.Label(self.master, text="Séparateur :")
        self.separator_text.grid(row=3, column=0, sticky=tk.E)
        self.separator = tk.Entry(self.master)
        self.separator.grid(row=3, column=1)
        self.separator.insert(0, ";")

    def setup_replace_input(self):
        """
        Configure les widgets pour spécifier le texte de remplacement.
        """
        self.replace_text = tk.Label(self.master, text="Si le séparateur est dans la colonne, on le remplace par :")
        self.replace_text.grid(row=4, column=0, sticky=tk.E)
        self.replace = tk.Entry(self.master)
        self.replace.grid(row=4, column=1)
        self.replace.insert(0, ",")

    def setup_result_name_input(self):
        """
        Configure les widgets pour spécifier le nom du fichier généré.
        """
        self.result_name_text = tk.Label(self.master, text="Nom du fichier généré :")
        self.result_name_text.grid(row=5, column=0, sticky=tk.E)
        self.result_name = tk.Entry(self.master)
        self.result_name.grid(row=5, column=1)
        self.result_name.insert(0, "result.txt")

    def browse_file(self):
        """
        Ouvre une boîte de dialogue pour choisir un fichier CSV.
        Met à jour le champ d'entrée du fichier avec le chemin choisi.
        """
        file_path = filedialog.askopenfilename()
        if file_path:
            self.csv_file.delete(0, tk.END)
            self.csv_file.insert(0, file_path)

    def process_file(self):
        """
        Traite le fichier CSV en remplaçant le séparateur dans une colonne donnée.
        Génère un nouveau fichier CSV avec les modifications.
        Affiche une boîte de dialogue d'information lorsque l'opération est terminée.
        """
        # Appelle la fonction process_file avec les paramètres spécifiés
        process_file(
            file_path=self.csv_file.get(),
            separator=self.separator.get(),
            column=self.column.get(),
            replace=self.replace.get(),
            result_name=self.result_name.get()
        )

        # Affiche un message de fin
        messagebox.showinfo("Terminé", "Le fichier " + self.result_name.get() + " a été généré avec succès!")


# Point d'entrée pour l'application
if __name__ == "__main__":
    # Crée la fenêtre principale Tkinter
    root = tk.Tk()
    root.geometry("600x400")  # Définit la taille initiale de la fenêtre
    app = FileModifierApp(root)
    root.mainloop()  # Lance la boucle d'événements Tkinter

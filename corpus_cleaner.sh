#!/bin/bash

# Vérifie si le nombre d'arguments est égal à 1 (le nom du fichier d'entrée)
if [ "$#" -ne 1 ]; then
    echo "Utilisation : $0 <nom_fichier>"
    exit 1
fi

# Vérifie si le fichier d'entrée existe
if [ ! -f "$1" ]; then
    echo "Le fichier $1 n'existe pas."
    exit 1
fi

# Nom du fichier d'entrée
fichier_entree="$1"

# Nom du fichier de sortie
fichier_sortie="${fichier_entree%.txt}_nettoye.txt"

# Appliquer les opérations de nettoyage sur le fichier
sed 's/[^[:alnum:] ]/ /g' "$fichier_entree" | tr '\n' ' ' | tr -s ' ' | tr '[:upper:]' '[:lower:]' > "$fichier_sortie"

echo "Le texte a été nettoyé et enregistré dans $fichier_sortie."


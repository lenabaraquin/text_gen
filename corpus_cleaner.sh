#!/bin/bash

# Vérifie si le nombre d'arguments est égal à 1 (le nom du fichier)
if [ "$#" -ne 1 ]; then
    echo "Utilisation : $0 <nom_fichier>"
    exit 1
fi

# Vérifie si le fichier existe
if [ ! -f "$1" ]; then
    echo "Le fichier $1 n'existe pas."
    exit 1
fi

# Nom du fichier d'entrée
fichier_entree="$1"

# Nom du fichier de sortie
fichier_sortie="${fichier_entree%.txt}.txt"

# Utilise la commande 'sed' pour supprimer les caractères non alphanumériques
sed "s/[^[:alnum:]' ]//g" "$fichier_entree" > "$fichier_sortie"
#sed "s/\n/ /g" "$fichier_sortie" > "$fichier_sortie"
#sed "s/ \+/ /g" "$fichier_sortie" > "$fichier_sortie"

echo "Le texte a été nettoyé et enregistré dans $fichier_sortie."

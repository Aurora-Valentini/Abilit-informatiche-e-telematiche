#!/bin/bash

# Inserire il percorso della cartella
echo "Inserire il percorso della cartella da analizzare:"
read dir_path

# Per verificare creo io dei file e directories di prova.
# Utilizzo un ciclo for che crea 5 files di prova.
for i in {1..5}
do
    touch "prova_file$i.txt"  
done
echo " Sono stati creati 5 files di prova"

# Utilizzo un ciclo for che crea 3 directories di prova.
for i in {1..3}
do
    mkdir "prova_cartella$i.txt"  
   
done
echo " Sono state create 3 directories di prova"


# Verifico se la cartella esiste e analizzo il contenuto
if [ -d "$dir_path" ]; then
    echo "La cartella '$dir_path' esiste. Il contenuto è il seguente:"
    
    # Entro nella cartella
    cd "$dir_path"
    
    # Listo solo i file regolari (non vuoti)
    # Uso -maxdepth 1 perchè altrimenti l'opzione find andrà a cercare anche nelle sottodirectory contenute
    # nella directory che sto analizzando.

    echo -e "\nFile regolari (non vuoti):"
    find . -maxdepth 1 -type f -size +0  
    
    # 2. Lista solo i file vuoti
    echo -e "\nFile vuoti:"
    find . -maxdepth 1 -type f -size 0 
    
    
    # Listo solo le directory
    # Uso ls per elencare il contenuto della directory
    # L'opzione -p aggiunge / ai nomi delle directory, con grep filtro solo le directory
    echo -e "\nDirectory:"
    ls -p | grep '/'  
    
else
    echo "Errore: La cartella '$dir_path' non esiste."
fi





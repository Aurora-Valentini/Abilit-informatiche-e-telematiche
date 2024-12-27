#!/bin/bash

# Definisco la funzione file_count

file_count() {
    local dir=$1  # Primo argomento: percorso della directory
    if [ -d "$dir" ]; then
        # Uso ls per elencare il contenuto della directory
        # L'opzione -p aggiunge / ai nomi delle directory
        local lista_contenuti=$(ls -p "$dir")
        
        # Filtro con grep i risultati escludendo le directory 
        local lista_file=$(echo "$lista_contenuti" | grep -v '/$')
        
        # Tramite wc conto il numero di righe 
        local numero=$(echo "$lista_file" | wc -l)
        
        # Stampo il risultato
        echo "La directory '$dir' contiene $numero file."
    else
        echo "Errore: '$dir' non è una directory valida."
    fi
}

# Utilizzo un ciclo for che crea 5 file vuoti e 3 dummy directories. 
for i in {1..5}
do
    touch "dummy_file$i.txt"  
done
echo " Sono stati creati 5 dummy files"

for i in {1..3}
do
    mkdir "dummy_cartella$i.txt"  
   
done
echo " Sono state create 3 dummy directories"


# Voglio che il percorso della directory su cui usare la fuznione venga dato come input dall'esecutore 
if [ $# -eq 0 ]; then
    echo "Inserire il percorso della directory su cui usare file_count:"
    read path_directory  
else
    path_directory=$1  # Se l'argomento è fornito, usalo
fi

# Ho utilizzato la funzione nella stessa cartella in cui ho creato dummy files e dummy directories per verificare.

# Chiamo infine la funzione con il percorso
file_count "$path_directory"



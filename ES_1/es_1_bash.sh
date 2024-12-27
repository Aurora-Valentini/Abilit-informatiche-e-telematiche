#!/bin/bash

# Utilizzo un ciclo for che crea 5 file vuoti. 
#Scrive anche su terminal che i file sono stati creati correttamente.
for i in {1..5}
do
    touch "prova$i.txt"  
    echo "File prova$i.txt creato."
done

# Creo un array vuoto che riempirò con i file precedenti
array_prove=()

# Faccio un ciclo per mettere i file nell'array
for i in {1..5}
do
    nome_prova="prova$i.txt"  
    array_prove+=("$nome_prova")
done

# Controllo se l'array è vuoto,ossia verifico se la lunghezza dell'array è zero.
# Sappiamo già che non lo è quindi faccio stampare i nomi di tutti i file che contiene come output.
if [ ${#array_prove[@]} -eq 0 ]; then
    echo "L'array è vuoto."
else
    echo "I file nell'array sono:"
    for file in "${array_prove[@]}"; do
        echo "$file"
    done
fi

# Ora modifico i nomi dei file, facendoli precedere dalla data odierna.
# Ottengo la data corrente nel formato YYYY-MM-DD

data_oggi=$(date +%F)

# Faccio un ciclo per rinominare ogni file nell'array
for file in "${array_prove[@]}"; do

        # Creo il nuovo nome del file con la data 
        new_filename="${data_oggi}_$file"
        
        # Rinomino il file
        mv "$file" "$new_filename"
        
        # Stampo il nuovo nome del file
        echo "Il file '$file' è stato rinominato in '$new_filename'."

done




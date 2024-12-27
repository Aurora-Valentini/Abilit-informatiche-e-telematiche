#!/bin/bash

# Definisco il nome del mio file
file="numeri_es5.txt"

# Creo un file vuoto
> "$file"

# Scrivo con un ciclo for i primi 10 numeri interi in colonna
for i in {1..10}; do
    echo "$i" >> "$file"  
done

# Faccio scrivere al terminale che i numeri sono stati correttamente scritti.
echo "Numeri scritti in $file"

# Faccio la somma di tutti i numeri della prima colonna (l'unica)
awk '{ sum += $1 } END { print "Somma:", sum}' numeri_es5.txt

# Applico la formula di sommazione di Gauss per verificare
n=10
sum_gauss=$(( n * (n + 1) / 2 ))

echo "Somma con Gauss: $sum_gauss"

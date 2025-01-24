# Abilita_informatiche_telematiche
In questa pagina repository ho caricato i file necessari per sostenere l'esame di abilità informatiche e telematiche.
Ho deciso di svolgere gli esercizi di Bash numero 1,3,5 e 8. Ogni script si trova nella specifica cartella. 
Si noti che per gli esercizi 3 e 8 è richiesta l’immissione da terminale della directory da analizzare. 
Io ho utilizzato proprio la cartella in cui è presente lo script dell’esercizio. Per verificare ho creato anche file e directory aggiuntive in suddetta cartella. 

Per il programma in Python ho deciso di salvare le immagini dei grafici ottenuti in una cartella su desktop chiamata "Grafici_ESAME".
Nel terminale ho fatto printare delle informazioni utili per fare delle verifiche nel programma e per risolvere punti particolari dell'esercizio 
(ad es. per trovare la struttura più massiccia nel set di dati, risultati dei fit, media e mediana).

Commenti sull'esercizio in Python:
- Per il pt.1  ho notato che era meglio utilizzare la scala log-log (grafico_1a). Per fare il fit ho calcolato il logaritmo dei dati lasciando invariata la scala degli assi, ho fatto un fit lineare sfruttando la funzionalita di python chiamata numpy.polyfit. Il risultato ottenuto non è un buon fit (grafico_1b).

- Per il pt.2 ho rappresentato la massa totale in funzione della distanza sia in scala log-lineare (grafico_2a) sia in scala log-log (grafico_2b), credo che quest'ultima permetta di studiare meglio  la distribuzione.

- Per il pt.3 ho creato un istogramma della distribuzione di materia oscura negli aloni (grafico_3). La retta rossa tratteggiata rappresenta la media mentre quella blu la mediana come riportato in legenda. L'asse dei conteggi è in scala logatirmica perchè riscalando in questo modo è meglio visibile la distibuzione. Per ottenere un grafico migliore visivamente ho scartato 4 aloni ossia quelli con masse maggiori di 1.5 * 10^10 M_sun/h.
  
- Per il pt.4 ho creato prima 2 pannelli affiancati con le distibuzione degli aloni proiettate rispettivamente nei piani x-y e z-y (grafico_4a). Poi ho aggiunto un pannello in basso a sinistra con il piano x-z. In questi pannelli il colore nei punti è codificato dal logaritmo in base 10 della massa del gas mentre la dimensione dei punti scala con la massa stellare (grafico_5b).

- Per il pt.5 ho cercato la relazione tra massa del buco nero e massa stellare in scala log-log (grafico_5a). Come fatto al pt.1 ho fatto il logaritmo dei dati per poi fare un fit lineare. Questa volta il fit ottenuto sembra essere in buon accordo con i dati (grafico_5b).

- Per il pt.6 ho creato un istogramma cumulativo. Ho cercato i 5 aloni con massa del gas maggiore e ho calcolato la distanza di questi aloni massivi da tutti gli altri. L'istogramma ottenuto è la somma di 5 istogrammi (grafico_6).

Spero che gli esercizi siano abbastanza chiari.


"""
Creato per l'esame di abilità informatiche e telematiche
@author: auroravalentini
"""
#Importo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt

#Definisco una funzione che legge le colonne del file in input
def leggi_colonne(file_path):
    
    #Inizializzo le variabili
    m_tot = []
    m_gas = []
    m_dm = []
    m_star = []
    m_bh= []
    pos_x= []
    pos_y= []
    pos_z= []
    
    with open(file_path, 'r') as file:
        # Salto la lettura della prima riga (header)
        header = file.readline() 
        for line in file:
            # Legge una colonna alla volta
            col0 = line.strip().split()[0]     
            col1 = line.strip().split()[1]     
            col2 = line.strip().split()[2]
            col3 = line.strip().split()[3]
            col4 = line.strip().split()[4]
            col5 = line.strip().split()[5]
            col6 = line.strip().split()[6]
            col7 = line.strip().split()[7]
            
            m_tot.append(float(col0))
            m_gas.append(float(col1))
            m_dm.append(float(col2))
            m_star.append(float(col3))
            m_bh.append(float(col4))
            pos_x.append(float(col5))
            pos_y.append(float(col6))
            pos_z.append(float(col7))

            
    return m_tot, m_gas, m_dm, m_star, m_bh, pos_x, pos_y, pos_z


# Percorso del file di input
input_file = "file2_Groups_AGN-wWU_500Mpc_Data.txt"

# Leggo i dati dal file di input
m_tot, m_gas, m_dm, m_star, m_bh, pos_x, pos_y, pos_z = leggi_colonne(input_file)


#Trasformo le liste in array
m_tot_arr = np.array(m_tot)
m_gas_arr = np.array(m_gas)
m_dm_arr = np.array(m_dm)
m_star_arr = np.array(m_star)
m_bh_arr = np.array(m_bh)
pos_x_arr = np.array(pos_x)
pos_y_arr = np.array(pos_y)
pos_z_arr = np.array(pos_z)

# Creo un unico array con tutti i dati e faccio il trasposto in modo da averli in colonna
matrix_tot = np.array([m_tot_arr, m_gas_arr, m_dm_arr, m_star_arr, m_bh_arr, pos_x_arr, pos_y_arr, pos_z_arr])
matrix_tot = matrix_tot.T


#---------------------------PUNTO 1-----------------------------

# Calcolo la massa barionica
m_bar= np.sum(matrix_tot[:, [1,3]], axis=1)

#Converto il risultato in un array
m_bar_arr= np.array(m_bar)

#Faccio un plot della DM mass di ogni alone (asse y) in funzione della massa barionica (asse x)
folder_path = "/Users/auroravalentini/desktop/ESAME_AB_INF/es_python/grafici"
file_name1a = "Grafico_1a.png"
file_path1a = folder_path + "/" + file_name1a

# Dal grafico successivo in scala lineare non ottengo un buon risultato.
# plt.figure()  
# plt.xlabel('  (Baryonic mass $[M_\odot/h]$)',fontsize=12)
# plt.ylabel('  (DM mass $[M_\odot/h]$)',fontsize=12)
# plt.plot(m_bar_arr, m_dm_arr, marker='o', linestyle='',color= 'blue', markersize=2.5)
# plt.savefig(file_path1, dpi=300, bbox_inches='tight')
# plt.close()

#Passo in scala log-log.

plt.figure()  
plt.xlabel(' Baryonic mass $[10^{10} M_\odot/h]$',fontsize=12)
plt.ylabel(' DM mass $[10^{10} M_\odot/h]$',fontsize=12)
plt.xscale('log')             
plt.yscale('log') 
plt.title('Log-log scale')
plt.plot(m_bar_arr, m_dm_arr, marker='o', linestyle='', markersize=2.5, alpha=0.5)
plt.savefig(file_path1a, dpi=300, bbox_inches='tight')
plt.close()


# Provando a fare il fit mi sono accorta che è comparso un errore di runtime
# Stavo dividendo per zero quindi il fit non riusciva a convergere
# Trovo gli indici degli zeri
#zeros = np.where(m_bar_arr == 0)

# Indici degli zeri
#print("Indici degli zeri:", zeros[0])  

# Rimuovo i dati dove la massa è uguale a zero
mask = m_bar_arr != 0
m_bar_filtered = m_bar_arr[mask]
m_dm_filtered = m_dm_arr[mask]


# Faccio un fit lineare di grado 1. Devo calcolare pendenza e intercetta.
# Per fare ciò uso una funzionalità intrinseca chiamata np.polyfit.
# Sono passata in scala logaritmica quindi per fare il fit sui dati ne calcolo il log

log_m_bar= np.log10(m_bar_filtered)
log_m_dm= np.log10(m_dm_filtered)

coeff = np.polyfit(log_m_bar, log_m_dm, 1)
pendenza= coeff[0]
intercetta= coeff[1]

print(f"Pendenza fit: {pendenza}")
print(f"Intercetta fit: {intercetta}")

# Calcolo i valori di y previsti dalla retta
y_fit = log_m_bar*pendenza + intercetta


# Ottengo: 
# Pendenza: 0.392
# Intercetta: -0.303

file_name1b = "Grafico_1b.png"
file_path1b = folder_path + "/" + file_name1b

#Ora la scala sarà lineare poichè ho già fatto il log dei dati
plt.figure()
plt.plot(log_m_bar, log_m_dm, marker='o', linestyle='', markersize=2.5, label= 'Dati', alpha=0.5)
plt.plot(log_m_bar, y_fit, color='red', label='Fit lineare: y = {:.2f}x  {:.2f}'.format(pendenza, intercetta))
plt.xlabel(' log (Baryonic mass $[10^{10} M_\odot/h]^{-1}$)',fontsize=12)
plt.ylabel(' log (DM mass $[10^{10} M_\odot/h]^{-1}$)',fontsize=12)
plt.title('Fit lineare')
plt.legend()
plt.savefig(file_path1b, dpi=300, bbox_inches='tight')
plt.close()

#---------------------------PUNTO 2-----------------------------
mass_max= np.max(m_tot_arr)

# Cerco la struttura con massa totale maggiore
print('Massa della stuttura più massiva:',mass_max, '10^{10} M_\odot/h')
print('La struttura più massiccia è la numero:', np.where(m_tot_arr==mass_max))

#Ho scoperto che la struttura più massiva è la prima di tutto il mio array
#Estrapolo le posizioni x,y,z della struttura più massiva:
    
#prima_riga=matrix_tot[0,:]
#print(prima_riga)    

x_max1=matrix_tot[0,5] 
y_max1=matrix_tot[0,6]
z_max1=matrix_tot[0,7]


print("Posizione x della struttura più massiccia:", x_max1)
print("Posizione y della struttura più massiccia:", y_max1)
print("Posizione z della struttura più massiccia:", z_max1)



#Ora calcolo la distanza euclidea, devo fare un ciclo if
#Verifico la dimensione del mio array totale per capire su quali indici 
#far girare il ciclo 
 
#dim_tot= np.shape(matrix_tot)
#print("Dimensioni array totale",dim_tot)
#Ottengo un array di 456 righe e 8 colonne OK

# Creo  array vuoti da riempire
dist_tot= np.zeros(456)
dist_x= np.zeros(456)
dist_y= np.zeros(456)
dist_z= np.zeros(456)

for i in range(456):
  dist_x[i]= (x_max1-pos_x_arr[i])**2 
  dist_y[i]= (y_max1-pos_y_arr[i])**2 
  dist_z[i]= (z_max1-pos_z_arr[i])**2
 
  dist_tot[i]= np.sqrt(dist_x[i]+dist_y[i]+dist_z[i])
 
    
#Faccio un plot di x=dist_tot versus y=m_tot

file_name2a = "Grafico_2a.png"
file_path2a = folder_path + "/" + file_name2a

plt.figure()  
plt.ylabel('$ Mass[10^{10} M_\odot/h]$',fontsize=12)
plt.xlabel('$ Distance (ckpc/h)$',fontsize=12)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
plt.plot(dist_tot, m_tot_arr, marker='o', linestyle='',markersize=2.5, alpha=0.5)
#plt.xscale('log')             
plt.yscale('log') 
plt.title("Log-linear scale")
plt.savefig(file_path2a, dpi=300, bbox_inches='tight')
plt.close()

file_name2b = "Grafico_2b.png"
file_path2b = folder_path + "/" + file_name2b

plt.figure()  
plt.ylabel('$ Mass[10^{10} M_\odot/h]$',fontsize=12)
plt.xlabel('$ Distance (ckpc/h)$',fontsize=12)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
plt.plot(dist_tot, m_tot_arr, marker='o', linestyle='',markersize=2.5, alpha=0.5)
plt.xscale('log')             
plt.yscale('log') 
plt.title("Log-log scale")
plt.savefig(file_path2b, dpi=300, bbox_inches='tight')
plt.close()

#---------------------------PUNTO 3-----------------------------
#Per ottenere un grafico più significativo scarto i valori più grandi di masse
m_dm_piccoli= m_dm_arr[(m_dm_arr < 1.5)]

#print(m_dm_piccoli.shape)
# Vedo dalla dimensione dell'array che ho 452 masse < 1.5 quindi ne ho scartate 456-452= 4

#Calcolo media e mediana su tutto l'array di masse di DM

media = np.mean(m_dm_arr)
mediana = np.median(m_dm_arr)

print(f"Media DM mass: {media}")
print(f"Mediana DM mass: {mediana}")


file_name3 = "Grafico_3.png"
file_path3 = folder_path + "/" + file_name3

# Creo un istogramma delle masse di materia oscura
plt.figure()
plt.hist(m_dm_piccoli, bins=30, edgecolor='black', alpha=0.4, log=True, label='Dati')
plt.xlabel('$Mass[10^{10} M_\odot/h]$', fontsize=13)
plt.ylabel('Counts', fontsize=13)

# Aggiunta della linea verticale per la media
plt.axvline(media, color='red', linestyle='dashed', linewidth=1.5, label=f'Media: {media:.2f}')

# Aggiunta della linea verticale per la mediana
plt.axvline(mediana, color='blue', linestyle='dashed', linewidth=1.5, label=f'Mediana: {mediana:.2f}')

plt.title("DM mass distribution")
plt.legend()
plt.savefig(file_path3, dpi=300, bbox_inches='tight')
plt.close()

#-----------------------PUNTO 4------------------------------

file_name4a = "Grafico_4a.png"
file_path4a = folder_path + "/" + file_name4a

# Creo una figura con due pannelli orizzontali (1 riga, 2 colonne)
fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(14, 14))
fig.suptitle('Projected Distribution')

# Primo grafico sinistra: Mostra il grafico pos_x vs pos_y  
ax1.set_ylabel('$ x (ckpc/h)$',fontsize=12)
ax1.set_xlabel('$ y (ckpc/h)$',fontsize=12)
ax1.ticklabel_format(axis='y', scilimits=(0,0))
ax1.ticklabel_format(axis='x', scilimits=(0,0))
ax1.plot(pos_y_arr, pos_x_arr, marker='o', linestyle='',markersize=2.5, alpha=0.5)



# Secondo grafico destra: Mostra il grafico pos_z vs pos_y  
ax2.set_ylabel('$ z (ckpc/h)$',fontsize=12)
ax2.set_xlabel('$ y (ckpc/h)$',fontsize=12)
ax2.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
ax2.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
ax2.plot(pos_y_arr, pos_z_arr, marker='o', linestyle='',markersize=2.5, alpha=0.5)



# Mostra entrambi i grafici
plt.tight_layout()  # Aggiusta il layout per evitare sovrapposizioni
plt.savefig(file_path4a, dpi=300, bbox_inches='tight')
plt.close()

#Definisco colori e dimensioni variabili.
# il colore varia in base alla massa del gas.
# la dimensione dei punti varia in base alla massa stellare.

size = np.where(m_star_arr > 0, 
                 (m_star_arr - m_star_arr.min()) / (m_star_arr.max() - m_star_arr.min()) * 100 +30, 
                 10)

m_gas_ok = np.where(m_gas_arr > 0, m_gas_arr, 1e-10)  # Imposta un minimo per evitare log(0)
color = np.log10(m_gas_ok) 


# Crea il layout con due pannelli

file_name4b = "Grafico_4b.png"
file_path4b = folder_path + "/" + file_name4b

fig, axes = plt.subplots(2, 2, figsize=(14, 14))
fig.suptitle('Projected Distribution')
# Estrai i singoli assi
ax1, ax2, ax3, ax4 = axes.flatten()

# Primo grafico sinistra: pos_x vs pos_y
scatter1 = ax1.scatter(pos_y_arr, pos_x_arr, c=color, s=size, cmap="plasma", alpha=0.7, edgecolor="none")
ax1.set_ylabel('$x$ (ckpc/h)', fontsize=12)
ax1.set_xlabel('$y$ (ckpc/h)', fontsize=12)
ax1.ticklabel_format(axis='y', scilimits=(0, 0))
ax1.ticklabel_format(axis='x', scilimits=(0, 0))
ax1.set_title(" X-Y plane")

# Secondo grafico destra: pos_z vs pos_y
scatter2 = ax2.scatter(pos_y_arr, pos_z_arr, c=color, s=size, cmap="plasma", alpha=0.7, edgecolor="none")
ax2.set_ylabel('$z$ (ckpc/h)', fontsize=12)
ax2.set_xlabel('$y$ (ckpc/h)', fontsize=12)
ax2.ticklabel_format(axis='y', scilimits=(0, 0))
ax2.ticklabel_format(axis='x', scilimits=(0, 0))
ax2.set_title(" Z-Y plane")

# Terzo grafico sotto a sinistra (pos_x vs pos_z)
scatter3 = ax3.scatter(pos_z_arr, pos_x_arr, c=color, s=size, cmap="plasma", alpha=0.7, edgecolor="none")
ax3.set_ylabel('$x$ (ckpc/h)', fontsize=12)
ax3.set_xlabel('$z$ (ckpc/h)', fontsize=12)
ax3.ticklabel_format(axis='y', scilimits=(0, 0))
ax3.ticklabel_format(axis='x', scilimits=(0, 0))
ax3.set_title("X-Z plane")

ax4.axis('off')

# Barra dei colori comune
cbar = fig.colorbar(scatter1, ax=ax2, orientation="vertical", fraction=0.03, pad=0.04)
cbar.set_label("Log(gas mass [10^{10} M_\odot/h]^{-1})", fontsize=12)


plt.tight_layout()
plt.savefig(file_path4b, dpi=300, bbox_inches='tight')
plt.close(fig)

#-----------------------PUNTO 5------------------------------
# Faccio un plot della BH mass (y-axis) VS stellar mass (x-axis)
# Ricavo prima gli aloni con massa di BH > di 8 × 10^5 M⊙/h

m_bh_grandi_indices = np.where(m_bh_arr > 8 * 10**(-5))
#print("Indici degli aloni con BH mass > 8*10^5:", m_bh_grandi_indices)
#Ottengo 8 aloni che soddisfano tale condizione
#Ora che conosco gli indici posso estrapolare anche le relative m_star
#Gli indici sono: 
# 0, 1, 2, 3, 87, 88, 101, 104

m_bh_grandi= m_bh_arr[m_bh_grandi_indices]
m_star_grandi= m_star_arr[m_bh_grandi_indices]


file_name5a = "Grafico_5a.png"
file_path5a = folder_path + "/" + file_name5a

plt.figure()  
plt.xlabel(' (Stellar mass $[10^{10} M_\odot/h]$)',fontsize=12)
plt.ylabel(' (BH mass $[10^{10} M_\odot/h]$)',fontsize=12)
plt.xscale('log')             
plt.yscale('log') 
plt.title('BH mass-stellar mass relation(log-log scale)')
plt.plot(m_star_grandi, m_bh_grandi, marker='o', linestyle='', markersize=3, alpha=0.5)
plt.savefig(file_path5a, dpi=300, bbox_inches='tight')
plt.close()


#Faccio un fit lineare di grado 1. Devo calcolare pendenza e intercetta.
#Per fare ciò uso una funzionalità intrinseca chiamata np.polyfit.
#Sono passata in scala logaritmica quindi per fare il fit sui dati devo calcolarne il log

log_m_bh_grandi= np.log10(m_bh_grandi)
log_m_star_grandi= np.log10(m_star_grandi)

coeffs = np.polyfit(log_m_star_grandi, log_m_bh_grandi, 1)
pend= coeffs[0]
inter= coeffs[1]

print(f"Pendenza fit: {pend}")
print(f"Intercetta fit: {inter}")

# Calcolo i valori di y previsti dalla retta
mass_bh_fit = log_m_star_grandi*pend + inter


# Ottengo: 
# Pendenza: 
# Intercetta: 


file_name5b = "Grafico_5b.png"
file_path5b = folder_path + "/" + file_name5b

plt.figure()
plt.xlabel(' log (Stellar mass $[10^{10} M_\odot/h]^{-1}$)',fontsize=12)
plt.ylabel(' log (BH mass $[10^{10} M_\odot/h]^{-1}$)',fontsize=12)
plt.title('BH mass-stellar mass relation')
plt.legend()
plt.plot(log_m_star_grandi, log_m_bh_grandi, marker='o', linestyle='', markersize=3, label= 'Dati', alpha=0.5)
plt.plot(log_m_star_grandi, mass_bh_fit, color='red', label='Fit lineare: y = {:.2f}x  {:.2f}'.format(pend, inter), zorder=1)
plt.savefig(file_path5b, dpi=300, bbox_inches='tight')
plt.close()


#-----------------------PUNTO 6------------------------------
# Per risolverre l'ultimo punto impongo una Mass threshold
mass_threshold = 3.07e9

m_gas_ok= m_gas_arr*10**10
# Seleziono gli aloni con massa > threshold
massive_indices = np.where(m_gas_ok > mass_threshold)[0]
massive_halo_mass = m_tot_arr[massive_indices]

#Verifico di ottenere proprio 5 aloni più massivi
#print(massive_indices)

#Calcolo le distanze di ogni alone massivo dagli altri


pos_x_arr = matrix_tot[:, 5]  # Coordinate x
pos_y_arr = matrix_tot[:, 6]  # Coordinate y
pos_z_arr = matrix_tot[:, 7]  # Coordinate z

#Ora calcolo la distanza euclidea

indici= [0, 1, 87, 101, 104]

x_max2=matrix_tot[1,5] 
y_max2=matrix_tot[1,6]
z_max2=matrix_tot[1,7]

x_max3=matrix_tot[87,5] 
y_max3=matrix_tot[87,6]
z_max3=matrix_tot[87,7]

x_max4=matrix_tot[101,5] 
y_max4=matrix_tot[101,6]
z_max4=matrix_tot[101,7]

x_max5=matrix_tot[104,5] 
y_max5=matrix_tot[104,6]
z_max5=matrix_tot[104,7]

distanze1= np.zeros(456)
distanze2= np.zeros(456)
distanze3= np.zeros(456)
distanze4= np.zeros(456)
distanze5= np.zeros(456)


dist_xi= np.zeros(456)
dist_yi= np.zeros(456)
dist_zi= np.zeros(456)

for i in range(456):
    # Calcolo delle distanze
    dist_xi[i] = (x_max1 - pos_x_arr[i]) ** 2
    dist_yi[i]= (y_max1 - pos_y_arr[i]) ** 2
    dist_zi[i] = (z_max1 - pos_z_arr[i]) ** 2
    distanze1[i] = np.sqrt(dist_xi[i] + dist_yi[i] + dist_zi[i])
  
for i in range(456):
    dist_xi[i] = (x_max2 - pos_x_arr[i]) ** 2
    dist_yi[i]= (y_max2 - pos_y_arr[i]) ** 2
    dist_zi[i] = (z_max2 - pos_z_arr[i]) ** 2
    distanze2[i] = np.sqrt(dist_xi[i] + dist_yi[i] + dist_zi[i])
  
for i in range(456):
    dist_xi[i] = (x_max3 - pos_x_arr[i]) ** 2
    dist_yi[i]= (y_max3 - pos_y_arr[i]) ** 2
    dist_zi[i] = (z_max3 - pos_z_arr[i]) ** 2
    distanze3[i] = np.sqrt(dist_xi[i] + dist_yi[i] + dist_zi[i])

for i in range(456):
    dist_xi[i] = (x_max4 - pos_x_arr[i]) ** 2
    dist_yi[i]= (y_max4 - pos_y_arr[i]) ** 2
    dist_zi[i] = (z_max4 - pos_z_arr[i]) ** 2
    distanze4[i] = np.sqrt(dist_xi[i] + dist_yi[i] + dist_zi[i])
   
for i in range(456):
    dist_xi[i] = (x_max5 - pos_x_arr[i]) ** 2
    dist_yi[i]= (y_max5 - pos_y_arr[i]) ** 2
    dist_zi[i] = (z_max5 - pos_z_arr[i]) ** 2
    distanze5[i] = np.sqrt(dist_xi[i] + dist_yi[i] + dist_zi[i])
    
#Passo in scala logaritmica nelle masse
log_m_tot= np.log10(m_tot_arr)

# Definisco i bin 
mass_bins = np.linspace(-2.4, 2.4, 70)  # 50 bin per le masse
distance_bins = np.linspace(0, 2200, 70)  # 50 bin per le distanze

# Creo gli istogrammi individuali usando numpy.histogram2d
hist1, _, _ = np.histogram2d(log_m_tot, distanze1, bins=[mass_bins, distance_bins])
hist2, _, _ = np.histogram2d(log_m_tot, distanze2, bins=[mass_bins, distance_bins])
hist3, _, _ = np.histogram2d(log_m_tot, distanze3, bins=[mass_bins, distance_bins])
hist4, _, _ = np.histogram2d(log_m_tot, distanze4, bins=[mass_bins, distance_bins])
hist5, _, _ = np.histogram2d(log_m_tot, distanze5, bins=[mass_bins, distance_bins])

# Somma cumulativa degli istogrammi
cumulative_histogram = hist1 + hist2 + hist3 + hist4 + hist5

file_name6 = "Grafico_6.png"
file_path6 = folder_path + "/" + file_name6


# Visualizzo l'istogramma cumulativo
plt.imshow(
    cumulative_histogram.T,  # Transponi per allineare correttamente gli assi
    origin="lower",
    aspect="auto",
    cmap="Blues",
    extent=[mass_bins[0], mass_bins[-1], distance_bins[0], distance_bins[-1]],
)
plt.colorbar(label="Number of halos")
plt.xlabel("log(mass $[10^{10} M_\odot/h]^{-1}$)")
plt.ylabel("Distance (ckpc/h)")
plt.title("Cumulative 2D histogram")
plt.savefig(file_path6, dpi=300, bbox_inches='tight')
plt.show()











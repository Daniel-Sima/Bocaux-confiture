import matplotlib.pyplot as plt
import time
import Algorithme_I as A1
import Algorithme_II as A2
import Algorithme_III as A3

#-------------------------------------------------------------------------------#
def Complexite_K_S_AlgoI(nomFichier, kMax, sMax, d, function): # Car condition sur le temps mis par le CPU
  open(nomFichier, 'w').close()  # Pour effacer ce qu'il y a dans le fichier.data
  writer = open(nomFichier, 'a') # Ouverture pour ecrire les données
  V = [pow(d, i) for i in range(kMax)]   # Creation du systeme de capacités avec un d choisi au préalable 
  print(V)
  time_start = time.time()      # Pour mesurer le temps mis par le CPU
  time_end = time_start + 60    # Arreter au bout de time_end 
  # Pour c allant de 0 à sMax
  for c in range(sMax+1):
    # Pour i allant de 0/1 à kMax tant que le CPU ne depasse pas time_end 
    for i in range(kMax+1):
      
      # Mesure du temps d'execution 
      start = time.time()
      function(c, i, V)
      end = time.time()
      temps = round(end-start, 5)
      writer.write(str(c)+' ')       # On ecrit pour chaque ligne le c qu'on mesure
      writer.write(str(i)+' ')       # On ecrit pour chaque colonne le i qu'on mesure
      writer.write(str(temps)+'\n')  # Ecriture du temps mesuré
    
    # Sortie si le temps de calcul depasse
    if (time.time() > time_end):
      break 

  writer.close()                    # Fermeture du fichier .data
  return
#-------------------------------------------------------------------------------#
def Complexite_K_S_AlgoII_et_III(nomFichier, kMax, sMax, d, function): # Car condition sur le temps mis par le CPU
  open(nomFichier, 'w').close()  # Pour effacer ce qu'il y a dans le fichier.data
  writer = open(nomFichier, 'a') # Ouverture pour ecrire les données
  V = [pow(d, i) for i in range(kMax)]   # Creation du systeme de capacités avec un d choisi au préalable 
 
  # Pour c allant de 0 à sMax
  for c in range(sMax+1):
    # Pour i allant de 1 à kMax 
    for i in range(kMax+1):
      # Mesure du temps d'execution 
      start = time.time()
      function(c, i, V)
      end = time.time()
      temps = round(end-start, 5)
      writer.write(str(c)+' ')       # On ecrit pour chaque ligne le c qu'on mesure
      writer.write(str(i)+' ')       # On ecrit pour chaque colonne le i qu'on mesure
      writer.write(str(temps)+'\n')  # Ecriture du temps mesuré

  writer.close()                    # Fermeture du fichier .data
  return
#-------------------------------------------------------------------------------#
def Recuperation_Donnees(k, S): 
  #Complexite_K_S_AlgoI("AlgoRecursif_d2.data", k, S, 2, A1.AlgoRecursif)
  #Complexite_K_S_AlgoI("AlgoRecursif_d3.data", k, S, 3, A1.AlgoRecursif)
  Complexite_K_S_AlgoI("AlgoRecursif_d4.data", k, S, 4, A1.AlgoRecursif)

  #Complexite_K_S_AlgoII_et_III("AlgoRetour_d2.data", k, S, 2, A2.AlgoRetour)
  #Complexite_K_S_AlgoII_et_III("AlgoRetour_d3.data", k, S, 3, A2.AlgoRetour)
  #Complexite_K_S_AlgoII_et_III("AlgoRetour_d4.data", k, S, 4, A2.AlgoRetour)

  #Complexite_K_S_AlgoII_et_III("AlgoGlouton_d2.data", k, S, 2, A3.AlgoGlouton)
  #Complexite_K_S_AlgoII_et_III("AlgoGlouton_d3.data", k, S, 3, A3.AlgoGlouton)
  #Complexite_K_S_AlgoII_et_III("AlgoGlouton_d4.data", k, S, 4, A3.AlgoGlouton)
  
  return
#-------------------------------------------------------------------------------#
Recuperation_Donnees(10, 1000)
#-------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------#
def Complexite_en_K(nomFichier, S, k, function):
  open(nomFichier, 'w').close()  # Pour effacer ce qu'il y a dans le fichier.data
  writer = open(nomFichier, 'a') # Ouverture pour ecrire les données
  
  time_start = time.time()
  time_end = time_start + 60  # fin dans une minute 
  for i in range(k):  
    writer.write(str(i)+' ')
    # On fait varier d de 2 à 4
    d = 2
    while (time.time() < time_end) & (d < 5):
      V = [pow(d, i) for i in range(k)]
      start = time.time()
      function(S, i, V)
      end = time.time()
  
      temps = round(end-start, 5)
      
      writer.write(str(temps)+' ')
      d += 1
    writer.write('\n')
  writer.close()

  return
#-------------------------------------------------------------------------------#
def Complexite_en_S(nomFichier, S, k, function):
  open(nomFichier, 'w').close()  # Pour effacer ce qu'il y a dans le fichier .txt
  writer = open(nomFichier, 'a') 
  
  for s in range(0, S, 5):
    time_start = time.time()
    time_end = time_start + 60  # fin dans une minute 
  
    writer.write(str(s)+' ')
    # On fait varier d de 2 à 4
    d = 2
    while (time.time() < time_end) & (d < 5):
      V = [pow(d, i) for i in range(k)]
      start = time.time()
      function(s, k, V)
      end = time.time()
  
      temps = round(end-start, 5)
      
      writer.write(str(temps)+' ')
      #print("i = ", i,"time = ", time.time(), "time_end = ", time_end)
      d += 1
    writer.write('\n')
  writer.close()

  return


def Tracer_Courbe(nomFichier, axisX, title):
  print("Graphe:")
  x = []
  y1 = []
  y2 = []
  y3 = []

  for line in open(nomFichier, 'r'):
    lines = [i for i in line.split()]
    x.append(lines[0])
    y1.append(float(lines[1]))
    y2.append(float(lines[2]))
    y3.append(float(lines[3]))

      
  plt.title(title)
  plt.xlabel(axisX)
  plt.ylabel("Temps d'execution en Sec")

  plt.plot(x, y1, marker = 'o', c = 'g')
  plt.plot(x, y2, marker = 'o', c = 'r')
  plt.plot(x, y3, marker = 'o', c = 'b')
  plt.legend(['d = 2', 'd = 3', 'd = 4'])

  plt.show()

  return

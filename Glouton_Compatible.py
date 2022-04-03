import random
import Algorithme_II as A2
import Algorithme_III as A3
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------- # 
def Generer_Systeme(k, pmax):
  #k = random.randint(0, 10) #generer un entier entre 0 et 9 inclus
  V = [1] + random.sample(range(2, pmax+1), k-1)  # Generer une liste de longueur k-1 avec des entiers entre 2 et pmax
  V.sort()  #trier la liste V
  return V
# --------------------------------------------------------------------------------- # 
def TestGloutonCompatible(k, V):
  if (k >= 3):
    for S in range(V[2]+2, V[k-2]+V[k-1]):
      for j in range(1, k):
        m1, A1 = A3.AlgoGlouton(S, j, V)
        m2, A2 = A3.AlgoGlouton(S - V[j], j, V)
        if (V[j] < S) and (m1 > 1+m2):  
          return False
  return True 
# --------------------------------------------------------------------------------- # 
def Courbe_Tirage_kMax(nomFichier):
  print("Graphe:")
  x = []
  y = []

  for line in open(nomFichier, 'r'):
    lines = [i for i in line.split()]
    x.append(lines[0])
    y.append(float(lines[1]))

      
  plt.title(nomFichier)
  plt.xlabel("Valeurs de k")
  plt.ylabel("Systemes Glouton Compatibles en %")

  plt.plot(x, y, marker = 'o', c = 'b')

  plt.show()

  return
  # --------------------------------------------------------------------------------- # 
def Tirage_en_kMax(nomFichier, pMax, kMax):
  open(nomFichier, 'w').close()  # Pour effacer ce qu'il y a dans le fichier .txt
  writer = open(nomFichier, 'a') 
  
  for i in range(2, kMax+1):
    writer.write(str(i)+' ')
    cptGloutonCompatible = 0 

    # On teste pour pMax/10 valeurs 
    for j in range(kMax+1, pMax):   
      V = Generer_Systeme(i, j)
      if(TestGloutonCompatible(i, V)):
        cptGloutonCompatible += 1

    pourcentage = cptGloutonCompatible/((pMax-kMax-1))*100
      
    writer.write(str(pourcentage)+'\n')
  writer.close()
  Courbe_Tirage_kMax(nomFichier)
  return
# ------------------------------------------------------------------------------- #
def Courbe_Ecart(nomFichier):
  print("Graphe:")
  x = []
  y1 = []
  y2 = []

  for line in open(nomFichier, 'r'):
    lines = [i for i in line.split()]
    x.append(lines[0])
    y1.append(float(lines[1]))
    y2.append(float(lines[2]))

      
  plt.title(nomFichier)
  plt.xlabel("Valeurs de k")
  plt.ylabel("Ecart Moyen")
  plt.plot(x, y1, marker = 'o', c = 'b')
  plt.show()

  plt.title(nomFichier)
  plt.xlabel("Valeurs de k")
  plt.ylabel("Pire Ecart")
  plt.plot(x, y2, marker = 'o', c = 'g')
  plt.show()

  return
  # --------------------------------------------------------------------------------- # 
def Ecart(nomFichier, pmax, f, k): # Faire la moyenne des ecarts
  open(nomFichier, 'w').close()  # Pour effacer ce qu'il y a dans le fichier .txt
  writer = open(nomFichier, 'a') 
  
  for i in range(1, k+1):
    ecarts = []
    V = Generer_Systeme(i, pmax)
    pire_ecart = 0 
    ecart_moyen = 0 
    print(i)
    if not(TestGloutonCompatible(i, V)):
      for S in range(pmax, f*pmax+1):
        
        mII, tabA2 = A2.AlgoRetour(S, i, V)
        mIII, tabA3 = A3.AlgoGlouton(S, i, V)

        ecarts = ecarts + [abs(mII - mIII)]

        if abs(mII - mIII) > pire_ecart:
          pire_ecart = abs(mII - mIII)
          
      ecart_moyen = sum(ecarts)/len(ecarts)
      writer.write(str(i)+' ')
      writer.write(str(ecart_moyen)+' ')
      writer.write(str(pire_ecart)+'\n')
   
  writer.close()
  Courbe_Ecart(nomFichier)
  return

# --------------------------------------------------------------------------------- # 
def testAlgoGloutonCompatible():
  print(Generer_Systeme(4, 5))
  print(Generer_Systeme(4, 10))
  print(Generer_Systeme(4, 1000))

  V1 = [1, 10, 14]
  V2 = [1, 2]
  V3 = [1, 8, 9]
  if (TestGloutonCompatible(3, V1)):  # k=3????
    print(V1, "est un systeme de capacité glouton-compatible")
  else:
    print(V1, "n'est PAS un systeme de capacité glouton-compatible")
  print()

  if (TestGloutonCompatible(2, V2)):  # k=2????
    print(V2, "est un systeme de capacité glouton-compatible")
  else:
    print(V2, "n'est PAS un systeme de capacité glouton-compatible")
  print()

  if (TestGloutonCompatible(3, V3)):  # k=3????
    print(V3, "est un systeme de capacité glouton-compatible")
  else:
    print(V3, "n'est PAS un systeme de capacité glouton-compatible")
  print()

  return
# --------------------------------------------------------------------------------- # 
#Tirage_en_kMax("Tirage_Systemes_Glouton-Compatibles.data", 100, 8)
Ecart("Ecarts_en_fonction_de_k.data", 15, 50, 15)
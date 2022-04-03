import math

# ----------------------------------------------------------------------------- #
## Algorithme II
# Question 5)
def AlgoOptimise(S, k, V):
  # Creation d'une matrice de taille S*k avec tous les valeurs à l'infini
  M = [[math.inf for i in range(k+1)] for j in range(S+1)] # Colonnes puis lignes

  # Pour c allant de 0 à S
  for c in range(S+1):
    # Pour i allant de 0 à k
    for i in range(k+1):
      if (c==0):            # Cas de base, si pas de quantité le nombre de bocaux est nul
        M[c][i] = 0
      elif (i==0):          # Cas de base, si pas de bocaux => infini
        continue
      else:
        if (c-V[i-1]<0):    # Si le bocal est trop grand, on pourra pas le remplir et on prendra le bocal de poids immédiatement inferieure 
          M[c][i] = M[c][i-1]
        else:               # Si le bocal n'est pas trop grand, on prend le min
          M[c][i] = min(M[c][i-1], M[c-V[i-1]][i]+1)

  return M[S][k]            # Retour de la valeur qui nous interesse

# ----------------------------------------------------------------------------- #
# Question 6 - a)
def AlgoOptimise2(S, k, V):
  A = [0 for j in range(k)]  # Liste de taille k initialisé a 0
  M = [[A for i in range(k+1)] for j in range(S+1)] # Colonnes puis lignes

  # Pour c allant de 0 à S
  for c in range(S+1):
    # Pour i allant de 0 à k
    for i in range(k+1):
      if (c==0):          # Cas de base, si pas de quantité le nombre de bocaux est nul
        if (i==0):
          M[c][i] = [0]   # Cas exception
        else:
          M[c][i] = [0 for j in range(k)]     # Cas de base, si pas de bocaux => infini
      elif (i==0): 
        M[c][i] = [math.inf] 
      else:
        if (c-V[i-1]<0):   # Si le bocal est trop grand, on pourra pas le remplir et on prendra le bocal de poids immédiatement inferieure 
          M[c][i] = M[c][i-1].copy()
        else:              # Si le bocal n'est pas trop grand, on prend le min
          if (sum(M[c][i-1]) < (sum(M[c-V[i-1]][i])+1)): 
            M[c][i] = M[c][i-1].copy()
          else:
            M[c][i] = M[c-V[i-1]][i].copy()
            (M[c][i])[i-1] += 1   # On ajoute un bocal dans ce cas

  return (sum(M[S][k]), M[S][k])  # Retour du tuple contenant le nombre de bocaux min et la liste A de bocaux utilisés 

# ----------------------------------------------------------------------------- #
# Question 6 - b)
def AlgoRetour(S, k, V):
  # Creation d'une matrice de taille S*k avec tous les valeurs à l'infini
  M = [[math.inf for i in range(k+1)] for j in range(S+1)] # Colonnes puis lignes

  # Pour c allant de 0 à S
  for c in range(S+1):
    # Pour i allant de 0 à k
    for i in range(k+1):
      if (c==0):            # Cas de base, si pas de quantité le nombre de bocaux est nul
        M[c][i] = 0
      elif (i==0):          # Cas de base, si pas de bocaux => infini
        continue
      else:
        if (c-V[i-1]<0):    # Si le bocal est trop grand, on pourra pas le remplir et on prendra le bocal de poids immédiatement inferieure 
          M[c][i] = M[c][i-1]
        else:               # Si le bocal n'est pas trop grand, on prend le min
          M[c][i] = min(M[c][i-1], M[c-V[i-1]][i]+1)
 
  A = [0 for j in range(k)] # Liste contenant les bocaux utilisés
  nbBoc = M[S][k]           # On utilise la donnée de l'algorithme initial, nombre de bocaux
  
  if (c == 0):              # Cas de base, si pas de quantité le nombre de bocaux est nul
    if (k==0):
      return (0, [0])  # cas exception
    else:
      return (0, A)
  elif (k==0):              # Cas de base, si pas de bocaux => infini
    return (0, [math.inf])
  elif (c < 0):             # Cas de base, pas possible de remplir une quantité infinie => infini
    return (0, [math.inf for i in range(k)])

  # Tant qu'on a des bocaux a trovuer l'indice on continue
  while (nbBoc!=0):
    if ((c-V[i-1]) < 0):    # Si le bocal est plus grand que la quantité de confiture on passe au bocal de poids inferieur
      i -= 1   
    else:                   # Sinon, on a choisi un bocal
      if (M[c][i-1] < M[c-V[i-1]][i]): # On a choisi le bocal immédiatement inferieur 
        i -= 1              # On passe a l'indice de ce bocal
        nbBoc -= 1          # Comme on a choisi un bocal, on diminue le nb de bocaux
        c = c-V[i-1]        # La quantité de confiture est diminuée
        A[i-1] += 1         # On incrémente de 1 l'indice du bocal choisi
      else:                 # On a choisi le bocal d'indice actuel
        nbBoc -= 1          # Comme on a choisi un bocal, on diminue le nb de bocaux
        c = c-V[i-1]        # La quantité de confiture est diminuée
        A[i-1] += 1         # On incrémente de 1 l'indice du bocal choisi
  
  return (sum(A), A)
# ----------------------------------------------------------------------------- #
## Lecture des données:
def LectureAlgoRetour(nomFichier):
  V = []          # Liste stockant le système de capcités du fichier 
  # Lecture du fichier texte "nomFichier" en mode lecture
  with open(nomFichier, 'r') as reader:
    S = int(reader.readline())        # Recuperation de S
    k = int(reader.readline())        # Recuperation de k
    # Recuperation des differents V[i] ligne par ligne 
    line = reader.readline()
    while line != '': 
      V.append(int(line))
      line = reader.readline()


  # Affichage du resultat:
  print("S : ", S, "\nk : ", k)
  print("Poids des differents bocaux V = ", V)
  for i in range(k+1):
    print("AlgoRetour(" + str(S) + ", " + str(i) + ") = " + str(AlgoRetour(S, i, V)))

  return
# ----------------------------------------------------------------------------- #
#LectureAlgoRetour("text.data")
  
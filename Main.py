import math
# Poids des differents bocaux
V = [1, 2, 5, 10, 20, 50, 100, 200]


# ----------------------------------------------------------------------------- #
# Algorithme I
def AlgoRecursif(S, k, V):
  # On rempli aucun bocal avec 0 quantité 
  if (S==0):
    return 0
  # On peut pas remplir une quantité negative et on peut pas remplir avec aucun bocal
  elif (S<0) or (k==0):
    return math.inf
  # On cherche le nombre minimal de bocaux pour une quantité S
  else:
    return min(AlgoRecursif(S, k-1, V), AlgoRecursif(S-V[k-1], k, V)+1)


# Affichage de la matrice resultat 
def TestAlgoRecursif():
  print("/------------------------Algorithme1-----------------/\n", end = '   ')
  for i in range(9):
    print(i, end=' ')
  print("\n------------------------")
  for i in range(11):
    print(i,"|", end="")
    for j in range(9):
      print(AlgoRecursif(i, j, V), end=' ')
    print()
  print()

  return 
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


# Affichage de la matrice resultat 
def TestAlgoOptimise():
  print("/----------------------Algorithme2-------------------------------/\n", end = '   ')
  for i in range(9):
    print(i, end=' ')
  print("\n------------------------")
  for i in range(11):
    print(i,"|", end="")
    for j in range(9):
        print(AlgoOptimise(i, j, V), end=' ')
    print()
  print()

  return
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

# Affichage de la matrice resultat: 
def TestAlgoOptimise2():
  print("/--------------------------AlgoOptimise2-----------------------------/")
  for i in range(10):
    for j in range(6):
      m, LR = AlgoOptimise2(i, j, V)
      print(LR, end=' ')
    print()
  print()

  return;
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
      return (0, [0])       # Cas exception
    else:
      return (0, A)
  elif (k==0):              # Cas de base, si pas de bocaux => infini
    return (math.inf, [math.inf])
  elif (c < 0):             # Cas de base, pas possible de remplir une quantité infinie => infini
    return (math.inf, [math.inf for i in range(k)])

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

# Affichage des jeux de test:
def TestAlgoRetour():
  print("/------------------------AlgoRetour----------------------------/")
  for i in range(10):
    for j in range(6):
      m, LR = AlgoRetour(i, j, V)
      print(LR, end=' ')
    print()
  print()

  return
# ----------------------------------------------------------------------------- #
## Algorithme III
# Question 8)
def AlgoGlouton(S, k, V): 
  A = [0 for i in range(k)]             # Liste contenant les bocaux utilisés

  if (S==0):               # Cas de base, si pas de quantité le nombre de bocaux est nul
    if (k==0):
      return (0, [0])           # Cas exception 
    else:
      return (0, A)
  elif (k==0):                  # Cas de base, si pas de bocaux => infini
    return (math.inf, [math.inf])
  elif (S<0):                   # Cas de base, pas possible de remplir une quantité infinie => infini
    return (math.inf, [math.inf for i in range(k)]) 

  # Pour ne pas modifier les parametres d'entrée
  c = S
  i = k-1
  # Tant que la capacité de confiture est non nulle 
  while (c != 0): 
    if ((c - V[i]) < 0):    # Si le bocal est de poids > que le poids de la confiture
      i-=1                  # On passe au bocal suivant plus petit
    else:                   # Sinon, on peut rajouter la confiture dans ce bocal
      A[i]+=1               # On marque qu'on a utilisé un bocal de ce poids
      c=c-V[i]              # On diminue par consequent la quantité de confiture enlevée

  return (sum(A), A)

# Affichage des jeux de test:
def TestAlgoGlouton():
  print("/------------------------AlgoGlouton--------------------------/")
  for i in range(10):
    for j in range(6):
      print(AlgoGlouton(i, j, V)[1], end=' ')
    print()
  print()

  return; 
# ----------------------------------------------------------------------------- #
#TestAlgoRecursif()
#TestAlgoOptimise()
#TestAlgoOptimise2()
#TestAlgoRetour()
#TestAlgoGlouton()

print("//------------------Alogirthme III-----------------------//")
# Question 9)
V = [1, 10, 14] 
#V = [1, 2, 5, 10, 20, 50, 100, 200]

print("Nouvelle liste V =", V)
print("Algorithme1(34, 3): ", AlgoRecursif(34, 3, V))
print("AlgorithmeOptimise(34, 3): ", AlgoOptimise(34, 3, V))
print("AlgoOptimise2(34, 3): ", AlgoOptimise2(34, 3, V))
print("AlgoRetour(34, 3): ", AlgoRetour(34, 3, V))
print("AlgoGlouton(34, 3): ", AlgoGlouton(34, 3, V))
# ----------------------------------------------------------------------------- #



import math

# ----------------------------------------------------------------------------- #
## Algorithme III
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
# ----------------------------------------------------------------------------- #
## Lecture des données:
def LectureAlgoGlouton(nomFichier):
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
    print("AlgoGlouton(" + str(S) + ", " + str(i) + ") = " + str(AlgoGlouton(S, i, V)))
    
  return
# ----------------------------------------------------------------------------- #
#LectureAlgoGlouton("text.data")
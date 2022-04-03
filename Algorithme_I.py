import math

# ----------------------------------------------------------------------------- #
## Algorithme I
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

  return
# ----------------------------------------------------------------------------- #
## Lecture des données:
def LectureAlgoRecursif(nomFichier):
  V = []            # Liste stockant le système de capcités du fichier 
  # Lecture du fichier texte "nomFichier" en mode lecture
  with open(nomFichier, 'r') as reader:
    S = int(reader.readline())    # Recuperation de S
    k = int(reader.readline())    # Recuperation de k
    # Recuperation des differents V[i] ligne par ligne 
    line = reader.readline()
    while line != '': 
      V.append(int(line))
      line = reader.readline()

  # Affichage du resultat:
  print("S : ", S, "\nk : ", k)
  print("Poids des differents bocaux V = ", V)
  for i in range(k+1):
    print("AlgoRecursif("+str(S)+", "+str(i)+") = ", AlgoRecursif(S, i, V))
# ----------------------------------------------------------------------------- #
#LectureAlgoRecursif("text.data")







def lecture():
   global L
   L=[]
   fichier='/media/dossiers/Documents/Cours/agreg/Informatique/Python/input_advent_2019_2.txt'
   with open(fichier,'r') as f:
      L=f.read().split(',')
   L=[int(elt) for elt in L]
#   L=[1,1,1,4,99,5,6,0,99]


def traitement(cursor):
#   global L
#   print(cursor, L)
   if L[cursor]==1:
      L[L[cursor+3]]=L[L[cursor+1]]+L[L[cursor+2]]
   elif L[cursor]==2:
         L[L[cursor+3]]=L[L[cursor+1]]*L[L[cursor+2]]
   else:
      print("arrêt : cursor = ", L[cursor])
 #  print(L)
   return(cursor+4)

def main(noun,verb):
#   global L
   lecture()
   length = len(L)
   L[1]=noun
   L[2]=verb
   cursor=0
   while cursor< length and L[cursor]!=99:
      cursor=(traitement(cursor))
   return(L[0])

def main2():
   for noun in range(100):
      for verb in range(100):
         if main(noun,verb)==19690720:
            print(100*noun+verb)
   

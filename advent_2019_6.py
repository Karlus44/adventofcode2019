

def lecture():
   global A #dico reverse
   global dico
   global List #adjacency list
   global List2 #double adjacency list
   global B
   dico=dict()
   k=0
   A=[]
   B=[]
   
   fichier='/media/dossiers/Documents/Cours/agreg/Informatique/Python/input_advent_2019_6.txt'
   with open(fichier,'r') as f:
      for line in f:
         L1=line.rstrip('\n')
         L1=L1.split(')')
         if L1[0] not in dico:
            dico[L1[0]]=k
            k=k+1
            A.append(L1[0])
         if L1[1] not in dico:
            dico[L1[1]]=k
            k=k+1
            A.append(L1[1])
         B=B+[L1]
   List=[[]]*len(A)
   List2=[[]]*len(A)
   for elt in B:
      List[dico[elt[0]]]= List[dico[elt[0]]]+ [dico[elt[1]]]
      List2[dico[elt[0]]]= List2[dico[elt[0]]]+ [dico[elt[1]]]
      List2[dico[elt[1]]]= List2[dico[elt[1]]]+ [dico[elt[0]]]
         

def recursive_tour(pointer,weight):
   S=0
   for elt in List[pointer]:
      S=S+ weight + recursive_tour(elt, weight + 1)
   return S

def recursive_search(pointer,dist,dejavu):

         for elt in List2[pointer]:
            if elt not in dejavu:
   #            print(elt, dist+1, dejavu+[pointer])
   #            print(elt)
               if elt==Santa:
                  print("Santa :", dist-1)
                  return(dist)
               else:
                  recursive_search(elt, dist+1, dejavu+[pointer])

   


def main():
   lecture()
   k=dico['COM']
   answer=recursive_tour(k,1)
   print(answer)

        
def main2():
   global Santa
   lecture()
   k1=dico['YOU']
   k2=dico['SAN']
   Santa=k2
   recursive_search(k1,0,[k1])



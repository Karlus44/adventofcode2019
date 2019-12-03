

def lecture():
   global A
   A=[]
   fichier='/media/dossiers/Documents/Cours/agreg/Informatique/Python/input_advent_2019_1.txt'
   with open(fichier,'r') as f:
      for line in f:
         L1=int(line)//3-2
         A.append(L1)
        
def lecture2():
   global A
   A=[]
   fichier='/media/dossiers/Documents/Cours/agreg/Informatique/Python/input_advent_2019_1.txt'
   with open(fichier,'r') as f:
      for line in f:
         L1=int(line)//3-2
         S1=L1
         while L1>0:
               L1=int(L1)//3-2
               S1=S1+max(L1,0)
         A.append(S1)


def main():
   lecture2()
   S=0
   for k in A:
      S=S+k
   print(S)

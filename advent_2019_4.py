
def lecture():
   global G, D
   L=[]
   R=[]

   fichier='/media/dossiers/Documents/Cours/agreg/Informatique/Python/input_advent_2019_3.txt'
   with open(fichier,'r') as f:
      R=f.readline().split(',')
      L=f.readline().split(',')
   G=pointlist(L)
   D=pointlist(R)
   
   

def digit(k,n):
   #nth digit of k from the left
   if n<0 or 10**n>k:
      return 0
   else:
      return k//10**(5-n) % 10


def test1(k):
   #digits increase
   test=True
   for i in range(5):
      test=test and digit(k,i)<=digit(k,i+1)
   return test

def test2(k):
   #pair of digits
   test=False
   for i in range(5):
      test=test or digit(k,i)==digit(k,i+1)
   return test

def test2bis(k):
   #pair of digits and only pair
   test=False
   for i in range(5):
      test=test or (digit(k,i)==digit(k,i+1) and digit(k,i)!=digit(k,i-1) and digit(k,i+1)!=digit(k,i+2))
   return test

def main():
   cpt=0
   for k in range(245182,790573):
      if test1(k) and test2(k):
         cpt=cpt+1
   print(cpt)

def main2():
   cpt=0
   for k in range(245182,790573):
      if test1(k) and test2bis(k):
         cpt=cpt+1
#         print(k)
   print(cpt)


   

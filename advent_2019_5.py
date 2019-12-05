

def lecture():
   global L
   L=[]
   fichier='/media/dossiers/Documents/Cours/agreg/Informatique/Python/input_advent_2019_5.txt'
   with open(fichier,'r') as f:
      L=f.read().split(',')
   L=[int(elt) for elt in L]
#   L=[1,1,1,4,99,5,6,0,99]


def param(position,mode):
   # returns the address of the parameter
   if mode==0:
      return(L[position])
   elif mode==1:
      return(position)
   else:
      print("problem : mode =", mode)

def parameters(cursor):
   # returns the address of the three parameters
   instruction_code = L[cursor]
   parameter1=param(cursor+1,instruction_code// 100 % 10)
   parameter2=param(cursor+2,instruction_code// 1000 % 10)
   parameter3=param(cursor+3,instruction_code// 10000 % 10)
   return parameter1, parameter2, parameter3

def parameters2(cursor):
   # returns the address of the two parameters
   instruction_code = L[cursor]
   parameter1=param(cursor+1,instruction_code// 100 % 10)
   parameter2=param(cursor+2,instruction_code// 1000 % 10)
   return parameter1, parameter2


def traitement(cursor):
#   global L
#   print(cursor, L)
   opcode = L[cursor]% 100
   if opcode == 3:
      L[L[cursor+1]]=int(input('input'))
      return(cursor+2)
   elif opcode == 4:
      if L[cursor]==4:
         print("output : ", L[L[cursor+1]], ", cursor : ", cursor)
      elif L[cursor]==104:
         print("output : ", L[cursor+1], ", cursor : ", cursor)
      else:
         print("problem : L[cursor] =", L[cursor])
      return(cursor+2)
   elif opcode == 1:
      param1, param2, param3 = parameters(cursor)
      L[param3]=L[param1]+L[param2]
      return(cursor+4)
   elif opcode ==2:
      param1, param2, param3 = parameters(cursor)
      L[param3]=L[param1]*L[param2]
      return(cursor+4)
   elif opcode ==99:
      print("end of program")
      return(cursor)
   else:
      print("problem : instruction code = ", L[cursor])
 #  print(L)

def main():
#   global L
   lecture()
   length = len(L)
   cursor=0
   while cursor< length and L[cursor]!=99:
      cursor=(traitement(cursor))

def traitement2(cursor):
#   global L
#   print(cursor, L)
   opcode = L[cursor]% 100
   if opcode == 3:
      L[L[cursor+1]]=int(input('input'))
      return(cursor+2)
   elif opcode == 4:
      if L[cursor]==4:
         print("output : ", L[L[cursor+1]], ", cursor : ", cursor)
      elif L[cursor]==104:
         print("output : ", L[cursor+1], ", cursor : ", cursor)
      else:
         print("problem : L[cursor] =", L[cursor])
      return(cursor+2)
   elif opcode == 1:
      param1, param2, param3 = parameters(cursor)
      L[param3]=L[param1]+L[param2]
      return(cursor+4)
   elif opcode ==2:
      param1, param2, param3 = parameters(cursor)
      L[param3]=L[param1]*L[param2]
      return(cursor+4)
   elif opcode ==5:
      param1, param2 = parameters2(cursor)
      if L[param1]!=0:
         return(L[param2])
      else:
         return(cursor+3)
   elif opcode ==6:
      param1, param2 = parameters2(cursor)
      if L[param1]==0:
         return(L[param2])
      else:
         return(cursor+3)
   elif opcode ==7:
      param1, param2, param3 = parameters(cursor)
      if L[param1]<L[param2]:
         L[param3]=1
      else:
         L[param3]=0
      return(cursor+4)
   elif opcode ==8:
      param1, param2, param3 = parameters(cursor)
      if L[param1]==L[param2]:
         L[param3]=1
      else:
         L[param3]=0
      return(cursor+4)
   elif opcode ==99:
      print("end of program")
      return(cursor)
   else:
      print("problem : instruction code = ", L[cursor])
 #  print(L)



def main2():
#   global L
   lecture()
   length = len(L)
   cursor=0
   while cursor< length and L[cursor]!=99:
      cursor=(traitement2(cursor))

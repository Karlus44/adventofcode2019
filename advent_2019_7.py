

def lecture():
   global L
   L=[]
   fichier='/media/dossiers/Documents/Cours/agreg/Informatique/Python/input_advent_2019_7.txt'
   with open(fichier,'r') as f:
      L=f.read().split(',')
   L=[int(elt) for elt in L]



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



def traitement3(cursor,keys):

   global L, output, finished
   opcode = L[cursor]% 100
   if opcode == 3:
      L[L[cursor+1]]=keys[0]
      keys=keys[1:]
      return(cursor+2,keys)
   elif opcode == 4:
      if L[cursor]==4:
         output=True
         keys=[L[L[cursor+1]]]
      elif L[cursor]==104:
         output=True
         keys=[L[cursor+1]]
      else:
         print("problem : L[cursor] =", L[cursor])
      return(cursor+2,keys)
   elif opcode == 1:
      param1, param2, param3 = parameters(cursor)
      L[param3]=L[param1]+L[param2]
      return(cursor+4,keys)
   elif opcode ==2:
      param1, param2, param3 = parameters(cursor)
      L[param3]=L[param1]*L[param2]
      return(cursor+4,keys)
   elif opcode ==5:
      param1, param2 = parameters2(cursor)
      if L[param1]!=0:
         return(L[param2],keys)
      else:
         return(cursor+3,keys)
   elif opcode ==6:
      param1, param2 = parameters2(cursor)
      if L[param1]==0:
         return(L[param2],keys)
      else:
         return(cursor+3,keys)
   elif opcode ==7:
      param1, param2, param3 = parameters(cursor)
      if L[param1]<L[param2]:
         L[param3]=1
      else:
         L[param3]=0
      return(cursor+4,keys)
   elif opcode ==8:
      param1, param2, param3 = parameters(cursor)
      if L[param1]==L[param2]:
         L[param3]=1
      else:
         L[param3]=0
      return(cursor+4,keys)
   elif opcode ==99:
      print("end of program")
      finished = True
      return(cursor,keys)
   else:
      print("problem : instruction code = ", L[cursor])
 #  print(L)




def amplifier(keys):

   global output
   output = False
   lecture()
   length = len(L)
   cursor=0
   while cursor< length and L[cursor]!=99 and not output:
      cursor,keys=traitement3(cursor,keys)
   if output:
      return keys[0]



def sequence(combination):
   global L
   global finished
   global output
   global maximum
   finished = False   
   output=0
   k=0
   while not finished and k<5: 
      keys=[combination[k],output]
      output=amplifier(keys)
      k=k+1
#   print(output)
   if output>maximum:
      maximum=output


def sublists(L1,L2):
   if L2==[]:
       sequence(L1)
   else:
      for k in range(len(L2)):
         m=max(k-1,0)
         sublists(L1+[L2[k]],L2[:k]+L2[k+1:])
      
maximum=0

def main2():
   global maximum
   List=[0,1,2,3,4]
   sublists([],List)
   print(maximum)
   
 

                        

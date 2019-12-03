
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
   
   

def pointlist(list):
   D=[[0,0]]
   for elt in list:
      P=D[-1]
      if elt[0]=='R':
         D=D+[[P[0]+int(elt[1:]),P[1]]]
      if elt[0]=='L':
         D=D+[[P[0]-int(elt[1:]),P[1]]]
      if elt[0]=='U':
         D=D+[[P[0],P[1]+int(elt[1:])]]
      if elt[0]=='D':
         D=D+[[P[0],P[1]-int(elt[1:])]]
   return D



def inter(xA, yA, xB, yB, xC, yC, xD, yD, sd, sg):
   #retourne la liste des points d'intersections entre [AB] et [CD]
   global stepsI
   liste=[]
   A=[xA,yA]
   B=[xB,yB]
   C=[xC,yC]
   D=[xD,yD]
   M=[xA,yC]
   N=[xC,yA]
   if xA==xB and yC==yD:
      if ((yA<= yC and yC<= yB) or (yA>= yC and yC>= yB)) and ((xC<= xA and xA<= xD) or (xC>= xA and xA>= xD)):
         liste=liste+[[xA,yC]]
         
         stepsI=stepsI+[[min(stepsG[sg]+dist(C,M), stepsG[sg+1]+dist(D,M)),
                        min(stepsD[sd]+dist(A,M), stepsD[sd+1]+dist(B,M))]]
         
   if yA==yB and xC==xD:
      if ((xA<= xC and xC<= xB) or (xA>= xC and xC>= xB)) and ((yC<= yA and yA<= yD) or (yC>= yA and yA>= yD)):
         liste=liste+[[xC,yA]]
         stepsI=stepsI+[[min(stepsG[sg]+dist(C,N), stepsG[sg+1]+dist(D,N)),
                        min(stepsD[sd]+dist(A,N), stepsD[sd+1]+dist(B,N))]]
         
   if yA==yB and yB==yC and yC==yD:
      if (min(xA,xB)<=max(xC,xD) and min(xC,xD)<=max(xA,xB)):
         a=max(min(xA,xB), min(xC,xD))
         b=min(max(xA,xB), max(xC,xD))
         for k in range(a,b+1):
            liste=liste+[[k,yA]]
#            stepsI=stepsI+[[min(steps[sg]+dist([xC,yC],[k,yA]), steps[sg+1]+dist([xD,yD],[k,yA])),
#                       min(steps[sd]+dist([xA,yA],[k,yA]), steps[sd+1]+dist([xB,yB],[k,yA]))]]

   if xA==xB and xB==xC and xC==xD:
      if (min(yA,yB)<=max(yC,yD) and min(yC,yD)<=max(yA,yB)):
         a=max(min(yA,yB), min(yC,yD))
         b=min(max(yA,yB), max(yC,yD))
         for k in range(a,b+1):
            liste=liste+[[xA,k]]
 #           stepsI=stepsI+[[min(steps[sg]+dist([xC,yC],[xA,k]), steps[sg+1]+dist([xD,yD],[xA,k])),
 #                       min(steps[sd]+dist([xA,yA],[xA,k]), steps[sd+1]+dist([xB,yB],[xA,k]))]]
   return(liste)

def manhattan(elt):
   x=elt[0]
   y=elt[1]
   return(abs(x)+abs(y)) 

def dist(elt1,elt2):
   x1=elt1[0]
   y1=elt1[1]
   x2=elt2[0]
   y2=elt2[1]
   return(abs(x2-x1)+abs(y2-y1))

def steps(liste):
   results=[0]
   lg=len(liste)
   for k in range(1,lg):
      results=results+[results[k-1]+dist(liste[k],liste[k-1])]
   return(results)

def main():
   global Intersections
   global stepsD
   global stepsG
   global stepsI
   stepsI=[[0,0]]
   Intersections=[]

   lecture()
   stepsD=steps(D)
   stepsG=steps(G)
   ld=len(D)-1
   lg=len(G)-1
   for k1 in range(ld):
      for k2 in range(lg):
         Intersections=Intersections+inter(D[k1][0], D[k1][1], D[k1+1][0], D[k1+1][1], \
                                           G[k2][0], G[k2][1], G[k2+1][0], G[k2+1][1], k1,k2)
   mini=manhattan(Intersections[1])
   for elt in Intersections[2:]:
      if manhattan(elt)<mini:
         mini=manhattan(elt)
   print(mini)

  


   

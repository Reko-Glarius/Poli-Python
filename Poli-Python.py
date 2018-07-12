"""
Nombre del Creador: Ricardo Aliste G. (Reko)
Fecha: 25/04/2017
Descripcion: Algoritmo que realiza operaciones polinomicas basicas.
"""

def origen(res):
    while(len(res)!=0):
        alfa=res[0]
        res.remove(alfa)
""" Transforma los numeros del txt a numeros operables (de char a int) """
def evaluar(res):       
    for i in range(0,(len(res))):
        res[i]=eval(res[i])
        
def ordenado(res):      
    a=-99999
    b=99999
    q=len(res)
    for i in range(1, q, 2):
        if(res[i]>a):
            a=res[i]
        if(res[i]<b):
            b=res[i]
    aux=[]
    while(b<=a):
        suma=0
        coef=b
        for j in range(1, q, 2):
            if(coef==res[j]):
                suma+=res[j-1]
        aux.append(suma)
        aux.append(coef)
        b+=1
    origen(res)
    alfa=len(aux)
    for i in range(0, alfa):
        res.append(aux[i])
"""Muestra los polinomios en base a la informacion del vector con la informacion del polinomio"""
def mostrar(res):       
    ordenado(res)
    o=False
    for i in range(0,(len(res))):
        if(i%2==0 and o==False):
            print(res[i], end="")
            o=True
        elif(i%2==0 and o==True):
            if(res[i]>0):
                print("+",res[i], end="")
            else:
                print(res[i], end="")
        elif(i%2!=0):
            if(res[i]!=0):
                print("x^",res[i], end="")
            elif(res[i]==0):
                print("",end="")
    print()
""" Operacion de Suma, siendo esta la primera operacion de su ejercicio """ 
def agregar(p1, p2, res):   
    for i in range(0, (len(p1))):
        res.append(p1[i])
    for i in range(0, (len(p2))):
        res.append(p2[i])
""" Operacion de Resta, siendo esta la primera operacion de su ejercicio """
def quitar(p1, p2, res):  
    for i in range(0, (len(p1))):
        res.append(p1[i])
    for i in range(0, (len(p2))):
        if(i%2==0):
            res.append(-(p2[i]))
        else:
            res.append(p2[i])
""" Operacion de Multiplicacion, siendo esta la primera operacion de su ejercicio """
def por(p1, p2, res):
    print("")
    for i in range(0, (len(p1)), 2):
        for j in range(0, (len(p2)), 2):
            res.append(p1[i]*p2[j])
            res.append(p1[i+1]+p2[j+1])
""" Operacion de Division, siendo esta la primera operacion de su ejercicio """
def corte(p1, a, res):     
    print("")
    for i in range(0, (len(p1))):
        if(i%2==0):
            res.append(p1[i]/a)
        else:
            res.append(p1[i])
""" Operacion de Derivar, siendo esta la primera operacion de su ejercicio """
def bajar(p1, res):        
    for i in range(1, len(p1), 2):
        res.append(p1[i-1]*p1[i])
        if(p1[i]!=0):
            res.append(p1[i]-1)
""" Operacion de Suma, siendo que ya se hecho una operacion en su ejercicio"""
def agregarr(p, res):       
    for i in range(0, len(p)):
        res.append(p[i])
""" Operacion de Resta, siendo que ya se hecho una operacion en su ejercicio"""
def quitarr(p, res):        
    for i in range(0, len(p)):
        if(i%2==0):
            res.append(-(p[i]))
        else:
            res.append(p[i])
""" Operacion de Multiplicacion, siendo que ya se hecho una operacion en su ejercicio"""
def porr(p, res):           
    aux=[]
    for i in range(0, (len(res)), 2):
        for j in range(0, (len(p)), 2):
            aux.append(res[i]*p[j])
            aux.append(res[i+1]+p[j+1])
    origen(res)
    for b in range(0, len(aux)):
        res.append(aux[b])
""" Operacion de Division, siendo que ya se hecho una operacion en su ejercicio"""
def corter(a, res):         
    for i in range(0, len(res)):
        if(i%2==0):
            res[i]=res[i]/a
            
print("La caceria de Polinomios nunca se acaba!")
print("------------------------------------------------------------------------")
print("Este programa resuelve, en parte, operaciones con polinomios")
print("consta de las sgtes. limitaciones, ya que esta en fase beta:")
print("1-La derivada solo funciona con un polinomio a la vez.")
print("2-Las divisiones se efectuan usando escalares entero de max. 1 digito.")
print("4-Las operaciones se van tomando en orden de izquierda a derecha.")
print("5-No se pueden usar parentesis.")
print("6-Solo puede haber 1 derivada y debe ser la primera operacion.")
print("------------------------------------------------------------------------")
print("Ahora esta avisado; que tenga gran diversion con esta caceria.")
print("------------------------------------------------------------------------")
file=open("texto.txt","r")
siono=False
cont=1
npol=0
resultado=[]
""" Empieza a leer el txt con los polinomios y las operaciones deseadas, para poder desplegar los datos """ 
libro=file.readlines()      
for pagina in libro:       
    if(npol==0):
        print(pagina)
        npol+=1
    elif(npol==1):
        if(pagina[0]=='P'):
            papu=pagina.split('=')
            p1=papu[1].split('#')
            evaluar(p1)
            print("P",cont, end=":")
            cont+=1
            mostrar(p1)
        npol+=1
    elif(npol==2):
        if(pagina[0]=='P'):
            papu=pagina.split('=')
            p2=papu[1].split('#')
            evaluar(p2)
            print("P",cont, end=":")
            cont+=1
            mostrar(p2)
        npol+=1
    elif(npol==3):
        if(pagina[0]=='P'):
            papu=pagina.split('=')
            p3=papu[1].split('#')
            evaluar(p3)
            print("P",cont, end=":")
            cont+=1
            mostrar(p3)
        npol+=1
    elif(npol==4):
        if(pagina[0]=='P'):
            papu=pagina.split('=')
            p4=papu[1].split('#')
            evaluar(p4)
            print("P",cont, end=":")
            cont+=1
            mostrar(p4)
        npol+=1
    elif(npol==5):
        if(pagina[0]=='P'):
            papu=pagina.split('=')
            p5=papu[1].split('#')
            evaluar(p5)
            print("P",cont, end=":")
            cont+=1
            mostrar(p5)
        npol+=1
    elif(npol==6):
        """ Desde aqui empieza a desplegar los ejercicios y los resultados de estos """
        print("Ejercicios:")         
        npol+=1
    elif(npol>6 and npol<13):
        text=len(pagina)
        print(pagina, end="")
        for i in range(0, text):
            if(pagina[i]=='+'):
                c1=pagina[i-1]
                c2=pagina[i+2]
                if(siono==False):
                    if(c1=='1'):
                        if(c2=='1'):
                            agregar(p1, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            agregar(p1, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            agregar(p1, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            agregar(p1, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            agregar(p1, p5, resultado)
                            siono=True
                    elif(c1=='2'):
                        if(c2=='1'):
                            agregar(p2, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            agregar(p2, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            agregar(p2, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            agregar(p2, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            agregar(p2, p5, resultado)
                            siono=True
                    elif(c1=='3'):
                        if(c2=='1'):
                            agregar(p3, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            agregar(p3, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            agregar(p3, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            agregar(p3, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            agregar(p3, p5, resultado)
                            siono=True
                    elif(c1=='4'):
                        if(c2=='1'):
                            agregar(p4, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            agregar(p4, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            agregar(p4, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            agregar(p4, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            agregar(p4, p5, resultado)
                            siono=True
                    elif(c1=='5'):
                        if(c2=='1'):
                            agregar(p5, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            agregar(p5, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            agregar(p5, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            agregar(p5, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            agregar(p5, p5, resultado)
                            siono=True
                else:
                    if(c2=='1'):
                        agregarr(p1, resultado)
                    elif(c2=='2'):
                        agregarr(p2, resultado)
                    elif(c2=='3'):
                        agregarr(p3, resultado)
                    elif(c2=='4'):
                        agregarr(p4, resultado)
                    elif(c2=='5'):
                        agregarr(p5, resultado)
            elif(pagina[i]=='-'):
                c1=pagina[i-1]
                c2=pagina[i+2]
                if(siono==False):
                    if(c1=='1'):
                        if(c2=='1'):
                            quitar(p1, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            quitar(p1, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            quitar(p1, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            quitar(p1, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            quitar(p1, p5, resultado)
                            siono=True
                    elif(c1=='2'):
                        if(c2=='1'):
                            quitar(p2, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            quitar(p2, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            quitar(p2, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            quitar(p2, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            quitar(p2, p5, resultado)
                            siono=True
                    elif(c1=='3'):
                        if(c2=='1'):
                            quitar(p3, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            quitar(p3, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            quitar(p3, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            quitar(p3, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            quitar(p3, p5, resultado)
                            siono=True
                    elif(c1=='4'):
                        if(c2=='1'):
                            quitar(p4, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            quitar(p4, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            quitar(p4, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            quitar(p4, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            quitar(p4, p5, resultado)
                            siono=True
                    elif(c1=='5'):
                        if(c2=='1'):
                            quitar(p5, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            quitar(p5, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            quitar(p5, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            quitar(p5, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            quitar(p5, p5, resultado)
                            siono=True
                else:
                    if(c2=='1'):
                        quitarr(p1, resultado)
                    elif(c2=='2'):
                        quitarr(p2, resultado)
                    elif(c2=='3'):
                        quitarr(p3, resultado)
                    elif(c2=='4'):
                        quitarr(p4, resultado)
                    elif(c2=='5'):
                        quitarr(p5, resultado)
            elif(pagina[i]=='*'):
                c1=pagina[i-1]
                c2=pagina[i+2]
                if(siono==False):
                    if(c1=='1'):
                        if(c2=='1'):
                            por(p1, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            por(p1, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            por(p1, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            por(p1, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            por(p1, p5, resultado)
                            siono=True
                    elif(c1=='2'):
                        if(c2=='1'):
                            por(p2, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            por(p2, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            por(p2, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            por(p2, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            por(p2, p5, resultado)
                            siono=True
                    elif(c1=='3'):
                        if(c2=='1'):
                            por(p3, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            por(p3, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            por(p3, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            por(p3, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            por(p3, p5, resultado)
                            siono=True
                    elif(c1=='4'):
                        if(c2=='1'):
                            por(p4, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            por(p4, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            por(p4, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            por(p4, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            por(p4, p5, resultado)
                            siono=True
                    elif(c1=='5'):
                        if(c2=='1'):
                            por(p5, p1, resultado)
                            siono=True
                        elif(c2=='2'):
                            por(p5, p2, resultado)
                            siono=True
                        elif(c2=='3'):
                            por(p5, p3, resultado)
                            siono=True
                        elif(c2=='4'):
                            por(p5, p4, resultado)
                            siono=True
                        elif(c2=='5'):
                            por(p5, p5, resultado)
                            siono=True
                else:
                    if(c2=='1'):
                        porr(p1, resultado)
                    elif(c2=='2'):
                        porr(p2, resultado)
                    elif(c2=='3'):
                        porr(p3, resultado)
                    elif(c2=='4'):
                        porr(p4, resultado)
                    elif(c2=='5'):
                        porr(p5, resultado)
            elif(pagina[i]=='/'):
                c1=pagina[i-1]
                c2=pagina[i+1]
                if(siono==False):
                    if(c1=='1'):
                        corte(p1, eval(c2), resultado)
                        siono=True
                    elif(c1=='2'):
                        corte(p2, eval(c2),resultado)
                        siono=True
                    elif(c1=='3'):
                        corte(p3, eval(c2), resultado)
                        siono=True
                    elif(c1=='4'):
                        corte(p4, eval(c2), resultado)
                        siono=True
                    elif(c1=='5'):
                        corte(p5, eval(c2), resultado)
                        siono=True
                else:
                    corter(eval(c2), resultado)
                    
            elif(pagina[i]=='d'):
                c1=pagina[i+3]
                if(c2=='1'):
                    bajar(p1, resultado)
                elif(c2=='2'):
                    bajar(p2, resultado)
                elif(c2=='3'):
                    bajar(p3, resultado)
                elif(c2=='4'):
                    bajar(p4, resultado)
                elif(c2=='5'):
                    bajar(p5, resultado)
                siono=True    
                    
        mostrar(resultado)
        origen(resultado)
        siono=False
print("")
print("")
print("")
final=input("Ingrese cualquier tecla para terminar:")

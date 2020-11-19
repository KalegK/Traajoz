import numpy as np
import matplotlib.pyplot as plt



def f(x):
    y= ((x**3.0)/3.0)+((x**2.0)/2.0)+2.0*x-(17/6)
    return y

def f_prima(x):
    y=(x**2.0)+x+2.0
    return y

def f_prima_prima(x):
    y=(2.0*x)+1.0
    return y

def error_absoluto(valor_real, valor_cifras_significativas):
    #| real - punto flotante|
    return np.absolute((valor_real-valor_cifras_significativas))

def N_R_mejorado(P0):
    pn=P0
    pn_sig= pn - (f(pn)*f_prima(pn))/ ( f_prima(pn)**2  - f(pn)*f_prima_prima(pn))
    iteraciones=0
    while (1):
        #print(pn,pn -  (f(pn)*f_prima(pn))/ ( f_prima(pn)**2  - f(pn)*f_prima_prima(pn)) )
        pn=pn_sig
        pn_sig=pn - (f(pn)*f_prima(pn))/ ( f_prima(pn)**2  - f(pn)*f_prima_prima(pn))
        error = error_absoluto(pn,pn_sig)
        #print(error)
        iteraciones=iteraciones+1
        if(error <= 0.000001):
        	print("dinr")
        	break

    print("iteraciones: ", iteraciones)
    print("pn_sig", pn_sig)

def Newton_raphson(P_sub_0):
    P_sub_n=P_sub_0
    p_sig = P_sub_n- (1/f_prima(P_sub_n) )*f(P_sub_n)
    iteraciones = 0
    while(1):
    	#print(P_sub_n, (P_sub_n- (1/f_prima(P_sub_n) )*f(P_sub_n) ) ,iteraciones)
    	P_sub_n = p_sig
    	p_sig = P_sub_n- (1/f_prima(P_sub_n) )*f(P_sub_n)
    	error = (error_absoluto(P_sub_n,p_sig))
    	iteraciones = iteraciones + 1
    	#print(error)
    	if(error <= 0.000001):
    		print("di")
    		break
    	
    print("resultado: ", p_sig,"ite: " ,iteraciones)


def steffesen(P0):
    x0=P0
    iteraciones = 0
    x1 = x0 - (x0-f(x0))**2 / (f(f(x0)) - 2*f(x0) + x0)
    #print("\nx0, x1: ",x0, x1)
    while(1):
        #print(x0,  x0 - (x0-f(x0))**2 / (f(f(x0)) - 2*f(x0) + x0))
        x0 = x1
        x1=  x0 - (x0-f(x0))**2 / (f(f(x0)) - 2*f(x0) + x0) 
        iteraciones = iteraciones + 1
        error = error_absoluto(x0,x1)
        if(error <= 0.000001):
        	print("distef")
        	break
        #print("x0,x1: ",x0,x1)
    print("res: ", round(x1,6), "ite: ", iteraciones)

def Secante(P_sub_0,P_sub_1):
    P_sub_n1=P_sub_0
    P_sub_n2=P_sub_1
    cont=0
    while(((f(P_sub_n2)-f(P_sub_n1)))* f(P_sub_n1) != 0.0):
        print(P_sub_n1,P_sub_n2, P_sub_n1- ((P_sub_n2-P_sub_n1)/(f(P_sub_n2)-f(P_sub_n1)))* f(P_sub_n1))
        aux=P_sub_n2
        P_sub_n2=P_sub_n1- ((P_sub_n2-P_sub_n1)/(f(P_sub_n2)-f(P_sub_n1)))* f(P_sub_n1)
        P_sub_n1=aux
        cont=cont+1
    return P_sub_n1,P_sub_n2,cont

PS0=50
PS1=3

print("NR mejorado") 
N_R_mejorado(PS0)
print("\nniuton")
Newton_raphson(PS0)
print("\nsteffesen")
steffesen(PS0)
print("\nSecante")
Secante(PS0,PS1)

import math

#Amaury Mario Ribeiro Neto 

#soma de pontos para curvas elipcticas em corpos finitos
 
def calcular_pontos_curva (A, B, p):
    pontos = []
    X = []
    Y = []
    for i in range (0,p):  #calculando tabelinha de valores
        Y.append([i, (i**2) % p])  
        X.append([i, ( (i**3) + A*i + B) % p ])
    #print(Y) #debug
    #print(X)  #debug
    
    for i in range (0,p): 
        for j in range (0,p): 
            if( Y[i][1] == X[j][1] ): #verificando se cada Y é igual ao X da tabela, se for encontramos um ponto...
                pontos.append([ X[j][0], Y[i][0] ])

    pontos.append([math.inf,math.inf]) # acrescentando o ponto no infinito
    #print(pontos) #debug lista de pontos da curva
    return pontos

def pertence_curva(X, Y, A, B, p):

    pontos = calcular_pontos_curva(A, B, p)

    for i in range(len(pontos)): 
        if ( (pontos[i][0] == X) and (pontos[i][1] == Y) ): #verificando se tem algum ponto com o X igual ao passado
            return True
        #print(pontos[i][0], X) #debug
    return False

def algoritmo_euclidiano(a,b):
    x1 = 1; y1 = 0  
    x2 = 0; y2 = 1

    while b != 0: 
        quociente = a // b
        a, b = b, a - (quociente * b) #atualizando pares de valores ao mesmo tempo em python
        y1, x1 = x1, y1 - (quociente * x1)
        y2, x2 = x2, y2 - (quociente * x2)

    ###return mdc, x, y
    return a, y2, y1   

def modInverso (a, b):

    mdc, x, y = algoritmo_euclidiano(a, b) #algoritmo euclediano para obter somente o X desejado...

    if x<0:
        x += b 
    
    return x

def soma_pontos(P_X, P_Y, Q_X, Q_Y, A, B, p):

    if(P_X and P_Y and Q_X and Q_Y == 0): # 0 + 0 = 0
        return 0, 0

    elif (P_X == Q_X) and (P_Y == (-Q_Y % p)): # P + 'P = 0
        return 0, 0

    elif (P_X == 0) and (P_Y == 0) :  # 0 + Q = Q
        return Q_X, Q_Y

    elif (Q_X ==0 ) and (Q_Y == 0) : # P + 0 = P
        return P_X, P_Y 
    
    elif (P_X == Q_X) and (P_Y == Q_Y): # P = Q
        aux = (3*(P_X**2) + A) % p
        aux2 = (2*P_Y) % p
        M =  (aux * modInverso(aux2,p)) % p
        #print("M = ", M)  #debug

    else:
        aux = (P_Y - Q_Y) % p
        aux2 = (P_X - Q_X) % p
        M =  (aux * modInverso(aux2,p)) % p
        #print("M = ", M)  #debug

    R_X = ( M**2 - P_X - Q_X ) % p
    R_Y = ( -P_Y - M * (R_X - P_X) ) % p

    return R_X, R_Y

def main():
    '''soma de pontos em curvas elípticas sobre corpos finitos, com parâmetros da curva (coeficientes A e B),
     o módulo p e as coordenadas dos pontos a serem somados e a verificação para saber se os pontos de fato pertencem à curva).'''

    #coeficientes:
    A = 3
    B = 4
    #pontos P e Q
    P_X = 1 
    P_Y = 6
    Q_X = 5
    Q_Y = 5
    p = 7

    #alguns pontos para testar o programa: parametros
    # (5,8) + (12, 11) mod 13  = (6,12)
    # (1,1) + (5, 2) mod 7  = (5,5)
    # (0,2) + (2, 5) mod 7 = (2,2)
    # (1, 6) + (1, 6) mod 7 = (0, 5)  #pontos iguais
    # (0, 5) + (0, 0) mod 7 = (0,5)
    # (0, 0) + (2, 5) mod 7 = (2,5)
    # (1, 6) + (1, 1) mod 7 = (0,0) #soma do ponto e do inverso
    # (0, 0) + (0, 0) mod 7 = (0,0)

    print("\nA curva eliptica com os coeficientes A={0}, B={1} e  mod(p) = mod({2})".format(A,B,p))
    print("Os pontos que deseja verificar e somar sao: P=({0},{1}) e Q=({2},{3})".format(P_X, P_Y, Q_X, Q_Y))
    
    #verificando se o ponto pertence
    check = pertence_curva(P_X, P_Y, A, B, p)
    if not check :
        print("O Ponto P não pertence a curva")
        exit()

    check = pertence_curva(Q_X, Q_Y, A, B, p)
    if not check :
        print("O Ponto Q não pertence a curva")
        exit()

    #verificação terminada
    R_X, R_Y = soma_pontos(P_X, P_Y, Q_X, Q_Y, A, B, p) #valor de R'

    print("Os pontos pertencem a curva eliptica e a soma dos pontos é dada por: R'=({0},{1})\n".format(R_X,R_Y))

if __name__ == "__main__":

    print("\nPrograma para calcular soma de pontos em curvas elipticas sobre CORPOS FINITOS e também verificação de pontos pertencentes a curva")   
    print("A representação para pontos no infinito e: (inf) definido pela biblioteca math.inf")

    main()
    print("FIM do programa")
#matriz_ori = [[1,2,4,3,2],[1,1,3,2,3],[0,2,1,3,2],[0,0,1,0,3],[0,0,0,-1,-8]] # 5x5
matriz_ori = [ [ 1 , 1 ,3 ] , [ 1, 0 , 1 ] , [ 1 , -2 , -1 ] ] # 3x3
#matriz_ori = [[1,-2,2,2],[0,4,-2,1],[1,-2,4,0],[1,-1,2,2] ] #4x4
#matriz_ori = [[2,1,3],[-1,2,4],[0,1,3]] # 3x3

def imprimir_matriz (matriz_final):
    for i in range(len(matriz_final)):
        a = ''
        for j in range(len(matriz_final)):
            a += str(matriz_final[ i ][ j ])
            if j < len(matriz_final)-1:
                a += '  '
        print(a)
        
def print_matrices (matriz , matriz_id):
    for i in range(len(matriz)):
        a = ''
        
        for j in range(len(matriz)):
            a += str(matriz[i][j])
            if j < len(matriz)-1:
                a += '  '
                
        a += "  |  "   
        for k in range(len(matriz)):
            a += str(matriz_id[i][k])
            if k < len(matriz)-1:
                a += '  '
                
        print(a)
                
def matriz_identidad (matriz_o):
    matriz_iden = []
    for i in range(len(matriz_o)):
        m_resul = []
        for j in range(len(matriz_o)):
            if j == i : 
                m_resul += [1]
            else:
                m_resul += [0]
        matriz_iden += [m_resul]
    return(matriz_iden)

##################################################################

def determinante (valores , posicion ,m_co):# valores | posicion | matriz copia
    #=====CAMBIOS DE NOMBRE=====
    val = valores[ 0 ]
    diag = valores[ 1 ]
    v = posicion[0] # i
    d = posicion[1] # j
    #=========================
    m_resul = []
    
    if val != 0:
        if diag%val == 0:
            x = diag//val
            for j in range(len(m_co)):
                m_resul += [-m_co[d][j] * 1 + m_co[v][j] * x]
            m_co[v] = m_resul
            
        elif val%diag == 0 :
            x = val//diag
            for j in range(len(m_co)):
                m_resul += [-m_co[d][j] * x + m_co[v][j] * 1]
            m_co[v] = m_resul
            
        else:
            for j in range(len(m_co)):
                m_resul += [-m_co[d][j] * val + m_co[v][j] * diag]
            m_co[v] = m_resul

##################################################################

def verificar_m (matriz):
    n = matriz
    filas = len(n)
    columnas = len(n[0])
    
    if filas == columnas:
        cant = -1 
        determi = 1 # es 1 para poder multiplicar
        c = list(n) # copia de la matriz
        
        for i in range(len(c)):# columnas
            for j in range(len(c)):# filas 
                if j > cant:
                    if j != i:
                        a = [c[ j ][ i ],c[ i ][ i ]] # 01 | 00 
                        b = [ j , i ] 
                        determinante (a , b , c )
            cant += 1 
        
        for h in range(filas):# recorre la diagonal
            determi *= c[h][h] # multiplica
        #print(determi)
        
        if determi != 0:
            return True
        else:
            return False
        
#######################################

def m_inversa (numero ,posicion):
    #======= MENU =======
    # ma_o = matriz_ori 
    # ma_i = matriz_iden
    val = numero[ 0 ] # numeros de las esquinas
    diag = numero[ 1 ] # numeros de la diagonal
    n_v = posicion[ 0 ]#k
    n_d = posicion[ 1 ]#i
    #===================
    resta = []
    resta_i = []
    
    for j in range(len(matriz_ori)):
        resta += [round(-matriz_ori[n_v][j]*diag + matriz_ori[n_d][j]*val,2)]
        resta_i += [round(-matriz_iden[n_v][j]*diag + matriz_iden[n_d][j]*val,2)]
    
    matriz_iden[n_d] = resta_i # matriz identidad
    matriz_ori[n_d] = resta # matriz original
    
    print(" ------------ ")
    print_matrices (matriz_ori , matriz_iden)
    #print(" ------------ ")
    
def matriz_inversa(m_n,m_id):# matriz final 
    if verificar_m(m_n)==True:
        tam = len(m_n) # tamaño de la matriz
        cant = -1
        
        for i in range(tam): # columnas
            for k in range(tam): # filas
                if k > cant: # solo toma esta parte ◣ de la matriz 
                    if k == i : # solo lo numeros de la diagonal ╲ 
                        if m_n[k][k] !=1: # si los valores de la  ╲ es diferente de 1
                            divi = [] 
                            divi_id = []
                            d = m_n[k][k] 
                            
                            for j in range(tam):
                                divi += [round( m_n[k][j]/d , 2)]
                                divi_id += [round( m_id[k][j]/d , 2)]
                            m_n[k] = divi
                            m_id[k] = divi_id
                            
                    if k !=i:# toma los valores de abajo de la diagonal 
                        nums = [m_n[i][i] , m_n[k][i] ]
                        posi = [i , k]
                        m_inversa(nums , posi)
            cant += 1
        # toma estos valores ◥, de la matriz
        for a in range(tam):# columnas
            for b in range(a):# filas
                valores = [ m_n[a][a] , m_n[b][a] ]
                posi_ = [a , b]
                m_inversa(valores , posi_)
    else:
        print("NO puede ser una matriz inversa")
        
imprimir_matriz(matriz_ori)

matriz_iden = matriz_identidad (matriz_ori)
matriz_inversa (matriz_ori , matriz_iden)

print("\n MATRIZ ")
imprimir_matriz(matriz_ori)
print("\n MATRIZ IDENTIDAD")
imprimir_matriz(matriz_iden)
      




#matriz_ori = [ [ 1 , 2 ,3 ] , [ 4, 5 , 6 ] , [ 7 , 8 , 9 ] ]
matriz_ori = [ [ 1 , 1 ,3 ] , [ 1, 0 , 1 ] , [ 1 , -2 , -1 ] ]
#matriz_ori = [ [ 1 , 1 ,3 ] , [ 0, 1 , 2 ] , [ 0 , 0 , 1 ] ]
def imprimir_matriz (matriz_final):
    for i in range(len(matriz_final)):
        a = ''
        for j in range(len(matriz_final)):
            a += str(matriz_final[ i ][ j ])
            if j < len(matriz_final)-1:
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
    #imprimir_matriz (matriz_iden)
matriz_iden = matriz_identidad (matriz_ori)

############################################

def determinante (valor_1 , valor_2,m_copia,): # solo determinante
    #=====CAMBIOS DE NOMBRE=====
    val = valor_1[ 0 ]
    diag = valor_1[ 1 ]
    v = valor_2[0] # i
    d = valor_2[1] # j
    m_o = m_copia
    #=========================
    #print(m_o)
    m_resul = []
    m_resul_id = []
    if diag%val == 0:
        x = diag//val
        for j in range(len(m_o)):
            m_resul += [-m_o[d][j] * 1 + m_o[v][j] * x]
        m_o[v] = m_resul
        
        print(m_resul)
        
    elif val%diag == 0:
        x = val//diag
        for j in range(len(m_o)):
            m_resul += [-m_o[d][j] * x + m_o[v][j] * 1]
        m_o[v] = m_resul
        
        print(" ")

    elif val%2 !=0 and diag%2==0:
        for j in range(len(m_o)):
            m_resul += [- m_o[d][j] * val + m_o[v][j] * diag]
        m_o[v] = m_resul
        
        print(m_resul)
        print(m_resul_id)
        
    elif diag%2 !=0 and val%2==0:
        for j in range(len(m_o)):
            m_resul += [- m_o[d][j] * val + m_o[v][j] * diag]
        m_o[v] = m_resul
        iden[v] = m_resul_id
        print(m_resul)
        print(m_resul_id)
    
        
########################################

'''def verificar_m (matriz):
    imprimir_matriz (matriz_ori)
    n = matriz
    filas = len(n)
    columnas = len(n[0])
    if filas == columnas:
        num_ceros = ((filas*columnas) -filas) // 2 #cantidad de numeros para convertir en ceros
        determi = 1
        c = list(n)
        for i in range(num_ceros):
            for j in range(i):
                a = [c[ i ][ j ],c[ j ][ j ]]
                b = [ i , j ]
                #print("Valor = ",c[ i ][ j ],"  Diagonal = ",c[ j ][ j ])
                determinante (a , b , c )
        imprimir_matriz(c)
        
        for h in range(filas):
            determi *=c[h][h]
        print(determi)
        if determi != 0:
            return True
        else:
            return False'''
#######################################

def m_inversa (numero ,posicion):
    #======= MENU =======
    ma_o = matriz_ori # no
    ma_i = matriz_iden
    val = numero[ 0 ] # numeros de las esquinas
    diag = numero[ 1 ] # numeros de la diagonal
    n_v = posicion[ 0 ]#i
    n_d = posicion[ 1 ]#k
    print("a: ",n_v,"    b",n_d)
    print("val: ",val,"diag: ",diag)
    
    #===================
    resta = []
    resta_i = []
    for j in range(len(ma_o)):
        #resta += [-ma_o[n_v][j]*val + ma_o[n_d][j]*diag]
        #resta_i += [-ma_o[n_v][j]*val + ma_o[n_d][j]*diag]
        resta += [-ma_o[n_v][j]*diag + ma_o[n_d][j]*val]
        resta_i += [-ma_i[n_v][j]*diag + ma_i[n_d][j]*val]
        #print(-ma_o[n_v][j],val ,"+", ma_o[n_d][j],diag)
       #print( -ma_o[n_v][j],diag ," + ", ma_o[n_d][j],val )
    #print(resta,n_d)
    ma_i[n_d] = resta_i
    ma_o[n_d] = resta
    
        
    
def matriz_inversa(m_normal , m_identidad):# matriz final
    # ______ Cambiar Nombre _______
    m_n = m_normal
    m_id = m_identidad
    # ________________________________
    
    #if verificar_m(m_n)==True:
    tam = len(m_n) # tamaño de la matriz
    cant = -1
    for i in range(tam):
        for k in range(tam):
            if k > cant:
                #print("k: ",k,"cant: ",cant, "i: ",i)
                if k == i : #encontra la diagonal 
                    if m_n[k][k] !=1:
                        divi = []
                        divi_id = []
                        d = m_n[k][k]
                        for j in range(tam):
                            divi += [round( m_n[k][j]/d , 2)]
                            divi_id += [round( m_id[k][j]/d , 2)]
                        m_n[k] = divi
                        m_id[k] = divi_id
                if k !=i:
                    #print("i: " , i , "k: " , k)
                    #print(m_n[i][i] , m_n[k][i])
                    nums = [m_n[i][i] , m_n[k][i] ]
                    posi = [i , k]
                    m_inversa(nums , posi)
        #print(m_n)
        cant += 1
    for a in range(tam):
        for b in range(a):
            valores = [ m_n[a][a] , m_n[b][a] ]
            posi_ = [a , b]
            m_inversa(valores , posi_)
            
matriz_inversa (matriz_ori , matriz_iden)
#print(matriz_ori)
print("\n MATRIZ ")
imprimir_matriz(matriz_ori)
print("")
print("MATRIZ IDENTIDAD")
imprimir_matriz(matriz_iden)
      




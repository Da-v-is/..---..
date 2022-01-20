matriz_ori = [ [ 1 , 1 ,3 ] , [ 1, 0 , 1 ] , [ 1 , -2 , 1 ] ]
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

def determinante (valor_1 , valor_2,m_copia,):# solo determinante
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
    #FALTA EL INVERSO DE ARRIBA
    

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
    
def m_inversa (numero ,posicion):
    #======= MENU =======
    ma_o = matriz_ori
    val = numero[ 0 ]
    diag = numero[ 1 ]
    n_v = posicion[ 0 ]#i
    n_d = posicion[ 1 ]#j
    #print(n_v,"----",n_d)
    #===================
    m_resul = [ ]
    m_resul_in = [ ]
    print(ma_o)
    for j in range(len(ma_o)):
        m_resul += [ round(-ma_o[ n_d ][ j ]*val + ma_o[ n_v ][ j ] , 2)] 
        print("---------",-ma_o[ n_d ][ j ],val , ma_o[ n_v ][ j ] )
    ma_o[n_v] = m_resul
        
    
def matriz_inversa(m_normal , m_identidad):# matriz final 
    m_n = m_normal
    m_in = m_identidad
    #if verificar_m(m_n)==True:
    tam = len(m_n)
    for i in range(tam):
        #print(m_n[i][i])
        
        dg = m_n[i][i]
        print(dg)
        
        opera = []
        opera_2 = []
        for k in range(i):
            print("aaa", k)
        if dg != 1:
            print("1111")    
            #---- cambiar las diagonales por UNO -----
            '''for j in range(len(m_n)):
                opera += [round(m_n[i][j]/dg , 2)]
                opera_2 += [round(m_in [i][j]/dg , 2)]
            m_n[i] = opera
            m_in[i] = opera_2'''
                
            #-------------------------------------------------
        else:
            print("22222")
            

      
matriz_inversa (matriz_ori , matriz_iden)
#print(matriz_ori)
imprimir_matriz(matriz_ori)

      




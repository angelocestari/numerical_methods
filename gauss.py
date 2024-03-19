import numpy as np

def elim_gauss(A, b):
    n = A.shape[0] # Número de equações
    # Altera a matriz A até transformá-la em triangular superior
    print('Matriz A inicial: \n', A, '\n', b, '\n---------------')
    for k in range(n - 1):
        # Faz a verificação se o pivô é zero
        if A[k,k] == 0:
            for i in range(k + 1, n):
                if A[i, k] != 0:
                    A[[k,i]] = A[[i,k]] # Troca as linhas da matriz A
                    b[[k,i]] = b[[i,k]] # Troca as linhas de b
                    print('Matriz após troca de pivô: \n', A, '\n', b, '\n---------------')
                    break
                else:
                    print('Não foi possível encontrar um pivô não nulo.')
                    return None
        # Faz as operações para zerar abaixo da diagonal principal        
        for i in range(k + 1, n):
            xmult = A[i, k] / A[k, k] # Encontra o multiplicador
            A[i, k:] = A[i, k:] - xmult * A[k, k:] 
            b[i] = b[i] - xmult * b[k]
        print(f'Passo {k + 1}: \n', A, '\n', b, '\n------------')
    
    x = np.zeros(n) # matriz para colocar os resultados
    if A[-1, -1] == 0: 
        print('Divisão por zero detectada no último passo!')
        return None
    
    x[-1] = b[-1] / A[-1, -1]
    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i,i]
    
    return x


A = np.array([[1, 4, 0],
              [2, -1, 0],
              [0, 3, 1]])

b = np.array([6,3,5])

resultado = elim_gauss(A, b)
print('Resultado:', resultado)


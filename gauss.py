import numpy as np

def elim_gauss(A, b):
    n = A.shape[0] 
    for k in range(n - 1):
        for i in range(k + 1, n):
            if A[k,k] == 0:
                print('Divisão por zero detectada!')
                return None
            xmult = A[i, k] / A[k, k]
            A[i, k:] = A[i, k:] - xmult * A[k, k:]
            b[i] = b[i] - xmult * b[k]
        print(f'Passo {k + 1}: \n', A, '\n', b, '\n------------')
    
    x = np.zeros(n)
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

b = np.array([6, 3, 5])

resultado = elim_gauss(A, b)
print('Resultado:', resultado)


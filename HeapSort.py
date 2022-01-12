#Criação do codígo do heapsort.
#O algoritmo faz a ordenação de um vetor
#por meio do uso de heaps.


#Criando o Heap
def heapStart(arr, tam, i):
    auxiliar = i #To muito sem entender se vale a pena por isso.
    auxiliar2 = arr[i]
    l = 2*i + 1 #Valores de index da Esquerda do heap (Impares).
    r = 2*i + 2 #Valores de index da Direita do heap (Pares).


    #Vamos usar os auxiliares para alterar a nossa raiz
    #sem necessariamente criar uma arvore.


    if l < tam and auxiliar2 < arr[l]:
        auxiliar = l
        auxiliar2 = arr[l]

    if r < tam and auxiliar2 < arr[r]:
        auxiliar = l
        auxiliar2 = arr[r]

    if auxiliar2 != arr[i]:
        arr[i], arr[auxiliar] = arr[auxiliar], arr[i]

        

    


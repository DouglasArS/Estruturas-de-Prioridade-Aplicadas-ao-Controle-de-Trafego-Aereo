#Criação do codígo do heapsort.
#O algoritmo faz a ordenação de um vetor
#por meio do uso de heaps.


#Criando o Heap
def heapStart(arr, tam, i):
    #arr = é um array
    #tam = é o 'len' do array
    #i = susposto "endereço" da raiz

    #Nessa heap não iremos criar diretamente uma arvore, e sim emular uma
    #dentro de um vetor estatico.
    #Sabendo disso fica mais facil o entendimento do algoritmo.

    auxiliar = i #Nessa Variavel auxiliar vamos armazenar o "endereço" da raiz.
    auxiliar2 = arr[i] #Nessa vamos armazenar o valor da raiz.

    #Nessa proxima parte criamos a logica por tras da "arvore" criada.

    e = 2*i + 1 #Valores de index da Esquerda do heap (Impares).
    d = 2*i + 2 #Valores de index da Direita do heap (Pares).


    #Vamos usar os auxiliares para alterar a nossa raiz
    #sem necessariamente criar uma arvore.

    #Comparamos o Valor imediatamente a esquerda da raiz com a raiz.
    #Se for maior, passamos a referenciar esse valor como uma nova raiz
    #mesmo não tendo feito a troca ainda.
    if e < tam and auxiliar2 < arr[e]:
        auxiliar = e
        auxiliar2 = arr[e]

    
    #Comparamos o Valor imediatamente a direita da raiz com a raiz.
    #Se for maior, passamos a referenciar esse valor como uma nova raiz
    #mesmo não tendo feito a troca ainda.
    if d < tam and auxiliar2 < arr[d]:
        auxiliar = d
        auxiliar2 = arr[d]


    #Nesse if, vemos se houve alteração na raiz, caso tenha, efetuamos a troca
    #no vetor.
    if auxiliar2 != arr[i]:
        arr[i], arr[auxiliar] = arr[auxiliar], arr[i]


    #Entedemos que essa troca afeta apenas 3 elementos dentro do vetor estatico
    #logo usamos a recursividade para usarmos tanto o valor a esquerda quanto a 
    #direita como se fosse uma sub-arvore, assim percorrendo o vetor todo.
    heapStart(arr, tam, e)
    heapStart(arr, tam, d)


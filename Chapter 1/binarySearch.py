#Algoritmo de busqueda binaria. Consiste en tomar el dato de la mitad del arreglo, compararlo con nuestro dato
# y dependiendo de si es mayor o menor, proceder al mismo procedimiento en una de las mitades restantes.
#Variables
cards = [13, 10, 8, 7, 5, 3, 2]
query = 10

#Función principal
def locateCards(cards, query):
    lo, hi = 0, len(cards) - 1 #Valor minimo y máximo del arreglo
    
    #Mientras que el minimo sea menor o igual que el máximo, evitando errores por arreglos vacíos
    while lo <= hi:
        mid = (lo + hi) // 2 #Mitad del arreglo
        midNumber = cards[mid] #Dato que se encuentra a la mitad
        
        print("lo: ", lo, "hi: ", hi, "mid: ", mid, "midNumber: ", midNumber)
        
        #Si el dato a la mitad es igual a nuestra busqueda, se regresa
        if midNumber == query:
            return mid
        elif midNumber < query:  #Si es menor, el valor alto se pone antes del primer valor de mitad
            hi = mid - 1
        elif midNumber > query:  #Si es mayor, el valor bajo se pone despues del primer valor de mitad
            lo = mid + 1
        
    return - 1
    
locateCards(cards, query)

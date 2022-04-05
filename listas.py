from tkinter import N


inicio =0
fin=-1
indice=2
salto=1


#index:      0    1     2      3      4
lista_l= ["hola", "soy", "Nico",[1,2],3] 
print ("\n*****elementos de la lista*****\n")
print (lista_l[0])
print (lista_l[1])
print (lista_l[2])
print (lista_l[3][0])
print (lista_l[3][1])
print (lista_l[4])
print (lista_l[-1])


print ("\n*****formatear elementos de la lista*****\n")
print ("las cadenas son: " +lista_l[0]+" "+lista_l[1]+" "+lista_l[2])
print("los elementos formateados son: " +str(lista_l[3])+" y " +str(lista_l[4]))


print ("posicion inicial:" + str(inicio)+"\n")
print ( lista_l[inicio])

print ("posicion final:" + str(fin)+"\n")
print (lista_l[fin])

print("\n*********particionado versus numeros magicos********\n")
print("imprimir listas:" "\n")
print(lista_l)

####lista (inicio:fin)#####
######se omite el ultimo elemento (fin)#####
print("\n particionado:lista(inicio:fin)\n")
print(lista_l[0:4]) ##no saldra el ultimo##
print(lista_l[0:])#tomara datos hasta el fin##

#lista(onicio:fin:salto)
print("\n particionado: lista(inicio:fin:salto)")
print("lista: (0:2:1)\n")
print(lista_l[0:2:1])

print("\nparticionado:lista(inicio:fin:salto)")
print("constantes: lista(inicio:indice:salto)\n")
print(lista_l[inicio:indice:salto])

print("\n mostrar datos de dos en dos \n") #ojo que aqui si la lista es impar solo se imprime el ultimo par
print(lista_l[::2])

#####para modificar un dato#####
lista_l[0]="holy"
print(lista_l)

####para crear lista vacia o lista nueva para ingresar datos###
lista_2=[]
print(lista_2)

#######para agregar un elemento o varios en una lista dentro de otra lista####
lista_l.append([10])
print (lista_l)
lista_l.append([5,6,7,8,9])
print(lista_l)


#########para agregar varios elementos independientes a la lista#########
lista_l.extend([5,6,7,8,9])
print(lista_l)
#######para saber la extencion de una lista (cuantos elementos tiene)####
len(lista_l)
print(len(lista_l))

#######para saber que lugar ocupa un elemente en la lista######
print ("index de un elemento:lista_l.index (elemento)")
print("holy ocupa la posicion: ", lista_l.index("holy"))

####para eliminar un elemento de la lista#####
lista_l.remove(3)
print(lista_l)
###para eliminar un elemendo por el indice######
lista_l.pop(0)
print(lista_l)

#####para saber cuantas veces se repite un elemento en la lista#####
lista_l.count(3)
print("el numero 3 se repite %d veces en la lista: "  %(lista_l.count (3)))

#####para invertir el contenido de una lista#######
lista_l.reverse ()
print(lista_l)



#Estilo de Python Pep8

platillos = ["Pollo Tipico", "Pinchos", "Chuleta", "lasagna", "Camarones Empanizados"]

pedidos = []


def imprimir_menu():
	print("1 Mostrar Platillos")
	print("2 Agregar Pedido")
	print("3 Imprimir Pedidos")
	print("4 Eliminar Pedidos")
	print("5 Salir")
	print("0 Almacenar pedidos")
	
	valor = int(input("Escriba el numero de la accion que desea realizar"))
	return valor

def mostrar_platillos():
	print("Listado de Platillos Disponibles")

	for platillo in platillos:
		print(platillos)


def agregar_pedido():
	plato = input("Escriba el nombre del platillo que desea")
	cantidad = int(input("Escriba la cantidad de platillos que desea"))
	mesa = int(input("Escriba el numero de la mesa"))
	pedido = "{0}, cantidad: {1}, mesa: {2}".format(plato, cantidad, mesa)

	pedidos.append(pedido)
#Estilo de Python Pep8

platillos = ["Pollo Tipico", "Pinchos", "Chuleta", "lasagna", "Camarones Empanizados"]

pedidos = []


def imprimir_menu():
	print("1 Mostrar Platillos")
	print("2 Agregar Pedido")
	print("3 Imprimir Pedidos")
	print("4 Eliminar Pedidos")
	print("5 Salir")
	print("0 Almacenar pedidos")
	
	valor = int(input("Escriba el numero de la accion que desea realizar"))
	return valor

def mostrar_platillos():
	print("Listado de Platillos Disponibles")

	for platillo in platillos:
		print(platillos)


def agregar_pedido():
	plato = input("Escriba el nombre del platillo que desea")
	cantidad = int(input("Escriba la cantidad de platillos que desea"))
	mesa = int(input("Escriba el numero de la mesa"))
	pedido = "{0}, cantidad: {1}, mesa: {2}".format(plato, cantidad, mesa)

	pedidos.append(pedido)


def mostrar_pedidos():
	print("Listado de Pedidos Pendientes")
	
	for pedido in pedidos:
		print(pedido)

def eliminar_pedidos():
	pedidos = []
	print("se eliminaron todos los pedidos")

def almacenar():
	f = open("pedidos.txt", "w+")
	for pedido in pedidos:
		f.write(pedido)

continuar = True

while continuar:
	accion = imprimir_menu()
	if accion == 1:
		mostrar_platillos()
	elif accion == 2:
		agregar_pedido()
	elif accion == 3:
		mostrar_pedidos()
	elif accion == 4:
		eliminar_pedidos()
	elif accion == 5:
		continuar = False
	else:
print("Accion Desconocida")

def mostrar_pedidos():
	print("Listado de Pedidos Pendientes")
	
	for pedido in pedidos:
		print(pedido)

def eliminar_pedidos():
	pedidos = []
	print("se eliminaron todos los pedidos")

def almacenar():
	f = open("pedidos.txt", "w+")
	for pedido in pedidos:
		f.write(pedido)

continuar = True

while continuar:
	accion = imprimir_menu()
	if accion == 1:
		mostrar_platillos()
	elif accion == 2:
		agregar_pedido()
	elif accion == 3:
		mostrar_pedidos()
	elif accion == 4:
		eliminar_pedidos()
	elif accion == 5:
		continuar = False
	else:
print("Accion Desconocida")

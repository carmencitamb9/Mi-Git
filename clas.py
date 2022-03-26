class cliente:
    def cliente (objetocliente):
        objetocliente.nombre= "Laura L"
        objetocliente.edad= 20
        objetocliente.rut= "12.230.000-3"
        objetocliente.direccion= "Los montes 015"
    def reserva_pasaje(objetocliente,cantidad):
        objetocliente.reserva= "uno"
    def retiro_pasaje(objetocliente,cantidad):
        objetocliente.retiro="uno"

if  cliente   =="objetocliente":
    pasajero=cliente()
    print ("****************pasajero***************")
    print ("nombre:", pasajero.nombre)
    print ("edad:", pasajero.edad)
    print ("rut:" , pasajero.rut)
    print ("direccion:" , pasajero.direccion)
    print("reserva_pasaje:", pasajero.reserva)
    print("retiro_pasaje:", pasajero.retiro)


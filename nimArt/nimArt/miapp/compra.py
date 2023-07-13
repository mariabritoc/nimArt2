    
class carrito:
    def __init__(self,request):
        self.request = request
        self.session =request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito 
    #CREA UN OBJETO VEHICULO CRUD
    def agregar_producto(self, producto):
        if producto.nombre not in self.carrito.keys():
            self.carrito[producto.nombre]={
                'nombre' : producto.nombre,
                'precio' : producto.precio,
                'descripcion' : producto.descripcion,
                'cantidad' : 1,
                'total' : producto.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key == producto.nombre:
                    value['cantidad'] = value['cantidad']+1
                    value['precio'] = producto.precio
                    value['total'] = float(value['total']) + producto.precio

                    break
       
        total_carrito = sum(value['total'] for value in self.carrito.values() if isinstance(value, dict))
        self.carrito['total'] = total_carrito
        self.guardar_carrito()
    
    #GUARDA UN VEHICULO CRUD
    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True
    #ELIMINA UN VEHICULO CRUD
    def eliminar(self, producto):
        id= producto.nombre
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    #ELIMINA LA CANTIDAD, EL VALOR DEL VEHICULO SEGUN EL KEYS Y ELIMINA EL VEHICULO -- ELIMINA EL VEHICULO ELEGIDO SEGUN PATENTE
    def restar (self, producto):
        for key , value in self.carrito.items():
            if key == producto.nombre:
                value['cantidad'] = value['cantidad']-1
                value['total'] = float(value['total']) - producto.precio

                if value['cantidad']<1:
                    self.eliminar(producto)
                break
        self.guardar_carrito()
    #LIMPIA EL INGRESO
    def limpiar(self):
        self.session['carrito']={}
        self.session.modified= True 

    


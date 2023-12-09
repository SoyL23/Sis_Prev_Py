validaciones = {
        'max_len' : 25,
        'min_len':4,
        'type_data': str,
        }
validaciones_password = {
    'max_len':16,
    'min_len':8,
    'regex':''
}

class Validar_User():

    def validar_nombre(self, nombre):
        if len(nombre) > validaciones['max_len'] or len(nombre) < validaciones['min_len']:
            mensaje = 'El nombre debe tener entre 4 y 25 caracteres'
            print(mensaje)
            return False
        if type(nombre) == validaciones['type_data']:
            mensaje = 'Tipo de dato no válido'
            print(mensaje)
            return False
        return True
        
    def validar_apellido(self, apellido): 
        if len(apellido) > validaciones['max_len'] or len(apellido) < validaciones['min_len']:
            return 'El apellido debe tener entre 4 y 25 caracteres'
        if type(apellido) == validaciones['type_data']:
            return 'Tipo de dato no válido'
        

    def validar_email(self):
        pass
    def validar_username(self):
        pass
    def validar_password(self, password):
        if len(password) > validaciones_password['max_len'] or len(password) < validaciones_password['min_len']:
            return 'La contraseña debe tener entre 8 y 16 caracteres'
        pass
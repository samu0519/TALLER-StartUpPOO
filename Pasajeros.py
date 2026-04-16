class Pasajero:
    def __init__(self, id, nombre, edad, numtlf):
        if id < 12:
            raise ValueError("Esa monda ta mala")
        self.__id = id #Se asigna como privado
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_numtlf(numtlf)

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_numtlf(self):
        return self.__numtlf

    # Setters
    def set_nombre(self, new_nom):
        """Validación del nombre con resstricción de solo caracter de texto"""
        
        if not new_nom.replace(" ","").isalpha(): #con isalpha podremos verificar si se poseen solo caracteres de texto pero si tiene espacios lo marca invalido, para eso se utiliza el replace para eliminar temporalmente los espacios y el isalpha pueda trabajar 
            raise TypeError("Solo se permiten caracteres de texto")
        self.__nombre = new_nom.upper() .strip() #Strip es para eliminar los espacios y upper para todo en mayuscula
        """Se aplica raise para que tome el valor de error y detenga el programa"""


    def set_edad(self, new_edad):
        """Validación de la edad con resstricción de numeros de 0 a 120
            solo podrá contener números"""
       
        if new_edad < 0 or new_edad > 120:
            raise ValueError("Edad no valida") 
        self.__edad = new_edad
        print("Numero valido registrao")
        """Se aplica raise para que tome el valor de error y detenga el programa"""
          
    def set_numtlf(self, new_numtlf):
        """Validación de la numero de telefono tiene una resstricción de caracteres de 12 y
            solo podrá contener números"""
       
        if not new_numtlf.isdigit(): #isdigit verifica los caracteres sean numeros dentro de un caracter tipo str
            raise ValueError("Solo se permiten números")
        if not len(new_numtlf) == 10: #Len lee longitud del string en numeros
            raise ValueError("Número no valido")
        self.__numtlf = new_numtlf
        """Se aplica raise para que tome el valor de error y detenga el programa"""


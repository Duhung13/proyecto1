class Resultado:
    def __init__(self, nombre, formula, valor_obtenido, limite_inferior, limite_superior):
        self.nombre = nombre
        self.formula = formula
        self.valor_obtenido = valor_obtenido
        self.limite_inferior = limite_inferior
        self.limite_superior = limite_superior

    def es_aceptable(self):
        return self.limite_inferior <= self.valor_obtenido <= self.limite_superior
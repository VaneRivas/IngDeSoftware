#*****************************************************************************
# Clase : Articulo.py
#
# Descripcion : Clase que implementa los Articulos a presentar en el CLEI
#
# Autores : Vanessa Rivas . #  carnet: 10-10608
#           Gabriel Russo   #  carnet  08-11021
# Grupo :1 
# Seccion : 1
#
#*****************************************************************************
class Articulo:

    def __init__(self, Id, Titulo, Autor, Palabras_Claves, Topico):
        """Constructor"""
        self.Id_Articulo = Id
        self.Titulo = Titulo
        self.Autor = Autor
        self.Palabras_Claves = Palabras_Claves
        self.Topico = Topico
        self.Jurado = []                # Arreglo de miembro_cp que evaluan el articulo
        self.Aceptable = False            # es true si el puntaje promedio del articulo es mayot o igual a 3,00
        self.Calificaciones = []            # almacena el voto de cada miembro de cp
        self.Puntaje_promedio = 0
        
    def Calificar(self, miembro_cp, puntuacion):
        """ Metodo : Calificar
       Parametros : self 
             Miembro_Cp  miembro_cp, 
             int  puntuacion (entero entre 1 y 5)
       Descripcion; dado un miembro del cp y una puntuacion se le asigna
                      esa calificacion al articulo
      """
    # se verifica que un miembro no vote mas de una vez
        if miembro_cp in self.Jurado:
            print('ya voto')
            return False
        else:
            #si la puntuacion es valida se alamacena en el arreglo de Calificaciones
            # y se registra el miembro que voto por el articulo en el arreglo Jurado
            if puntuacion >= 1 and puntuacion <= 5:
                self.Calificaciones.append(puntuacion)
                self.Jurado.append(miembro_cp) 
                return True
            else:
                print('La calificacion no tuvo exito : puntaje invalido, debe ingresar un numero del 1 al 5,')
                return False
              
    def calcular_promedio(self):
        """ Metodo : calcular_promedio
       Parametros : self
       Descripcion; toma el arreglo de Calificaciones y suma cada uno de los
                       votos dividiendolo por el numero de votantes
      """
        self.Puntaje_promedio = 0 
        for n in self.Calificaciones:
            self.Puntaje_promedio += n
        if len(self.Calificaciones) > 0:
            self.Puntaje_promedio = self.Puntaje_promedio/(float(len(self.Calificaciones)))
            
    def verificar_Aceptable(self):
        """ Metodo : verificar_Aceptable
       Parametros : self
       Descripcion; calcula el puntaje promedio de un articulo, si es mayor
                       o igual a 3,00 coloca el atributo aceptable en True, sino permanece False
      """
        self.Aceptable = False
        if len(self.Jurado) > 1:
            self.calcular_promedio()
            if self.Puntaje_promedio >= 3.0:
                self.Aceptable = True
        return self.Aceptable
        
            
    def to_String(self):
        """ Metodo : to_String
       Parametros : self
       Descripcion; imprime en un string los datos de un articulo
      """
        datos_articulo = '\n\nId_Articulo: ' + str(self.Id_Articulo)
        datos_articulo += '\nTitulo: ' + str(self.Titulo)
        datos_articulo += '\nAutor: ' + self.Autor.Nombre +' '+self.Autor.Apellido
        #if len(self.Autor) > 0:
        #for i in self.Autor:
        #p = i.to_String
        #datos_articulo += p
        #datos_articulo += '\nPalabras Claves: '
        #if len(self.Palabras_Claves) > 0:
        #    for i in self.Palabras_Claves:
        #        datos_articulo += i+' '
        datos_articulo += '\nTopico: ' + self.Topico.Nombre
        if self.Aceptable:
            datos_articulo += '\nAceptable: Si' 
        else:
            datos_articulo += '\nAceptable: No'
        datos_articulo += '\nPuntaje promedio: ' + str(self.Puntaje_promedio) + '\n\n'
        return datos_articulo
    
#if __name__ =="__main__":

        #art = Articulo(1,"Titulo1", "Pedro Perez", ["Palabra" ,"clave"], "bases de datos" )
        #print (art.to_String())
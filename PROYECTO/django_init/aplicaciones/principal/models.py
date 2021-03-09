from django.db import models
from django.db.models import Count

# Create your models here.
class Persona( models.Model ):
    id = models.AutoField( primary_key= True )
    nombre = models.CharField( max_length = 50 )
    puntaje = models.IntegerField( max_length = 50 )

    def __str__( self ):
        return  'Nickname : {} , Score : {}'.format(self.nombre,self.puntaje)
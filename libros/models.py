from django.db import models

# Create your models here.
class libros (models.Model):
    titulo=models.CharField(max_length=255)
    contenido=models.CharField(max_length=255)
    imagen=models.ImageField(upload_to='libros')
    rating=models.IntegerField()
   
       
    class Meta: 
        verbose_name='libro'
        verbose_name_plural='libros'
        
    def _str_(self):
        return self.titulo

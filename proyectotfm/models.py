from django.db import models

# Create your models here.
class proyectotfm (models.Model):
    titulo=models.CharField(max_length=255)
    imagen=models.ImageField(upload_to='proyectotfm')
    
   
       
    class Meta: 
        verbose_name='proyectotfm'
        verbose_name_plural='proyectotfms'
        
    def _str_(self):
        return self.titulo
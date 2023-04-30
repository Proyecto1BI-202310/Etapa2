from django.db import models

# Create your models here.
class Single(models.Model):
    texto = models.TextField()
    negativo = models.BooleanField(default=False)
    activated = models.BooleanField(default=False)


    
    def __str__(self):
        return '%s' % ( self.texto, self.negativo)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
from django.db import models

# Create your models here.
class Comentario(models.Model):
    idd = models.PositiveSmallIntegerField(default=5, primary_key=True)
    title = models.TextField(max_length=200)
    rating = models.PositiveSmallIntegerField(default=5)
    texto = models.TextField()
    location = models.TextField(max_length=200)
    hotel = models.TextField(max_length=200)
    negativo = models.BooleanField(default=False)


    
    def __str__(self):
        return '%s' % (self.idd, self.title, self.rating, self.texto, self.location, self.hotel, self.negativo)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

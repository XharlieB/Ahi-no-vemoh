from django.db import models


class Movies(models.Model):

    CINES_CHOICES = {
        ('cmxco', 'Cinemex Condesa'),
        ('cmxca', 'Cinemex Coapa'),
        ('cmxre', 'Cinemex Reforma'),
        ('cmxsa', 'Cinemex Saltillo'),
    }

    HORARIO_CHOICES = {
        ('hoco', ('12:00', '13:00', '15:00', '19:50', '20:45')),
        ('hoca', ('12:00', '13:00', '15:00', '19:50', '20:45')),
        ('hore', ('12:00', '13:00', '15:00', '19:50', '20:45')),
        ('hosa', ('12:00', '13:00', '15:00', '19:50', '20:45')),
    }

    titulo = models.CharField(max_length=200)
    cine = models.CharField(max_length=50, choices=CINES_CHOICES)
    horario = models.CharField(max_length=50, choices=HORARIO_CHOICES)
    imagen = models.ImageField(upload_to='media')

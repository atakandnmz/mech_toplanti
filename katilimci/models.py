from django.db import models

# Create your models here.
class Toplanti_Konusu(models.Model):
    t_konu=models.CharField(max_length=50)
    t_tarih=models.DateField()
    t_bassaat=models.TimeField()
    t_bitsaat=models.TimeField()
    t_katilimcilar=models.CharField(max_length=300)

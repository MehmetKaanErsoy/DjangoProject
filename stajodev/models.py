from django.db import models


class fakulteeekle(models.Model):
    fakulte_ismii = models.CharField(max_length=30)
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fakulte_ismii

    class Meta:
        db_table = "fakulte_isimleriii"


class bolumekle(models.Model):
    fakulte_ismi = models.CharField(fakulteeekle, max_length=30)
    Bolum_ismi = models.CharField(max_length=50)
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Bolum_ismi

    class Meta:
        db_table = "bolumler"


class sorumlu_ekle(models.Model):
    ünvanı = models.CharField(max_length=30)
    adisoyadi = models.CharField(max_length=50)
    telefon = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    fakulte = models.CharField(fakulteeekle, max_length=30)
    bolum = models.CharField(bolumekle, max_length=30)

    def __str__(self):
        return self.ünvanı + self.adisoyadi

    class Meta:
        db_table = "sorumlular"


class ünvan_model(models.Model):
    unvan = models.CharField(max_length=50)

    def __str__(self):
        return self.unvan

    class Meta:
        db_table = "unvan"

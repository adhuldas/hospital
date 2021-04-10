from django.db import models

# Create your models here.
from django.urls import reverse


class Deprt(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    img = models.ImageField(upload_to='department')


    class Meta:
        ordering = ('name',)
        verbose_name = 'Deprt'
        verbose_name_plural = 'Deprts'

    def get_url(self):
        return reverse("hospitalapp:products_by_category", args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Doctor(models.Model):
    name = models.CharField(max_length=250)
    dept = models.TextField(max_length=250)
    slug = models.SlugField(max_length=250)
    img = models.ImageField(upload_to='doctor')
    deprt = models.ForeignKey(Deprt, on_delete=models.CASCADE)
    ph_no = models.TextField(max_length=12)
    email = models.EmailField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def get_url(self):
        return reverse("hospitalapp:catdetail",args=[self.deprt.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)

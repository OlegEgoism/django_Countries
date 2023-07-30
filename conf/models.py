from django.db import models
from django_countries.fields import CountryField


class Person(models.Model):
    """Персонал"""
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    surname = models.CharField(verbose_name='Отчество', max_length=100)
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo/', blank=True, null=True)
    birthday = models.DateField(verbose_name='Дата рождения')
    country = CountryField(verbose_name='Старна', default='BY')
    organization = models.OneToOneField('Organization', verbose_name='Организация', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.surname}'


class Organization(models.Model):
    """Организация"""
    name = models.CharField(verbose_name='Организация', max_length=250)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организация'

    def __str__(self):
        return self.name

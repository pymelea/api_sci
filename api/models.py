from django.db import models

# Create your models here.



class Environment(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Environment')
    capacity = models.IntegerField(verbose_name='Capacity of environment')
    address = models.CharField(max_length=150, verbose_name='Address')
    available = models.BooleanField(verbose_name='Available')
    description = models.TextField(verbose_name='Description of environment')
    created_by = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_by = models.DateTimeField(auto_now=True, verbose_name='Updated')


    class Meta:
        verbose_name = "Environment"
        verbose_name_plural = "Environments"
        ordering = ['available', 'address', 'description', ]

    def __str__(self):
        return self.name

    def toJSON(self):
        return {
            'name': self.name,
            'capacity': self.capacity,
            'address': self.address,
            'available': self.available,
            'description': self.description,
            'created': self.created_by,
            'updated': self.updated_by,
        }
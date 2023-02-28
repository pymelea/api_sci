from django.db import models

# Create your models here.


class Environment(models.Model):
    name = models.CharField(max_length=150, unique=True,
                            verbose_name='Environment')
    capacity = models.IntegerField(verbose_name='Capacity of environment')
    address = models.CharField(max_length=150, verbose_name='Address')
    available = models.BooleanField(verbose_name='Available')
    description = models.TextField(verbose_name='Description of environment')
    created_by = models.DateTimeField(
        auto_now_add=True, verbose_name='Created')
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


class Booking(models.Model):
    name = models.CharField(max_length=150)
    cpf = models.CharField(
        max_length=15, verbose_name='CPF by responsable person', unique=True)
    fee = models.DecimalField(
        decimal_places=2, max_digits=9, verbose_name='Use Fee')
    real_value_pay = models.DecimalField(max_digits=9, decimal_places=2)
    capacity = models.IntegerField()
    start_day = models.DateField()
    end_day = models.DateField()
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)
    status = models.BooleanField(
        verbose_name='Are you ready for do the booking?')
    env = models.ForeignKey(
        Environment, on_delete=models.CASCADE, verbose_name='Environment')

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return self.name

    def toJSON(self):
        return {
            'name': self.name,
            'cpf': self.cpf,
            'fee': self.fee,
            'real_value_pay': self.real_value_pay,
            'capacity': self.capacity,
            'start_day': self.start_day,
            'end_day': self.end_day,
            'created': self.created,
            'updated': self.updated,
            'status': self.status,
            'env': self.env.toJSON(),
        }

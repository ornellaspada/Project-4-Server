from django.db import models

# Create your models here.
class Runaway(models.Model):
    brand = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    season = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    sale_price = models.CharField(max_length=200)
    rent_price = models.CharField(max_length=200)
    description = models.TextField(max_length=350)
    favorited_by = models.ManyToManyField(
        'jwt_auth.User',
        related_name='favorites',
        blank=True
    )
  

    def __str__(self):
        return f'{self.brand} - {self.year}'

class Comment(models.Model):
    content = models.TextField(max_length=250)
    runaway = models.ForeignKey(
        Runaway,
        related_name='comments',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='comments',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'Comment {self.id} on {self.runaway}'

class Rental(models.Model):

    date_rented= models.DateField(max_length=250)
    date_returned= models.DateField(max_length=250, null=True)
    rented= models.BooleanField()
    runaway = models.ForeignKey(
        Runaway,
        related_name='rentals',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='rentals',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'Rental {self.id} on {self.runaway}'

class Purchase(models.Model):

    date_purchased= models.DateField(max_length=250)
    runaway = models.ForeignKey(
        Runaway,
        related_name='purchases',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='purchases',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'Purchase {self.id} on {self.runaway}'



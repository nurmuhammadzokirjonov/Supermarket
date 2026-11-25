from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=70)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=70)
    image=models.ImageField(upload_to="")
    price=models.PositiveIntegerField(default=0)
    description=models.TextField(max_length=500)
  
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
        
    
    def __str__(self):
        return self.name

class Checkout(models.Model):
     PAYMENT_CHOICES = [
        ('cash', 'Naqd pul'),
        ('card', 'Bank kartasi'),
        ('online', 'Online to‘lov'),
    ]

full_name = models.CharField(max_length=150)
phone = models.CharField(max_length=20)
address = models.TextField()

total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
created_at = models.DateTimeField(auto_now_add=True)
is_completed = models.BooleanField(default=False)

def __str__(self):
        return self.full_name

class Discount(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='discounts'
    )
    discount_percent = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product} - {self.discount_percent}%"

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 yulduz'),
        (2, '2 yulduz'),
        (3, '3 yulduz'),
        (4, '4 yulduz'),
        (5, '5 yulduz'),
    ]

    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product}"
    
class Wishlist(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='wishlists'
    )
    added_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.user.username} - {self.product}"


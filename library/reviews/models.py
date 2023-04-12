from django.db import models
from catalog.models import Book
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=1024)
    pub_date = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(choices=RATING_CHOICES,default=5)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'{self.book.title}/{self.user.username} - {self.value}'


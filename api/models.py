from django.db import models
import string, random

# Create your models here.


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Post.objects.filter(
                code=code).count() == 0 and Category.objects.filter(
                    code=code).count() == 0:
            break

    return code


class Category(models.Model):
    code = models.CharField(max_length=8,
                            default=generate_unique_code,
                            unique=True)
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.category}"


class Post(models.Model):
    code = models.CharField(max_length=8,
                            default=generate_unique_code,
                            unique=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 null=False)
    date = models.DateTimeField(auto_now_add=True)

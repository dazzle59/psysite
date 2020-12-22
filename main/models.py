from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_name = models.CharField(max_length=50)
    article_text = models.TextField()
    pub_date = models.DateTimeField('date published')


class Diplom(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='media/diploms')


class Contact(models.Model):
    name = models.CharField(max_length=124)
    email = models.CharField(max_length=40)
    message = models.TextField()

    def __str__(self):
        return self.name




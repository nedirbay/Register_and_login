from django.db import models
from ckeditor.fields import RichTextField,RichTextFormField


class ServiceCategory(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='ServiceCategories'
        verbose_name='ServiceCategory'
        ordering=['name']
        db_table='ServiceCategory'

class BookUpload(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    file=models.FileField(upload_to='files/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='BookUploads'
        verbose_name='BookUpload'
        ordering=['name']
        db_table='BookUpload'
        

class NewsCategory(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='NewsCategories'
        verbose_name='NewsCategory'
        ordering=['name']
        db_table='NewsCategory'


class News(models.Model):
    title=models.CharField(max_length=250)
    content=RichTextField()
    category=models.ForeignKey(NewsCategory,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/news/')
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='News'
        verbose_name='News'
        ordering=['-date']
        db_table='News'
        


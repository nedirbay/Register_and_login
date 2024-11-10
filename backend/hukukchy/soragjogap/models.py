from django.db import models
from django.contrib.auth.models import User

class KanunUpload(models.Model):
    name=models.CharField(max_length=250)
    file=models.FileField(upload_to='books/')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'KanunUpload'
        verbose_name = 'KanunUpload'
        verbose_name_plural = 'KanunUploads'
        ordering = ['id']
        unique_together = ('name', 'file',)

class Maddalar(models.Model):
    kanun=models.CharField(max_length=250)
    maddalar=models.TextField()

    def __str__(self):
        return self.maddalar
    
    class Meta:
        db_table = 'maddalar'
        verbose_name = 'madda'
        verbose_name_plural = 'maddalar'
        ordering = ['-id']



class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        db_table = 'Questions'

class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
    
    class Meta:
        db_table = 'answers'
        verbose_name = 'answer'
        verbose_name_plural = 'answers'
        ordering = ['-created_at']
        
from django.db import models

# Create your models here.
class News (models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    
    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

        

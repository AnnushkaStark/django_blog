from django.db import models

# Create your models here.
class Post(models.Model):
    '''Данные о записях в блоге'''
    title = models.CharField('Заголовок записи', max_length= 100)
    description = models.TextField('Текст записи')
    author = models.CharField('Автор статьи', max_length=100)
    date = models.DateField('Дата')
    image = models.ImageField('Изображение',upload_to='image/%Y')
    
    def __str__(self):
        return f'{self.title} {self.author}' 

    #class Meta:
        #verbous_name = 'Запись'
        #verbous_name_plural = 'Записи'

    
    

    
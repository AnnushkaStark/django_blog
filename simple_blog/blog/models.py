from django.db import models


# Create your models here.
class Post(models.Model):
    """Данные о записях в блоге"""

    title = models.CharField("Заголовок записи", max_length=100)
    description = models.TextField("Текст записи")
    author = models.CharField("Автор статьи", max_length=100)
    date = models.DateField("Дата")
    image = models.ImageField("Изображение", upload_to="image/%Y")

    def __str__(self):
        return f"{self.title} {self.author}"


class Comment(models.Model):
    """Сохранение комментариев пользовтелей"""

    email = models.EmailField()
    name = models.CharField("Имя пользователя", max_length=50)
    text_comment = models.TextField("Текст комментария", max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.name} {self.text_comment} {self.post} {self.date}"


class Like(models.Model):
    """Модель для хранения лайков пользователей"""

    ip = models.CharField(
        max_length=100
    )  # т.к на сайте не реализована регистрация и авторизация сохраняем ip адрес чтобы с одного ip можно было поставить только 1 лайк
    article = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.ip} {self.article}"

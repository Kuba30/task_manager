from django.db import models


class Category(models.Model):

    name = models.CharField("Название", max_length=100, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField("Название", max_length=50, unique=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", blank=True)
    is_completed = models.BooleanField("Выполнена", default=False)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name="Теги",
        blank=True,
        related_name="tasks",
    )

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

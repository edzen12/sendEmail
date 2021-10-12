from django.db import models


class Person(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='name',
        db_index=True,
        blank=True, null=True,
    )
    lastName = models.CharField(
        max_length=255,
        verbose_name='lastName',
        db_index=True,
        blank=True, null=True,
    )
    patronymic = models.CharField(
        max_length=255,
        verbose_name='patronymic',
        db_index=True,
        blank=True, null=True,
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='phone',
        null=True, blank=True
    )
    email = models.EmailField(
        blank=True, null=True,
        verbose_name='email'
    )
    dateOfBirth = models.CharField(
        max_length=255,
        verbose_name='dateOfBirth',
        null=True, blank=True
    )
    passNumber = models.CharField(
        max_length=255,
        verbose_name='passNumber',
        null=True, blank=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name='address',
        null=True, blank=True
    )
    analysisDate = models.CharField(
        max_length=255,
        verbose_name='analysisDate',
        null=True, blank=True
    )
    completeDate = models.CharField(
        max_length=255,
        verbose_name='completeDate',
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.name}---{self.lastName}"

    class Meta:
        ordering = ('-id',)

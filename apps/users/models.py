from django.db import models
import secrets
# Create your models here.

class User(models.Model):
    user_name = models.CharField(
        verbose_name = "Имя пользователя",
        max_length=255
    )
    email = models.EmailField(
        verbose_name= "Ваша электронная почта"
    )
    phone_number = models.CharField(
        verbose_name="Ваш телефонный номер",
        max_length=50
    )
    created_ad = models.DateTimeField(
        auto_now_add= True
    )
    age = models.CharField(
        verbose_name="Ваш возраст",
        max_length=100
    )
    wallet_address = models.CharField(
        verbose_name="Адрес кошелька",
        max_length=12,
        blank= True , null = True,
        unique= True
    )

    def __str__(self):
        return self.wallet_adress
    
    class Meta:
        verbose_name = "Пользователь",
        verbose_name_plural = "Пользователи"

    def save(self, *args, **kwargs):
        if not self.wallet_address:
            self.wallet_address =  secrets.token_hex(6)
        super().save(*args, **kwargs)


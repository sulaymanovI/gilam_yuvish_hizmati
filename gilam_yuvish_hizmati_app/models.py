from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


HIZMAT_TURLARI={
    "GY" : "Gilam yuvish",
    "YMY" : "Yumshoq mebel yuvish",
    "B" : "Boshqa...",
}

HIZMAT_HOLATI={
    "Y" : "Yangi",
    "B" : "Bajarilmoqda",
    "BD" : "Bajarildi",
}


class Buyurtma(models.Model):
    fullname=models.CharField(max_length=250,verbose_name="Ism Familiya")
    telefon_raqam=models.CharField(max_length=13,validators=[RegexValidator(
            regex=r'^\+998\d{9}$',
            message="Noto'g'ri formatdagi telefon raqam kiritildi! \n \
                     Telefon +998XXXXXXXXX shakliga to'gri kelishi kerak."
        )],verbose_name="Telefon raqam")
    hizmat_turi=models.CharField(max_length=125,choices=HIZMAT_TURLARI , default="Hizmat turini tanlang")
    hizmat_holati=models.CharField(max_length=125,choices=HIZMAT_HOLATI , default="Yangi")
    buyurtma_sanasi=models.DateTimeField(default=timezone.now, verbose_name="Buyurtma sanasi")
    manzil=models.TextField(blank=True , null=True)

    class Meta:
        verbose_name_plural="Buyurtmalar"

    def __str__(self) -> str:
        return self.fullname


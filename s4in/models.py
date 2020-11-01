from django.db import models

# Create your models here.
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Sectors(models.Model):
    name=models.CharField(max_length=40,verbose_name='Sektor Adı')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Sektorlar'


class Projects(models.Model):
    jobTypes=(
        ('b2b', 'b2b'),
        ('b2c', 'b2c'),
        ('depo_otomasyon', 'depo_otomasyon'),
        ('arac_takip', 'arac_takip'),
    )
    name = models.CharField(max_length=30,verbose_name='Proje Adı')
    shortDescription = models.TextField(null=True,blank=True,max_length=1250,verbose_name='Kısa Açıklama')
    description = models.TextField(null=True,blank=True,max_length=1250,verbose_name='Proje Hakkında')
    sector = models.ForeignKey(Sectors, null=True, on_delete=models.CASCADE, verbose_name='Sektor')
    type = MultiSelectField(choices=jobTypes,max_choices=3,max_length=100,verbose_name='Tip')
    link = models.URLField(max_length=100,null=True)
    logo = models.ImageField("Logo",null=True)
    date = models.DateField(null=True,verbose_name="Proje tarihi")
    showInMainPage = models.BooleanField(default=True,verbose_name='Bu Proje Ana Sayfada Gosterilsin Mi?')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Projeler'
    def delete(self,*args,**kwargs):
        self.logo.delete()
        super().delete(*args,**kwargs)


class MainPage(models.Model):
    title = models.TextField(max_length=400,verbose_name='Unvan')
    description = models.CharField(max_length=400,verbose_name='Alt Yazi',null=True,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Anasayfa Yazısı'

class AboutUs(models.Model):
    title = models.TextField(max_length=400, verbose_name='Unvan')
    description = models.CharField(max_length=400, verbose_name='Alt Yazi',null=True,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Hakkımızda'

class Services(models.Model):
    name = models.CharField(max_length=100, verbose_name='Hizmet adi',null=True,blank=True)
    description = models.TextField(max_length=400, verbose_name='Aciklama',null=True,blank=True)
    pic = models.ImageField("Png Resim Seciniz", null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Hizmetlerimiz'
    def delete(self,*args,**kwargs):
        self.pic.delete()
        super().delete(*args,**kwargs)

class WhyUs(models.Model):
    reason = models.CharField(max_length=200, verbose_name='Hizmet adi',null=True,blank=True)
    reasonMavi = models.CharField(max_length=100, verbose_name='Mavi kelemeyle cumlenin basina opsiyonel olarak eklenecek',null=True,blank=True)
    description = models.TextField(max_length=400, verbose_name='aciklama',null=True,blank=True)
    def __str__(self):
        return self.reason
    class Meta:
        verbose_name_plural = 'Neden Biz?'

class Advantages(models.Model):
    note = models.TextField(max_length=75,verbose_name='avantaji')
    def __str__(self):
        return self.note
    class Meta:
        verbose_name_plural = 'Avantajlarımız'

class Address(models.Model):
    address1 = models.TextField(max_length=200, verbose_name='Adres 1',null=True,blank=True)
    address2 = models.TextField(max_length=200, verbose_name='Adres 2',null=True,blank=True)
    telephone = models.CharField(max_length=30, verbose_name='Telefon',null=True,blank=True)
    fax = models.CharField(max_length=30, verbose_name='Fax)',null=True,blank=True)
    email = models.EmailField(max_length=200, verbose_name='Eposta',null=True,blank=True)

    def __str__(self):
        return self.address1
    class Meta:
        verbose_name_plural = 'Iletisim'


class Pictures(models.Model):
    project = models.ForeignKey(Projects, related_name="Pictures", verbose_name="resimler",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    status = models.BooleanField(default=True,verbose_name='Gosterilsin mi?')
    cover = models.BooleanField(default=False,verbose_name='kapak resim mi?')
    def delete(self,*args,**kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)

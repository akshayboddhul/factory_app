import sys
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from io import BytesIO

# Create your models here.


class powerloom(models.Model):
    PLNO = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )
    SIZE = (
        ('3672', '3672'),
        ('3060', '3060'),
        ('2754', '2754'),
        ('2448', '2448'),
        ('1827', '1827'),
        ('1218', '1218'),
    )
    STATUS = (
        ('Active', 'Active'),
        ('Not Active', 'Not Active'),
        ('Repair', 'Repair'),

    )
    LOCATION = (
        ('Factory1', 'Factory1'),
        ('Factory3', 'Factory3'),
        ('Factory4', 'Factory4'),
        ('Factory5', 'Factory5'),
    )
    plno = models.CharField(max_length=255, choices=PLNO)
    qty_name = models.CharField(max_length=225, blank=False, null=False)
    size = models.CharField(max_length=255, choices=SIZE)
    location = models.CharField(
        max_length=255, choices=LOCATION, blank=True, null=True)
    image = models.ImageField(upload_to='photos/')
    status = models.CharField(max_length=255, choices=STATUS)
    comment = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.plno

    def save(self, *args, **kwargs):
        kwargs['force_insert'] = True
        im = Image.open(self.image)
        output = BytesIO()
        im = im.resize((800, 800))
        im.save(output, format='png', quality=20)
        output.seek(0)
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.png" % self.image.name.split(
            '.')[0], 'image/png', sys.getsizeof(output), None)

        super(powerloom, self).save()


class production(models.Model):
    doprod = models.DateField(blank=True)
    plno = models.ForeignKey(powerloom, max_length=255,
                             on_delete=models.DO_NOTHING)
    pcs = models.IntegerField()
    weight = models.IntegerField()
    total_prod = models.CharField(max_length=255, null=True, blank=True)

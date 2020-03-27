import sys
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.
class upload(models.Model):
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to="photos/",default='/media/photos/default.jpg') 
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.image = self.compressImage(self.image)
        super(upload, self).save(*args, **kwargs)
    def compressImage(self,image):
        imageTemproary = Image.open(image)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        image = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return image




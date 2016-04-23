from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models import Q


# Create your models here.
class BaseModel(models.Model):
    created_datetime = models.DateTimeField('created_datetime', auto_now_add=True)
    modified_datetime = models.DateTimeField( blank = True )

    def save(self, *args, **kwargs):
        if not kwargs.pop('skip_modified_datetime', False):
            self.modified_datetime = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
        super(BaseModel, self).save(*args, **kwargs)

    class Admin:
        pass

    class Meta:
        abstract = True


class HttpProxy(BaseModel):
    def __unicode__(self):
        return "nick_name: %s" % str(self.nick_name)

    nick_name = models.CharField(max_length=100, blank=True, null=True)
    hash_id = models.CharField(max_length=100, blank=True, null=True)
    lan_ip = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default = False)

    def save(self, *args, **kwargs):
        history_records = HttpProxy.objects.filter(hash_id = self.hash_id).exclude(Q(nick_name__isnull=True) | Q(nick_name__exact='')).order_by("-modified_datetime")
        
        if self.hash_id and self.pk is None and not self.nick_name and history_records.count() > 0:
            self.nick_name = history_records[0].nick_name
            
        super(HttpProxy, self).save(*args, **kwargs)


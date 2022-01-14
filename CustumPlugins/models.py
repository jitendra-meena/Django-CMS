from django.db import models
from tinymce.models import HTMLField
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
# from auditlog.registry import auditlog

class Hello(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Guest')


class UserList(CMSPlugin):
    first_name =  models.CharField(max_length = 50, default='Jitendra')
    company_name =  HTMLField()
    contact_number =  models.IntegerField(blank = True)

    def __str__(self):
        return self.first_name

class AdminInformations(CMSPlugin):
    name =  models.CharField(max_length = 50, default ='Admin')
    contact_number = models.IntegerField(null = True)
    about_us = HTMLField()         


class ContactNumber(CMSPlugin):
    """
    Contact number details, where user can contact to cait
    """
    service_number = models.CharField(_('WhatsApp Number'), max_length=16, blank=True, default='')
    whatsapp_url = models.URLField(_('WhatsApp URL'), max_length=256, blank=True, default='')
    authority_number = models.CharField(_('Authority Number'), max_length=16, blank=True, default='')

    class Meta:
        verbose_name = _("Contact Number")
        verbose_name_plural = _("Contact Number")





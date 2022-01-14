from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import Hello, UserList, ContactNumber  
from cms.models.pluginmodel import CMSPlugin

@plugin_pool.register_plugin
class DataPlugin(CMSPluginBase):
    model = Hello
    name = _("Hello Plugin")
    render_template = "hello_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context



@plugin_pool.register_plugin
class UserData(CMSPluginBase):
    model = UserList
    name = _("Users details")
    render_template = "userdata.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ContactNumbers(CMSPluginBase):
    model = ContactNumber
    name = ("Contact Number")
    
    render_template = 'contact.html'

    def render(self, contaxt, instance, placeholder):
        context = super().render(contaxt ,instance ,placeholder)
        return contaxt



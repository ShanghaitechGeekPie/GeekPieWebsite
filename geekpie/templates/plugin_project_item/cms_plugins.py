from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import ProjectItemModel

class ProjectItemPlugin(CMSPluginBase):
    model = ProjectItemModel
    name = _("Project Item Plugin")
    render_template = "plugins/ProjectItemPlugin.html"
    cache = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(ProjectItemPlugin)

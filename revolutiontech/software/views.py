"""
:Created: 17 July 2015
:Author: Lucas Connors

"""

from basecategory.views import CategoryPageView

from software.models import Software


class SoftwareListView(CategoryPageView):

    def get_context_data(self, **kwargs):
        context = super(SoftwareListView, self).get_context_data(**kwargs)
        context['page'] = 'software'

        software = Software.objects.all().order_by('name')
        context['items'] = {
            'heroes': software.filter(hero=True),
            'regular': software.filter(hero=False),
        }
        return context

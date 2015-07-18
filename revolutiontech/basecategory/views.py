"""
:Created: 13 July 2015
:Author: Lucas Connors

"""

from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class CategoryPageView(TemplateView):

    template_name = "category_page.html"

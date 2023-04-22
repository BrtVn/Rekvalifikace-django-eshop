from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy, reverse
from django.db.models import Q, CharField

from eshop.forms.search_forms import SearchForm

from eshop.models.products import Product, ProductCategory
from blog.models.posts import Post, PostCategory


class SearchFormView(FormView):
    form_class = SearchForm
    success_url = reverse_lazy('search_results')

    def form_valid(self, form):
        search_query = form.cleaned_data["search_query"]
        print(search_query)
        queries = search_query.split()
        print(queries)
        search_results = []
        # Add your models here, in any way you find best.
        search_models = [ProductCategory, PostCategory, Product,  Post, ]

        for model in search_models:
            fields = [x for x in model._meta.fields if isinstance(
                x, CharField)]
            search_queries = [
                Q(**{x.name + "__contains": search_query}) for x in fields]
            q_object = Q()
            for query in search_queries:
                q_object = q_object | query

            results = model.objects.filter(q_object)
            search_results.append(results)
        print(search_results)
        # return super().form_valid(form)
        return render(self.request, "eshop/search_results.html", {'search_results': search_results})


class SearchResultsTemplateView(TemplateView):
    template_name = "eshop/search_results.html"

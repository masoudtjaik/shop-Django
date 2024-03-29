from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, FormView, CreateView, DeleteView, \
    UpdateView
from django.views.generic.list import ListView
from products.models import Product, Category
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from order.models import OrderItem


# Create your views here.


# class Home(View):
#     template = 'core/home.html'

#     def get(self, request):
#         return render(request, self.template)


class Home(ListView):
    template_name = 'core/home.html'
    model = Category
    queryset = Category.objects.all()[:3]
    context_object_name = 'items'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["products"] = [(product.can_like(self.request.user), product) for product in
                                   Product.objects.ten_product_new()]
        else:
            context["products"] = [(False, product) for product in Product.objects.ten_product_new()]

        context["top_cells"] = OrderItem.top_cell_product()
        context["ten_discounts"] = Product.objects.ten_is_discount()
        # cart = self.request.session.get('sabad')
        # if cart:
        #     products = []
        #     for cart_id in cart:
        #         # print(cart_id)
        #         # print('cart5',cart['5'])
        #         if Product.objects.get(id=int(cart_id)):
        #             products.append((cart[str(cart_id)]['numbers'], Product.objects.get(id=int(cart_id))))
        #     context['carts'] = products
        #     context['len'] = len(products)
        #     context['total'] = sum(number * product.price_discount for number, product in products)
        return context

    # def get_context_data(self, **kwargs) :
    #     context = super().get_context_data(**kwargs)
    #     context["form"] = Search()
    #     return context
    # def get_queryset(self):
    #     print('session',self.request.session.get('sabad'))
    #     # print(self.request.GET.get('search'))
    #     if self.request.GET.get('search') :
    #          return Item.objects.select_related('category').filter(name__icontains=self.request.GET.get('search')).order_by('category__create')
    #     return Item.objects.select_related('category').order_by('category__create')


class ShowCategorys(ListView):
    template_name = 'core/categories.html'
    model = Category
    context_object_name = 'items'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.ten_product_new()
        context["top_cells"] = OrderItem.top_cell_product()
        context["ten_discounts"] = Product.objects.ten_is_discount()
        context['len'] = len(self.get_queryset())
        return context


class NewProduct(ListView):
    template_name = 'core/categories.html'
    model = Product
    queryset = Category.objects.all()[:3]
    context_object_name = 'products'

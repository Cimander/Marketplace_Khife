from apps.shop.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .models import Profile, ProductImage, Product, ProductSpecifications, Category
#from django_filters.rest_framework import DjangoFilterBackend
from django.views import generic
#from .serializers import ProductSerializer
#from rest_framework import generics

def home(request):
    product = Product.objects.all()
    product_image = ProductImage.objects.all()
    return render(request, 'home.html', context={'product_list': product,'product_image_list': product_image})






def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Wellcome {username}')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'shop/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'shop/profile.html')

def blog(request):
    return render(request, 'shop/blog.html')

class BlogDetailView(generic.DetailView):
    model = Product
    template_name = 'shop/blog-detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        return context




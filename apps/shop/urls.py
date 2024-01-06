from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register, profile, home, blog, BlogDetailView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='shop/login.html',
        success_url='profile'
    ), name='login'),
    path('', home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),

    ]

#
#    path('', auth_views.product_list, name='product_list'),
#    path('<slug:category_slug>/', auth_views.product_list,
#         name='product_list_by_category'
#         ),
#    path('<int:id>/<slug:slug>', auth_views.product_detail,
#         name='product_detail')
#
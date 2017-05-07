from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
app_name='shoppinglist'

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/shoppinglist/'}, name='logout'),
    url(r'^add/$', views.addProduct, name='addProduct'),
    url(r'^categories/$', views.adminCategory, name='adminCategory'),
    url(r'^productTypes/$', views.adminProductType, name='adminProductType'),
    url(r'^recipes/$', views.recipes, name='recipes'),
    url(r'^about/$', views.aboutUs, name='aboutUs'),
    url(r'^removeProduct/(?P<productId>[0-9]+)/$', views.removeProduct, name='removeProduct'),
    url(r'^removeCategory/(?P<categoryId>[0-9]+)/$', views.removeCategory, name='removeCategory'),
    url(r'^removeProductType/(?P<productTypeId>[0-9]+)/$', views.removeProductType, name='removeProductType'),
    url(r'^removeRecipe/(?P<recipeId>[0-9]+)/$', views.removeRecipe, name='removeRecipe'),
]
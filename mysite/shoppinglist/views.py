from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .models import *
from .forms import *
@login_required(login_url=LOGIN_URL)
def index(request):
   products = Product.objects.all().order_by('predefinedProduct__category', 'predefinedProduct__name')
   return render(request, "shoppinglist/index.html", {"products": products})
@login_required(login_url=LOGIN_URL)
def addProduct(request):
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			product = form.save(commit=False)
			product.requester = request.user
			product.save()
			return redirect('shoppinglist:addProduct')
	else:
		form = ProductForm()
	return render(request, 'shoppinglist/addProduct.html', {"form": form})
@login_required(login_url=LOGIN_URL)
def adminCategory(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = form.save(commit=False)
			category.save()
			return redirect('shoppinglist:adminCategory')
	else:
		form = CategoryForm()
	categories = Category.objects.all().order_by('name')
	return render(request, 'shoppinglist/adminCategory.html', {"form": form, "categories": categories})
@login_required(login_url=LOGIN_URL)
def adminProductType(request):
	if request.method == "POST":
		form = ProductTypeForm(request.POST)
		if form.is_valid():
			productType = form.save(commit=False)
			productType.save()
			return redirect('shoppinglist:adminProductType')
	else:
		form = ProductTypeForm()
	products = PredefinedProduct.objects.all().order_by('name')
	return render(request, 'shoppinglist/adminProductType.html', {"form": form, "products": products})
@login_required(login_url=LOGIN_URL)
def recipes(request):
	if request.method == "POST":
		form = RecipesForm(request.POST)
		if form.is_valid():
			recipe = form.save(commit=False)
			recipe.save()
			return redirect('shoppinglist:recipes')
	else:
		form = RecipesForm()
	recipes = Recipe.objects.all()
	return render(request, 'shoppinglist/recipes.html', {"form": form, "recipes": recipes})
@login_required(login_url=LOGIN_URL)
def removeProduct(request, productId):
	Product.objects.filter(id = productId).delete()
	return redirect('shoppinglist:index')
@login_required(login_url=LOGIN_URL)
def removeCategory(request, categoryId):
	Category.objects.filter(id = categoryId).delete()
	return redirect('shoppinglist:adminCategory')
@login_required(login_url=LOGIN_URL)
def removeProductType(request, productTypeId):
	PredefinedProduct.objects.filter(id = productTypeId).delete()
	return redirect('shoppinglist:adminProductType')
@login_required(login_url=LOGIN_URL)
def removeRecipe(request, recipeId):
	Recipe.objects.filter(id = recipeId).delete()
	return redirect('shoppinglist:recipes')
@login_required(login_url=LOGIN_URL)
def aboutUs(request):
	return render(request, 'shoppinglist/about.html', {})
def login(request):
	if(request.user.is_authenticated):
		return redirect('shoppinglist:index')
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password = request.POST['password'])
		if user:
			if user.is_active:
				auth_login(request, user)
				return redirect('shoppinglist:index')
		else:
			error = "User/password does not match."
			return render(request, 'shoppinglist/login.html', {'error': error})
	else:
		return render(request, 'shoppinglist/login.html', {})
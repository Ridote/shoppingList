from django import forms
from django.contrib.auth.models import User
from .models import *
from .constants import *

'''
class CategoryTreeWidget(SelectMultiple):
    def render_options(self, choices, selected_choices):
        selected_choices=set([force_unicode(v) for v in selected_choices])
        top_level_cats = Category.objects.filter(parent=None)
        def _render_category_list(cat_list, level=0):
            for category in cat_list:
                self.render_option(selected_choices, category.pk, (("---"*level + " ") if level) + category.name)
                def _render_category_list(category.children, level+1)
        _render_category_list(top_level_cats)
'''

class ProductForm(forms.ModelForm):
	predefinedProduct = forms.ModelChoiceField(queryset=PredefinedProduct.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label=None)
	unit = forms.ModelChoiceField(queryset=Unit.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label=None)
	def __init__(self, *args, **kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
		self.fields['quantity'].label = "Product quantity"
		self.fields['quantity'].initial = MODEL_PRODUCT_MIN_QUANTITY
		self.fields['predefinedProduct'].label = "Product name"
		self.fields['unit'].label = "Product meassurement unit"
		self.fields['unit'].initial = 3
		self.fields['comment'].label = "Comment"
	class Meta:
		model = Product
		fields = ('predefinedProduct', 'quantity', 'unit', 'comment')
		widgets = {
			'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity', 'min': MODEL_PRODUCT_MIN_QUANTITY, 'max': MODEL_PRODUCT_MAX_QUANTITY}),
			'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment', 'max': MODEL_PRODUCT_MAX_COMMENT})
		}
class CategoryForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CategoryForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "Category name"
	class Meta:
		model = Category
		fields = ('name',)
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name', 'min': 3, 'max': MODEL_CATEGORY_NAME_LENGTH})
		}
class ProductTypeForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label=None)
	def __init__(self, *args, **kwargs):
		super(ProductTypeForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "Product name"
		self.fields['category'].label = "Product category"
	class Meta:
		model = PredefinedProduct
		fields = ('name', 'category')
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name', 'min': 3, 'max': MODEL_PREDEFINED_PRODUCT_NAME_LENGTH})
		}
class RecipesForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(RecipesForm, self).__init__(*args, **kwargs)
		self.fields['link'].label = "Recipe link"
	class Meta:
		model = Recipe
		fields = ('link',)
		widgets = {
			'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name', 'min': 3, 'max': MODEL_RECIPE_LINK_LENGTH})
		}
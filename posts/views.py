from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
from .models import Post
from django.utils.text import slugify

class ListView(View):
	 def get(self, request):
	 	 template_name = 'lista.html'
	 	 posts = Post.objects.all().filter(publicado=True)
	 	 context = {
	 	 	'posts':posts,
	 	 	}
	 	 return render(request, template_name, context)

class DetailView(View):
	 def get(self, request, slug):
	 	template_name = 'detalle.html'
	 	post = Post.objects.get(slug=slug)
	 	compa = {
	 	'post':post
	 	}
	 	return render(request, template_name, compa)

class NuevoPost(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = 'nuevopost.html'
		form = NewPostForm()
		context ={
		'form':form,
		}
		return render(request, template_name, context)

	def post(self, request):
		form = NewPostForm(request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.slug = slugify(new_post.titulo)
			new_post.save()
			return redirect('lista')
		else:
			context = {
			'form':form,
			}
			template_name = 'nuevopost.html'
			return render(request, template_name, context)


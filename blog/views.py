from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Post,Commentaire
from .forms import PostForm, CommentaireForm 


# Create your views here.


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):    
	post = get_object_or_404(Post,pk = pk)
	commentaires = post.commentaires.filter(active=True)
	new_comment= None 
	if request.method == 'POST':
		comment_form = CommentaireForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post=post
			new_comment.save()
	else :
		comment_form= CommentaireForm()

	return render(request,'blog/post_detail.html',{'post':post, 'commentaires':commentaires, 'new_comment':new_comment, 'comment_form': comment_form})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.auteur = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else :
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

def post_editt (request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST" :
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.auteur = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else :
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})
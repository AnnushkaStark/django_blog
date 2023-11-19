from django.shortcuts import render,redirect
from django.views.generic.base import View
from .models import Post, Like
from .form import CommentsForm
# Create your views here.

class PostView(View):
    '''Вывод записей'''
    def get(self,request):
        posts = Post.objects.all()
        return render(request,'blog/blog.html',{'post_list' : posts})

class PostDetail(View):
    '''Отображение записей на отдельной странице'''
    def get(self, request, pk):
        post = Post.objects.get(id = pk)
        return render(request, 'blog/blog_detail.html', {'post':post})
    

class AddComments(View):
    '''Добавление комментариев'''
    def post(self, request, pk):
        try:
            form = CommentsForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.post_id = pk
                form.save()
                return redirect(f'/{pk}')
            
            return redirect(f'/{pk}')
        except ValueError:
            return redirect(f'/{pk}')
            

        
def get_client_ip(request):
    '''Функция для полуения ip адреса пользователя'''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    '''Проставление лайков под постами'''
    def get(self,request, pk):
        ip_client = get_client_ip(request)
    
        try:
            Like.objects.get_or_create(ip = ip_client, article_id = pk)
            return redirect(f'/{pk}')
        except Exception:
        
            return redirect(f'/{pk}')
        
class DelLike(View):
    '''Удаление лайка'''
    def get(self,request, pk):
        ip_client = get_client_ip(request)
        try:
            like= Like.objects.get(ip= ip_client, article_id = pk)
            like.delete()
            return redirect(f'/{pk}')
        except Exception:
            return redirect(f'/{pk}')
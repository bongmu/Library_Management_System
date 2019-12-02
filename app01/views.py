from django.shortcuts import render,HttpResponse,redirect,reverse
from app01 import models
# Create your views here.

# 主页
def home(request):
    return render(request,'home.html')

# 登录
def login(request):
    return render(request,'login.html')
    pass

# 注册
import json
# from django.core import serializers
def register(request):
    if request.method == "POST":
        res = {'flag':False}
        username = request.POST.get('username')
        if username == "qinyj":
            res['flag'] = True
            return HttpResponse(json.dumps(res))
        # user_obj = models.User.objects.filter(username=username)
        # # print(user_obj)
        # if user_obj:
        #     res['flag'] = True
        #     # res = serializers.serialize('json', user_obj)
        #     return HttpResponse(json.dumps(res))
        # password = request.POST.get('password')
        # gender = request.POST.get('gender')
        # print('gender的值', gender)
        # models.User.objects.create(username=username,password=password,gender=int(gender))
        # return redirect(reverse('login'))

    return render(request,'register.html')


# 书籍列表
# from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from app01.utils.mypage import Pagination
import time
from django.http import JsonResponse
def boot_list(request):
    if request.is_ajax():
        back_dic = {'code':200,'msg':''}
        delete_id = request.POST.get('delete_id')
        time.sleep(1)
        models.Book.objects.filter(pk=delete_id).delete()
        back_dic['msg'] = "删除成功"
        return JsonResponse(back_dic)
    # # ORM 的循环插入数据更快捷的方法：
    # book_list = []
    # for i in range(1000):
    #     book_list.append(models.Book(title='第%s本书'%i))
    # models.Book.objects.bulk_create(book_list)
    # 查询所有的书籍。
    book_list = models.Book.objects.all()
    # 自定义分页器的使用
    current_page = request.GET.get('page',1)
    all_count = book_list.count()
    page_obj = Pagination(current_page=current_page,
                          all_count=all_count,
                          per_page_num=15,
                          pager_count=11)
    # 参数说明：
    # current_page 当前的页数
    # all_count 所有的页数
    # per_page_num 每页显示多少
    # pager_count 分页器显示的条数
    page_queryset = book_list[page_obj.start:page_obj.end]
    return render(request,'book_list.html',locals())


# 添加书籍
def add_book(request):
    publish_list = models.Publish.objects.all()
    author_list = models.Author.objects.all()
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        book_price = request.POST.get('book_price')
        publish_id = request.POST.get('publish_id')
        author_id = request.POST.getlist('author_id')
        author_id = [int(x) for x in author_id]
        book_obj = models.Book.objects.create(title=book_name,
                                              price=book_price,
                                              publish_id=publish_id)
        book_obj.authors.set(author_id)
        return redirect(reverse('book_list'))

    return render(request,'add_book.html',{'publish_list':publish_list,'author_list':author_list})

# 编辑书籍
def edit_book(request,edit_id):
    book_obj = models.Book.objects.filter(pk=edit_id).first()
    publish_list = models.Publish.objects.all()
    author_list = models.Author.objects.all()
    # currentPage = request.GET.get('currentPage')
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        book_price = request.POST.get('book_price')
        publish_id = request.POST.get('publish_id')
        author_id = request.POST.getlist('author_id')
        author_id = [int(x) for x in author_id]
        # book_obj = models.Book.objects.create(title=book_name,
        #                                       price=book_price,
        #                                       publish_id=publish_id)
        book_obj.authors.set(author_id)
        return redirect(reverse('book_list'))

    return render(request,'edit_book.html',locals())

# 删除书籍
def delete_book(request,delete_id):
    book_obj = models.Book.objects.filter(pk=delete_id).delete()
    return redirect(reverse('book_list'))


# 出版社列表
def publish_list(request):
    publish_list = models.Publish.objects.all()
    return render(request,'publish_list.html',locals())

# 添加出版社
def add_publish(request):
    if request.method == "POST":
        publish_name = request.POST.get('publish_name')
        publish_addr = request.POST.get('publish_addr')
        models.Publish.objects.create(name=publish_name,addr=publish_addr)
        return redirect(reverse('publish_list'))
    return render(request,'add_publish.html')

# 编辑出版社
def edit_publish(request,edit_id):
    publish_obj = models.Publish.objects.filter(pk=edit_id).first()
    book_list = models.Book.objects.all()
    # print(publish_obj.name)
    if request.method == "POST":
        publish_name = request.POST.get('publish_name')
        publish_addr = request.POST.get('publish_addr')
        # book_id_list = request.POST.getlist('book_id')
        models.Publish.objects.filter(pk=edit_id).update(name=publish_name,addr=publish_addr)
        # publish_obj.book_set.pri
        # print(publish_obj.book_set.all().update())
        return redirect(reverse('publish_list'))
    return render(request,'edit_publish.html',locals())

# 删除出版社
def delete_publish(request,delete_id):
    models.Publish.objects.filter(pk=delete_id).delete()
    return redirect(reverse('publish_list'))

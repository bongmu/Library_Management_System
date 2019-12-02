from django.test import TestCase

# Create your tests here.
import os
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Library_Management_System.settings")

    import django
    django.setup()
    from app01 import models,views
    # l1 = []
    # for i in range(1,101):
    #     l1.append(models.Book.objects.create(
    #         title='图书%s' %i,price=20+i,publish_id=4
    #     ))
    # 要想实现分页器，必须导入模块
    from django.core.paginator import Paginator

    list1 = [i for i in range(0,150)]
    # print(list1)

    # 生成一个paginator对象，第二个参数表示每页显示几条内容。
    page1 = Paginator(list1,10)
    # 打印总的记录数，即列表元素的长度
    print(page1.count)
    # 打印有多少页数，即总记录数除以每页显示的条目数
    print(page1.num_pages)
    # 页数的列表
    print(page1.page_range)
    # 打印第一页的page对象
    print(page1.page(2))
    # 打印第一页的所有记录
    print(page1.page(1).object_list)
    print(page1.page(2).next_page_number())
    print(page1.page(2).has_next())
    print(page1.page(2).has_other_pages())
    print(page1.page(2).has_previous())
    # 打印第二页的开始、结束的序号
    print(page1.page(2).start_index())
    print(page1.page(2).end_index())

    print(page1.page(15).object_list)


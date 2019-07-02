import xadmin
from .models import *


from xadmin import views
# Register your models here.

xadmin.site.site_header = '发现生活后台管理'
xadmin.site.site_title = '发现生活'

# # 创建xadmin的最基本管理器配置，并与view绑定
# class BaseSetting(object):
#     # 开启主题功能
#     enable_themes = True
#     use_bootswatch = True
#
# # 将基本配置管理与view绑定
# xadmin.site.register(views.BaseAdminView,BaseSetting)

# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '高仿点评后台管理界面'
    # 修改footer
    site_footer = '中北大学大数据学院物联网工程大型软件实验周课设'
    # 收起菜单
    menu_style = 'accordion'

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)

# 进行类配置
class AddressAdmin(object):
    # 显示的列
    list_display = ['id', 'userid', 'addressName', 'tel','province','detail']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['id', 'userid', 'addressName', 'tel','province','detail']
    # 过滤
    list_filter = ['id', 'userid', 'addressName', 'tel','province','detail']

class CategoryAdmin(object):
    # 显示的列
    list_display = ['category_id', 'category_name', 'category_parent']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['category_id', 'category_name', 'category_parent']
    # 过滤
    list_filter = ['category_id', 'category_name', 'category_parent']


class CityAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'sortKey']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['id', 'name', 'sortKey']
    # 过滤
    list_filter = ['id', 'name', 'sortKey']


class CommentAdmin(object):
    # 显示的列
    list_display = ['comment_id', 'user', 'prodouct','comment_conent', 'comment_time']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['comment_id', 'user', 'prodouct','comment_conent', 'comment_time']
    # 过滤
    list_filter = ['comment_id', 'user', 'prodouct','comment_conent', 'comment_time']

class OrdersAdmin(object):
    # 显示的列
    list_display = ['orders_id', 'user', 'orders_time','orders_all_price', 'orders_paystate','orders_prodouct_id']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['orders_id', 'user', 'orders_time','orders_all_price', 'orders_paystate','orders_prodouct_id']
    # 过滤
    list_filter = ['orders_id', 'user', 'orders_time','orders_all_price', 'orders_paystate','orders_prodouct_id']

class ProdouctAdmin(object):
    # 显示的列
    list_display = ['id', 'categoryId', 'shopId','CityId', 'sortTitle','value', 'price', 'ribat',]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['id', 'categoryId', 'shopId','CityId', 'sortTitle','value', 'price', 'ribat',]
    # 过滤
    list_filter = ['id', 'categoryId', 'shopId','CityId', 'sortTitle','value', 'price', 'ribat',]

class ShopAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'tel','address', 'area','opentime', 'lon', 'lat',]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['id', 'name', 'tel','address', 'area','opentime', 'lon', 'lat',]
    # 过滤
    list_filter = ['id', 'name', 'tel','address', 'area','opentime', 'lon', 'lat',]

class UserAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'loginPwd','payPwd', 'tel',]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['id', 'name', 'loginPwd','payPwd', 'tel',]
    # 过滤
    list_filter = ['id', 'name', 'loginPwd','payPwd', 'tel',]


xadmin.site.register(Address,AddressAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(City,CityAdmin)
xadmin.site.register(Comment,CommentAdmin)
# xadmin.site.register(Favorite)
xadmin.site.register(Orders,OrdersAdmin)
xadmin.site.register(Prodouct,ProdouctAdmin)
xadmin.site.register(Shop,ShopAdmin)
# xadmin.site.register(SubCategory)
# xadmin.site.register(Ticket)
xadmin.site.register(User,UserAdmin)

from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^def_user/',include(('def_user.urls',"def_user"),namespace='def_user')),#用户模块
    url(r'^def_goods/',include(('def_goods.urls',"def_goods"),namespace='def_goods')),#商品模块
    url(r'^def_order/',include(('def_order.urls',"def_order"),namespace='def_order')),#订单模块
    url(r'^def_message',include(('def_message.urls',"def_message"),namespace='def_message')),#消息模块
]

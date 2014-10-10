from django.conf.urls import patterns, include, url
from django.contrib import admin
from cloudtrum.electrum.views import BalanceList





urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloudtrum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/balances', BalanceList.as_view(), name='balance-list'),

)




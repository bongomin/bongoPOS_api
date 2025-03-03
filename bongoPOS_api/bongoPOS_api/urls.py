from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    # path('api/inventory/', include('inventory.urls')),
    # path('api/products/', include('products.urls')),
    # path('api/reports/', include('reports.urls')),
    # path('api/salessettings/', include('salessettings.urls')),
    # path('api/receipts/', include('receipts.urls')),
]
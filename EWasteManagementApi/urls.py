from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import Blogs.urls as blogs
import Complaints.urls as complaints
import User.urls as user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include(user)),
    path('api/complaints/', include(complaints)),
    path('api/blogs/', include(blogs)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

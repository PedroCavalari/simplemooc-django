"""simplemooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from simplemooc.core import views #importar views da aplicação
from django.conf.urls import include

urlpatterns = [
	path('',include(('simplemooc.core.urls', 'core'), namespace = 'core')), #ira nos redirecionar para o arquivo urls dentro da pasta core
	# pois iportamos as views diratemente de core

    # accounts
    path('conta/', include('simplemooc.accounts.urls', namespace='accounts')),
    path('forum/', include(('simplemooc.forum.urls', 'forum'), namespace = 'forum')), 

    path('cursos/',include(('simplemooc.courses.urls', 'courses'), namespace = 'courses')), 
    #ira nos redirecionar para o arquivo urls dentro da pasta COURSES

	#path(r'^',include('blog.urls')), #adicionado modularizando diferentes arquivos url
    path('admin/', admin.site.urls),

]

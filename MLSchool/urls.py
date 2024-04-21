"""MLSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('base_template.urls')),
    path('map/', include('map.urls')),
    path('practice_prob', include('practice_prob.urls')),
    path('admin/', admin.site.urls),
    path('LR_one_variable/', include('LR_one_variable.urls')),
    path('gradient_descent_basics/', include('gradient_descent_basics.urls')),
    path('logistic_regression/', include('logistic_regression.urls')),
    path('KMeans/',include('KMeans.urls')),
    path('GMM/',include('GMM.urls')),
    path('Decision_Tree/',include('Decision_Tree.urls')),
    path('ensemble_model/',include('ensemble_model.urls')),
    path('random_forest/',include('random_forest.urls')),
    path('code_editor/',include('code_editor.urls')),
    path('ML_practice_questions/',include('practice_ML.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]

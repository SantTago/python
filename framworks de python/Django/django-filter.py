
INSTALLED_APPS = [
    ...
    'django_filters',
]

#Em seguida, adicione 'django_filters' ao seu INSTALLED_APPS.

#Django-filter pode ser usado para gerar interfaces semelhantes 
# à interface list_filter do administrador do Django. Possui uma 
# API muito semelhante ao ModelForms do Django. Por exemplo, se você 
# tivesse um modelo de produto, poderia ter um conjunto de filtros para 
# ele com o código:

import django_filters

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name', 'price', 'manufacturer']
        
# 
# E então, na sua visão, você poderia fazer:



def product_list(request):
    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'my_app/template.html', {'filter': filter})

# Uso com Django REST Framework
# O Django-filter fornece um FilterSet customizado e back-end de
# filtro para uso com o Django REST Framework.

# Para usar isso, ajuste sua importação para usar django_filters.rest_framework.FilterSet.

from django_filters import rest_framework as filters

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ('category', 'in_stock')



#Django-filter é um aplicativo Django reutilizável 
# que permite aos usuários adicionar filtragem dinâmica 
# de QuerySet de forma declarativa a partir de parâmetros de URL.

#Django-Filter é um pacote maduro e estável. Ele usa um esquema de 
# versão CalVer de duas partes, como 21.1. O primeiro número é o ano. 
# O segundo é o número de lançamento naquele ano.

#Em uma base contínua, o Django-Filter visa suportar todas as 
# Versões atuais do Django, as versões correspondentes do Python 
# atual e a versão mais recente do Django REST Framework.

#O suporte para as versões Python e Django será descartado quando 
# chegarem ao fim da vida útil. O suporte para as versões do Python 
# será descartado quando chegarem ao fim da vida útil, mesmo quando 
# ainda forem suportados por uma versão atual do Django.

#Outras mudanças de ruptura são raras. Quando necessário, todos os esforços 
# serão feitos para aplicar um período de descontinuação de “Ano mais dois”. 
# Por exemplo, uma alteração inicialmente introduzida na versão 23.x ofereceria 
# um substituto quando viável e, finalmente, seria removida na versão 25.1.
# Onde os fallbacks não são viáveis, as alterações de interrupção sem descontinuação 
# serão chamadas no

# pip install django-filter
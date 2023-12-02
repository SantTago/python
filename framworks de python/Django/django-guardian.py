# pip install django-guardian

# Configuração
# Precisamos nos conectar django-guardianao nosso projeto.

# 1 Coloque guardianno seu INSTALLED_APPSmódulo de configurações:

INSTALLED_APPS = (
 ...
 'guardian',
)

# 2 Adicione back-end de autorização extra ao seu settings.py:

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'guardian.backends.ObjectPermissionBackend',
)

# 3 Crie guardiantabelas de banco de dados executando:

python manage.py migrar

#Uso
#Após a instalação e os ganchos do projeto, podemos finalmente 
# usar as permissões de objeto com o Django .
# Vamos começar bem rápido:.

>>> from django.contrib.auth.models import User, Group
>>> jack = User.objects.create_user('jack', 'jack@example.com', 'topsecretagentjack')
>>> admins = Group.objects.create(name='admins')
>>> jack.has_perm('change_group', admins)
False
>>> from guardian.models import UserObjectPermission
>>> UserObjectPermission.objects.assign_perm('change_group', jack, obj=admins)
<UserObjectPermission: admins | jack | change_group>
>>> jack.has_perm('change_group', admins)
True

#  É claro que nosso agente jack aqui não seria capaz de change_group globalmente:

>>> jack.has_perm('change_group')
False


# Integração do administrador
# Substitua admin.ModelAdminpor GuardedModelAdminaqueles modelos que devem ter suporte a permissões de objeto no painel de administração.

# Por exemplo:

from django.contrib import admin
from myapp.models import Author
from guardian.admin import GuardedModelAdmin

# Old way:
#class AuthorAdmin(admin.ModelAdmin):
#    pass

# With object permissions support
class AuthorAdmin(GuardedModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)
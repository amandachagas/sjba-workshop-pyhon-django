Instalar o django: pip install django


Iniciar o projeto: django-admin startproject devweb


Entrar na pasta criada


No settings.py adicionar: ALLOWED_HOSTS=['*']


No nivel do projeto rodar: python3 manage.py runserver


Criar um app: python3 manage.py startapp agenda


No settings.py adicionar: INSTALLED_APPS = [ ... 'agenda.apps.AgendaConfig', ]


Na pasta do app (agenda) criar o arquivo urls.py  -  Colar o texto passado  -   agenda/urls.py


Na pasta do projeto, mesmo nivel do setting.py, alterar o arquivo urls.py  -  Colar o texto passado  -  devweb/urls.py


Na pasta do app (agenda) acessar o views.py  -  criar a funcao index  -  Colar o texto passado  -  views_01.py


No nivel do projeto rodar: python3 manage.py runserver


Na views.py comentar o return HttpResponse da funcao index e descomentar o return render() que esta la, para a views redirecionar pro html


No nivel do projeto rodar: python3 manage.py runserver


ERROR - O que houve? - Precisamos criar a pasta templates e informar ao settings.py onde esse arquivos estao


No nivel do projeto criar a pasta templates. Dentro dessa pasta, criar o arquivo agenda.html - Colar o texto passado  -  agenda_01.html


No settings.py , na variavel TEMPLATES, substituir 1) Ubuntu/Mac: 'DIRS': [os.path.join(BASE_DIR, 'templates')],		2) Debian: 'DIRS': [ BASE_DIR / 'templates', ],


No nivel do projeto rodar: python3 manage.py runserver  -  TUDO OK? Voce deve visualizar o form agora


Carregando arquivos estaticos (css, js...): 


1) Criar no nivel do projeto uma pasta chamada static e dentro dela o arquivo style.css  -  Colar o texto passado  -  style.css
2) Configurar o settings.py (pode variar, aqui eh como colcoar no Debian) para apontar para os arquivos estaticos: 2.1) STATIC_URL = str(BASE_DIR / 'site/static') + '/'		2.2) STATICFILES_DIRS = [BASE_DIR / 'static',]		2.3) STATIC_ROOT = str(BASE_DIR / 'site/static/')
3) No nivel do projeto, rodar o comando: python3 manage.py collectstatic
4) Na primeira linha do agenda.html adicionar a tag: {% load static %}
5) Dentro do head importar o arquivo css: <link rel="stylesheet" href="{% static 'style.css' %}">


TUDO OK? Voce deve visualizar o template bonito agora


Criar o modelo: dentro da pasta 'agenda' editar o arquivo models.py  -  Colar o texto passado


Apos criar o model, rodar os seguintes comandos: 1) python3 manage.py makemigrations		2) python3 manage.py migrate


Focando no form agora, precisamos focar em persistir os dados quando enviados. Altere o method do form para method="post". Adicione a tag {% csrf_token %} dentro do form.


Focando na view.py agora, na views.py importar o model para manipularmos os objetos e exibir no template. Como nesse exemplo faremos tudo no mesmo arquivos html, a views index sera responsavel tanto por salvar os contatos como por exibir os contatos salvos.


Para retornar os contatos salvos, crie uma variavel contatos que ira receber os objetos existentes na aplicacao da seguinte forma: <contatos = Contato.objects.all()> Para enviar essa variavel para o template, basta adiciona-la no formato de um dicionario como terceiro parametro do render()  -  Colar o texto passado  -  views_02.py


No agenda.html, utilizaremos tags de listagem para exibir os objetos salvos. Para tal, faremos isso de forma dinamica utilizando as Template Tags do Django. Iremos utilizar um for para exibir cada um dos objetos  -  Colar o texto passado  -  agenda_02.html


Para persistir os dados enviados pelo form no banco de dados, primeiro precisamos verificar se o request da view eh do tipo POST. Caso seja, criamos um objeto com os dados do form e retornamos a lista de objetos existentes  -  Colar o texto passado  -  views_03.py


>>>>> EXTRA 


O django oferece uma area administrativa 'http://localhost:8000/admin/'. Caso tenha reparado, existe um arquivo dentro no app agenda chamado admin.py. Eh nesse arquivo que voce configura o que quer exibir na area administrativa.


Atividade extra: Criar um super usuario admin no django *dica: usar comandos do django no terminal*; Configurar o admin.py para exibir os contatos na area administrativa.
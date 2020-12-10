# Guia de conducao do workshop

1. Instalar o django: `pip install django`

1. Iniciar o projeto: `django-admin startproject devweb`

1. Entrar na pasta do projeto criada: `cd devweb` 

1. No **settings.py** adicionar: `ALLOWED_HOSTS=['*']`

1. No nivel do projeto rodar: `python3 manage.py runserver`

1. Criar um app: `python3 manage.py startapp agenda`

1. No **settings.py** adicionar: `INSTALLED_APPS = [ ... 'agenda.apps.AgendaConfig', ]`

1. Na pasta do app (agenda) criar o arquivo **urls.py**  *-  Colar o texto passado  -   agenda/urls.py*

1. Na pasta do projeto, dentro da pasta devweb, mesmo nivel do **setting.py**, alterar o arquivo **urls.py**  *-  Colar o texto passado  -  devweb/urls.py*

1. Na pasta do app (agenda) acessar o **views.py** para criar a funcao index  *-  Colar o texto passado  -  views_01.py*

1. No nivel do projeto rodar: `python3 manage.py runserver`

1. Na **views.py** comentar o `return HttpResponse` da funcao index e descomentar o `return render()` que esta la, para a views redirecionar pro arquivo **agenda.html**

1. No nivel do projeto rodar: `python3 manage.py runserver`

1. **ERROR** - O que houve? - Precisamos criar a pasta templates e informar ao **settings.py** onde esses arquivos estao

1. No nivel do projeto criar a pasta templates. Dentro dessa pasta, criar o arquivo **agenda.html** *- Colar o texto passado  -  agenda_01.html*

1. No **settings.py** , na variavel TEMPLATES, substituir:
   1. Ubuntu/Mac: `'DIRS': [os.path.join(BASE_DIR, 'templates')],`
   1. Debian: `'DIRS': [ BASE_DIR / 'templates', ],`

1. No nivel do projeto rodar: `python3 manage.py runserver`  -  **TUDO OK?** Voce deve visualizar o form agora

1. Carregando arquivos estaticos (css, js...):
   1. Criar no nivel do projeto uma pasta chamada static e dentro dela o arquivo **style.css**  *-  Colar o texto passado  -  style.css*
   1. Configurar o **settings.py** (pode variar, aqui eh como colcoar no Debian) para apontar para os arquivos estaticos, no final do arquivo adicione: `STATIC_URL = str(BASE_DIR / 'site/static') + '/'`, `STATICFILES_DIRS = [BASE_DIR / 'static',]` e `STATIC_ROOT = str(BASE_DIR / 'site/static/')`
   1. No nivel do projeto, rodar o comando: `python3 manage.py collectstatic`
   1. Na primeira linha do **agenda.html** adicionar a tag: `{% load static %}`
   1. Ainda no html, dentro do head importar o arquivo css: `<link rel="stylesheet" href="{% static 'style.css' %}">`

1. **TUDO OK?** Voce deve visualizar o template bonito agora

1. Criar o modelo: dentro da pasta 'agenda' editar o arquivo **models.py**  *-  Colar o texto passado - agenda/models.py*

1. Apos criar o model, rodar os seguintes comandos:
   1. `python3 manage.py makemigrations`
   1. `python3 manage.py migrate`

1. Focando no form do html agora, precisamos focar em persistir os dados quando enviados. 
   1. Altere o method do form para `method="post"` 
   1. Adicione a tag `{% csrf_token %}` dentro do form.

1. Focando na **view.py** agora eh preciso importar o model para manipularmos os objetos e exibe-los no template. Como nesse exemplo faremos tudo no mesmo arquivos html, a views index sera responsavel **tanto por salvar** os contatos **como por exibir** os contatos salvos.

1. Para retornar os contatos salvos, crie uma variavel contatos que ira receber os objetos existentes na aplicacao da seguinte forma: `contatos = Contato.objects.all()`. Para enviar essa variavel para o template, basta adiciona-la no formato de um dicionario como terceiro parametro do `render()`  *-  Colar o texto passado  -  views_02.py*

1. No **agenda.html**, utilizaremos tags html de listagem para **exibir** os objetos salvos. Para tal, faremos isso de forma dinamica utilizando as Template Tags do Django. Iremos utilizar um for para exibir cada um dos objetos  *-  Colar o texto passado  -  agenda_02.html*

1. Para **persistir** os dados enviados pelo form no banco de dados, primeiro precisamos verificar se o `request` da view eh do tipo `POST`. Caso seja, criamos um objeto com os dados do form e retornamos a lista de objetos existentes  *-  Colar o texto passado  -  views_03.py*

1. **Parabens, voce concluiu o workshop!** Agora voce sabe fazer uma aplicacao Django com registro de objetos e listagem dinamica dos mesmos no template!!!

## Atividade Extra

O Django oferece uma area administrativa `http://localhost:8000/admin/`. Caso tenha reparado, existe um arquivo dentro no app agenda chamado **admin.py**. Eh nesse arquivo que voce configura o que quer exibir na area administrativa.

* **Atividade extra:** 
   * Criar um super-usuario no django para acessar essa area *dica: usar o comando do django no terminal*; 
   * Configurar o **admin.py** para exibir os contatos na area administrativa.
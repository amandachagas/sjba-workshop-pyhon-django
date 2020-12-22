# Workshop Python + Django -- Guia de condução

1. Criar uma conta gratuita no [Paiza Cloud](https://paiza.cloud/signup). Já no Paiza Cloud, **criar um server com Django**.

1. Iniciar o projeto: `django-admin startproject devweb`

1. Entrar na pasta do projeto criada: `cd devweb` 

1. No **settings.py** adicionar: `ALLOWED_HOSTS=['*']`

1. No nível do projeto rodar: `python3 manage.py runserver`

1. Criar um app: `python3 manage.py startapp agenda`

1. No **settings.py** adicionar: `INSTALLED_APPS = [ ... 'agenda.apps.AgendaConfig', ]`

1. Na pasta do app (agenda), criar o arquivo **urls.py**  *-  Colar o texto passado  -   agenda/urls.py*

1. Na pasta do projeto, dentro da pasta devweb, mesmo nível do **setting.py**, alterar o arquivo **urls.py**  *-  Colar o texto passado  -  devweb/urls.py*

1. Na pasta do app (agenda) acessar o **views.py** para criar a função index  *-  Colar o texto passado  -  views_01.py*

1. No nível do projeto rodar: `python3 manage.py runserver`

1. Na **views.py** comentar o `return HttpResponse` da função index e descomentar o `return render()` que está lá, para assim a views redirecionar pro arquivo **agenda.html**

1. No nível do projeto rodar: `python3 manage.py runserver`

1. **ERROR** - O que houve? - Precisamos criar a pasta templates e informar ao **settings.py** onde esses arquivos estão

1. No nível do projeto criar a pasta templates. Dentro dessa pasta, criar o arquivo **agenda.html** *- Colar o texto passado  -  agenda_01.html*

1. No **settings.py** , no DIR da variável TEMPLATES, substituir:
   1. Ubuntu/Mac: `'DIRS': [os.path.join(BASE_DIR, 'templates')],`
   1. Debian: `'DIRS': [ BASE_DIR / 'templates', ],`

1. No nível do projeto rodar: `python3 manage.py runserver`  -  **TUDO OK?** Você deve visualizar o form agora

1. Carregando arquivos estáticos (css, js...):
   1. Criar no nível do projeto uma pasta chamada static e dentro dela o arquivo **style.css**  *-  Colar o texto passado  -  style.css*
   1. Configurar o **settings.py** (essa parte varia de acordo com o SO utilizado) para apontar para os arquivos estáticos, no final do arquivo adicione:
      1. **Ubuntu:** `STATIC_URL = '/static/'`, `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'site/static'),]` e `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`
      1. **Ubuntu (alternativa flat):** `STATIC_URL = '/home/ubuntu/devweb/site/static/'`, `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]` e `STATIC_ROOT = os.path.join(BASE_DIR, '/home/ubuntu/devweb/site/static')`
      1. **Debian:** `STATIC_URL = str(BASE_DIR / 'site/static') + '/'`, `STATICFILES_DIRS = [BASE_DIR / 'static',]` e `STATIC_ROOT = str(BASE_DIR / 'site/static/')`
   1. No nível do projeto, rodar o comando: `python3 manage.py collectstatic`
   1. Na primeira linha do **agenda.html** adicionar a tag: `{% load static %}`
   1. Ainda no html, dentro do head importar o arquivo css: `<link rel="stylesheet" href="{% static 'style.css' %}">`

1. **TUDO OK?** Você deve visualizar o template bonito agora

1. Criar o model: dentro da pasta 'agenda' editar o arquivo **models.py**  *-  Colar o texto passado - agenda/models.py*

1. Após criar o model, rodar os seguintes comandos:
   1. `python3 manage.py makemigrations`
   1. `python3 manage.py migrate`

1. Focando no form do html agora, precisamos persistir os dados quando enviados. 
   1. Altere o method do form para `method="post"` 
   1. Adicione a tag `{% csrf_token %}` dentro do form.

1. Focando na **view.py** agora, é preciso importar o model para manipularmos os objetos e exibí-los no template. Como nesse exemplo faremos tudo no mesmo arquivo html, a views index será responsável **tanto por salvar** os contatos **como por exibir** os contatos salvos.

1. Para retornar os contatos salvos, crie uma variável 'contatos' que irá receber os objetos existentes da aplicação da seguinte forma: `contatos = Contato.objects.all()`. Para enviar essa variável para o template, basta adicioná-la no formato de um dicionário como terceiro parâmetro do `render()`  *-  Colar o texto passado  -  views_02.py*

1. No **agenda.html**, utilizaremos tags html de listagem para **exibir** os objetos salvos. Para tal, faremos isso de forma dinâmica utilizando as **Template Tags** do Django. Iremos utilizar um 'for' para exibir cada um dos objetos  *-  Colar o texto passado  -  agenda_02.html*

1. Para **persistir** os dados enviados pelo 'form' no banco de dados, primeiro precisamos verificar se o `request` da view é do tipo `POST`. Caso seja, criamos um objeto com os dados do 'form' e retornamos a lista de objetos existentes  *-  Colar o texto passado  -  views_03.py*

1. **Parabéns, você concluiu o Workshop!** Agora você sabe fazer uma aplicação Django com registro de objetos e listagem dinâmica dos mesmos no template!!!

## Exercício

Considerando que agora a agenda deve registrar também a **cidade** dos contatos, realize as alterações necessárias para:
   - Informar a cidade no registro do contato
   - Persistir a informação da cidade
   - Listar, além de nome e telefone, a cidade
>

### Extra: Curiosidade/Aprofundamento

O Django oferece uma área administrativa `http://localhost:8000/admin/`. Caso tenha reparado, existe um arquivo dentro no app agenda chamado **admin.py**. É nesse arquivo que você configura o que quer exibir na área administrativa.

* **Atividade extra:** 
   * Criar um super-usuário no Django para acessar essa área *dica: usar o comando do Django no terminal*
   * Configurar o **admin.py** para exibir os contatos na area administrativa


### Créditos
Esse Workshop foi realizado como uma atividade avaliativa da disciplina Desenvolvimento Web do curso Residência em Software SJBA oferecido pela UFBA em 2020. Workshop realizado em 21/12/2020, alunos responsáveis: Amanda Chagas de Oliveira e Reno Costa Alencar.
   

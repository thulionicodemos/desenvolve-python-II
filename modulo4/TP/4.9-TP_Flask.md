### 1. Faça como eu fiz na aula

Prepare o código que vimos em aula. Confira se o seu código possui a mesma estrutura de arquivos descrita no final do capítulo da apostila.
```
microblog/
|-- .flaskenv
|-- flask_env/
|-- app/
|   |-- __init__.py
|   |-- alquimias.py
|   |-- routes.py
|   |-- templates/
|   |   |-- base.html
|   |   |-- index.html
|   |   |-- login.html
|   |-- models/
|   |   |-- models.py
|-- microblog.py
|-- instance/
|   |-- microblog.db
```

---

### 2. Incorpore o módulo Flask-Login

Incorpore o módulo Flask-Login para gerenciar usuários conectados no nosso sistema. Para isso, basta seguir as instruções a seguir. Você também pode consultar os tutoriais do [Mega Tutorial de Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins) e do [Real Python](https://realpython.com/using-flask-login-for-user-management-with-flask/).

> Antes de tudo, instale **no ambiente virtual deste projeto** a extensão Flask-Login: `pip install flask-login`.

```python
# No arquivo __init__.py

# inclua o import do LoginManager no início do arquivo
from flask_login import LoginManager

# Após instanciar o objeto principal da aplicação
# instancie o objeto LoginManager
# e crie uma chave secreta da sua aplicação 
# (se ainda não tinha criado acompanhando a apostila)
app = Flask(__name__)
# ...
login = LoginManager(app)
app.config['SECRET_KEY'] = "PD12345678"
```

---

```python
# No arquivo models.py
# adicionaremos 2 novos imports e uma função

# UserMixin será a superclasse do nosso modelo User
# incluindo atributos e métodos de gerência de login, como:
# is_authenticated, is_active, is_anonymous, get_id()
from flask_login import UserMixin

# importe também o objeto login (LoginManager) inicializado
# em __init__.py
from app import login

# Nosso modelo User agora estará numa relação de herança múltipla
# herdando também os atributos e métodos de UserMixin
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    # ...

# crie a função decorada load_user.
# Note que o objeto login que acabamos de importar tem o decorador user_loader.
# Essa função será usada internamente pelo Flask para recuperar o usuário atual
@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
```

---

```python
# No arquivo alquimias.py
# Todas as funções devem retornar o objeto User

def validate_user_password(username, password):
    # res = query...
    user = res.first()
    if user and user.password == password: return user ### 
    else: return None 

def user_exists(username):
    # res = query...
    user = res.first()
    return user ###

def create_user(username, password, remember=False, last_login=None):
    # definição de new_user e sua adição no banco
    return new_user   
```

---

```python
# No arquivo routes.py

# Vamos importar os módulos de gerência de login
from flask_login import (
    current_user,  ## objeto User atual
    login_user,    ## método de login
    logout_user,   ## método de logout
    login_required ## decorador de funções que só podem ser acessadas após login
)

# Na rota principal, usaremos o objeto current_user para recuperar
# as informações do usuário autenticado (caso haja). 
# Este objeto terá todos os atributos que definimos no db.Model User,
# incluindo o username, necessário no template index.html
@app.route('/')
@login_required
def index():
    user=None
    if current_user.is_authenticated:
        user = current_user
    # return render_template ... 

# Na rota de login, o principal é invocar o método login_user
# com o objeto User que será referenciado por current_user.
# Note que para isso pegamos o retorno User de alquimias.validate_user_password
#
# Também adicionamos uma verificação no início se já existe algum
# usuário autenticado, redirecionando para a página principal em caso positivo.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: ###### 
        return redirect(url_for('index')) ######
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password'].lower()

        user = alquimias.validate_user_password(username, password) ######
        if user:
            print("\nLogin bem sucedido!\n")
            ########### EFETIVANDO LOGIN ############
            login_user(user, remember=user.remember) 
            #########################################
            return redirect(url_for(f"index"))
        else:
            print("\nUsuário ou senha inválidos\n")
            return redirect(url_for('login'))
    # request.method == GET
    return render_template('login.html')

# Na rota de cadastro também precisamos invocar o método login_user
# seguindo a mesma lógica da rota de login.
@app.route('/cadastro', methods=['POST'])
def cadastro():
    username = request.form['username'].lower()
    if alquimias.user_exists(username):
        print("\nUsuário já existe!\n")
        return redirect(url_for('login'))
    else:
        username = username
        password = request.form['password'].lower()
        remember = True if request.form.get('remember') == 'on' else False
        user = alquimias.create_user(username, password, remember) ###### 
        ######## EFETIVANDO LOGIN #########
        login_user(user, remember=remember)
        ###################################
        return redirect(url_for(f"index"))

# Por fim, criamos uma nova rota /logout
# para invocar a função logout_user 
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(f"index"))
```

---

```html
<!-- 
Por fim, no arquivo base.html
precisamos adicionar o botão logout, apontando para
a nova rota /logout que criamos há pouco.
-->
<div>Microblog: 
    <a href="/">Home</a>
    <a href="/login">Login</a>
    <a href="/logout">Logout</a> <!-- botão para nova rota -->
</div>
```

---

### 3. Incrementando User

Vamos adicionar uma foto de perfil e uma bio para o usuário! Para isso você deve:

* Criar um novo template `cadastro.html` (e criar uma nova referência para ele em `base.html`), para separar os formulários de cadastro e de login. Lembre-se de remover o botão cadastro do formulário em `login.html` e passá-lo para `cadastro.html`.

* Acrescente em `cadastro.html`, além das informações do formulário de login, também os campos: 
    * foto de perfil: recebe uma URL com o link para a foto desejada
    * bio: caixa de texto para o usuário se descrever brevemente

* Alterar o modelo User, adicionando os campos correspondentes 

* Alterar a função associada à rota de cadastro para coletar os novos campos do formulário e enviá-los para a função que cria um novo usuário no banco.

* Alterar o template `index.html` para renderizar os atributos foto e bio para usuários autenticados. Lembre-se que o template deve verificar se recebeu um objeto User válido.

---

### 4. Adicionando posts!

Vamos permitir que o usuário cadastre posts textuais. Para isso você deve:

#### 4.1 Criar o modelo Post como definido a seguir.

Crie uma classe Post em models.py com o ORM referente à seguinte tabela.

|      Post                     |
| ----------------------------- |
| id         : int, PK          |
| body       : str              |
| timestamp  : datetime         |
| user_id    : int, FK(User.id) |

#### 4.2 Incremente ambos os modelos `User` e `Post` com objetos `relationship` 

Objetos do tipo `relationship` pertencem ao SQLALchemy ORM. Estes objetos não fazem parte do modelo SQL de dados, porém alimentam os modelos ORM com os relacionamentos existentes. Em termos simples, podemos adicionar atributos a um objeto que permitem acessar facilmente os dados relacionados. Por exemplo, ao adicionar o relacionamento entre User e Posts (como orientado a seguir), podemos executar o seguinte trecho de código:
```python
user = db.session.get(User, 1) # seleciona um usuário do banco
for post in user.posts: # acessa o atributo de relacionamento User.posts
    print(post.body)    # acessa atributos do Post sem precisar fazer join das tabelas
```

Para implementar os relacionamentos, faça:
    
```python
# Importe relationship do SQLAlchemy ORM
from sqlalchemy.orm import relationship
# ...
class User(db.Model):
    # ...
    ## Adicione o atributo posts ao User
    ## O Mapped[list['Post']] anota esse campo como uma coleção 
    ## de referências à tabela Post.
    ## O campo back_populates indica o outro lado da relação. Na classe
    ## Post haverá um atributo author que deve ser populado com uma 
    ## referência à User.
    posts: Mapped[list['Post']] = relationship(back_populates='author')

class Post(db.Model):
    # ...
    ## Adicione o atributo author ao Post
    ## O campo está anotado como uma referência à tabela User, Mapped[User]
    ## Mais uma vez, o argumento back_populates indica o outro lado da relação,
    ## ou seja, User tem um campo posts que será populado com identificadores
    ## de Post que integram a relação. 
    author: Mapped[User] = relationship(back_populates='posts')
```

Você pode testar a sua aplicação adicionando usuários e/ou posts manualmente com o seguinte código (<span style="color:red">**não incorpore ele ao seu projeto! É somente para teste!!**</span>). Note que, ao alimentar o atributo de relacionamento `author` de um novo post, a chave estrangeira `user_id` será automaticamente definida. Para outros detalhes sobre relacionamentos com SQLAlchemy ORM [confira a documentação](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-many).
```python
from app import app, db
from app.models.models import User, Post
from datetime import datetime

app.app_context().push()

## adicionando usuários
user = User(username='maria', password='123', last_login=datetime.now())
db.session.add(user)
db.session.commit()

## adicionando posts
user = db.session.get(User, 1) # get usuário pelo seu id no banco
post = Post(body='olá mundo!', author=user, timestamp=datetime.now())
db.session.add(post)
db.session.commit()

# listando posts de um usuário
user = db.session.get(User, 1) # get usuário pelo seu id no banco
for post in user.posts: # itera no atributo de relacionamento
    print(post.id, post.body, post.user_id, post.author.username)
```


#### 4.3 Incorpore o CRUD dos posts no seu sistema

* Criando novos posts
    * Crie um template `post.html` com um formulário simples. Apenas um campo de texto para o usuário digitar o post e um botão submit para registrar o post no banco.
    * Crie em `alquimias.py` um método `create_post` que recebe o texto (body) do post e uma referência ao usuário autenticado, e cria um novo post no banco.
    * Crie uma rota `/post` decorada com `@login_required` do Flask-Login que suporta os métodos GET e POST. Para requisições GET, deve renderizar o formulário `post.html`. Para requisições POST deve invocar o méotodo `create_post` enviando os dados necessários, e em seguida redirecionar para a página principal `index`.
    * Adicione no template `index.html` um botão ou link `Escrever post` referenciando a rota `/post`. Lembre-se que o link só deve aparecer caso o template recebe um usuário válido.

* Visualizando posts  
    * Crie em `alquimias` uma função `get_timeline()` que retorna os 5 posts mais recentes. Você deve criar um select na tabela Post ordenado pelo timestamp. Se você incluiu os objetos `relationship` nos modelos, não precisa dar join nas tabelas para acessar o nome do usuário a partir de um objeto `Post` :)
    * Incremente a página principal. Para isso, você deve:
        * Alterar a função associada à rota principal `/` para invocar a função `get_timeline()` apenas caso exista um usuário autenticado. A lista de posts retornada será passada para o template `index.html`.
        * Você deve alterar o `index.html` para apresentar a lista de posts. Lembre-se que você deve verificar se o template recebeu uma lista válida.
     
---

### 5. Hora de estilizar a sua aplicação

Aprimore os templates da sua aplicação incorporando scripts de estilização CSS. Tenha em mente os seguintes critérios:
* Aparência: Utilização eficaz de CSS para estilizar o layout do site, seguindo as práticas recomendadas
* Usabilidade: Facilidade de navegação e interação
* Acessibilidade: Implementação de práticas como uso adequado de marcadores, descrições alternativas para imagens (alt), contraste de cores para facilitar a leitura, etc.

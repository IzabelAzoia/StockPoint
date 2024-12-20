# StockPoint

Este é o repositório do projeto **StockPoint**, um sistema de gerenciamento de estoque que permite o controle eficiente de produtos, entradas e saídas, além de gerar relatórios e acompanhar o status do estoque em tempo real.

## Como rodar o projeto

### 1. Clonar o repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/IzabelAzoia/StockPoint.git
cd StockPoint
```

### 2. Criar e ativar o ambiente virtual

Para garantir que todas as dependências sejam isoladas, crie um ambiente virtual em Python:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual com o comando apropriado:

- **Windows**:

```bash
.\.venv\Scripts\activate
```

- **Linux/macOS**:

```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

Instale todas as dependências listadas no arquivo `requirements.txt` para que o projeto funcione corretamente:

```bash
pip install -r requirements.txt
```

### 4. Configurar o banco de dados

Crie as configurações do ambiente (se necessário) com o seguinte comando:

```bash
python contrib/env_gen.py
```

Agora, aplique as migrações para configurar o banco de dados e garantir que todas as tabelas necessárias sejam criadas:

```bash
python manage.py migrate
```

### 5. Rodar o servidor de desenvolvimento

Com o banco de dados configurado, inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

Abra o navegador e acesse `http://127.0.0.1:8000/` para visualizar o aplicativo em funcionamento.

### 6. Acessar a interface de administração

Se você configurou um superusuário para acessar o painel administrativo do Django, poderá fazer login e gerenciar os dados do sistema. Se ainda não criou o superusuário, use o comando abaixo para criá-lo:

```bash
python manage.py createsuperuser
```

Depois, faça login no painel de administração acessando `http://127.0.0.1:8000/admin/` e utilize as credenciais do superusuário.

## Links Úteis

Aqui estão alguns links úteis para aprender mais sobre as tecnologias e recursos utilizados neste projeto:

- [Python Decouple no PyPI](https://pypi.org/project/python-decouple/) - Usado para carregar variáveis de ambiente de forma segura.
- [Bootstrap Starter Template](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template) - Template básico do Bootstrap para facilitar o desenvolvimento do front-end.
- [Emmet - Ferramenta de aceleração de codificação](https://emmet.io/) - Extensão para editores de texto que facilita o desenvolvimento de HTML.
- [Bootstrap Starter Template (versão 5)](https://getbootstrap.com/docs/5.3/getting-started/rtl/#starter-template) - Novo modelo de starter template do Bootstrap para a versão 5.
- [Class Based View (CCBV)](https://ccbv.co.uk/) - Recurso útil para entender melhor as views baseadas em classe no Django.
- [Django Form Inline Class-Based Views](https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-editing/#using-forms) - Guia sobre como trabalhar com formulários em views baseadas em classe no Django.
- [django-bootstrap-form](https://django-bootstrap-form.readthedocs.io/en/latest/) - Biblioteca para integrar o Bootstrap com o Django Forms de maneira mais simples.

## Outros Detalhes

- **Requisitos**: Este projeto foi desenvolvido com Python 3.x e Django 5.x. A versão exata de Python necessária pode ser especificada no arquivo `requirements.txt`.
- **Licença**: (Adicione informações sobre a licença do seu projeto, se necessário. Caso contrário, remova essa seção).

## Contribuições

Se você quiser contribuir para o desenvolvimento deste projeto, siga estas etapas:

1. Fork o repositório.
2. Crie uma branch para sua modificação (`git checkout -b minha-modificacao`).
3. Faça suas alterações e faça commit (`git commit -am 'Adicionando minha modificação'`).
4. Envie para o seu repositório fork (`git push origin minha-modificacao`).
5. Crie um pull request para que possamos revisar suas alterações.

---

Boa sorte com o desenvolvimento do seu projeto StockPoint! Se precisar de ajuda, sinta-se à vontade para abrir uma issue ou entrar em contato.



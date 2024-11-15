# StockPoint

Este é o repositório do projeto **StockPoint**, um sistema de gerenciamento de estoque.

## Como rodar o projeto

### 1. Clonar o repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/IzabelAzoia/StockPoint.git
cd StockPoint
python3 -m venv .venv
.\.venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate

## Links Úteis

- [Python Decouple no PyPI](https://pypi.org/project/python-decouple/)
- [bootstrap starter-template](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template)
- [emmet](https://emmet.io/)
- [start.html](https://getbootstrap.com./docs/5.3/getting-started/rtl/#starter-template)
- [ Class Based View - ccbv.co.uk](https://ccbv.co.uk/)
- [form-inline-cbv](https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-editing/#using-forms)
- [django-bootstrap-form](https://django-bootstrap-form.readthedocs.io/en/latest/)


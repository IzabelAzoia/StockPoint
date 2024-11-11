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



# PipeRun Extractor

Biblioteca Python 3.11+ para extração de dados dos endpoints do CRM PipeRun de Vendas

## Instalação
A instalação desta biblioteca pode ser executada utilizando a ferramenta `pip` 21+
### Método 1
```shell
python3 -m pip install git+https://github.com/crmpiperun/piperun-extractor.git@1.0.0
```
### Método 2
```shell
python3 -m pip install https://github.com/crmpiperun/piperun-extractor/archive/stable/1.0.0.zip
```

## Uso como CLI
```shell
piperun-extractor --help 
piperun-extractor deals --token "abcdefghijklmnopqrstuvwxyz" --after "2025-01-01T00:00:00" --ext jsonl --output deals.jsonl
```

## Uso como Biblioteca
```python
from datetime import datetime
from piperun.extractor import PipeRunExtractor

extractor = PipeRunExtractor(token='abcdefghijklmnopqrstuvwxyz')
deals = extractor.deals(after=datetime(2025, 1, 1))

for deal in deals:
    print(deal.title)
```

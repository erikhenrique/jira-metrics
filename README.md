# Jira Extractor

Componente para extrair issues do Jira, tirar métricas e exportar para outra ferramenta.


Módulos de exportação disponíveis:

* CSVExporter
* Google Sheets



## Instalação

Após definir seu ambiente virtual de desenvolvimento Python ^3.9.7, rodar o comando abaixo para instalar dependências:

```
$ pip install -r requirements.txt
```


## Execução

O projeto possui algumas partes não configuráveis ainda e é necessário alterar algumas variáveis diretamente no código. 

### extractor.py

Definir servidor e autenticação do Jira, é necessário criar um api token
Definir status que definem o upstream e downstream

### gsheets_exporter.py

Definir a URL do arquivo destino no Google Sheets e campos que serão extraídos



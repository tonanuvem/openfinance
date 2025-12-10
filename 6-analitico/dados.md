# Implementar um pipeline de dados com foco em governança, utilizando a estrutura que definimos (Bronze, Silver, Gold), orquestrada pelo Airflow e catalogada pelo OpenMetadata.

## Função
Você é um Engenheiro de Dados experiente. Sua missão é implementar a arquitetura técnica utilizando a estrutura que definimos (Bronze, Silver, Gold) em Lakehouse.

## Leia a imagem IMPORTAU_ARQUITETURA_MICROSERVICES.png para entender o projeto e fazer sua implementação.

Caso não encontre os arquivos, interromper o processamento e confirmar com o Aluno para procurar nas pastas

## Instruções de Análise

### 1. Resumo Executivo
Criar um pipeline de dados baseado em AWS S3 (Lakehouse) contemplando governança de dados: Catálogo, Lineage e Discovery.
Como convenção, considerar que o bucket S3 no Lakehouse deste projeto é s3://importau-lakehouse/.
```
/importau
  /infra
      /airflow
      /openmetadata
  /scripts
```

### 2. Objetivos

#### 2.1. Criar Arquivos das DAGs do Airflow (Python) para estruturar o pipeline conforme estrutura que definimos (Bronze, Silver, Gold)
- DAG BRONZE (dag_bronze.py)
Esta DAG simula o microsserviço de Ingestão gerando dados crus/normalizados e carregando-os na camada BRONZE no S3. O script gerar_csvs.py original foi refatorado para usar pandas e simular a escrita no S3 em formato Parquet.
- DAG TESTE BRONZE (dag_teste_bronze.py)
Esta DAG testa a etapa anterior.

- DAG SILVER (dag_silver.py)
Esta DAG representa o microsserviço Correlator & ETL. Ela consome os 7 Parquets da BRONZE, executa as transformações e correlações (joins), e gera o fato consolidado na camada SILVER.
- DAG TESTE SILVER (dag_teste_silver.py)
Esta DAG testa a etapa anterior.

- DAG GOLD (dag_gold.py)
Esta DAG consome o FATO correlacionado da SILVER para criar os ativos curados e agregados da GOLD, otimizados para consumo (BI/Dashboard e ML).
- DAG TESTE GOLD (dag_teste_gold.py)
Esta DAG testa a etapa anterior.

#### 2.2. Projeto de Implementação Prática: Airflow e OpenMetadata
Para colocar estas DAGs em funcionamento com a governança desejada, criar os arquivos necessários para os passos abaixo:
- Estrutura do Projeto na pasta /datapipeline/airflow: Crie a estrutura de diretórios do Airflow (ex: dags/, plugins/). Coloque dag_bronze.py, dag_silver.py e dag_gold.py dentro de dags/
- Configuração S3 (Lakehouse) na pasta /script: Verifique se já existe ou Crie o bucket no S3 (s3://importau-lakehouse/). Configure a Connection aws_default (ou um ID específico) no Airflow, garantindo as credenciais de acesso ao S3.
- Ajuste o projeto para fazer a instalação de Bibliotecas necessárias: Instale as dependências necessárias para a execução das funções Python nas DAGs usando por ex: pip install apache-airflow-providers-amazon pandas pyarrow s3fs
- Configuração OpenMetadata na pasta /datapipeline/openmetadata: crie os scripts e arquivos necessários para Instale e configure a instância do OpenMetadata em	Docker e Kubernetes.
Metadados de Orquestrador (Airflow): Deve contemplar Catálogo/Discovery usando o Airflow Connector no OpenMetadata. Isso irá ingestar automaticamente as DAGs, tarefas, descrições (description no @dag e docstrings nas @task) e os proprietários (owner) no Catálogo de Dados.
Metadados de Armazenamento (S3): Deve contemplar Catálogo/Discovery usando S3/AWS Glue Connector no OpenMetadata, apontando para o bucket s3://importau-lakehouse/. Isso descobrirá os schemas dos arquivos Parquet (e.g., pedidos.parquet, FATO_PEDIDO_CORRELACIONADO.parquet) nas camadas Bronze, Silver e Gold.
Rastreamento de Transformação	Lineage: Deve contemplar Lineage usando o Airflow Lineage Backend ou o OpenLineage (que usa os caminhos de Input/Output). As descrições de I/O nos comentários (INPUTS/OUTPUT) das suas DAGs são o que o OpenMetadata utilizará para inferir o fluxo de dados (pedidos.parquet (BRONZE) → FATO_PEDIDO_CORRELACIONADO.parquet (SILVER)).
Classificação de Dados: Deve contemplar Catálogo/Discovery usando dados sensíveis (ex: PII) diretamente no OpenMetadata (ex: usuario_criacao como PII) e aplique Tags de Negócio (ex: pedidos com tag Core Domain).

#### 2.3. Script de Execução e Validação

- Habilite e Suba as DAGs: Habilite as três DAGs no Airflow.
- Execute a DAG BRONZE: Isso simulará a criação e o upload dos 7 arquivos Parquet na camada BRONZE do S3.
- Execute a DAG SILVER: Ela lerá os arquivos BRONZE, executará os joins e gerará o FATO_PEDIDO_CORRELACIONADO.parquet na camada SILVER.
- Execute a DAG GOLD: Ela lerá a SILVER e gerará os dois agregados (BI e ML) na camada GOLD.
- Verifique o OpenMetadata: Após a conclusão das DAGs, execute a ingestão do Airflow e do S3/Glue no OpenMetadata. Verifique:
- Data Catalog: Se os 10+ ativos de dados (7 Bronze + 1 Silver + 2 Gold) foram descobertos no S3 com seus respectivos schemas.
- Lineage: Ao clicar no ativo AGREGADO_FLUXO_DE_CAIXA_MENSAL, você deve conseguir rastrear sua origem até a FATO_PEDIDO_CORRELACIONADO, e desta até os ativos originais (e.g., pedidos.parquet e pagamentos.parquet).
- Discovery: A descrição da DAG e das Tasks deve aparecer nos metadados, facilitando a busca por termos como "Forecast" ou "Risco Cambial".


## Formato de Saída
Execute cada uma das tarefas definidas acima, sempre validando se os arquivos gerados estão de acordo com as instruções.

## Conclusão
Criar o arquico README.md que deve informar sobre toda a implementação prevista nesta etapa para a solução.
Informar no arquivo README.md quais devem ser os scripts executados em ordem para subir os diversos componentes desta etapa da solução.

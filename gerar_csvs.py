#!/usr/bin/env python3
"""
Script para gerar todos os arquivos CSV do sistema de Análise de Dados Comerciais
Execute: python gerar_csvs.py

ARQUITETURA DE DADOS:
- 7 arquivos CSV com dados correlacionados
- Simula pipeline Bronze → Silver → Gold
- Dados prontos para análise preditiva e dashboards
"""

import os
import csv
from datetime import datetime

def criar_diretorio():
    """Cria diretório para os CSVs"""
    os.makedirs('csv_exports', exist_ok=True)
    print("✓ Diretório 'csv_exports' criado/verificado")

def gerar_pedidos():
    """
    Gera pedidos.csv
    
    CAMPOS-CHAVE: pedido_id (PK), fornecedor_id (FK), data_pedido
    CORRELAÇÃO: 
        - pedidos.fornecedor_id → fornecedores.fornecedor_id
        - pedidos.pedido_id → itens_pedido.pedido_id
        - pedidos.pedido_id → pagamentos.pedido_id
    USO: Matheus (Analista de Dados) - Base para análise de compras e previsões
    """
    dados = [
        ["pedido_id","data_pedido","fornecedor_id","valor_total_brl","status","tipo_pagamento","prazo_dias","data_entrega_prevista","usuario_criacao","observacoes"],
        ["PED001","2024-10-15","FORN001","15750.50","ENTREGUE","BOLETO","30","2024-11-14","matheus.silva","Pedido urgente"],
        ["PED002","2024-10-16","FORN002","8920.00","EM_TRANSITO","TRANSFERENCIA","45","2024-12-01","matheus.silva","Frete incluso"],
        ["PED003","2024-10-17","FORN003","12300.75","PENDENTE","CARTAO_CREDITO","15","2024-11-01","matheus.silva",""],
        ["PED004","2024-10-18","FORN001","25600.00","ENTREGUE","BOLETO","60","2024-12-17","matheus.silva","Desconto 5%"],
        ["PED005","2024-10-19","FORN004","5400.25","CANCELADO","PIX","0","2024-11-03","matheus.silva","Cancelado pelo fornecedor"],
        ["PED006","2024-10-20","FORN005","18900.00","EM_TRANSITO","BOLETO","30","2024-11-19","matheus.silva",""],
        ["PED007","2024-10-21","FORN002","9850.50","ENTREGUE","TRANSFERENCIA","45","2024-12-06","matheus.silva","Pedido recorrente"],
        ["PED008","2024-10-22","FORN006","32100.00","PENDENTE","BOLETO","90","2025-01-20","matheus.silva","Importação"],
        ["PED009","2024-10-23","FORN003","7200.00","ENTREGUE","PIX","7","2024-10-30","matheus.silva","Pagamento à vista"],
        ["PED010","2024-10-24","FORN007","14500.75","EM_TRANSITO","CARTAO_CREDITO","30","2024-11-23","matheus.silva",""],
        ["PED011","2024-10-25","FORN001","19800.00","ENTREGUE","BOLETO","45","2024-12-09","matheus.silva",""],
        ["PED012","2024-10-26","FORN008","6700.50","PENDENTE","TRANSFERENCIA","15","2024-11-10","matheus.silva",""],
        ["PED013","2024-10-27","FORN004","28900.00","EM_TRANSITO","BOLETO","60","2024-12-26","matheus.silva","Grande volume"],
        ["PED014","2024-10-28","FORN009","11200.25","ENTREGUE","PIX","7","2024-11-04","matheus.silva",""],
        ["PED015","2024-10-29","FORN005","16500.00","PENDENTE","CARTAO_CREDITO","30","2024-11-28","matheus.silva",""],
        ["PED016","2024-10-30","FORN002","22400.75","EM_TRANSITO","BOLETO","45","2024-12-14","matheus.silva",""],
        ["PED017","2024-10-31","FORN010","8900.00","ENTREGUE","TRANSFERENCIA","30","2024-11-30","matheus.silva",""],
        ["PED018","2024-11-01","FORN003","13700.50","PENDENTE","BOLETO","15","2024-11-16","matheus.silva",""],
        ["PED019","2024-11-02","FORN006","45200.00","EM_TRANSITO","BOLETO","90","2025-02-01","matheus.silva","Importação EUA"],
        ["PED020","2024-11-03","FORN001","9500.25","ENTREGUE","PIX","7","2024-11-10","matheus.silva",""],
        ["PED021","2024-11-04","FORN007","17800.00","PENDENTE","CARTAO_CREDITO","30","2024-12-04","matheus.silva",""],
        ["PED022","2024-11-05","FORN008","12100.75","EM_TRANSITO","TRANSFERENCIA","45","2024-12-20","matheus.silva",""],
        ["PED023","2024-11-06","FORN004","24600.00","ENTREGUE","BOLETO","60","2025-01-05","matheus.silva",""],
        ["PED024","2024-11-07","FORN009","7800.50","PENDENTE","PIX","7","2024-11-14","matheus.silva",""],
        ["PED025","2024-11-08","FORN005","19200.00","EM_TRANSITO","BOLETO","30","2024-12-08","matheus.silva",""],
        ["PED026","2024-11-09","FORN002","15400.25","ENTREGUE","CARTAO_CREDITO","45","2024-12-24","matheus.silva",""],
        ["PED027","2024-11-10","FORN010","10900.00","PENDENTE","TRANSFERENCIA","15","2024-11-25","matheus.silva",""],
        ["PED028","2024-11-11","FORN003","26700.75","EM_TRANSITO","BOLETO","30","2024-12-11","matheus.silva",""],
        ["PED029","2024-11-12","FORN006","38500.00","PENDENTE","BOLETO","90","2025-02-10","matheus.silva","Importação China"],
        ["PED030","2024-11-13","FORN001","14200.50","ENTREGUE","PIX","7","2024-11-20","matheus.silva","Pagamento antecipado"]
    ]
    
    with open('csv_exports/pedidos.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(dados)
    print("✓ pedidos.csv gerado (30 linhas)")

def gerar_fornecedores():
    """
    Gera fornecedores.csv
    
    CAMPOS-CHAVE: fornecedor_id (PK), pais_origem, moeda_negociacao
    CORRELAÇÃO:
        - fornecedores.fornecedor_id → pedidos.fornecedor_id
        - fornecedores.fornecedor_id → produtos.fornecedor_id
        - fornecedores.moeda_negociacao → cambio.moeda
    USO: Márcio Arbues - Gestão de fornecedores nacionais e internacionais
    """
    dados = [
        ["fornecedor_id","razao_social","cnpj","pais_origem","categoria","rating","tempo_parceria_anos","condicoes_pagamento","moeda_negociacao","contato_email","telefone"],
        ["FORN001","TechSupply Brasil Ltda","12.345.678/0001-90","Brasil","Tecnologia","A","5","30-60 dias","BRL","contato@techsupply.com.br","+55-11-3456-7890"],
        ["FORN002","Global Parts International","98.765.432/0001-11","Brasil","Componentes","A+","8","45 dias","BRL","sales@globalparts.com","+55-11-9876-5432"],
        ["FORN003","EletroMax Distribuidora","11.222.333/0001-44","Brasil","Eletrônicos","B+","3","15-30 dias","BRL","vendas@eletromax.com.br","+55-21-2345-6789"],
        ["FORN004","IndustriaPro Solutions","22.333.444/0001-55","Brasil","Industrial","A","6","60 dias","BRL","comercial@industriapro.com","+55-11-3344-5566"],
        ["FORN005","MegaStock Logística","33.444.555/0001-66","Brasil","Logística","B","4","30 dias","BRL","logistica@megastock.com.br","+55-19-9988-7766"],
        ["FORN006","USA Tech Imports LLC","--","Estados Unidos","Tecnologia","A+","10","90 dias","USD","import@usatech.com","+1-555-123-4567"],
        ["FORN007","QuímicaBrasil Industrial","44.555.666/0001-77","Brasil","Químicos","A","7","45 dias","BRL","quimica@quimicabr.com","+55-11-5544-3322"],
        ["FORN008","FastParts Distribuição","55.666.777/0001-88","Brasil","Autopeças","B+","2","15 dias","BRL","fastparts@fastparts.com.br","+55-11-7788-9900"],
        ["FORN009","NacionalTex Têxtil","66.777.888/0001-99","Brasil","Têxtil","A-","4","30-45 dias","BRL","textil@nacionaltex.com","+55-11-8899-0011"],
        ["FORN010","China Manufacturing Co","--","China","Manufatura","B","3","90 dias","USD","export@chinamfg.cn","+86-21-5555-8888"],
        ["FORN011","AgriSupply Nacional","77.888.999/0001-00","Brasil","Agrícola","A","5","30 dias","BRL","agri@agrisupply.com.br","+55-16-3344-5577"],
        ["FORN012","EuroTech Germany GmbH","--","Alemanha","Tecnologia","A+","12","60-90 dias","EUR","info@eurotech.de","+49-30-1234-5678"],
        ["FORN013","PlastBrasil Indústria","88.999.000/0001-11","Brasil","Plásticos","B+","3","30 dias","BRL","plastbr@plastbrasil.com","+55-11-9988-7755"],
        ["FORN014","MetalMecanica Sul","99.000.111/0001-22","Brasil","Metalúrgica","A","8","45-60 dias","BRL","metal@metalsul.com.br","+55-51-3322-4455"],
        ["FORN015","PaperSupply Distribuidora","00.111.222/0001-33","Brasil","Papel e Celulose","B","2","15-30 dias","BRL","paper@papersupply.com","+55-11-5566-7788"],
        ["FORN016","AsianElectronics Ltd","--","Coreia do Sul","Eletrônicos","A","6","90 dias","USD","sales@asianelec.kr","+82-2-5555-9999"],
        ["FORN017","BioProdutos Naturais","11.222.444/0001-55","Brasil","Alimentos","A-","4","30 dias","BRL","bio@bioprodutos.com.br","+55-11-4433-2211"],
        ["FORN018","TechMexico SA","--","México","Tecnologia","B+","2","60 dias","USD","mexico@techmx.com.mx","+52-55-8877-6655"],
        ["FORN019","BrasilPack Embalagens","22.333.555/0001-66","Brasil","Embalagens","A","5","30-45 dias","BRL","pack@brasilpack.com","+55-11-2233-4455"],
        ["FORN020","IndiaTech Exports","--","Índia","Tecnologia","B","3","90 dias","USD","export@indiatech.in","+91-11-7788-9900"],
        ["FORN021","SulFerro Siderúrgica","33.444.666/0001-77","Brasil","Siderurgia","A+","10","60 dias","BRL","ferro@sulferro.com.br","+55-51-5544-6677"],
        ["FORN022","JapanParts Corporation","--","Japão","Autopeças","A+","15","60-90 dias","JPY","parts@japanparts.jp","+81-3-9988-7766"],
        ["FORN023","MadeiraBrasil Indústria","44.555.777/0001-88","Brasil","Madeira","B+","4","30 dias","BRL","madeira@madeirabr.com","+55-41-3344-5566"],
        ["FORN024","ArgentinaMetal SA","--","Argentina","Metalúrgica","B","2","45 dias","USD","metal@armetal.com.ar","+54-11-6677-8899"],
        ["FORN025","TecnoBrasil Inovação","55.666.888/0001-99","Brasil","Tecnologia","A","6","30-60 dias","BRL","inova@tecnobr.com.br","+55-11-9988-0011"],
        ["FORN026","FranceParts SARL","--","França","Componentes","A+","8","90 dias","EUR","france@frparts.fr","+33-1-5555-7777"],
        ["FORN027","MinasSul Mineração","66.777.999/0001-00","Brasil","Mineração","A","7","45 dias","BRL","minas@minassul.com","+55-31-4455-6677"],
        ["FORN028","CanadaTech Industries","--","Canadá","Tecnologia","A","5","60 dias","CAD","canada@cantech.ca","+1-416-8899-0011"],
        ["FORN029","NordestePack Ltda","77.888.000/0001-11","Brasil","Embalagens","B+","3","30 dias","BRL","nordeste@nordestepack.com","+55-81-7788-9900"],
        ["FORN030","SpainSupply SL","--","Espanha","Geral","B","2","60-90 dias","EUR","supply@spainsup.es","+34-91-6677-5544"]
    ]
    
    with open('csv_exports/fornecedores.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(dados)
    print("✓ fornecedores.csv gerado (30 linhas)")

def gerar_produtos():
    """
    Gera produtos.csv
    
    CAMPOS-CHAVE: produto_id (PK), fornecedor_id (FK), moeda_origem
    CORRELAÇÃO:
        - produtos.produto_id → itens_pedido.produto_id
        - produtos.fornecedor_id → fornecedores.fornecedor_id
        - produtos.moeda_origem → cambio.moeda
    USO: Felipe - Catálogo de produtos com preços em múltiplas moedas
         Lari (Forecast) - Previsão de preços de produtos
    """
    dados = [
        ["produto_id","nome_produto","categoria","subcategoria","fornecedor_id","preco_unitario_brl","moeda_origem","preco_origem","unidade_medida","peso_kg","estoque_atual","estoque_minimo","lead_time_dias","origem_fabricacao"],
        ["PROD001","Processador Intel i7","Tecnologia","Hardware","FORN001","2500.00","BRL","2500.00","UN","0.5","150","50","15","Brasil"],
        ["PROD002","Memória RAM 16GB DDR4","Tecnologia","Hardware","FORN006","450.00","USD","85.00","UN","0.2","300","100","45","Estados Unidos"],
        ["PROD003","SSD 1TB NVMe","Tecnologia","Armazenamento","FORN002","580.00","BRL","580.00","UN","0.1","200","80","30","Brasil"],
        ["PROD004","Placa Mãe ATX","Tecnologia","Hardware","FORN010","1200.00","USD","220.00","UN","1.2","80","30","60","China"],
        ["PROD005","Cabo HDMI 2m","Eletrônicos","Cabos","FORN003","35.00","BRL","35.00","UN","0.3","500","150","10","Brasil"],
        ["PROD006","Motor Elétrico 5HP","Industrial","Motores","FORN004","3200.00","BRL","3200.00","UN","25.0","40","15","45","Brasil"],
        ["PROD007","Sensor de Temperatura","Industrial","Sensores","FORN006","280.00","USD","52.00","UN","0.4","180","60","30","Estados Unidos"],
        ["PROD008","Válvula Solenoide 1/2","Industrial","Válvulas","FORN007","420.00","BRL","420.00","UN","1.8","120","40","20","Brasil"],
        ["PROD009","Pneu 205/55 R16","Autopeças","Pneus","FORN008","380.00","BRL","380.00","UN","9.5","250","80","15","Brasil"],
        ["PROD010","Filtro de Óleo Automotivo","Autopeças","Filtros","FORN022","45.00","JPY","3800.00","UN","0.5","600","200","40","Japão"],
        ["PROD011","Tecido Algodão 1m","Têxtil","Tecidos","FORN009","28.00","BRL","28.00","M","0.3","1500","500","20","Brasil"],
        ["PROD012","Parafuso M6x20mm","Industrial","Fixação","FORN014","0.85","BRL","0.85","UN","0.02","10000","3000","25","Brasil"],
        ["PROD013","Notebook Dell 15","Tecnologia","Computadores","FORN006","4500.00","USD","850.00","UN","2.1","60","20","60","Estados Unidos"],
        ["PROD014","Impressora Multifuncional","Tecnologia","Periféricos","FORN016","1800.00","USD","340.00","UN","8.5","45","15","50","Coreia do Sul"],
        ["PROD015","Tinta Industrial 5L","Químicos","Tintas","FORN007","180.00","BRL","180.00","L","5.2","300","100","15","Brasil"],
        ["PROD016","Resina Epóxi 1kg","Químicos","Resinas","FORN007","95.00","BRL","95.00","KG","1.0","400","150","15","Brasil"],
        ["PROD017","Papel A4 500 folhas","Papel e Celulose","Papel","FORN015","32.00","BRL","32.00","PCT","2.5","800","250","10","Brasil"],
        ["PROD018","Embalagem Plástica 100un","Embalagens","Plástico","FORN019","85.00","BRL","85.00","PCT","1.8","350","120","15","Brasil"],
        ["PROD019","Chapa de Aço 1m²","Metalúrgica","Chapas","FORN021","145.00","BRL","145.00","M2","7.8","200","60","30","Brasil"],
        ["PROD020","Tubo PVC 50mm 6m","Plásticos","Tubos","FORN013","68.00","BRL","68.00","UN","3.2","180","60","20","Brasil"],
        ["PROD021","Fertilizante NPK 50kg","Agrícola","Fertilizantes","FORN011","220.00","BRL","220.00","SC","50.0","100","30","25","Brasil"],
        ["PROD022","Semente Milho Híbrido","Agrícola","Sementes","FORN011","380.00","BRL","380.00","SC","20.0","80","25","30","Brasil"],
        ["PROD023","Madeira Pinus 3m","Madeira","Madeira Serrada","FORN023","120.00","BRL","120.00","M3","45.0","150","40","20","Brasil"],
        ["PROD024","Rolamento SKF 6205","Industrial","Rolamentos","FORN022","85.00","JPY","7200.00","UN","0.3","250","80","45","Japão"],
        ["PROD025","Switch Gigabit 24 portas","Tecnologia","Rede","FORN012","2800.00","EUR","550.00","UN","2.8","35","10","75","Alemanha"],
        ["PROD026","Minério Ferro ton","Mineração","Minério","FORN027","580.00","BRL","580.00","TON","1000.0","500","100","40","Brasil"],
        ["PROD027","Compressor Ar 10HP","Industrial","Compressores","FORN004","8500.00","BRL","8500.00","UN","180.0","20","5","60","Brasil"],
        ["PROD028","LED Strip 5m RGB","Eletrônicos","Iluminação","FORN010","125.00","USD","23.00","UN","0.4","280","90","55","China"],
        ["PROD029","Transformador 220V","Eletrônicos","Transformadores","FORN003","340.00","BRL","340.00","UN","4.5","90","30","25","Brasil"],
        ["PROD030","Bateria Lítio 12V 100Ah","Eletrônicos","Baterias","FORN016","1850.00","USD","350.00","UN","12.5","55","15","65","Coreia do Sul"]
    ]
    
    with open('csv_exports/produtos.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(dados)
    print("✓ produtos.csv gerado (30 linhas)")

def gerar_itens_pedido():
    """
    Gera itens_pedido.csv
    
    CAMPOS-CHAVE: item_id (PK), pedido_id (FK), produto_id (FK)
    CORRELAÇÃO:
        - itens_pedido.pedido_id → pedidos.pedido_id
        - itens_pedido.produto_id → produtos.produto_id
    USO: Análise detalhada de volumes e valores
         Lari (Forecast) - Previsão de volume de importação por produto
         Gerente Marketing - Análise de categorias mais vendidas
    """
    dados = [
        ["item_id","pedido_id","produto_id","quantidade","preco_unitario","desconto_percentual","valor_total_item","data_inclusao","observacoes"],
        ["ITEM001","PED001","PROD001","5","2500.00","2.0","12250.00","2024-10-15",""],
        ["ITEM002","PED001","PROD003","6","580.00","0.0","3480.00","2024-10-15",""],
        ["ITEM003","PED002","PROD002","20","450.00","5.0","8550.00","2024-10-16","Volume alto"],
        ["ITEM004","PED002","PROD005","10","35.00","0.0","350.00","2024-10-16",""],
        ["ITEM005","PED003","PROD006","4","3200.00","0.0","12800.00","2024-10-17",""],
        ["ITEM006","PED004","PROD004","15","1200.00","3.0","17460.00","2024-10-18",""],
        ["ITEM007","PED004","PROD007","25","280.00","5.0","6650.00","2024-10-18","Desconto negociado"],
        ["ITEM008","PED004","PROD012","2000","0.85","10.0","1530.00","2024-10-18","Grande quantidade"],
        ["ITEM009","PED005","PROD009","12","380.00","0.0","4560.00","2024-10-19","Pedido cancelado"],
        ["ITEM010","PED005","PROD010","18","45.00","0.0","810.00","2024-10-19","Pedido cancelado"],
        ["ITEM011","PED006","PROD011","500","28.00","2.0","13720.00","2024-10-20",""],
        ["ITEM012","PED006","PROD017","200","32.00","0.0","6400.00","2024-10-20",""],
        ["ITEM013","PED007","PROD008","25","420.00","0.0","10500.00","2024-10-21",""],
        ["ITEM014","PED008","PROD013","8","4500.00","4.0","34560.00","2024-10-22","Importação USA"],
        ["ITEM015","PED009","PROD015","40","180.00","0.0","7200.00","2024-10-23","Pagamento à vista"],
        ["ITEM016","PED010","PROD014","8","1800.00","2.0","14112.00","2024-10-24",""],
        ["ITEM017","PED011","PROD006","6","3200.00","1.0","19008.00","2024-10-25",""],
        ["ITEM018","PED011","PROD008","2","420.00","0.0","840.00","2024-10-25",""],
        ["ITEM019","PED012","PROD019","50","145.00","5.0","6887.50","2024-10-26",""],
        ["ITEM020","PED013","PROD021","100","220.00","3.0","21340.00","2024-10-27",""],
        ["ITEM021","PED013","PROD022","20","380.00","2.0","7448.00","2024-10-27",""],
        ["ITEM022","PED014","PROD018","150","85.00","8.0","11730.00","2024-10-28",""],
        ["ITEM023","PED015","PROD016","180","95.00","4.0","16416.00","2024-10-29",""],
        ["ITEM024","PED016","PROD024","300","85.00","10.0","22950.00","2024-10-30","Importação Japão"],
        ["ITEM025","PED017","PROD020","150","68.00","2.0","9996.00","2024-10-31",""],
        ["ITEM026","PED018","PROD023","120","120.00","5.0","13680.00","2024-11-01",""],
        ["ITEM027","PED019","PROD025","18","2800.00","6.0","47376.00","2024-11-02","Importação Alemanha"],
        ["ITEM028","PED020","PROD029","30","340.00","3.0","9894.00","2024-11-03",""],
        ["ITEM029","PED021","PROD027","2","8500.00","2.0","16660.00","2024-11-04",""],
        ["ITEM030","PED021","PROD006","1","3200.00","0.0","3200.00","2024-11-04",""],
        ["ITEM031","PED022","PROD028","100","125.00","5.0","11875.00","2024-11-05","Importação China"],
        ["ITEM032","PED023","PROD026","50","580.00","8.0","26680.00","2024-11-06","Mineração"],
        ["ITEM033","PED024","PROD009","22","380.00","4.0","8025.60","2024-11-07",""],
        ["ITEM034","PED025","PROD011","600","28.00","3.0","16296.00","2024-11-08",""],
        ["ITEM035","PED025","PROD005","100","35.00","2.0","3430.00","2024-11-08",""],
        ["ITEM036","PED026","PROD030","9","1850.00","5.0","15817.50","2024-11-09","Importação Coreia"],
        ["ITEM037","PED027","PROD017","400","32.00","8.0","11776.00","2024-11-10",""],
        ["ITEM038","PED028","PROD001","8","2500.00","2.0","19600.00","2024-11-11",""],
        ["ITEM039","PED028","PROD003","12","580.00","0.0","6960.00","2024-11-11",""],
        ["ITEM040","PED029","PROD013","10","4500.00","7.0","41850.00","2024-11-12","Importação USA"],
        ["ITEM041","PED030","PROD002","35","450.00","5.0","14962.50","2024-11-13","Volume alto"]
    ]
    
    with open('csv_exports/itens_pedido.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(dados)
    print("✓ itens_pedido.csv gerado (41 linhas)")

def gerar_pagamentos():
    """
    Gera pagamentos.csv
    
    CAMPOS-CHAVE: pagamento_id (PK), pedido_id (FK), fornecedor_id (FK), taxa_cambio_aplicada
    CORRELAÇÃO:
        - pagamentos.pedido_id → pedidos.pedido_id
        - pagamentos.fornecedor_id → fornecedores.fornecedor_id
        - pagamentos.moeda_origem → cambio.moeda
        - pagamentos.data_pagamento → cambio.data_cotacao (para aplicar PTAX correto)
    USO: Celso/Marcos - Gestão de pagamentos e Open Finance
         Gerente Financeiro - Análise de fluxo de caixa e conversões cambiais
    """
    dados = [
        ["pagamento_id","pedido_id","fornecedor_id","data_pagamento","valor_pago_brl","metodo_pagamento","status_pagamento","taxa_cambio_aplicada","moeda_origem","valor_moeda_origem","num_parcelas","parcela_atual","data_vencimento","usuario_aprovacao"],
        ["PAG001","PED001","FORN001","2024-11-14","15750.50","BOLETO","PAGO","1.0000","BRL","15750.50","1","1","2024-11-14","celso.oliveira"],
        ["PAG002","PED002","FORN002","2024-11-30","8920.00","TRANSFERENCIA","PENDENTE","1.0000","BRL","8920.00","1","1","2024-11-30","celso.oliveira"],
        ["PAG003","PED003","FORN003","2024-11-01","12300.75","CARTAO_CREDITO","PAGO","1.0000","BRL","12300.75","3","1","2024-11-01","marcos.santos"],
        ["PAG004","PED003","FORN003","2024-12-01","12300.75","CARTAO_CREDITO","AGENDADO","1.0000","BRL","12300.75","3","2","2024-12-01","marcos.santos"],
        ["PAG005","PED003","FORN003","2025-01-01","12300.75","CARTAO_CREDITO","AGENDADO","1.0000","BRL","12300.75","3","3","2025-01-01","marcos.santos"],
        ["PAG006","PED004","FORN001","2024-12-17","25600.00","BOLETO","PAGO","1.0000","BRL","25600.00","1","1","2024-12-17","celso.oliveira"],
        ["PAG007","PED005","FORN004","2024-10-19","5400.25","PIX","CANCELADO","1.0000","BRL","5400.25","1","1","2024-10-19","celso.oliveira"],
        ["PAG008","PED006","FORN005","2024-11-19","18900.00","BOLETO","PENDENTE","1.0000","BRL","18900.00","1","1","2024-11-19","celso.oliveira"],
        ["PAG009","PED007","FORN002","2024-12-06","9850.50","TRANSFERENCIA","PAGO","1.0000","BRL","9850.50","1","1","2024-12-06","celso.oliveira"],
        ["PAG010","PED008","FORN006","2025-01-20","32100.00","BOLETO","AGENDADO","5.2500","USD","6114.29","1","1","2025-01-20","marcos.santos"],
        ["PAG011","PED009","FORN003","2024-10-30","7200.00","PIX","PAGO","1.0000","BRL","7200.00","1","1","2024-10-30","celso.oliveira"],
        ["PAG012","PED010","FORN007","2024-11-23","14500.75","CARTAO_CREDITO","PENDENTE","1.0000","BRL","14500.75","2","1","2024-11-23","marcos.santos"],
        ["PAG013","PED010","FORN007","2024-12-23","14500.75","CARTAO_CREDITO","AGENDADO","1.0000","BRL","14500.75","2","2","2024-12-23","marcos.santos"],
        ["PAG014","PED011","FORN001","2024-12-09","19800.00","BOLETO","PAGO","1.0000","BRL","19800.00","1","1","2024-12-09","celso.oliveira"],
        ["PAG015","PED012","FORN008","2024-11-10","6700.50","TRANSFERENCIA","PENDENTE","1.0000","BRL","6700.50","1","1","2024-11-10","celso.oliveira"],
        ["PAG016","PED013","FORN004","2024-12-26","28900.00","BOLETO","AGENDADO","1.0000","BRL","28900.00","1","1","2024-12-26","celso.oliveira"],
        ["PAG017","PED014","FORN009","2024-11-04","11200.25","PIX","PAGO","1.0000","BRL","11200.25","1","1","2024-11-04","celso.oliveira"],
        ["PAG018","PED015","FORN005","2024-11-28","16500.00","CARTAO_CREDITO","PENDENTE","1.0000","BRL","16500.00","3","1","2024-11-28","marcos.santos"],
        ["PAG019","PED015","FORN005","2024-12-28","16500.00","CARTAO_CREDITO","AGENDADO","1.0000","BRL","16500.00","3","2","2024-12-28","marcos.santos"],
        ["PAG020","PED015","FORN005","2025-01-28","16500.00","CARTAO_CREDITO","AGENDADO","1.0000","BRL","16500.00","3","3","2025-01-28","marcos.santos"],
        ["PAG021","PED016","FORN002","2024-12-14","22400.75","BOLETO","PENDENTE","1.0000","BRL","22400.75","1","1","2024-12-14","celso.oliveira"],
        ["PAG022","PED017","FORN010","2024-11-30","8900.00","TRANSFERENCIA","PAGO","5.3200","USD","1672.93","1","1","2024-11-30","marcos.santos"],
        ["PAG023","PED018","FORN003","2024-11-16","13700.50","BOLETO","PENDENTE","1.0000","BRL","13700.50","1","1","2024-11-16","celso.oliveira"],
        ["PAG024","PED019","FORN006","2025-02-01","45200.00","BOLETO","AGENDADO","5.2800","USD","8560.61","1","1","2025-02-01","marcos.santos"],
        ["PAG025","PED020","FORN001","2024-11-10","9500.25","PIX","PAGO","1.0000","BRL","9500.25","1","1","2024-11-10","celso.oliveira"],
        ["PAG026","PED021","FORN007","2024-12-04","17800.00","CARTAO_CREDITO","PENDENTE","1.0000","BRL","17800.00","2","1","2024-12-04","marcos.santos"],
        ["PAG027","PED021","FORN007","2025-01-04","17800.00","CARTAO_CREDITO","AGENDADO","1.0000","BRL","17800.00","2","2","2025-01-04","marcos.santos"],
        ["PAG028","PED022","FORN008","2024-12-20","12100.75","TRANSFERENCIA","PENDENTE","1.0000","BRL","12100.75","1","1","2024-12-20","celso.oliveira"],
        ["PAG029","PED023","FORN004","2025-01-05","24600.00","BOLETO","AGENDADO","1.0000","BRL","24600.00","1","1","2025-01-05","celso.oliveira"],
        ["PAG030","PED024","FORN009","2024-11-14","7800.50","PIX","PENDENTE","1.0000","BRL","7800.50","1","1","2024-11-14","celso.oliveira"]
    ]
    
    with open('csv_exports/pagamentos.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(dados)
    print("✓ pagamentos.csv gerado (30 linhas)")

def gerar_emprestimos():
    """
    Gera emprestimos.csv
    
    CAMPOS-CHAVE: emprestimo_id (PK), instituicao_financeira, data_vencimento_proxima
    CORRELAÇÃO:
        - Independente de outras tabelas (domínio separado)
        - Alimenta previsão de fluxo de caixa junto com pagamentos
    USO: Celso - Gestão de empréstimos bancários
         Lari (Forecast) - Previsão de fluxo de caixa considerando parcelas
         Gerente Financeiro - Análise de endividamento e compromissos futuros
    """
    dados = [
        ["emprestimo_id","data_contratacao","instituicao_financeira","valor_principal_brl","taxa_juros_anual","prazo_meses","valor_parcela_mensal","saldo_devedor","status","finalidade","data_vencimento_proxima","num_parcelas_pagas","usuario_responsavel"],
        ["EMP001","2024-01-15","Banco Nacional","500000.00","12.5","36","17850.25","425000.00","ATIVO","Capital de Giro","2024-11-15","10","celso.oliveira"],
        ["EMP002","2024-03-20","Banco Comercial","250000.00","10.8","24","12450.80","187500.00","ATIVO","Aquisição de Equipamentos","2024-11-20","8","celso.oliveira"],
        ["EMP003","2024-05-10","Financeira Brasil","150000.00","14.2","48","4850.30","138750.00","ATIVO","Expansão","2024-11-10","6","celso.oliveira"],
        ["EMP004","2023-06-15","Banco Industrial","800000.00","11.5","60","18240.55","640000.00","ATIVO","Obras e Infraestrutura","2024-11-15","16","celso.oliveira"],
        ["EMP005","2024-07-22","BNDES","1200000.00","8.5","84","19850.40","1140000.00","ATIVO","Inovação Tecnológica","2024-11-22","4","celso.oliveira"],
        ["EMP006","2024-02-28","Banco Regional","180000.00","13.0","30","7120.45","144000.00","ATIVO","Capital de Giro","2024-11-28","9","celso.oliveira"],
        ["EMP007","2023-11-10","Cooperativa Crédito","95000.00","9.8","18","5980.25","31666.67","ATIVO","Importação","2024-11-10","16","celso.oliveira"],
        ["EMP008","2024-04-05","Banco Desenvolvimento","450000.00","10.2","48","13550.75","393750.00","ATIVO","Modernização","2024-11-05","7","celso.oliveira"],
        ["EMP009","2024-08-15","Fintech Capital","75000.00","15.5","12","6850.90","62500.00","ATIVO","Estoque","2024-11-15","3","celso.oliveira"],
        ["EMP010","2022-09-20","Banco Nacional","600000.00","12.0","48","17820.30","300000.00","ATIVO","Aquisição Veículos","2024-11-20","24","celso.oliveira"],
        ["EMP011","2024-06-12","Banco Comercial","320000.00","11.8","36","11450.60","280000.00","ATIVO","Marketing e Vendas","2024-11-12","5","celso.oliveira"],
        ["EMP012","2023-12-18","Financeira Brasil","220000.00","13.5","24","10980.75","146666.67","ATIVO","Tecnologia","2024-11-18","11","celso.oliveira"],
        ["EMP013","2024-09-03","Banco Industrial","550000.00","10.5","60","12850.40","532083.33","ATIVO","Expansão Nacional","2024-11-03","2","celso.oliveira"],
        ["EMP014","2024-01-25","BNDES","2000000.00","7.8","120","26540.85","1950000.00","ATIVO","Pesquisa e Desenvolvimento","2024-11-25","10","celso.oliveira"],
        ["EMP015","2023-08-14","Banco Regional","280000.00","12.8","30","10850.30","186666.67","ATIVO","Logística","2024-11-14","15","celso.oliveira"],
        ["EMP016","2024-10-05","Cooperativa Crédito","120000.00","11.2","24","5780.45","115000.00","ATIVO","Capital de Giro","2024-12-05","1","celso.oliveira"],
        ["EMP017","2024-03-08","Banco Desenvolvimento","680000.00","9.5","72","13420.75","623333.33","ATIVO","Automação Industrial","2024-11-08","8","celso.oliveira"],
        ["EMP018","2022-05-22","Fintech Capital","85000.00","16.0","12","7850.60","28333.33","ATIVO","Emergencial","2024-11-22","20","celso.oliveira"],
        ["EMP019","2024-07-16","Banco Nacional","430000.00","11.0","42","12580.95","395833.33","ATIVO","Novas Unidades","2024-11-16","4","celso.oliveira"],
        ["EMP020","2023-10-30","Banco Comercial","190000.00","12.2","18","11450.80","105555.56","ATIVO","Importação Equipamentos","2024-11-30","13","celso.oliveira"],
        ["EMP021","2024-04-18","Financeira Brasil","310000.00","13.8","36","11180.65","284166.67","ATIVO","Reestruturação","2024-11-18","7","celso.oliveira"],
        ["EMP022","2024-08-28","Banco Industrial","740000.00","10.8","54","17350.40","712962.96","ATIVO","Diversificação","2024-11-28","3","celso.oliveira"],
        ["EMP023","2023-07-12","BNDES","1500000.00","8.2","96","22480.55","1343750.00","ATIVO","Sustentabilidade","2024-11-12","15","celso.oliveira"],
        ["EMP024","2024-09-20","Banco Regional","210000.00","12.5","27","8950.70","201666.67","ATIVO","E-commerce","2024-11-20","2","celso.oliveira"],
        ["EMP025","2024-02-14","Cooperativa Crédito","145000.00","10.5","20","8120.45","123750.00","ATIVO","Treinamento","2024-11-14","9","celso.oliveira"],
        ["EMP026","2022-11-05","Banco Desenvolvimento","520000.00","9.8","48","14650.80","325000.00","ATIVO","Certificações","2024-11-05","24","celso.oliveira"],
        ["EMP027","2024-10-12","Fintech Capital","98000.00","14.8","15","7280.60","91466.67","ATIVO","Consultoria","2024-12-12","1","celso.oliveira"],
        ["EMP028","2024-06-25","Banco Nacional","370000.00","11.5","40","11080.75","342500.00","ATIVO","Infraestrutura TI","2024-11-25","5","celso.oliveira"],
        ["EMP029","2023-09-08","Banco Comercial","265000.00","12.0","30","9850.40","176666.67","ATIVO","Frota","2024-11-08","14","celso.oliveira"],
        ["EMP030","2024-05-03","Financeira Brasil","180000.00","13.2","24","8720.85","157500.00","ATIVO","Marketing Digital","2024-11-03","6","celso.oliveira"]
    ]
    
    with open('csv_exports/emprestimos.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(dados)
    print("✓ emprestimos.csv gerado (30 linhas)")

def gerar_cambio():
    """
    Gera cambio.csv
    
    CAMPOS-CHAVE: data_cotacao (PK composta), moeda (PK composta), taxa_ptax
    CORRELAÇÃO:
        - cambio.moeda → fornecedores.moeda_negociacao
        - cambio.moeda → produtos.moeda_origem
        - cambio.data_cotacao + moeda → pagamentos (para aplicar taxa correta)
    USO: Gustavo - Integração SISBACEN (PTAX)
         Analista de Dados - Correção monetária em pedidos internacionais
         Lari (Forecast) - Previsão de câmbio para planejamento
         Gerente Financeiro - Análise de exposição cambial
    """
    dados = [
        ["data_cotacao","moeda","taxa_compra","taxa_venda","taxa_ptax","variacao_dia_percentual","fonte","tipo_cambio","hora_atualizacao"],
        ["2024-10-15","USD","5.2350","5.2580","5.2465","0.15","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-15","EUR","5.6120","5.6380","5.6250","0.22","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-15","JPY","0.0348","0.0352","0.0350","-0.08","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-15","GBP","6.7850","6.8150","6.8000","0.18","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-15","CAD","3.8420","3.8680","3.8550","0.12","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-16","USD","5.2480","5.2710","5.2595","0.25","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-16","EUR","5.6280","5.6540","5.6410","0.28","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-16","JPY","0.0347","0.0351","0.0349","-0.29","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-17","USD","5.2620","5.2850","5.2735","0.27","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-17","EUR","5.6450","5.6710","5.6580","0.30","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-18","USD","5.2780","5.3010","5.2895","0.30","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-18","EUR","5.6620","5.6880","5.6750","0.30","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-18","JPY","0.0349","0.0353","0.0351","0.57","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-21","USD","5.2650","5.2880","5.2765","-0.25","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-21","EUR","5.6480","5.6740","5.6610","-0.25","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-22","USD","5.2850","5.3080","5.2965","0.38","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-22","EUR","5.6720","5.6980","5.6850","0.42","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-22","GBP","6.8320","6.8620","6.8470","0.35","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-23","USD","5.2720","5.2950","5.2835","-0.25","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-23","EUR","5.6580","5.6840","5.6710","-0.25","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-24","USD","5.2890","5.3120","5.3005","0.32","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-24","JPY","0.0350","0.0354","0.0352","0.28","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-25","USD","5.3050","5.3280","5.3165","0.30","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-25","EUR","5.6920","5.7180","5.7050","0.33","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-28","USD","5.3180","5.3410","5.3295","0.24","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-28","CAD","3.8750","3.9010","3.8880","0.28","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-29","USD","5.3320","5.3550","5.3435","0.26","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-29","EUR","5.7150","5.7410","5.7280","0.29","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-30","USD","5.3250","5.3480","5.3365","-0.13","SISBACEN","COMERCIAL","16:30:00"],
        ["2024-10-30","GBP","6.8720","6.9020","6.8870","0.22","SISBACEN","COMERCIAL","16:30:00"]
    ]
    
    with open('csv_exports/cambio.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(dados)
    print("✓ cambio.csv gerado (30 linhas)")



def gerar_todos_csvs():
    """Função principal que gera todos os CSVs"""
    print("\n🚀 Iniciando geração dos arquivos CSV...")
    print("=" * 50)
    
    criar_diretorio()
    gerar_pedidos()
    gerar_fornecedores()
    gerar_produtos()
    gerar_itens_pedido()
    gerar_pagamentos():
    gerar_emprestimos()
    gerar_cambio()
    
    print("=" * 50)
    print(f"✅ Arquivos gerados com sucesso em: csv_exports/")
    print(f"📅 Data de geração: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n💡 Dica: Avaliar DDD")
    print("")

if __name__ == "__main__":
    gerar_todos_csvs()

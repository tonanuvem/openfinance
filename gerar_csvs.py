#!/usr/bin/env python3
"""
Script para gerar todos os arquivos CSV do sistema
Execute: python gerar_csvs.py
"""

import os
import csv
from datetime import datetime

def criar_diretorio():
    """Cria diretório para os CSVs"""
    os.makedirs('csv_exports', exist_ok=True)
    print("✓ Diretório 'csv_exports' criado/verificado")

def gerar_pedidos():
    """Gera pedidos.csv"""
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
    """Gera fornecedores.csv"""
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

def gerar_todos_csvs():
    """Função principal que gera todos os CSVs"""
    print("\n🚀 Iniciando geração dos arquivos CSV...")
    print("=" * 50)
    
    criar_diretorio()
    gerar_pedidos()
    gerar_fornecedores()
    # Adicione as outras funções aqui para gerar os demais CSVs
    
    print("=" * 50)
    print(f"✅ Arquivos gerados com sucesso em: csv_exports/")
    print(f"📅 Data de geração: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n💡 Dica: Para gerar os demais CSVs, complete o script com as")
    print("   funções gerar_produtos(), gerar_itens_pedido(), etc.")

if __name__ == "__main__":
    gerar_todos_csvs()

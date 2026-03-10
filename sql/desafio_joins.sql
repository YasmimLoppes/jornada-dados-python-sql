-- 🚀 Desafio de Evolução: Relacionamento de Tabelas (JOINS)
-- Desenvolvido por: Yasmin Lopes

-- 1. Criando a tabela de Ativos
CREATE TABLE ativos (
    id_ativo INTEGER PRIMARY KEY,
    nome_ativo TEXT NOT NULL,
    ticker TEXT UNIQUE
);

-- 2. Criando a tabela de Transações
CREATE TABLE transacoes (
    id_transacao INTEGER PRIMARY KEY,
    id_ativo INTEGER,
    quantidade REAL,
    preco_unidade REAL,
    FOREIGN KEY (id_ativo) REFERENCES ativos(id_ativo)
);

-- 3. Inserindo dados de exemplo
INSERT INTO ativos (id_ativo, nome_ativo, ticker) VALUES 
(1, 'Bitcoin', 'BTC'),
(2, 'Ethereum', 'ETH');

INSERT INTO transacoes (id_ativo, quantidade, preco_unidade) VALUES 
(1, 0.5, 65000.00),
(2, 2.0, 3500.00);

-- 4. CONSULTA COM JOIN (A união das tabelas para ver o valor total)
SELECT 
    a.nome_ativo,
    a.ticker,
    t.quantidade,
    (t.quantidade * t.preco_unidade) AS valor_total
FROM ativos a
INNER JOIN transacoes t ON a.id_ativo = t.id_ativo;

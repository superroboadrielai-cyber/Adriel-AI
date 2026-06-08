<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adriel-AI Pro - Painel de Controle</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 1200px;
            margin: 20px auto;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }
        header {
            background: #007bff;
            color: #fff;
            padding: 20px;
            text-align: center;
            border-radius: 8px 8px 0 0;
        }
        nav {
            margin: 20px 0;
        }
        nav a {
            margin: 0 15px;
            text-decoration: none;
            color: #007bff;
        }
        nav a:hover {
            text-decoration: underline;
        }
        section {
            margin-bottom: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }
        th {
            background-color: #007bff;
            color: white;
        }
        .aprovado {
            color: green;
        }
        .revisar {
            color: orange;
        }
        button {
            background: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            margin-right: 10px;
        }
        button:hover {
            background: #218838;
        }
        .btn-blue {
            background: #007bff;
        }
        .btn-blue:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Adriel-AI Pro</h1>
            <p>Olá, [Seu Nome], Comandante do Adriel-AI Pro!</p>
            <p>Status: Sistema Online | Chave Mestre Ativa | Data: 06/06/2026</p>
        </header>
        <nav>
            <a href="#">Dashboard</a>
            <a href="#">Radar de Produtos</a>
            <a href="#">Auditor de Mercado</a>
            <a href="#">Gerador de Anúncios</a>
            <a href="#">Caçador de Lançamentos</a>
            <a href="#">Configurações</a>
            <a href="#">Sair</a>
        </nav>
        <section>
            <h2>MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</h2>
            <table>
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>Comissões</th>
                        <th>Verificado pela IA</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Produto-acionado 1</td>
                        <td>3.00%</td>
                        <td class="aprovado">APROVADO (Risco Baixo)</td>
                    </tr>
                    <tr>
                        <td>Produto-acionado 2</td>
                        <td>2.00%</td>
                        <td class="revisar">REVISAR (Risco Médio)</td>
                    </tr>
                    <tr>
                        <td>Produto-acionado 3</td>
                        <td>1.00%</td>
                        <td class="aprovado">APROVADO (Risco Baixo)</td>
                    </tr>
                    <tr>
                        <td>Produto-acionado 4</td>
                        <td>1.50%</td>
                        <td class="revisar">REVISAR (Risco Médio)</td>
                    </tr>
                </tbody>
            </table>
        </section>
        <section>
            <h2>MÓDULO 2: GERADOR DE ANÚNCIOS MASTER & PRE-SELL</h2>
            <p><strong>PRODUTO Gringo:</strong> Sugar Defender</p>
            <p><strong>RESUMO:</strong> Suplemento natural para equilíbrio de metabolismo.</p>
            <button>A GERAR ANÚNCIOS ADSMaster</button>
            <button class="btn-blue">FABRICAR PRE-SELL</button>
        </section>
    </div>
</body>
</html>

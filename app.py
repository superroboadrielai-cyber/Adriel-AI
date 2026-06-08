<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adriel-AI Pro - Painel de Controle</title>
    <style>
        * {
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 90%;
            max-width: 1200px;
            margin: auto;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }
        header {
            background: #007bff;
            color: #fff;
            padding: 20px;
            text-align: center;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }
        nav {
            background: #343a40;
            border-bottom: 2px solid #007bff;
        }
        nav ul {
            list-style: none;
            padding: 0;
            display: flex;
            justify-content: space-around;
        }
        nav ul li {
            margin: 0;
        }
        nav ul li a {
            color: #fff;
            text-decoration: none;
            padding: 15px 20px;
            display: block;
        }
        nav ul li a:hover {
            background: #007bff;
            border-radius: 5px;
        }
        main {
            padding: 20px;
        }
        section {
            margin-bottom: 20px;
        }
        h2 {
            color: #007bff;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border: 1px solid #ddd;
        }
        thead {
            background: #007bff;
            color: #fff;
        }
        .aprovado {
            color: green;
        }
        .revisar {
            color: orange;
        }
        .buttons {
            margin-top: 20px;
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
        button.fabricar {
            background: #007bff;
        }
        button.fabricar:hover {
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
            <ul>
                <li><a href="#">Dashboard</a></li>
                <li><a href="#">Radar de Produtos</a></li>
                <li><a href="#">Auditor de Mercado</a></li>
                <li><a href="#">Gerador de Anúncios</a></li>
                <li><a href="#">Caçador de Lançamentos</a></li>
                <li><a href="#">Configurações</a></li>
                <li><a href="#">Sair</a></li>
            </ul>
        </nav>
        <main>
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
                <div class="buttons">
                    <button class="gerar">A GERAR ANÚNCIOS ADSMaster (Copy + Roteiro Vídeo)</button>
                    <button class="fabricar">B FABRICAR PRE-SELL (Landing Page Text)</button>
                </div>
            </section>
        </main>
    </div>
</body>
</html>

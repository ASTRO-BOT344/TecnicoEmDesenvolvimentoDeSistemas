<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contato</title>
</head>
<body>
    <h1>Formulário de Contato</h1>
    <?php
    /*Requisições
    CRUD
    CREATE, READ, UPDATE, DELETE
    POST: PUBLICAÇÃO
    PUT: ATUALIZAR UM RECURSO INTEIRO
    PATCH: ATUALIZAÇÃO PARCIAL
    DELETE: EXCLUIR REGISTROS
    GET: SOLICITAR DADOS
    */
    if ($_POST){
        $nome = htmlspecialchars($_POST['nome']);
        $email = htmlspecialchars($_POST['email']);
        $msg = htmlspecialchars($_POST['msg']);

        //salvar em arquivo
        $dados = "$nome | $email | $msg\n";
        file_put_contents('mensagem.txt', $dados, FILE_APPEND);
        echo "<p style='color: green';> Mnesagem enviada com sucesso por $nome! </p>";
    }
    ?>

    <form method="POST">
        <label> Nome: <input type="text" name="nome" required></label><br><br>
        <label> E-mail: <input type="email" name="email" required></label><br><br>
        <label> Mensagem: <textarea type="text" name="msg" required></textarea><br><br>
        <button type="submit">Enviar</button>
    </form>
    <h2>Mnesagem Recebidas</h2>
    <?php
        if (file_exists('mensagem.txt')){
            $linhas = file('mensagem.txt');
            foreach($linhas as $linha){
                echo "<p>$$linha </p>";
            }
        } else{
            echo "<p> Nenhuma mnsagem encontrada </p>";
        }
    ?>
</body>
</html>
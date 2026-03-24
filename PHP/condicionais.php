<?php

    //$hora = 14;

    $hora = readline("Digite sua hora:");
    echo $hora;

    if($hora < 12){
        echo "Bom Dia!";
    } elseif($hora < 18){
        echo "Boa Tarde!";
    } else {
        echo"Boa Noite!";
    }

    // $nome = readline("Digite seu nome: "); ISSO É A CAIXA DE MENSAGEM PARA O USUÁRIO DIGITAR.

?>
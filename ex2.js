var readline = require('readline');
const ano_atual = Number;

var leitor = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

leitor.question("\n", function(answer) {
    var ano_atual = answer;
    console.log("Ano registrado:"+ano_atual);
    leitor.close();
});

///Desisti de usar js pois o paradigma da linguagem não é apropriado a obtenção de dados do usuário
///sem o uso de um navegadore e de métodos como "prompt"
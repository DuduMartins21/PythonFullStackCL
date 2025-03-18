const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function notas(n1, n2, n3, n4) {
    let medianotas = (n1 + n2 + n3 + n4) / 4;

    if (medianotas >= 7) {
        return "aprovado";
    } else if (medianotas <= 6) {
        return "reprovado";
    } else {
        return "recuperção";
    }

}

rl.question("Digite a primeira nota:", (n1) => {
    rl.question("Digite a segunda nota:", (n2) => {
        rl.question("Digite a terceira nota:", (n3) => {
            rl.question("Digite a quarta nota:", (n4) => {
                n1 = parseFloat(n1);
                n2 = parseFloat(n2);
                n3 = parseFloat(n3);
                n4 = parseFloat(n4);

                let resultado = notas(n1, n2, n3, n4);
                console.log("Classificação das notas: ", resultado);

                rl.close();
            });
        });
    });
});
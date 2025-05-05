
// Questão 1 :

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Digite a primeira nota (0 a 10): ', (nota1) => {
    rl.question('Digite a segunda nota (0 a 10): ', (nota2) => {
        rl.question('Digite a terceira nota (0 a 10): ', (nota3) => {
            rl.question('Digite a quarta nota (0 a 10): ', (nota4) => { 
                let media = (parseFloat(nota1) + parseFloat(nota2) + parseFloat(nota3) + parseFloat(nota4)) / 4;
                
                if (media >= 7) {
                    console.log("Aprovado! Sua média foi " + media.toFixed(1));
                } else if (media >= 5 && media < 7) {
                    console.log("Recuperação! Sua média foi " + media.toFixed(1));
                } else {
                    console.log("Reprovado! Sua média foi " + media.toFixed(1));
                }

                rl.close();
            });
        });
    });
});


// questão 2 :



rl.question('Digite o número inicial: ', (inicio) => {
    rl.question('Digite o número final: ', (fim) => {
        let soma = 0;
        let numInicio = parseInt(inicio);
        let numFim = parseInt(fim);

        // Loop para somar os números pares
        for (let i = numInicio; i <= numFim; i++) {
            if (i % 2 === 0) {
                soma += i;
            }
        }

        // Exibir o resultado
        console.log(`A soma dos números pares no intervalo de ${numInicio} a ${numFim} é: ${soma}`);

        rl.close();
    });
});
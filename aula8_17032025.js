/////////////////////////////////////////////////////
//   FOR/WHILE/DO WHILE em JavaScript - Aula 7     //
/////////////////////////////////////////////////////

// 1. Contagem Regressiva com FOR:
// Peça ao usuário um número e faça uma contagem regressiva a partir dele até 0.

let numero1 = parseInt(prompt("Digite um número para a contagem regressiva:"));
for (let i = numero1; i >= 0; i--) {
    console.log(i);
}


// 2. Soma de Números com WHILE:
// Peça ao usuário um número e some todos os números de 1 até ele.

let numero2 = parseInt(prompt("Digite um número para somar de 1 até ele:"));
let soma = 0;
let indice = 1;
while (indice <= numero2) {
    soma += indice;
    indice++;
}
console.log("Soma:", soma);


// 3. Tabuada com FOR:
// Peça ao usuário um número e mostre a tabuada dele de 1 a 10.

let numero3 = parseInt(prompt("Digite um número para ver sua tabuada:"));
for (let i = 1; i <= 10; i++) {
    console.log(`${numero3} x ${i} = ${numero3 * i}`);
}


// 4. Números Pares com FOR:
// Peça ao usuário um número e mostre todos os números pares de 1 até ele.

let numero4 = parseInt(prompt("Digite um número para ver os pares até ele:"));
for (let i = 2; i <= numero4; i += 2) {
    console.log(i);
}


// 5. Fatorial com WHILE:
// Peça ao usuário um número e calcule o fatorial dele.

let numero5 = parseInt(prompt("Digite um número para calcular o fatorial:"));
let fatorial = 1;
let i = 1;
while (i <= numero5) {
    fatorial *= i;
    i++;
}
console.log(`Fatorial de ${numero5}: ${fatorial}`);


// 6. Validação de Entrada com DO WHILE:
// Peça ao usuário um número maior que 10. Se ele digitar um número inválido, peça novamente.

let numero6;
do {
    numero6 = parseInt(prompt("Digite um número maior que 10:"));
} while (numero6 <= 10);
console.log("Número válido:", numero6);


// 7. Desenho com Loops Aninhados
// Peça ao usuário o tamanho de um quadrado e desenhe-o com asteriscos (*).

let tamanho = parseInt(prompt("Digite o tamanho do quadrado:"));
for (let i = 0; i < tamanho; i++) {
    let linha = "";
    for (let j = 0; j < tamanho; j++) {
        linha += "* ";
    }
    console.log(linha);
}

//


const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function calcularIMC(peso, altura) {
    let imc = peso / (altura * altura);

    if (imc < 18.5) {
        return "Abaixo do peso";
    } else if (imc >= 18.5 && imc <= 24.9) {
        return "Peso Normal";
    } else if (imc >= 25 && imc <= 29.9) {
        return "Sobrepeso";
    } else if (imc >= 30 && imc <= 34.9) {
        return "Obesidade Grau I";        
    } else if (imc >= 35 && imc <= 39.9) {
        return "Obesidade Grau II";
    } else {
        return "Obesidade Grau III";
    }
}

rl.question("Digite o seu peso: ", (peso) => {
    rl.question("Digite a sua altura: ", (altura) => {
        peso = parseFloat(peso);
        altura = parseFloat(altura);

        let resultado = calcularIMC(peso, altura);
        console.log("Classificação do IMC: ", resultado);

        rl.close();
    });
});
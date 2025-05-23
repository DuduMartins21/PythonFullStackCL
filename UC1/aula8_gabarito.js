// Questão 1 

function calcularMedia() {
    let soma = 0;
    for (let i = 0; i < 4; i++) {
        let nota = parseFloat(prompt(`Digite a ${i + 1}ª nota:`));
        soma += nota;
    }
    let media = soma / 4;
    console.log("Média:", media);
    if (media >= 7) {
        console.log("Aprovado");
    } else {
        console.log("Reprovado");
    }
}

calcularMedia();

// questão 2

function somaParesNoIntervalo() {
    let inicio = parseInt(prompt("Digite o início do intervalo:"));
    let fim = parseInt(prompt("Digite o fim do intervalo:"));
    let soma = 0;
    for (let i = inicio; i <= fim; i++) {
        if (i % 2 === 0) {
            soma += i;
        }
    }
    console.log("Soma dos números pares:", soma);
}

somaParesNoIntervalo();

// Questão 3

somaParesNoIntervalo();


function verificarPalindromo() {
    let texto = prompt("Digite uma palavra ou frase:").toLowerCase().replace(/ /g, "");
    let textoInvertido = texto.split("").reverse().join("");
    if (texto === textoInvertido) {
        console.log("É palíndromo");
    } else {
        console.log("Não é palíndromo");
    }
}

verificarPalindromo();

// Questão 4


function calcularJurosSimples() {
    let P = parseFloat(prompt("Digite o valor principal (P):"));
    let r = parseFloat(prompt("Digite a taxa de juros anual (r):")) / 100;
    let t = parseFloat(prompt("Digite o tempo em anos (t):"));
    let M = P * (1 + r * t);
    console.log("Montante final:", M);
}

calcularJurosSimples();

// Questão 5

function contarDigitos() {
    let numero = prompt("Digite um número inteiro positivo:");
    if (/^\d+$/.test(numero)) {
        console.log("Número de dígitos:", numero.length);
    } else {
        console.log("Entrada inválida. Digite um número inteiro positivo.");
    }
}

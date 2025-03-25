
let numero = parseInt(prompt("Digite um número:"));
for (let i = numero; i >= 0; i--) {
    console.log(i);
}



numero = parseInt(prompt("Digite um número para somar de 1 até ele:"));
let soma = 0;
let i = 1;
while (i <= numero) {
    soma += i;
    i++;
    console.log("Soma:", soma);
}



numero = parseInt(prompt("Digite um número:"));
for (let i = 1; i <= 10; i++) {
    console.log(`${numero} x ${i} = ${numero * i}`);
}



numero = parseInt(prompt("Digite um número:"));
i = 1;
while (i <= 10) {
    console.log(`${numero} x ${i} = ${numero * i}`);
    i++;
}
function operacoesBasicas(num1, num2) {
    const soma = num1 + num2;
    const subtracao = num1 - num2;
    const multiplicacao = num1 * num2;
    const divisao = num1 / num2;

    console.log(`${num1} + ${num2} = ${soma}`);
    console.log(`${num1} - ${num2} = ${subtracao}`);
    console.log(`${num1} x ${num2} = ${multiplicacao}`);
    console.log(`${num1} / ${num2} = ${divisao}`);
}

operacoesBasicas(4, 5);
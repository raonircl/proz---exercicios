document.addEventListener('DOMContentLoaded', function () {
    const titulo = document.getElementById('titulo');
    const listaNaoOrdenada = document.querySelector('ul');
    const link = document.getElementById('link');
    const listaOrdenada = document.getElementById('lista-ordenada');

    titulo.innerText = 'Titulo Projeto DOM';
    link.innerText = 'Visite o site da Proz Educação';

    listaNaoOrdenada.innerHTML = `
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    `;

    listaOrdenada.innerHTML = `
        <li><a href="https://site1.com">Link para o Site 1</a></li>
        <li><a href="https://site2.com">Link para o Site 2</a></li>
        <li><a href="https://site3.com">Link para o Site 3</a></li>
    `;
});

document.getElementById('titulo').innerHTML = 'Produto à venda';

const body = document.body;

const produtoContainer = document.createElement('div');
const nomeProduto = document.createElement('h2');
const descricaoProduto = document.createElement('p');
const precoProduto = document.createElement('p');
const imagemProduto = document.createElement('img');

produtoContainer.style.border = '1px solid #ccc';
produtoContainer.style.padding = '10px';
produtoContainer.style.margin = '10px';

nomeProduto.innerText = 'Teclado Terra';
nomeProduto.style.color = 'gray';

descricaoProduto.innerText = 'Teclado cor de banana.';

precoProduto.innerText = 'Preço: R$ 199,99';
precoProduto.style.fontWeight = 'bold';

imagemProduto.src = 'https://static3.tcdn.com.br/img/img_prod/403641/teclado_ampliado_teclas_amarelas_letras_pretas_usb_padrao_abnt2_1151_1_20190809120119.png';
imagemProduto.alt = 'Imagem do Produto';

produtoContainer.appendChild(nomeProduto);
produtoContainer.appendChild(descricaoProduto);
produtoContainer.appendChild(precoProduto);
produtoContainer.appendChild(imagemProduto);

body.appendChild(produtoContainer);
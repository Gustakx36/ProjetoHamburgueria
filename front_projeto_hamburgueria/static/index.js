var carrinhoAtual = []
var carrinhoTable = []
var media1200 = window.matchMedia("(max-width: 1200px)")
var media700 = window.matchMedia("(max-width: 700px)")
retirarMenu()
alterarTamanhoModal()
buscarItens(0)
media700.addListener(alterarTamanhoModal)
media1200.addListener(alterarTamanhoModal)
media1200.addListener(retirarMenu)
$(window).on("load", async function(){
    const resposta = await $.ajax({
        url: 'https://gustakx36.pythonanywhere.com/type',
        dataType: 'json',
        method: 'GET'
    });
    let itensHtml = `<h1 class="busca cursor-pointer text-xl p-2 hover:bg-blue-600 rounded-md mt-1" id="busca0" onclick="buscarItens(0)">Todos</h1>`
    for(let i = 0; i < resposta.length; i++){
        const item = resposta[i]
        itensHtml += `<h1 class="busca cursor-pointer text-xl p-2 hover:bg-blue-600 rounded-md mt-1" id="busca${item.id}" onclick="buscarItens(${item.id})">${item.descricao}</h1>`
    }
    $('#submenu').html(itensHtml);
})
$('.finalizarPedido').on('click', async function(){
    if($('.finalizarPedido').hasClass('cursor-not-allowed')){
        return;
    }
    $('.modalObservacaoF').css('display', 'flex')
    $('.modalTextF').html(montarTable())
    setTimeout(() => {$('.modalBaseF').css('transform', 'scale(1)')}, 50)
})
$('.menu').on('click', function(){
    rotate = 'rotate(0deg)'
    if($('.menu').css('left') == '310px' && media1200.matches) {
        rotate = 'rotate(90deg)'
    }
    if($('.menu').css('left') == '310px') {
        $('.sidebar').css('left', '-300px')
        $('.apoio').css('min-width', '0px')
        $('.menu').css('left', '0px')
        $('.menu').css('transform', rotate)
    }else{
        $('.sidebar').css('left', '0px')
        $('.apoio').css('min-width', '300px')
        $('.menu').css('left', '310px')
        $('.menu').css('transform', 'rotate(180deg)')
    }
})
function montarTable(){
    let valorTotal = 0
    let table = `
        <div style="height: 144px; overflow: auto; padding: 0 20px 0 20px;">
            <table  class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-black-700 uppercase bg-red-100 dark:bg-red-700 dark:text-black-400">
                    <tr>`
    Object.keys(carrinhoTable[0]).forEach((item) => {
        table += `<th scope="col" class="px-6 py-3">${item}<th>`
    })
    table += `  
                        <th scope="col" class="px-6 py-3">Opções<th>
                    <tr>
                </thead>
                <tbody class="bg-red-50 dark:bg-red-700">`
    for(var i = 0; i < carrinhoTable.length; i++){
        table += `
                    <tr scope="col" class="px-6 py-3">`
        Object.keys(carrinhoTable[i]).forEach((item) => {
            if(item == 'preco'){
                valorTotal += carrinhoTable[i][item]
            }
            table += `<td scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">${carrinhoTable[i][item]}<td>`
        })
        table += `
                        <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">Deletar<td>
                    <tr>`
    }
    table += `
                </tbody>
            </table>
        </div>
        <div style="margin-top: 4px; padding: 0 20px 0 20px;">
            <table  class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-black-700 uppercase bg-red-100 dark:bg-red-700 dark:text-black-400">
                    <tr>
                        <th scope="col" class="px-6 py-3">Valor Total<th>
                        <th>${valorTotal.toFixed(2)}<th>
                    </tr>
                </thead>
            <table>
        </div>`
    return table
}
function retirarMenu() {
    if(media1200.matches) {
        $('.sidebar').css('left', '-300px')
        $('.apoio').css('min-width', '0px')
        $('.menu').css('left', '0px')
        $('.menu').css('transform', 'rotate(90deg)')
    }else {
        $('.sidebar').css('left', '0px')
        $('.apoio').css('min-width', '300px')
        $('.menu').css('left', '310px')
        $('.menu').css('transform', 'rotate(180deg)')
    }
}
function addItemCarrinho(id, preco, nome){
    $('.finalizarObservacao').attr('id', JSON.stringify({id : id, preco : preco, nome : nome}));
    $('.modalObservacao').css('display', 'flex')
    setTimeout(() => {$('.modalBase').css('transform', 'scale(1)')}, 50)
}
function atualizarCarrinho(preco){
    const valorAtual = parseFloat($('.valorTotal').html().replace('$', ''))
    const valorNovo = valorAtual + preco
    if(valorNovo > 0){
        $('.finalizarPedido').removeClass('cursor-not-allowed')
    }
    $('.valorTotal').html(`$${valorNovo.toFixed(2)}`)
}
function finalizarObs(id){
    const objetoProduto = JSON.parse(id)
    const observacao = $('#observacao').val()
    carrinhoTable.push({nome : objetoProduto.nome, preco : objetoProduto.preco})
    carrinhoAtual.push({observacao : observacao, id_produto : objetoProduto.id, preco : objetoProduto.preco})
    fecharModal()
    atualizarCarrinho(objetoProduto.preco)
    $('#observacao').val('')
}
function fecharModal(){
    $('.finalizarObservacao').attr('id', '');
    $('.modalBase').css('transform', 'scale(0)')
    setTimeout(() => {$('.modalObservacao').css('display', 'none')}, 300)
}
async function finalizarObsF(){
    if($('#nome').val() == ''){
        return Swal.fire({
            icon: 'warning',
            title: 'É preciso um nome para finalizar o pedido!'
        })
    }
    const data = {pedidos : carrinhoAtual, nome_cliente : $('#nome').val()}
    const resposta = await $.ajax({
        url: 'https://gustakx36.pythonanywhere.com/orders',
        dataType: 'json',
        method: 'POST',
        data: JSON.stringify(data)
    });
    if(resposta.response){
        Swal.fire({
            icon: 'success',
            title: 'Pedido finalizado!'
        })
    }
    carrinhoAtual = []
    $('.valorTotal').html('$0.00')
    $('.finalizarPedido').toggleClass('cursor-not-allowed')
    fecharModalF()
}
function fecharModalF(){
    $('.finalizarObservacaoF').attr('id', '');
    $('.modalBaseF').css('transform', 'scale(0)')
    setTimeout(() => {$('.modalObservacaoF').css('display', 'none')}, 300)
}
function alterarTamanhoModal(){
    if(media1200.matches && media700.matches){
        $('.modalBase').css('width', '70%')
        $('.modalBaseF').css('width', '70%')
    }else if(media1200.matches) {
        $('.modalBase').css('width', '50%')
        $('.modalBaseF').css('width', '50%')
    }else{
        $('.modalBase').css('width', '30%')
        $('.modalBaseF').css('width', '30%')
    }
}
async function buscarItens(id){
    const resposta = await $.ajax({
        url: 'https://gustakx36.pythonanywhere.com/product',
        dataType: 'json',
        method: 'GET'
    });
    let itensHtml = ''
    for(let i = 0; i < resposta.length; i++){
        if(resposta[i].tipo_produto == id || id == 0){
            const item = resposta[i]
            itensHtml += `
                <div onmouseleave="mouseLeave(this)" onmouseenter="mouseEnter(this)" class="item bg-white dark:bg-orange-500 rounded-lg px-6 py-8 ring-1 ring-slate-900/5 shadow-xl">
                    <div style="
                        width: 300px;
                        height: 300px;
                        display: flex;
                        justify-content: center;
                        ">
                        <span class="flex justify-center">
                            <img class="p-2 bg-red-600 rounded-md shadow-lg" src="${item.imagem}">
                        </span>
                    </div>
                    <h3 class="text-slate-900 dark:text-white mt-5 text-xl font-medium tracking-tight"  style="width: 300px;">${item.nome} - $${item.preco}</h3>
                    <p class="descricao text-slate-500 dark:text-white mt-2 text-base" style="width: 300px;">
                    ${item.descricao}
                    </p>
                    <div style="
                        width: 100%;
                        display: flex;
                        justify-content: end;
                        margin-top: 13px;
                        ">
                        <div class="itemAdd p-2 bg-red-600 rounded-md shadow-lg" onclick="addItemCarrinho(${item.id}, ${item.preco}, '${item.nome}')">
                            <svg width="30px" height="30px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M4 12H20M12 4V20" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </div>
                </div>`
        }
    }
    $('#itens').html(itensHtml)
    if(media700.matches ){
        $('.menu').trigger('click')
    }
}
function mouseLeave(elemento){
    elemento.children[2].style.maxHeight = '0px'
}
function mouseEnter(elemento){
    elemento.children[2].style.maxHeight = '100px'
}
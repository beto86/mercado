from typing import List, Dict
from time import sleep
from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('================================================')
    print('=============== Bem vindo ======================')
    print('============= Roberto SHOP =====================')
    print('================================================')

    print('Selecione uma opcao')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    opcao: int = int(input())
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("Volte Senpre!!")
        sleep(3)
        exit(0)
    else:
        print('Opcao Invalida!')
        sleep(2)
        menu()
    
def cadastrar_produto() -> None:
    print('================================================')
    print('============= Cadastrar Produto ================')
    print('================================================')

    nome: str = input("Informe o nome do produto: ")
    preco: float = float(input("Informe o preço do produto: "))
    produto: Produto = Produto(nome, preco)
    produtos.append(produto)
    print(f"O produto {produto.nome} foi cadastrado com sucesso!")
    sleep(3)
    menu()

def listar_produto() -> None:
    if len(produtos) > 0:
        print('================================================')
        print('============= Listar Produto ===================')
        print('================================================')
        for produto in produtos:
            print(produto)
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
    else: 
        print('Ainda nao tem produtos cadastrados!')
    sleep(3)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('================================================')
        print('============= Compra de Produto ================')
        print('================================================')
        print('===========Produtos diponiveis =================')
        for produto in produtos:
            print(produto)
            print('================================================')
            sleep(2)
        codigo: int = int(input())
        produto: Produto = pega_produto_por_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f"O Produto {produto.nome} agora possui {quant + 1} unidades no carrinho.")
                        tem_no_carrinho = True
                        sleep(3)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                    sleep(3)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                sleep(3)
                menu()
        else:
            print(f"O produto com codigo {codigo} nao foi encontrado!")
    else:
        print('Ainda nao tem produtos cadastrados!')
    sleep(3)
    menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('================================================')
        print('============= Pedidos no carrinho ==============')
        print('================================================')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"quantidade: {dados[1]}")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                sleep(2)
    else:
        print("Ainda nao existem produtos no carrinho")

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print("Produtos do Carrinho")
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                valor_total += dados[0].preco * dados[1]
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                sleep(2)
        print(f'Sua fatura e {formata_float_str_moeda(valor_total)}')
        print("volte sempre!")
        carrinho.clear()
        sleep(5)
    else:
        print("Sinda nao existe produtos no carrinho.")

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p
    
if __name__ == '__main__':
    main()

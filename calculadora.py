def main():
    print('1 - multiplicacao de dois números inteiros')
    print('2 - divisao entre dois numeros inteiros')
    print('0 - para sair')
    opcao = int(input('Entre com o numero para a opcao desejada'))
    while opcao>0:
        if(opcao == 1):
            a = int(input('Entre com o multiplicando'))
            b = int(input('Entre com o multiplicador'))
            multiplicacao(a,b)
        elif(opcao == 2):
            a = int(input('Entre com o dividendo'))
            b = int(input('Entre com o divisor'))
            divisao(a,b)

def multiplicacao(a,b):
    total = a
    aux = 0
    if(b == 1):
        print(a,'x',b,'=',a)
        
    elif(a=0 or b=0):
        print(a,'x',b,'=0')
    else:
        if(aux< b):
            total = a + a(multiplicacao(a,b))
            aux += 1
            return total
        else:
            print(total)

        



def divisao(a,b):
    total = 

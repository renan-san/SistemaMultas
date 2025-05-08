
def classificacao_infracao(vel,vel_max):
    if vel < vel_max:
        infracao = "Nenhuma infração"
        multa = 0
    elif vel < vel_max * 1.20:
        infracao = "Infração leve"
        multa = 130.16
    elif vel < vel_max * 1.50:
        infracao = "Infração grave"
        multa = 195.23
    else:
        infracao = "Infração gravíssima"
        multa = 880.41
    return infracao, multa


def calculo_penalidade(infracao):
    if infracao == "Infração leve":
        print("Penalidade: Pagar o valor de R$: 130,16")
    elif infracao == "Infração grave":
        print("Penalidade: Pagar o valor de R$: 195,23 e adição de 5 pontos à CNH")
    elif infracao == "Infração gravíssima":
        print("Penalidade: Pagar o valor de R$: 880,41 e adição de 7 pontos à CNH e suspensão da carteira, o motorista também deverá realizar um curso de reciclagem no Detran")



def calcular_reicidencia(multado, multa):
    if multado == "S" or multado == "SIM":
        multa = multa * 2
        print("Multa atualizada por reincidência: R$", multa)
    return multa


def pagar_multa(pagar, multanova):
    if pagar == "S" or pagar == "SIM":
        desconto = 0.20
        multanova = multanova * (1 - desconto)
        print("Valor com 20% de desconto: R$", round(multanova, 2))
    else:
        print("Valor total sem desconto: R$", multanova)


placa = input("Digite a placa do veículo:\n")
nome = input("Digite o nome do motorista:\n")
vel = float(input("Digite a velocidade registrada: \n"))
vel_max = float(input("Digite a velocidade máxima permitida: \n"))
multado = input("O motorista já foi multado antes? S/N: \n").upper()
pagar = input("Deseja pagar a multa agora? Desconto de 20% S/N: \n").upper()

print("\nPlaca do veículo:",placa)
print("Nome do motorista:",nome)

infracao, multa = classificacao_infracao(vel, vel_max)
print(infracao, multa)

calculo_penalidade(infracao)

multanova = calcular_reicidencia(multado, multa)

pagar_multa(pagar, multanova)

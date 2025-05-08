
def classificacao_velocidade(velocidade_registrada, velocidade_maxima):
  if velocidade_registrada <= velocidade_maxima:
    normalidade_velocidade = True
  elif velocidade_maxima * 1.2 >= velocidade_registrada:
    classificacao = "Infração Leve"
    multa = 130.16
    pontos_carteira = 0
    normalidade_velocidade = False
  elif velocidade_maxima * 1.2 < velocidade_registrada and velocidade_maxima * 1.5 >= velocidade_registrada:
    classificacao = "Infração Grave"
    multa = 195.23
    pontos_carteira = 5
    normalidade_velocidade = False
  else:
    classificacao = "Infração Gravíssima"
    multa = 880.41
    pontos_carteira = 7
    reciclagem = True
    normalidade_velocidade = False
  return normalidade_velocidade

def devolutiva_informacoes(normalidade_velocidade, multa):
  print(f"\nPlaca: {placa_veiculo}")
  print(f"Motorista: {nome_motorista}")
  print(f"Velocidade registrada: {velocidade_registrada:.1f} km/h.")
  print(f"Velocidade maxima permitida: {velocidade_maxima:.1f} km/h.")
  
  if normalidade_velocidade:
    print("Velocidade dentro do limite.")
  else:
    if pontos_carteira == 7:
      print(f"Atenção: {classificacao} - Multa de R${multa:.2f}, 7 pontos na CNH e suspensão da carteira.")
      print("Atenção: CNH suspensa. Compareça ao Detran.")
      print("Atenção: Você precisa fazer um curso de reciclagem no Detran.")
    else:
      print(f"Atenção: {classificacao} - Multa de R${multa:.2f} {'.' if pontos_carteira == 0 else f', {pontos_carteira} pontos na CNH.'}")

  if reincidencia == "Sim" or reincidencia == "sim" or reincidencia == "S" or reincidencia == "s":
    print("Atenção: Multa DOBRADA por reincidência!")
    multa *= 2
  if pagamento_multa == "Sim" or pagamento_multa == "sim" or pagamento_multa == "S" or pagamento_multa == "s":
    multa -= multa * 0.2
    print(f"Pagamento realizado. Você recebeu um desconto de 20%. Valor final: R$ {multa}")
  else:
    print(f"Pagamento não realizado. Valor final: R$ {multa}")
  exit()

# entrada de dados
pontos_carteira = 0
multa = 0 
reciclagem = False
classificacao = ""
placa_veiculo = input("Placa do Veiculo: ")
nome_motorista = input("Nome do Motorista: ")
velocidade_registrada = float(input("Velocidade Registrada (km/h): "))
velocidade_maxima = int(input("Velocidade Maxima (km/h): "))
reincidencia = input("Dupla Incidencia? (Sim/Não): ")
pagamento_multa = input("Deseja pagar a multa agora? (Sim/Não): ")


# classificação da velocidade
resultado_velocidade = classificacao_velocidade(velocidade_registrada, velocidade_maxima)

devolutiva_informacoes(resultado_velocidade, multa)


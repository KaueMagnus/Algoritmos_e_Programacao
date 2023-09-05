'''
Rendimento de Poupança
   Solicite ao usuário um valor depositado na poupança.
   Calcule o valor após um mês, considerando uma taxa de rendimento fixa.
   Mostre o valor atualizado.
'''
taxa = float(2.5 / 100)
deposito = float(input("Digite o valor a ser depositado:"))
total = float(deposito + (deposito * taxa))

print(f"Após um mês o valor de R${deposito} foi alterado para R${total}")




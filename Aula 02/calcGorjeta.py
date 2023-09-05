'''Solicite ao usuário o valor de uma refeição. 
Calcule uma gorjeta de 10% com Gorjeta = Valor * 0.1.
Mostre tanto a gorjeta quanto o valor total.'''

valor= float(input("Coloque o valor sem a gorgeta"))
gorgeta= valor + valor * 0.10
print (f"O valor com a gorgeta fica: {gorgeta}")
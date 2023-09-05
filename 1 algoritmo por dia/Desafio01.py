'''dado o tamanho do copo (250 ml ou 180 ml) e a meta diária de 2 litros de água, 
calcule quantos copos ele deve beber por dia para atender à recomendação da nutricionista.'''

copo = int(input("Qual copo você vai usar? (180 ou 250)ml: "))

if copo == 180:
    meta = float(2000/180)
    print(f"Você vai precisar beber {meta:.1f} copos para bater a meta de 2L diários.")
elif copo == 250:
    meta = float(2000/250)
    print(f"Você vai precisar beber {meta:.1f} copos para bater a meta de 2L diários.")
else:
    print("Copo inválido!")        
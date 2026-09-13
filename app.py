# Apresentação do sistema de desconto progressivo de compras
print("Bem-vindo ao sistema de desconto progressivo!")

# Recebimento do valor total da compra
valor_total = float(input("Informe o valor total da compra: ")) 

# Cálculo do desconto
if valor_total < 200: #desconto de 5% para compras abaixo de R$ 200,00
    print("O desconto nesta compra é de 5%")
    desconto = valor_total * 0.05
    valor_desconto = valor_total - desconto
elif valor_total < 300: #desconto de 10% para compras entre R$ 200,00 até abaixo de R$ 300,00
    print("O desconto nesta compra é de 10%")
    desconto = valor_total * 0.10
    valor_desconto = valor_total - desconto
else: #desconto de 15% para compras de R$ 300,00 ou mais
    print("O desconto nesta compra é de 15%")
    desconto = valor_total * 0.15
    valor_desconto = valor_total - desconto

# Apresentação do valor final da compra após o desconto
print(f"O valor da compra com desconto é de R$ {valor_desconto:.2f}")
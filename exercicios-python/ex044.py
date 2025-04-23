price = float(input("Enter the price of the product: "))
print('===========================\n1) Cash/check payment\n2) One-time payment by card\n3) Two installments by card\n4) Three or more installments by card')
payment = int(input('Choose a payment method: '))
print('===========================')

if payment == 1:
    final_price = price * 0.9
    print(f'You received 10% discount\n\033[7mR${price:.2f} > R${final_price:.2f}\033[m')
elif payment == 2:
    final_price = price * 0.95
    print(f'You received 5% discount\n\033[7mR${price:.2f} > R${final_price:.2f}\033[m')
elif payment == 3:
    print(f'You will pay the normal price.\n\033[7mR${price:.2f}\033[m')
elif payment == 4:
    final_price = price * 1.2
    print(f'You received 20% interest\n\033[7mR${price} > R${final_price:.2f}\033[m')
    installments = int(input('How many installments? '))
    installment_value = final_price / installments
    print(f'Each installment will be R${installment_value}')
else:
    print('\033[91mOPÇÃO INVÁLIDA DE PAGAMENTO\033[m')

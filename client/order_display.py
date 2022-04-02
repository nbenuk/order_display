def new_deliveroo():
    order_number=input('Order number: ')
    # confirmation=input('Deliveroo: ' + order_number '? Y/N')
    # POST
    
def new_ubereats():
    order_ref=input('Order reference: ')
    # POST

def new_justeat():
    order_ref=input('Order reference: ')
    pass

def new_order_mode():
    inp=input('Order type: (D) Deliveroo, (U) UberEats, (J) JustEat, (Q) Quit: ')
    while (inp != 'Q'):
        if inp == 'D':
            new_deliveroo()
        elif inp == 'U':
            new_ubereats()
        elif inp == 'J':
            new_justeat()
        inp=input('Order type: (D) Deliveroo, (U) UberEats, (J) JustEat, (Q) Quit: ')    

def preparing_order_mode():
    pass
    # Query Orders
    # Display orders
    # Select and Mark Preparing

def mark_ready_mode():
    pass
    # Query Orders
    # Display orders
    # Select and Mark Ready or Delete



# MAIN
print('\n---------------Welcome------------------------------Welcome------------------------------Welcome---------------\n')
inp=input('Enter an operation mode: (N) New Order, (P) Preparing, (R) Ready, (Q) Quit ')

while (inp != 'Q'):
    if inp == 'N':
        new_order_mode()
    elif inp == 'P':
        preparing_order_mode()
    elif inp == 'R':
        mark_ready_mode()

    inp=input('Enter an operation mode: (N) New Order, (P) Preparing, (R) Ready, (Q) Quit ')

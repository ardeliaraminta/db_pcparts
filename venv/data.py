#represents 1 order transaction
# rule of thumb : return the data ( 1 row of data in table )
class OrderTransaction:
    order_transaction_id = -1
    customer_id = -1
    product_id = -1
    quantity = 0
    payment_type = ''
    orderDate = None
    tax = 0
    total_amount = 0

#store global variable 
class Data:
    transactions = []
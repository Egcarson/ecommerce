from fastapi import APIRouter, Depends

from schema.order import Order, OrderCreate, orders, OrderProcess
from services.order import order_service
from schema.product import Product, products

order_router = APIRouter()

# list all order
# create an order 

@order_router.get('/', status_code=200)
def list_orders():
    response = order_service.order_parser(orders)
    return {'message': 'success', 'data': response}

@order_router.post('/', status_code=201)
def create_order(payload: OrderCreate = Depends(order_service.check_availability)):
    customer_id: int = payload.customer_id
    product_ids: list[int] = payload.items
    # get curr order id
    order_id = len(orders) + 1
    new_order = Order(
        id=order_id,
        customer_id=customer_id,
        items=product_ids,
    )
    orders.append(new_order)
    return {'message': 'Order created successfully', 'data': new_order}

# @order_router.put("/{customer_id}", status_code=201)
# def order_status_update(customer_id: int, payload: Product):
#     for order in products:
#         if customer_id == order.customer_id:
#             order.status = products.get(status)
#         return {'message': 'Order status updated successfully', 'data': orders}

@order_router.put('/order_process/{order_id}', status_code=201)
def order_process(order_id: int = Depends(order_service.complete_order)):
    for order in orders:
        print('wahallllllllla')
        if order.id == order_id:
            print('double wahallllllllla')
            order.status = OrderProcess.completed.value
            return {'message': 'Order processed successfully', 'data': order}
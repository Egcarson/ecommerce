from typing import Union
from pydantic import BaseModel, Field
from enum import Enum
from schema.customer import Customer

from schema.product import Product

class OrderProcess(Enum):
    completed: str = "COMPLETED"
    pending: str = "PENDING"

class Order(BaseModel):
    id: int
    customer_id: Union[int, Customer]
    items: list[int | Product]
    status: str = OrderProcess.pending.value

class OrderCreate(BaseModel):
    customer_id: int
    items: list[int]

orders: list[Order] = [
    Order(id=1, customer_id=1, items=[1, 2])
]
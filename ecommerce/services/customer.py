from fastapi import HTTPException
from schema.customer import Customer, CustomerCreate, customers

class CustomerService:

    @staticmethod
    def username_check(payload: CustomerCreate):
        username: str = payload.username
        for customer in customers:
            if customer.username == username:
                raise HTTPException (status_code=400, detail='username already exists')
        return payload

customer_service = CustomerService()
from schema.customer import Customer, CustomerCreate, customers

class CustomerService:

    @staticmethod
    def username_check(username: str):
        for customer in customers:
            if customer.username == username:
                return True
        return False

customer_service = CustomerService()
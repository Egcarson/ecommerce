from fastapi import APIRouter, HTTPException

from schema.product import Product, ProductCreate, products, ProductUpdate

product_router = APIRouter()

# create product
# list all products

@product_router.post('/', status_code=201)
def create_product(payload: ProductCreate):
    # get the product id
    product_id = len(products) + 1
    new_product = Product(
        id=product_id,
        name=payload.name,
        price=payload.price,
        quantity_available=payload.quantity_available
    )
    products[product_id] = new_product
    return {'message': 'Product created successfully', 'data': new_product}

@product_router.get('/', status_code=200)
def list_products():
    return {'message': 'success', 'data': products}

@product_router.put('/{product_id}', status_code=200)
def update_product(product_id: int, payload: ProductUpdate):
    if product_id in products:
        curr_product = Product(
            id=product_id,
            name=payload.name,
            price=payload.price,
            quantity_available=payload.quantity_available
        )

        updated_product = curr_product.copy(update=payload.dict())
        
        products[product_id] = updated_product.dict()

        return {'message': 'product edited successfully', 'data': updated_product.dict()}

    raise HTTPException (status_code=404, detail="product not found")


import stripe

from config.settings import STRIPE_API_KEY


def create_stripe_price(payment):
    stripe.api_key = STRIPE_API_KEY

    if payment.course:
        prod_name = payment.course.name
    else:
        prod_name = payment.lesson.name

    stripe_product = stripe.Product.create(
        name=prod_name
    )

    stripe_price = stripe.Price.create(
        currency="usd",
        unit_amount=payment.payed_amount,
        product_data={"name": stripe_product.name}
    )

    return stripe_price.id


def create_stripe_session(stripe_price_id):
    stripe.api_key = STRIPE_API_KEY

    stripe_session = stripe.checkout.Session.create(
        line_items=[{
            'price': stripe_price_id,
            'quantity': 1
        }],
        mode='payment',
        success_url='https://example.com/success'
    )

    return stripe_session.url, stripe_session.id

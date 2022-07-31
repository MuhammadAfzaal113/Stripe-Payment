import stripe
from stripe_example.config import Config
env = Config.environment(mode_selection='development')


stripe.api_key = env['stripe_api_key']
payment_method = stripe.PaymentMethod.create(
    type="card",
    card={
        "number": "4242424242424242",
        "exp_month": 6,
        "exp_year": 2023,
        "cvc": "314",
    },
)

customer = stripe.Customer.create(
    payment_method=payment_method.id
)

intent = stripe.PaymentIntent.create(
    customer=customer,
    payment_method=payment_method.id,
    currency='usd',  # you can provide any currency you want
    amount=(150 * 100),  # I modified amount to distinguish payments
    off_session=True,
    confirm=True
)


refund = stripe.Refund.create(
  charge="ch_3LHs5HKZSvaz9gvr1VpBRxC2",  # could be found in payment_intent
)

re_refund = stripe.Refund.retrieve(
  refund.id,
)


# SATURDAY, JUN 18
# 01:11, 06:38 = 05:27

# SATURDAY, JUN 4
# 02:23, 08:59 = 07:22

# 12:49

# Create Account
ex_account = stripe.Account.create(type='express', email='mughal6346@gmail.com')


# Create AccountLink Link
account_link = stripe.AccountLink.create(
  account=ex_account.id,
  refresh_url="http://127.0.0.1:8000/api/v1/restaurant/keyword/search?keyword=abc",
  return_url="http://127.0.0.1:8000/api/v1/user/test/",
  type="account_onboarding",
)

# Get account details
stripe.Account.retrieve(ex_account.stripe_id)

# Payment
payment_intent = stripe.PaymentIntent.create(
  amount=9000,
  currency='usd',
    confirm=True,
  stripe_account='acct_1LLqdeQPNirPBubA',
)

# Transfer balance to connected account
transfer = stripe.Transfer.create(
  amount=1000,
  currency="usd",
  destination="acct_1LLqdeQPNirPBubA",
)

# get dashboard login link
stripe.Account.create_login_link(ex_account.id)
# acct_1LMx1T4FHa8lELNC

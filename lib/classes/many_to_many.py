class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name length must be at least 3 characters")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)


class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def add_order(self, order):
        self._orders.append(order)

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def num_orders(self):
        return len(self._orders)


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        if not isinstance(price, float):
            raise ValueError("Price must be a float")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        customer.add_order(self)
        coffee.add_order(self)
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee


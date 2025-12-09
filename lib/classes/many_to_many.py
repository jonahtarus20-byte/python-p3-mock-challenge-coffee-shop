class Coffee:
    def __init__(self, name: str):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string longer than 2 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Ignore assignment to make name immutable
        pass

    def orders(self):
        # return all orders where this coffee was ordered
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        # return unique list of customers who ordered this coffee
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total = sum(order.price for order in orders)
        return total / len(orders)


class Customer:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Mutable string but enforce type and length
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        # ignore invalid assignment

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)


class Order:
    all = []

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")
        self._price = float(price)
        self.customer = customer
        self.coffee = coffee
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        # Ignore assignment to make price immutable
        pass

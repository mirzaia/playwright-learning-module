"""Starter: implement an OrdersPage instead of repeating raw selectors."""

class OrdersPage:
    def __init__(self, page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self):
        # TODO: navigate to the login page and sign in.
        raise NotImplementedError

    def filter_by_status(self, status: str):
        # TODO: select the status using a user-facing locator.
        raise NotImplementedError

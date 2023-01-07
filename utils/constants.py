class Url:
    login_url = "https://www.saucedemo.com/"
    main_page_url = "https://www.saucedemo.com/inventory.html"
    basket_page_url = "https://www.saucedemo.com/cart.html"
    product_page = "https://www.saucedemo.com/inventory-item.html?id=4"
    checkout = "https://www.saucedemo.com/checkout-step-one.html"
    checkout_two = "https://www.saucedemo.com/checkout-step-two.html"
    complete = "https://www.saucedemo.com/checkout-complete.html"


class Sign:
    name_login = "standard_user"
    pass_login = "secret_sauce"


class ERROR:
    error_pass = "//h3[contains(text(), 'Password is required')]"
    error_name = "//h3[contains(text(), 'Username is required')]"
    invalid_name_pass = "//h3[contains(text(), 'Username and password do not match')]"
    order_first_form_lname = "//h3[contains(text(), 'Error: Last Name is required')]"
    order_first_form_fname = "//h3[contains(text(), 'Error: First Name is required')]"
    order_first_form_p_code = "//h3[contains(text(), 'Error: Postal Code is required')]"

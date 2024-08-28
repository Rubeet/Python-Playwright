from playwright.sync_api import Page


class AmazonPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://www.amazon.com/'
        self.sign_in_menu = '#nav-link-accountList'
        self.sign_in_text_elem = '#nav-link-accountList-nav-line-1'
        self.email_field = '#ap_email'
        self.continue_button = 'span>[type="submit"]'
        self.password_field = '#ap_password'
        self.sign_in_button = '#signInSubmit'
        self.search_field = '#twotabsearchtextbox'
        self.search_button = '#nav-search-submit-button'
        self.first_result = '[data-image-index="1"]'
        self.add_to_cart_button = '#add-to-cart-button'
        self.proceed_to_check_out_button = '[name="proceedToRetailCheckout"]'
        self.add_a_new_address_button = '[class="a-row a-spacing-extra-large addressbook-footer"]>span'
        self.country_dropdown = '#address-ui-widgets-countryCode-dropdown-nativeId'
        self.full_name_field = '#address-ui-widgets-enterAddressFullName'
        self.address_line_1_field = '#address-ui-widgets-enterAddressLine1'
        self.address_line_2_field = '#address-ui-widgets-enterAddressLine2'
        self.city_field = '#address-ui-widgets-enterAddressCity'
        self.state_field = '#address-ui-widgets-enterAddressStateOrRegion-dropdown-nativeId'
        self.zip_code_field = '#address-ui-widgets-enterAddressPostalCode'
        self.phone_number_field = '#address-ui-widgets-enterAddressPhoneNumber'
        self.use_this_address_button = 'input[aria-labelledby="address-ui-widgets-form-submit-button-announce"]'

    def go_to(self):
        self.page.goto(self.url)

    def pick_sign_in_text(self):
        return self.page.text_content(self.sign_in_text_elem)

    def go_to_login_page(self):
        self.page.wait_for_selector(self.sign_in_menu, state='visible')
        self.page.click(self.sign_in_menu)

    def fill_email_field(self, email):
        self.page.wait_for_selector(self.email_field, state='visible')
        self.page.fill(self.email_field, email)

    def click_on_continue_button(self):
        self.page.wait_for_selector(self.continue_button, state='visible')
        self.page.click(self.continue_button)

    def fill_password_field(self, password):
        self.page.wait_for_selector(self.password_field, state='visible')
        self.page.fill(self.password_field, password)

    def click_on_sign_in_button(self):
        self.page.wait_for_selector(self.sign_in_button, state='visible')
        self.page.click(self.sign_in_button)
        self.page.wait_for_timeout(10000)

    def fill_search_field(self, search_text):
        self.page.wait_for_selector(self.search_field, state='visible')
        self.page.fill(self.search_field, search_text)

    def click_on_search_button(self):
        self.page.wait_for_selector(self.search_button, state='visible')
        self.page.click(self.search_button)

    def click_on_first_search_result(self):
        self.page.wait_for_selector(self.first_result, state='visible')
        self.page.click(self.first_result)

    def click_on_add_to_cart_button(self):
        self.page.wait_for_selector(self.add_to_cart_button, state='visible')
        self.page.click(self.add_to_cart_button)

    def click_on_checkout_button(self):
        self.page.wait_for_selector(self.proceed_to_check_out_button, state='visible')
        self.page.click(self.proceed_to_check_out_button)

    def click_on_add_a_new_address_button(self):
        self.page.wait_for_timeout(3000)
        self.page.wait_for_selector(self.add_a_new_address_button, state='visible')
        self.page.click(self.add_a_new_address_button)

    def fill_country_field(self, country):
        self.page.wait_for_selector(self.country_dropdown, state='visible')
        self.page.select_option(self.country_dropdown, country)

    def fill_full_name_field(self, full_name):
        self.page.wait_for_selector(self.full_name_field, state='visible')
        self.page.fill(self.full_name_field, full_name)
        self.page.wait_for_timeout(2000)

    def fill_address_one_field(self, address_one):
        self.page.wait_for_selector(self.address_line_1_field, state='visible')
        self.page.fill(self.address_line_1_field, address_one)
        self.page.wait_for_timeout(2000)

    def fill_address_two_field(self, address_two):
        self.page.wait_for_selector(self.address_line_2_field, state='visible')
        self.page.fill(self.address_line_2_field, address_two)
        self.page.wait_for_timeout(2000)

    def fill_city_field(self, city):
        self.page.wait_for_selector(self.city_field, state='visible')
        self.page.fill(self.city_field, city)
        self.page.wait_for_timeout(2000)

    def fill_state_field(self, state):
        self.page.wait_for_selector(self.state_field, state='visible')
        self.page.select_option(self.state_field, state)

    def fill_zip_code_field(self, zip_code):
        self.page.wait_for_selector(self.zip_code_field, state='visible')
        self.page.fill(self.zip_code_field, zip_code)
        self.page.wait_for_timeout(2000)

    def fill_phone_number_field(self, phone_number):
        numeric_phone_number = ''.join(filter(str.isdigit, phone_number))
        self.page.wait_for_selector(self.phone_number_field, state='visible')
        self.page.fill(self.phone_number_field, numeric_phone_number)
        self.page.wait_for_timeout(2000)

    def click_on_use_this_address_button(self):
        self.page.wait_for_selector(self.use_this_address_button, state='visible')
        self.page.click(self.use_this_address_button)
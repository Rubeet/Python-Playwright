import pytest
import csv
from amazon_playwright_task.pages.amazon_page import AmazonPage
from amazon_playwright_task.playwright_config import get_playwright_instance


@pytest.fixture(scope="function")
def context():
    context = get_playwright_instance()
    yield context
    context.close()


def read_credentials_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)  # Debugging: Print each row
            if all(field in row for field in ['email', 'password', 'search_query', 'country', 'full_name', 'street_address', 'address_2', 'city', 'state', 'zip_code', 'phone_number']):
                return (
                    row['email'],
                    row['password'],
                    row['search_query'],
                    row['country'],
                    row['full_name'],
                    row['street_address'],
                    row['address_2'],
                    row['city'],
                    row['state'],
                    row['zip_code'],
                    row['phone_number']
                )
        raise ValueError("CSV file must contain 'email', 'password', 'search_query', 'country', 'full_name', "
                         "'street_address',"
                         "'address_2', 'city', 'state', 'zip_code', and 'phone_number' columns.")


def test_amazon_navigation(context):
    page = context.new_page()
    amazon_home_page = AmazonPage(page)

    # Read CSV
    email, password, search_query, country, full_name, street_address, address_2, city, state, zip_code, phone_number = read_credentials_from_csv(
        './data/file.csv')

    # Navigate to the Amazon Home Page
    amazon_home_page.go_to()

    sign_in_elem_text = amazon_home_page.pick_sign_in_text()
    if 'sign in' in sign_in_elem_text.lower():
        amazon_home_page.go_to_login_page()

        # Fill in the email field
        amazon_home_page.fill_email_field(email)

        # Verify the email field is filled correctly
        assert page.input_value(amazon_home_page.email_field) == email

        # Click on the Continue button
        amazon_home_page.click_on_continue_button()

        # Fill the password field
        amazon_home_page.fill_password_field(password)

        # Verify the password field is filled correctly
        assert page.input_value(amazon_home_page.password_field) == password

        # Click on Signin Button
        amazon_home_page.click_on_sign_in_button()

    # Fill the search field
    amazon_home_page.fill_search_field(search_query)

    # Click on the Search button
    amazon_home_page.click_on_search_button()

    # Click on the first searched result
    amazon_home_page.click_on_first_search_result()

    # Click on the Add to Cart button
    amazon_home_page.click_on_add_to_cart_button()

    # Click on the Checkout button
    amazon_home_page.click_on_checkout_button()

    # Click on the add a new address button
    amazon_home_page.click_on_add_a_new_address_button()

    # Fill the Country field
    amazon_home_page.fill_country_field(country)

    # Fill the Full name field
    # amazon_home_page.fill_full_name_field(full_name)

    # Fill the Phone Number field
    amazon_home_page.fill_phone_number_field(phone_number)

    # Fill the Address 1 field
    amazon_home_page.fill_address_one_field(street_address)

    # Fill the Address 2 field
    amazon_home_page.fill_address_two_field(address_2)

    # Fill the City field
    amazon_home_page.fill_city_field(city)

    # Fill the State field
    amazon_home_page.fill_state_field(state)

    # Fill the Zip Code field
    amazon_home_page.fill_zip_code_field(zip_code)

    # # Click on the Use this address button
    # amazon_home_page.click_on_use_this_address_button()




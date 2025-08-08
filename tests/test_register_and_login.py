import pytest
from playwright.sync_api import Page

@pytest.mark.order(1)
def test_register(page: Page):
    page.goto("https://parabank.parasoft.com/parabank/register.htm")

    page.fill("input[name='customer.firstName']", "Test")
    page.fill("input[name='customer.lastName']", "User")
    page.fill("input[name='customer.address.street']", "123 Test St")
    page.fill("input[name='customer.address.city']", "Testville")
    page.fill("input[name='customer.address.state']", "Testonia")
    page.fill("input[name='customer.address.zipCode']", "12345")
    page.fill("input[name='customer.phoneNumber']", "1234567890")
    page.fill("input[name='customer.ssn']", "123-45-6789")

    username = "testuser1234"
    password = "password123"
    page.fill("input[name='customer.username']", username)
    page.fill("input[name='customer.password']", password)
    page.fill("input[name='repeatedPassword']", password)

    page.click("input[value='Register']")
    page.wait_for_load_state('networkidle')

    assert "Your account was created successfully" in page.content()

    with open("test_creds.txt", "w") as f:
        f.write(f"{username},{password}")

@pytest.mark.order(2)
def test_login(page: Page):
    with open("test_creds.txt", "r") as f:
        username, password = f.read().strip().split(',')

    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.fill("input[name='username']", username)
    page.fill("input[name='password']", password)
    page.click("input[value='Log In']")
    page.wait_for_load_state('networkidle')

    assert "Accounts Overview" in page.content()
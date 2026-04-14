import pytest
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://the-internet.herokuapp.com"
LOGIN_URL = f"{BASE_URL}/login"
SECURE_URL = f"{BASE_URL}/secure"
CHECKBOX_URL = f"{BASE_URL}/checkboxes"

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


# Тест 1:
def test_main_page_header(page):
    page.goto(BASE_URL)
    header_text = page.locator("h2").inner_text()
    print(f"Текст заголовка: {header_text}")
    expect(page.locator("h2")).to_contain_text("Available Examples")
    print(f"Текст содержит: 'Available Examples'")


# Тест 2:
def test_login_failure(page):
    page.goto(LOGIN_URL)
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("123")
    page.get_by_role("button", name="Login").click()
    error_message = page.locator("#flash").inner_text()
    print(f"Текст ошибки: {error_message}")
    expect(page.locator("#flash")).to_contain_text("Your password is invalid!")


# Тест 3:
def test_login_success(page):
    page.goto(LOGIN_URL)
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(SECURE_URL)
    welcome_text = page.locator(".subheader").inner_text()
    print(f"Текст приветствия: {welcome_text}")
    expect(page.locator(".subheader")).to_contain_text("Welcome to the Secure Area")

# Тест 4:
def test_checkboxes(page):
    page.goto(CHECKBOX_URL)

    checkboxes = page.locator("input[type='checkbox']").all()
    print(f"\nНайдено чекбоксов: {len(checkboxes)}")

    for i, cb in enumerate(checkboxes):
        status = "checked" if cb.is_checked() else "unchecked"

        text = cb.evaluate("node => node.nextSibling.textContent.trim()")

        print(f"Чекбокс {i + 1} [{text}]: {status}")

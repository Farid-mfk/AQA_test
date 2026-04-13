from playwright.sync_api import sync_playwright, expect

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")

        header_text = page.locator("h2").inner_text()
        print(f"Текст заголовка: {header_text}")

        expect(page.locator("h2")).to_contain_text("Available Examples")
        print(f"Текст содержит: 'Available Examples'")

        browser.close()

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")

        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("123")

        page.get_by_role("button").click()

        error_message = page.locator("#flash").inner_text()
        print(f"Текст ошибки: {error_message}")

        expect(page.locator("#flash")).to_contain_text("Your password is invalid!")

        browser.close()

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")

        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")

        page.get_by_role("button").click()
        expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

        welcome_text = page.locator(".subheader").inner_text()
        print(f"Текст приветствия: {welcome_text}")
        expect(page.locator(".subheader")).to_contain_text("Welcome to the Secure Area")

        browser.close()
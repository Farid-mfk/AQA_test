from playwright.sync_api import sync_playwright, Page, expect

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://demoqa.com/buttons")

        button = page.locator("#doubleClickBtn")

        button_text = button.inner_text()

        print(f"Текст кнопки: {button_text}")

        assert button_text == "Double Click Me"

        browser.close()

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://demoqa.com/buttons")

        click_btn = page.get_by_role("button", name="Click Me", exact=True)
        click_btn.click()
        message_locator = page.locator("#dynamicClickMessage")
        expect(message_locator).to_have_text("You have done a dynamic click")

        message_text = page.locator("#dynamicClickMessage").inner_text()

        assert message_text == "You have done a dynamic click"
        print(f"Текст после клика: {message_text}")

        browser.close()
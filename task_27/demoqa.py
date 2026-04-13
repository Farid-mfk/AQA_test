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

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://demoqa.com/text-box")

        page.locator("#userName").fill("Farid")
        page.locator("#userEmail").fill("farid@example.com")

        name_value = page.locator("#userName").input_value()
        email_value = page.locator("#userEmail").input_value()

        print(f"Имя: {name_value}, Email: {email_value}")

        browser.close()

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://demoqa.com/select-menu")

        options_locator = page.locator("select#cars option")

        all_options = options_locator.all_inner_texts()

        print(f"Список опций: {all_options}")

        if "Optimus Prime" in all_options:
            print("Optimus Prime найден в списке.")
        else:
            print("Optimus Prime не найден.")

        browser.close()

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://demoqa.com/text-box")

        label_locator = page.locator("#currentAddress-label")

        text_inner = label_locator.inner_text()
        text_content = label_locator.text_content()

        print(f"inner_text():   {repr(text_inner)}")
        print(f"text_content(): {repr(text_content)}")

        if text_inner == text_content:
            print("\nРезультаты идентичны.")

        browser.close()
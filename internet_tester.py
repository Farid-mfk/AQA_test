from playwright.sync_api import sync_playwright, Page, expect

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")

        title_locator = page.locator(".heading").text_content()
        assert "the-internet" in title_locator

        print(f"✅ Сайт доступен. Заголовок: {title_locator}")

        browser.close()


def navigate_to_example(page: Page, example_name: str) -> str:
    link = page.get_by_role("link", name=example_name, exact=True)
    link.click()

    return page.url


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/")

        example = "Form Authentication"
        current_url = navigate_to_example(page, example)
        assert "/login" in current_url

        print(f"✅ Перешли в: {example} | URL: {current_url}")

        browser.close()


def login(page: Page, user: str, passw: str):
    page.locator("#username").fill(user)
    page.locator("#password").fill(passw)
    page.get_by_role("button", name="Login").click()


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")

        login(page, "tomsmith", "SuperSecretPassword!")

        current_url = page.url
        assert "/secure" in current_url

        print(f"✅ Успешный вход! URL: {current_url}")

        page.get_by_role("link", name="Logout").click()

        assert "/login" in page.url
        print(f"✅ Успешный выход! URL: {page.url}")

        browser.close()

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/checkboxes")

        checkboxes = page.locator("input[type='checkbox']")
        cb1 = checkboxes.nth(0)
        cb2 = checkboxes.nth(1)

        assert not cb1.is_checked()
        assert cb2.is_checked()

        cb1.check()

        cb2.uncheck()

        print(f"✅ Checkbox 1: checked={cb1.is_checked()}")
        print(f"✅ Checkbox 2: checked={cb2.is_checked()}")

        browser.close()

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/dropdown")

        dropdown = page.locator("#dropdown")

        initial_text = dropdown.locator("option[selected]").text_content()
        assert "Please select an option" in initial_text

        dropdown.select_option(label="Option 1")

        assert dropdown.input_value() == "1"

        dropdown.select_option(label="Option 2")

        assert dropdown.input_value() == "2"

        selected_text = page.eval_on_selector("#dropdown", "sel => sel.options[sel.selectedIndex].text")
        print(f"✅ Выбрано: {selected_text}")

        browser.close()

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/inputs")

        input_num = page.locator('input[type="number"]')
        input_num.fill("123")
        assert input_num.input_value() == "123"
        input_num.clear()
        input_num.fill("456")
        print(f"✅ Введено: {input_num.input_value()}")

        browser.close()


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/hovers")

        first_figure = page.locator(".figure").first

        first_figure.hover()


        user_name = first_figure.locator("h5")

        print(f"✅ Навели на изображение. Текст: {user_name.inner_text()}")

        browser.close()

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/javascript_alerts")

        page.get_by_role("button", name="Click for JS Alert").click()

        result_text = page.locator("#result")
        expect(result_text).to_have_text("You successfully clicked an alert")

        print(f"✅ Alert принят. Сообщение: {result_text.inner_text()}")

        browser.close()
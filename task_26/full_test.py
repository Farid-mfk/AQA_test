from playwright.sync_api import sync_playwright, Page, expect

def run_full_test():
    results = {}
    base_url = "https://the-internet.herokuapp.com"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        try:
            # 1. Form Authentication
            page.goto(f"{base_url}/login")
            page.locator("#username").fill("tomsmith")
            page.locator("#password").fill("SuperSecretPassword!")
            page.get_by_role("button", name="Login").click()
            expect(page).to_have_url(f"{base_url}/secure")
            page.get_by_role("link", name="Logout").click()
            page.screenshot(path="auth_success.png")
            results["Form Authentication"] = "✅"

            # 2. Checkboxes
            page.goto(f"{base_url}/checkboxes")
            checkboxes = page.locator("input[type='checkbox']")
            checkboxes.nth(0).check()
            checkboxes.nth(1).uncheck()
            page.screenshot(path="checkboxes_success.png")
            results["Checkboxes"] = "✅"

            # 3. Dropdown
            page.goto(f"{base_url}/dropdown")
            dropdown = page.locator("#dropdown")
            dropdown.select_option(label="Option 2")
            expect(dropdown).to_have_value("2")
            page.screenshot(path="dropdown_success.png")
            results["Dropdown"] = "✅"

            # 4. Inputs
            page.goto(f"{base_url}/inputs")
            input_num = page.locator('input[type="number"]')
            input_num.fill("999")
            expect(input_num).to_have_value("999")
            page.screenshot(path="inputs_success.png")
            results["Inputs"] = "✅"

            # 5. Hovers
            page.goto(f"{base_url}/hovers")
            first_figure = page.locator(".figure").first
            first_figure.hover()
            expect(first_figure.locator("h5")).to_be_visible()
            page.screenshot(path="hovers_success.png")
            results["Hovers"] = "✅"

        except Exception as e:
            print(f"❌ Ошибка в тесте: {e}")
        finally:
            browser.close()

        # Генерация отчета
        print("\n📊 ОТЧЁТ:")
        for test_name, status in results.items():
            print(f"{status} {test_name}")

        if len(results) == 5:
            print("\n✨ Все тесты пройдены!")


if __name__ == "__main__":
    run_full_test()
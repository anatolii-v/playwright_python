from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    #browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    context = browser.new_context()
    page = context.new_page()
    #page.set_default_timeout(15000)
    #page.pause()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click(timeout=5000)
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("potopad537@prdalu.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Qwerty123", timeout=5000)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    #page.pause()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    #expect(page.get_by_role("button", name="Log In")).to_be_visible(timeout=7000)
    print("yee")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

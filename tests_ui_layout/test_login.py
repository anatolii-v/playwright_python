import time
from playwright.sync_api import Playwright, sync_playwright
import pytest

def test_login(set_up) -> None:
    page = set_up
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
    #expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    #expect(page.get_by_role("button", name="Log In")).to_be_visible(timeout=7000)
    print("yee")
    # ---------------------
    #context.close()
    #browser.close()


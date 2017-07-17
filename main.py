"""
Sample script for selenium webdriver against demo app
"""

# import pytest -- not required; installed at OS

from selenium import webdriver


def main():
    """CLI"""

    # Initialize
    browser = webdriver.Firefox()
    browser.get('http://localhost:3000/users')

    # Do something
    link = browser.find_element_by_xpath('//a[text()="New User"]')
    assert link is not None  # Never gets here if xpath fails

    # Teardown
    browser.quit()

if __name__ == '__main__':
    main()

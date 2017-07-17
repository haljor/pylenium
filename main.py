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
    assert 0 == 0

    # Teardown
    browser.quit()

if __name__ == '__main__':
    main()

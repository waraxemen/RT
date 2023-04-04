#!/usr/bin/python3
# -*- encoding=utf8 -*-
import json
import time
from termcolor import colored
from pages.elements import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pickle


class WebPage(object):

    _web_driver = None

    def __init__(self, web_driver, url=''):
        self._web_driver = web_driver
        self.get(url)

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            self.__getattribute__(name)._set_value(self._web_driver, value)
        else:
            super(WebPage, self).__setattr__(name, value)

    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)

        if not item.startswith('_') and not callable(attr):
            attr._web_driver = self._web_driver
            attr._page = self

        return attr

    def get(self, url):
        self._web_driver.get(url)
        self.wait_page_loaded()

    def go_back(self):
        self._web_driver.back()
        self.wait_page_loaded()

    def refresh(self):
        self._web_driver.refresh()
        self.wait_page_loaded()

    def screenshot(self, file_name='screenshot.png'):
        self._web_driver.save_screenshot(file_name)

    def scroll_down(self, offset=0):
        """ Scroll the page down. """

        if offset:
            self._web_driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        """ Scroll the page up. """

        if offset:
            self._web_driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self._web_driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    def switch_to_iframe(self, iframe):
        """ Switch to iframe by it's name. """

        self._web_driver.switch_to.frame(iframe)

    def switch_out_iframe(self):
        """ Cancel iframe focus. """
        self._web_driver.switch_to.default_content()

    def get_current_url(self):
        """ Returns current browser URL. """

        return self._web_driver.current_url

    def get_page_source(self):
        """ Returns current page body. """

        source = ''
        try:
            source = self._web_driver.page_source
        except:
            print(colored('Con not get page source', 'red'))

        return source

    def check_js_errors(self, ignore_list=None):
        """ This function checks JS errors on the page. """

        ignore_list = ignore_list or []

        logs = self._web_driver.get_log('browser')
        for log_message in logs:
            if log_message['level'] != 'WARNING':
                ignore = False
                for issue in ignore_list:
                    if issue in log_message['message']:
                        ignore = True
                        break

                assert ignore, 'JS error "{0}" on the page!'.format(log_message)

    def wait_page_loaded(self, timeout=60, check_js_complete=True,
                         check_page_changes=False, check_images=False,
                         wait_for_element=None,
                         wait_for_xpath_to_disappear='',
                         sleep_time=2):
        """ This function waits until the page will be completely loaded.
            We use many different ways to detect is page loaded or not:
            1) Check JS status
            2) Check modification in source code of the page
            3) Check that all images uploaded completely
               (Note: this check is disabled by default)
            4) Check that expected elements presented on the page
        """

        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            time.sleep(sleep_time)

        # Get source code of the page to track changes in HTML:
        source = ''
        try:
            source = self._web_driver.page_source
        except:
            pass

        # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
        while not page_loaded:
            time.sleep(0.5)
            k += 1

            if check_js_complete:
                # Scroll down and wait when page will be loaded:
                try:
                    self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self._web_driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass

            if page_loaded and check_page_changes:
                # Check if the page source was changed
                new_source = ''
                try:
                    new_source = self._web_driver.page_source
                except:
                    pass

                page_loaded = new_source == source
                source = new_source

            # Wait when some element will disappear:
            if page_loaded and wait_for_xpath_to_disappear:
                bad_element = None

                try:
                    bad_element = WebDriverWait(self._web_driver, 0.1).until(
                        EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
                    )
                except:
                    pass  # Ignore timeout errors

                page_loaded = not bad_element

            if page_loaded and wait_for_element:
                try:
                    page_loaded = WebDriverWait(self._web_driver, 0.1).until(
                        EC.element_to_be_clickable(wait_for_element._locator)
                    )
                except:
                    pass  # Ignore timeout errors

            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)

            # Check two times that page completely loaded:
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        # Go up:
        self._web_driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')

    def wait_for_animation(web_browser, selector):
        """
        Waits until jQuery animations have finished for the given jQuery  selector.
        """
        WebDriverWait(web_browser, 10).until(lambda web_browser: web_browser.execute_script(
            'return jQuery(%s).is(":animated")' % json.dumps(selector))
                                                                 == False)

    def wait_for_ajax_loading(web_browser, class_name):
        """
        Waits until the ajax loading indicator disappears.
        """
        WebDriverWait(web_browser, 10).until(lambda web_browser: len(web_browser.find_elements_by_class_name(
            class_name)) == 0)


    def quit(self):
        """ Quit the browser. """
        self._web_driver.quit()


    def open_page(self, web_browser):
        """ This is advanced function which also checks that all images completely loaded. """
        url = self.get_current_url()
        web_browser.get(url)

        page_loaded = False
        images_loaded = False

        script = ("return arguments[0].complete && typeof arguments[0].natural"
                "Width != \"undefined\" && arguments[0].naturalWidth > 0")

    # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
        while not page_loaded and not images_loaded:
            time.sleep(1)

        # Scroll down and wait when page will be loaded:
            web_browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            page_loaded = web_browser.execute_script("return document.readyState == 'complete';")

        # Make sure that every image loaded completely
        # (sometimes we have to scroll to the image to push browser upload it):
            pictures = web_browser.find_elements(By.XPATH, '//img')
            res = []

            for image in pictures:
                src = image.get_attribute('src')
                if src:
                # Scroll down to each image on the page:
                    image.location_once_scrolled_into_view  # не обращайте внимание, код работает
                    web_browser.execute_script("window.scrollTo(0, 155)")

                    image_ready = web_browser.execute_script(script, image)

                    if not image_ready:
                    # if the image not ready, give it a try to load and check again:
                        time.sleep(5)
                        image_ready = web_browser.execute_script(script, image)

                    res.append(image_ready)

        # Check that every image loaded and has some width > 0:
            images_loaded = False not in res

    # Go up:
        web_browser.execute_script('window.scrollTo(document.body.scrollHeight, 0);')

class AuthPage(WebPage):  # для авторизации с паролем

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

    tab_phone = WebElement(id='t-btn-tab-phone')
    tab_mail = WebElement(id='t-btn-tab-mail')
    tab_login = WebElement(id='t-btn-tab-login')
    tab_ls = WebElement(id='t-btn-tab-ls')
    first_field = WebElement(id='username')
    password_field = WebElement(id='password')
    tab_phone_is_active = WebElement(xpath="//div[@id='t-btn-tab-phone'][@class='rt-tab rt-tab--small rt-tab--active']")
    tab_mail_is_active = WebElement(xpath= "//div[@id='t-btn-tab-mail'][@class='rt-tab rt-tab--small rt-tab--active']")
    tab_login_is_active = WebElement(xpath= "//div[@id='t-btn-tab-login'][@class='rt-tab rt-tab--small rt-tab--active']")
    tab_ls_is_active = WebElement(xpath= "//div[@id='t-btn-tab-ls'][@class='rt-tab rt-tab--small rt-tab--active']")
    btn = WebElement(id="kc-login")
    phone_action = WebElement(id="phone_action")
    button_forgot_password = WebElement(id="forgot_password")
    title = WebElement(xpath="//h1[@class='card-container__title']")
    left_panel = WebElement(id="page-left")
    slogan = WebElement(xpath="//p[@class='what-is__desc']")
    button_register = WebElement(id="kc-register")
    button_register_in = WebElement(xpath="//button[@name='register']")
    input_name = WebElement(name="firstName")
    input_last_name = WebElement(name="lastName")
    region = WebElement(xpath="//div[@class='rt-input-container rt-select__input']//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange']")
    input_mail_or_phone = WebElement(id="address")
    password_confirm_field = WebElement(id="password-confirm")
    city = WebElement(xpath="//div[13]")


class RegPage(WebPage):  # переход на страницу регистрации

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)
        web_driver.get(url)
        button_register = WebElement(id="kc-register")
        while not EC.visibility_of_element_located((By.ID, "kc-register")):
            time.sleep(7)
            page.refresh()
        WebDriverWait(web_driver, 3).until(EC.element_to_be_clickable((By.ID, "kc-register"))).click()
        WebDriverWait(web_driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='firstName']")))
        # time.sleep(0.5)

    input_name = WebElement(xpath="//input[@name='firstName']")
    name_error = WebElement(xpath="//span[@class='rt-input-container__meta rt-input-container__meta--error']")
    only_name_error = WebElement(xpath="//span[contains(text(),'30')]")
    input_last_name = WebElement(name="lastName")

class MainPage(WebPage):  # для авторизации с куки
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru/'

        super().__init__(web_driver, url)
        with open('../my_cookies.txt', 'rb') as cookiesfile:  # загружаем куки страницы
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                web_driver.add_cookie(cookie)  # добавляем куки в браузер
            web_driver.refresh()  # закрываем браузер

    phone_action = WebElement(id="phone_action")

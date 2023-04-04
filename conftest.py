# needs to be installed:
# pytest
# pytest-selenium
# termcolor
# allure-python-commons
from requests import request
import allure
import uuid
import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture(scope = 'session')  # (autouse=True) for yandex driver (при использовании другого браузера - закоментить всю фикстуру)
def driver():  # при использовании закомментить строку browser = webdriver.Chrome(executable_path= в def web_browser
    s = Service(r"C:\Users\Администратор\AppData\Local\Yandex\YandexBrowser\Application\yandexdriver.exe")  # Путь к драйверу
    driver = webdriver.Chrome(service=s)  # Инициализируем драйвер
    chromeOptions = webdriver.ChromeOptions()  # Создаем объект options
    chromeOptions.binary_location = r"C:\Users\Администратор\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    # driver.get('http://petfriends.skillfactory.ru/login')  # Переходим на страницу авторизации (pytest.driver)
    # driver.maximize_window()  # Развернем окно
    yield driver   # Возвращаем объект pytest.driver
    driver.quit()  # Закрываем браузер


@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')  # добавляет аргументы для браузера
    chrome_options.add_argument('--log-level=DEBUG')
    return chrome_options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
# def web_browser(request):
    # browser = webdriver.Firefox(executable_path=r"C:\Users\Ann\PycharmProjects\PageObjects\tests\geckodriver.exe")   # for firefox driver
    # browser = webdriver.Chrome(executable_path=r"C:\Users\Ann\PycharmProjects\PageObjects\tests\chromedriver.exe")   # for chrome driver
def web_browser(request, selenium):  # use this for yandex driver instead of 2 strings above
    browser = selenium   # use this for yandex driver
    # browser.set_window_size(1080, 720)
    browser.maximize_window()  # Развернем окно

    # Return browser instance to test case:
    yield browser

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Make screen-shot for local debug:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # Attach screenshot to Allure report:
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

            # For happy debugging:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass # just ignore any errors here
    # browser.quit()  # Закрываем браузер

def get_test_case_docstring(item):
    """ This function gets doc string from test case and format it
        to show this docstring instead of the test case name in reports.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ This function modifies names of test cases "on the fly"
        during the execution of test cases.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ This function modified names of test cases "on the fly"
        when we are using --collect-only parameter for pytest
        (to get the full list of all existing test cases).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to
            # it's doc string to show human-readable reports and to
            # automatically import test cases to test management system.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')
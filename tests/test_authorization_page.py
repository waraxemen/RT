from pages.base import AuthPage, RegPage, MainPage
import pytest
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pickle

phone = ('+7 242 424-24-22')
login = "valid_login"
email = 'test@mail.ru'
ls = '123456789012'
password = 'Test_pass1'
wrong_password = 'Test_pass2'
wrong_phone = '+71234567890'


"""При вводе номера телефона/почты/логина/лицевого счета - таб выбора телефонной аутентификации меняется автоматически. """
def test_phone_auth_auto_changing(web_browser):
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    try:  # в данном тесте удостоверяемся что при вводе номера телефона вкладка не меняется
        page.tab_mail.click(0.3)  # кликаем на вкладку "Телефон"
        page.first_field.send_keys(phone)  # вводим значение
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_phone_is_active.find()  # проверяем, что вкладка телефона активна
    except AssertionError:
        print(f'Автоматическое переключение со вкладки почты при вводе {phone} не произошло')
    try:
        page.tab_phone.click(0.3)  # кликаем на вкладку "Телефон"
        page.first_field.send_keys(email)  # вводим значение
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_mail_is_active.find()  # проверяем, что вкладка почты активна
    except AssertionError:
        print(f'Автоматическое переключение со вкладки телефона при вводе {email} не произошло')
    try:
        page.tab_phone.click(0.3)  # кликаем на вкладку "Телефон"
        page.first_field.send_keys(login)  # вводим значение
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_login_is_active.find()  # проверяем, что вкладка логина активна
    except AssertionError:
        print(f'Автоматическое переключение со вкладки телефона при вводе {login} не произошло')
    try:
        page.tab_phone.click(0.3)  # кликаем на вкладку "Телефон"
        page.first_field.send_keys(ls)  # вводим значение
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_ls_is_active.find()  # проверяем, что вкладка лицевой счета активна
    except AssertionError:
        print(f'Автоматическое переключение со вкладки телефона при вводе {ls} не произошло')


"""При вводе номера телефона/почты/логина/лицевого счета - таб выбора почтовой аутентификации меняется автоматически"""
def test_mail_auth_auto_changing(web_browser):
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    try:
        page.tab_mail.click(0.3)  # кликаем на вкладку "Телефон"
        page.first_field.send_keys(phone)  # вводим значение
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_phone_is_active.find()
    except AssertionError:
        print(f'Автоматическое переключение со вкладки почты при вводе {phone} не произошло')
    try:
        page.tab_mail.click()  # кликаем на вкладку "Телефон"
        page.first_field.send_keys(email)
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_mail_is_active.find()
    except AssertionError:
        print(f'Автоматическое переключение со вкладки почты при вводе {email} не произошло')
    try:
        page.tab_mail.click(0.3)  # кликаем на вкладку "Телефон"
        # page.first_field.clear()  # очистим поле
        page.first_field.send_keys(login)  # вводим значение
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_login_is_active.find()
    except AssertionError:
        print(f'Автоматическое переключение со вкладки почты при вводе {login} не произошло')
    try:
        page.tab_mail.click(0.3)  # кликаем на вкладку "Телефон"
        page.first_field.send_keys(ls)  # вводим значение
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_ls_is_active.find()
    except AssertionError:
        print(f'Автоматическое переключение со вкладки почты при вводе {ls} не произошло')


"""При вводе номера телефона/почты/логина/лицевого счета - таб выбора аутентификации по логину меняется автоматически"""
def test_login_auth_auto_changing(web_browser):
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    try:
        page.tab_login.click(0.3)  # кликаем на вкладку "Телефон"
        page.first_field.send_keys(phone)  # вводим значение
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_phone_is_active.find()
    except AssertionError:
        print(f'Автоматическое переключение со вкладки Логин при вводе {phone} не произошло')
    try:
        page.tab_login.click()  # кликаем на вкладку "Телефон"
        page.first_field.send_keys(email)
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_mail_is_active.find()
    except AssertionError:
        print(f'Автоматическое переключение со вкладки Логин при вводе {email} не произошло')
    try:
        page.tab_login.click(0.3)  # кликаем на вкладку "Телефон"
        # page.first_field.clear()  # очистим поле
        page.first_field.send_keys(login)  # вводим значение
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_login_is_active.find()
    except AssertionError:
        print(f'Автоматическое переключение со вкладки Логин при вводе {login} не произошло')
    try:
        page.tab_login.click(0.3)  # кликаем на вкладку "Телефон"
        page.first_field.send_keys(ls)  # вводим значение
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_ls_is_active.find()
    except AssertionError:
        print(f'Автоматическое переключение со вкладки Логин при вводе {ls} не произошло')


"""При вводе номера телефона/почты/логина/лицевого счета - таб выбора ЛС аутентификации меняется автоматически. """
def test_ls_auth_auto_changing(web_browser):
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    try:
        page.tab_ls.click(0.3)  # кликаем на вкладку "Телефон"
        page.first_field.send_keys(phone)  # вводим значение
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_phone_is_active.find()
    except AssertionError:
        print(f'Автоматическое переключение со вкладки ЛС при вводе {phone} не произошло')
    try:
        page.tab_ls.click()  # кликаем на вкладку "Телефон"
        page.first_field.send_keys(email)
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_mail_is_active.find()
    except AssertionError:
        print(f'Автоматическое переключение со вкладки ЛС при вводе {email} не произошло')
    try:
        page.tab_ls.click(0.3)  # кликаем на вкладку "Телефон"
        # page.first_field.clear()  # очистим поле
        page.first_field.send_keys(login)  # вводим значение
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_login_is_active.find()
    except AssertionError:
        print(f'Автоматическое переключение со вкладки ЛС при вводе {login} не произошло')
    try:
        page.tab_ls.click(0.3)  # кликаем на вкладку "Телефон"
        page.first_field.send_keys(ls)  # вводим значение
        page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность вкладке поменяться
        assert page.tab_ls_is_active.find()
    except AssertionError:
        print(f'Автоматическое переключение со вкладки ЛС при вводе {ls} не произошло')


"""Авторизация клиента по номеру телефона с валидными параметрами"""
def test_valid_authorisation(web_browser):  # авторизация
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    page.tab_phone.click(0.3)  # кликаем на вкладку "Телефон"
    page.first_field.send_keys(phone)  # вводим номер телефона
    page.password_field.send_keys(password)  # вводим пароль
    page.btn.click(1)  # жмём кнопку "Войти"
    try:
        assert page.phone_action.find()  # проверяем, что появилась настройка "Телефон" в ЛК
    except AssertionError:
        print('Авторизация не произошла, проверьте правильность ввода номера телефона и пароля')


"""Авторизация клиента по номеру телефона с невалидным паролем"""
def test_invalid_password_authorisation(web_browser):
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    page.tab_phone.click(0.3)  # кликаем на вкладку "Телефон"
    page.first_field.send_keys(phone)  # вводим номер телефона
    page.password_field.send_keys(wrong_password)  # вводим невалидный пароль
    page.btn.click(1)  # жмём кнопку "Войти"
    assert not page.phone_action.find()  # проверяем, что не появилась настройка "Телефон" в ЛК


"""Авторизация клиента по номеру телефона с невалидным номером телефона """
def test_invalid_phone_authorisation(web_browser):
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    page.tab_phone.click(0.3)  # кликаем на вкладку "Телефон"
    page.first_field.send_keys(wrong_phone)  # вводим значение с невалидным номером телефона
    page.password_field.send_keys(password)  # вводим пароль
    page.btn.click(1)  # жмём кнопку "Войти"
    assert not page.phone_action.find()  # проверяем, что не появилась настройка "Телефон" в ЛК


"""Наличие всех вкладок"""
def test_all_tabs_are_visible(web_browser):
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    assert page.tab_phone.is_visible()
    assert page.tab_mail.is_visible()
    assert page.tab_login.is_visible()
    assert page.tab_ls.is_visible()

"""Проверка кнопки "Забыл пароль" на странице авторизации"""
def test_button_forgot_password(web_browser):
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    page.button_forgot_password.click(0.3)  # кликаем на кнопку "Забыл пароль"
    text = page.title.get_text()  # получаем текст
    assert text == "Восстановление пароля"

"""Продуктовый слоган ЛК 'Ростелеком ID'."""
def test_product_skill(web_browser):
    page = AuthPage(web_browser)
    page.open_page(web_browser)
    text = page.slogan.get_text()  # получаем текст слогана
    assert text != '' and page.left_panel.is_visible()  # проверяем, что слоган есть и левая панель отображается

"""Кнопка "Зарегистрироваться" на странице авторизации"""
def test_button_register(web_browser):
    page = AuthPage(web_browser)
    page.button_register.click(0.3)  # кликаем на кнопку "Зарегистрироваться"
    assert page.button_register_in  # проверяем, что появилась кнопка "Зарегистрироваться" на странице регистрации

"""Форма ввода имени - валидное имя"""
@pytest.mark.parametrize('name', ['Си', 'Иван', 'Маша', 'Джон', 'Александра', 'Иван-Чай', 'Андвпвпвпвмвкмвкмвкпвкпвмвквв'])
def test_input_name(web_browser, name):
    page = RegPage(web_browser)
    # page.button_register.click(0.3)  # кликаем на кнопку "Зарегистрироваться"
    while not page.input_name.is_visible():
        page.refresh()  # перезагрузка страницы при ошибке загрузки
    page.input_name.send_keys(name)
    page.input_last_name.click(0.2)
    # assert not page.name_error.find()  # проверяем, что не появилась сообщение об ошибке ввода имени
    assert not page.name_error.is_visible()  # проверяем, что не появилась сообщение об ошибке ввода имени


"""Форма ввода имени - валидное имя из 2 символов и с символом "-" """
@pytest.mark.parametrize('name', ['Ф-', '-А', '--', '-А-', '---', '-Иван-Чай-'])
def test_input_name_(web_browser, name):
    page = RegPage(web_browser)
    while not page.input_name.is_visible():
        page.refresh()  # перезагрузка страницы при ошибке загрузки
    page.input_name.send_keys(name)
    page.input_last_name.click(0.2)
    try:
        assert not page.name_error.is_visible()  # проверяем, что не появилось сообщение об ошибке ввода имени
    except AssertionError:
        print(f'При вводе {name} высветилась ошибка')


"""Форма ввода имени невалидное имя"""
@pytest.mark.parametrize('name', ['Ф', ' ', '123', 'Антон2', 'Андвпвпвпвмвкмвкмвкпвкпвмвкввп', 'Андвпвпвпвмвкмвкмвкпвкпвмвкввпа','Иван Антонович',
                                  'Аванапрапривкеваикеиервкпвпиукпупаыпмкпкпвкпвамикпкпвмвкпвкпвапкпквпквпвмикеркпкпвпиукпупаыпмкпкпвкпвамикпкпвмвкпвкпвапкпквпквпвмикеркпкпвпиукпупаыпмкпкпвкпвамикпкпвмвкпвкпвапкпквпквпвмикеркпкпвпиукпупаыпмкпкпвкпвамикпкпвмвкпвкпвапкпквпквпвмикеркпкпвпппвп',
                                  'Andry','','"&&&','???','@@@','№№№',';;;','%%%','"""',"'''",'...','^^^','###','!!!','☺☺☺','صسغذئآ','龍門大酒家','<IMG src="#">','原千五百秋瑞',
                                  '<script>alert("Поле input уязвимо!")</script>','drop table keycloak.accounts','Bdfy Fynjyjdbx'])
def test_input_invalid_name(web_browser, name):
    page = RegPage(web_browser)
    while not page.input_name.is_visible():
        page.refresh()  # перезагрузка страницы при ошибке загрузки
    page.input_name.send_keys(name)
    page.input_last_name.click(0.2)
    try:
        assert page.name_error.is_visible()  # проверяем, что появилось сообщение об ошибке ввода имени
    except AssertionError:
        print(f'При вводе {name} не высветилась ошибка')


"""Форма ввода фамилии - валидная фамилия"""
@pytest.mark.parametrize('name', ['Си', 'Иван', 'Маша', 'Джон', 'Александра', 'Иван-Чай', 'Андвпвпвпвмвкмвкмвкпвкпвмвквв'])
def test_input_last_name(web_browser, name):
    page = RegPage(web_browser)
    while not page.input_last_name.is_visible():
        page.refresh()  # перезагрузка страницы при ошибке загрузки
    page.input_last_name.send_keys(name)
    page.input_name.click(0.2)
    assert not page.name_error.is_visible()  # проверяем, что не появилось сообщение об ошибке ввода имени


"""Форма ввода фамилии - не валидная фамилия"""
@pytest.mark.parametrize('name', ['Ф', ' ', '123', 'Антон2', 'Андвпвпвпвмвкмвкмвкпвкпвмвкввп', 'Андвпвпвпвмвкмвкмвкпвкпвмвкввпа','Иван Антонович',
                                  'Аванапрапривкеваикеиервкпвпиукпупаыпмкпкпвкпвамикпкпвмвкпвкпвапкпквпквпвмикеркпкпвпиукпупаыпмкпкпвкпвамикпкпвмвкпвкпвапкпквпквпвмикеркпкпвпиукпупаыпмкпкпвкпвамикпкпвмвкпвкпвапкпквпквпвмикеркпкпвпиукпупаыпмкпкпвкпвамикпкпвмвкпвкпвапкпквпквпвмикеркпкпвпппвп',
                                  'Andry','','"&&&','???','@@@','№№№',';;;','%%%','"""',"'''",'...','^^^','###','!!!','☺☺☺','صسغذئآ','龍門大酒家','<IMG src="#">','原千五百秋瑞',
                                  '<script>alert("Поле input уязвимо!")</script>','drop table keycloak.accounts','Bdfy Fynjyjdbx'])
def test_input_invalid_last_name(web_browser, name):
    page = RegPage(web_browser)
    while not page.input_last_name.is_visible():
        page.refresh()  # перезагрузка страницы при ошибке загрузки
    page.input_last_name.send_keys(name)
    page.input_name.click(0.2)
    try:
        assert page.name_error.is_visible()  # проверяем, что появилось сообщение об ошибке ввода имени
    except AssertionError:
        print(f'При вводе {name} не высветилась ошибка')


"""__________________________________________Бонусные тесты__________________________________________"""

"""Зарегистрироваться на странице авторизации"""
def test_registration(web_browser):
    page = AuthPage(web_browser)  # создаем объект страницы авторизации
    page.button_register.click(0.3)  # кликаем на кнопку "Зарегистрироваться"
    assert page.button_register_in  # проверяем, что появилась кнопка "Зарегистрироваться" на странице регистрации
    page.input_name.send_keys('Превед')  # вводим имя
    page.input_last_name.send_keys('Медвед')  # вводим фамилию
    page.input_mail_or_phone.send_keys(email)  # вводим email
    page.region.click()  #send_keys("Волгоградская обл")
    page.city.click()  # Подтверждение города
    page.password_field.send_keys(password)  # вводим пароль
    page.password_confirm_field.send_keys(password)  # вводим пароль повторно
    time.sleep(1)  # для визуализации и обхода возможной засветки автоматизации
    page.button_register_in.click(1)  # 1 - click hold 1 second on login button
    assert not page.button_register_in  # проверяем, что нет кнопки "Зарегистрироваться"


"""Формы ввода имени и фамилии - валидные данные"""
@pytest.mark.parametrize('name', ['Си', 'Иван', 'Маша', 'Джон', 'Александра', 'Иван-Чай', 'Андвпвпвпвмвкмвкмвкпвкпвмвквв'])
@pytest.mark.parametrize('last_name', ['Си', 'Иван', 'Маша', 'Джон', 'Александра', 'Иван-Чай', 'Андвпвпвпвмвкмвкмвкпвкпвмвквв'])
def test_input_last_name_and_name(web_browser, name, last_name):
    page = RegPage(web_browser)  # создаем объект страницы регистрации
    page.input_name.send_keys(name)  # вводим имя
    page.input_last_name.send_keys(last_name)  # вводим фамилию
    page.input_name.click(0.2)  # кликаем на поле имени
    assert not page.name_error.is_visible()  # проверяем, что не появилось сообщение об ошибке ввода имени


"""Использование значений из файла. Вводим значения в поля имени и фамилии"""
def test_input_file_names(web_browser):
    page = RegPage(web_browser)
    with open('names.txt',encoding = 'utf-8', mode = 'r') as names:
        lines = names.readlines()
        for name in lines:
            # print(name.strip())
            try:
                page.input_last_name.send_keys(name)
                page.input_name.send_keys(name)
                page.input_last_name.click(0.2)
                assert not page.only_name_error.is_visible()
            except AssertionError:
                print(f'При вводе {name} высветилась ошибка!')
    page.quit()


"""Получаем печеньку"""
def test_authorisation(web_browser):  # авторизация
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    page.tab_login.click(0.3)  # кликаем на вкладку "Логин"
    page.first_field.send_keys(login)  # вводим логин
    page.password_field.send_keys(password)  # вводим пароль
    page.btn.click(1)  # жмём кнопку "Войти"
    try:
        assert page.phone_action.find()  # проверяем, что появилась настройка "Телефон" в ЛК
    except AssertionError:
        print('Авторизация не произошла, проверьте правильность ввода номера телефона и пароля')

    with open('../my_cookies.txt', 'wb') as cookies:  # создание файла с cookies
        pickle.dump(web_browser.get_cookies(), cookies)  # сохранение cookies в файл
    page.quit()

"""Кормим браузер печенькой и фоткаемся с ним на память"""
def test_petfriends(web_browser):
    page = MainPage(web_browser)
    WebDriverWait(web_browser, 9).until((EC.visibility_of_element_located((By.ID, "phone_action"))))
    page.scroll_down()
    page._web_driver.save_screenshot('Main.png')















# def test_all_images_completely_loaded(web_browser):
#     """This is advanced test which also checks that all images completely loaded."""
#     page = MainPage(web_browser)
#     page.open_page(web_browser)

#  примеры использования JavaScript, more info: http://allselenium.info/javascript-using-python-selenium-webdriver/
#     web_browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 1
#     JavaScript = "document.getElementsByName('username')[0].click();"  # 2
#     web_browser.execute_script(JavaScript)


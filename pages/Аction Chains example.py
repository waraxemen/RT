from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base import MainPage

"""Тест не рабочий, чисто в информативных целях"""
def test_action_chains(web_browser):
    MainPage(web_browser)
    menu = web_browser.find_elements(By.CSS_SELECTOR, "img.card-img-top")
    hidden_submenu = web_browser.find_element_by_css_selector(".nav #submenu1")  # подменю, но на сайте негде такое использовать.
    ActionChains(web_browser).move_to_element(menu).click(hidden_submenu).perform()
    # или эта же команда разбитая по частям
    # actions = ActionChains(web_browser)  # создаем объект ActionChains
    # actions.move_to_element(menu)  # переходим на элемент
    # actions.click(hidden_submenu)   # клик по подменю
    # actions.perform()   # выполнить действия

    # Варианты методов для Action Chains:

    # click(on_element=None) — клик на элемент.

    # Аргументы: on_element - выбранный элемент. Если None — клик на текущей позиции мыши.

    # click_and_hold(on_element=None) — клик с зажатием клавиши. Подобный клик применяется,
    # когда веб - страница имеет дополнительную логику при нажатии элементов, и событие нажатия на элемент
    # не срабатывает, если нажатие совершено быстрее, чем это делают реальные пользователи.

    # drag_and_drop(source, target) — нажимаем левой клавишей мыши на элементе - источнике
    # и переносим на элемент - цель, отпускаем кнопку мыши.

    # Аргументы: source: нажатие кнопки мыши

    # target: отпускаем кнопку

    # pause(seconds) — пауза всех входных действий на время в секундах.

    # release(on_element=None) — отжатие нажатой кнопки мыши на элементе. Если None,
    # отпустить кнопку мыши на текущей позиции.

    # reset_actions() — сброс действий, которые были сохранены.

    # Аргументы: on_element: perform() — выполнение всех заданных действий.

    # Более подробно - https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains


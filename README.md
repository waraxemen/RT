# 28module
Final exercise
Итоговый проект по автоматизации тестирования
→ Объект тестирования: https://b2c.passport.rt.ru

Заказчик передал вам следующее задание:

Протестировать требования.
Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
Провести автоматизированное тестирование продукта (не менее 15 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.
Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов.

Перечислены инструменты, которые применялись для тестирования

Почему именно этот инструмент и эту технику.
Что им проверялось.
Что именно в нем сделано.

Классы эквивалентности, для сокращения количиства параметров, проверялись формы для ввода имени и фамилии, как пример  - тест "Форма ввода имени - валидное имя".

Граничные значения, для проверки граничных значений формы для ввода имени и фамилии, как пример  - тест "Форма ввода имени невалидное имя"

Техника предугадывания ошибки, на основе опыта определил возможные ошибки, как пример  - тест "Форма ввода имени - валидное имя из 2 символов и с символом '-' "

Тестирование состояний и переходов, для проверки соответствия заявленным требованиям, как пример  - тест "При вводе номера телефона/почты/логина/лицевого счета - таб выбора телефонной аутентификации меняется автоматически. "

Попарное тестирование, использовалось для проверки пар имя и фамилия,  как пример  - тест "Формы ввода имени и фамилии - валидные данные"

Тестирование по сценарию использования, для отработки необходимых действий пользователя для регистрации, как пример  - тест "Зарегистрироваться на странице авторизации"

Код писался в PyCharm, в качестве основы взял Smart Page Object, в нём модифицированы некоторые фикстуры и добавлены свои, так же добавлены драйверы для браузеров Chrome, Yandex, Firefox с возможностью выбора одного из них. Добавлены в основной код элементы clear_all, is_visible и базовый quit. 

Для авторизации используется 3 класса: AuthPage для авторизации с паролем, RegPage переход на страницу регистрации, MainPage для авторизации с куки.

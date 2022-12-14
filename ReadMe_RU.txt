Проект PostParcing
Идея проекта пришла в голову, когда выполнял задачу по анализу эффективности направления почтовых отправлений.
Во время работы с API Почты России появилась идея создания бота для телеграма,
которому будет передаваться трек-номер (barcode) для отслеживания отправления, а дальше он будет проводить мониторинг
его состояния и присылать информацию в Telegram.
Я хотел развить свои навыки работы с API, SOAP-протоколом и научиться создавать чат-ботов для Telegram.

Документация API Почты России здесь: https://tracking.pochta.ru/specification
Необходимо пройти регистрацию и получить логин и пароль. (Если интересно, напишите мне, я подготовлю пошаговый туториал
по регистрации на сайте и получению логина и пароля для работы с API)
Поэтому чтобы код сработал, Вам нужно будет использовать свой логин, пароль и трек-номер

На сайте Почты России пример кода для Python использует библиотеку SUDS
Но у меня с данной библиотекой ничего не получилось, поэтому я использовал Zeep

Размещаю 1 часть проекта: обращение к API, получение данные и сбор нужных данных в словарь.
В итоге данные систематизируются и собираются в 2 словаря:
1 - данные отправления и начальной стадии (main_information);
2 - данные текущей стадии (current_status).

Данные словаря 1 будут постоянными, а данные словаря 2 будут меняться по ходу следования отправления.

____________
Следующие этапы:
- создание отчета, который будет содержать все этапы следования отправления
- создание телеграм бота для управления и получения данных

Если будут идеи по улучшению кода, совместной работе или интересные проекты, то буду рад общению.
Павел Харитонов
GitHub: https://github.com/LinkVel
LinkedIn: https://www.linkedin.com/in/linkvel-596317b2/
E-Mail: Pavehar@gmail.com

_________________________________________________________________________________________________________________
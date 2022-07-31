PostParcing Project
The idea of the project came to mind when I was performing the task of analyzing the effectiveness of sending mail.
While working with the API of the Russian Post, the idea of creating a bot for telegram appeared,
to which a track number (barcode) will be transmitted to track the shipment, and then it will monitor
its status and send information to Telegram.
I wanted to develop my skills with the API, SOAP protocol and learn how to create chatbots for Telegram.

The Russian Post API documentation is here: https://tracking.pochta.ru/specification
You need to register and get a username and password(If you are interested, write to me,
I will prepare a step-by-step tutorial by registering on the site and getting a login and password to work with the API)
Therefore, in order for the code to work, you will need to use your username, password and track number

On the website of the Russian Post, an example code for Python uses the SUDS library
But nothing worked out for me with this library, so I used Zeep

I place 1 part of the project: accessing the API, getting data and collecting the necessary data into the dictionary.
As a result, the data is systematized and collected into 2 dictionaries:
1 - shipment and initial stage data (main_information);
2 - data of the current stage (current_status).

The data of dictionary 1 will be constant, and the data of dictionary 2 will change along the route of shipment.

____________
Next steps:
- creation of a report that will contain all the stages of the shipment
- creation of a telegram bot for managing and receiving data

If there are ideas for improving the code, collaboration or interesting projects, I will be glad to communicate.

Pavel Kharitonov
GitHub: https://github.com/LinkVel
LinkedIn: https://www.linkedin.com/in/linkvel-596317b2/
E-Mail: Pavehar@gmail.com
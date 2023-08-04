## Table of contents

- Installation
- Requirements
- Configuration


## Python Installation

- pip install webdriver-manager
- pip install --upgrade pip
- pip install --upgrade pip

## Requirements
Go to latlong  and create a user, the user and password will be used in lat-long-email and latlonf-password
    https://www.latlong.net/user/login
<br>
Go to api ninjas create an account and an api key for covid19 api and configure covidkey key
https://api-ninjas.com/
<br>
Go to api mail gun and  create an account and an api key to send email
https://www.mailgun.com/
<br>
Go to api mail gun create an account and an api key for mailgun api and configure mailgun-key attribute
https://api.mailgun.net/
<br>


## Configuration
To configure this bot to send you weather and covid19 status every day just configure the file config.txt:
* for that create a config.txt file in the same folder where the python file is and add followinf content
  * content
  <br>
  `address=Miguel Teles junior 129
   openweather-key=84ee24bcd5d71c885e690337672bb521
   covidkey=man1BvYsT+OAcPyjyhslmw==DreLZ2M4XiHtwnn7
   urlcovid=https://api.api-ninjas.com/v1/covid19?country=
   country=brazil
   latlong-email=marcel.ghisi@gmail.com
   latlong-password=M6a6r2c9\
  `
* variable description
  * address -  Is the address to get the weather information
  * openweather-key - Is the key to connect in open weather api to get the temperature
  * covidkey - is the key registered in ninja api
  * urlcovid - is the the url for covid api
  * country is the country you want to listen
  * latlong-email - is the latlong website email to login
  * latlong-password is the latlong website to login
from urllib.request import urlopen,Request
import json
import requests
from datetime import date


# selenium 4
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument("--headless")
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version='114.0.5735.90').install()))

#_id = '315202'  # id for Eskisehir
key = '84ee24bcd5d71c885e690337672bb521'   # api key
#url = 'https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}' + '&APPID=' + key   # full url

covidkey="man1BvYsT+OAcPyjyhslmw==DreLZ2M4XiHtwnn7"
urlcovid="https://api.api-ninjas.com/v1/covid19?country=switzerland"
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def send_simple_message(report,config):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox4d158f26b1034881b3f51f1c047fc9c4.mailgun.org/messages",
		auth=("api", config['mailgun-key'].strip()),
		data={"from": "Mailgun Sandbox <postmaster@sandbox4d158f26b1034881b3f51f1c047fc9c4.mailgun.org>",
			"to": "Marcel Ghisi <marcel.ghisi@elu.nl>",
			"subject": "Daily News",
			"text": report})

def fill_form2():
    URL = "https://online.transport.wa.gov.au/webExternal/registration/?0"

    rego = "01527010"

    PARAMS = {'endereco': rego}

    response = requests.get(url=URL, params=PARAMS)

    results = requests.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

    # print(response.headers)
    json = results.json
    print(results.json)
    print(results.content)
    print(results.text)
    print(results.headers)
    body = results.body
    print(results.body)

def create_report(temperature,country,total,new):
    email_body = (f"Today in your country {country} the temperature is {temperature}"
                  f" the total victims of covid19 is {total} and the new cases in your country is {new}"
                  f"")
    return email_body

def get_lat_long(city,config):
    from selenium.webdriver import Firefox
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.binary_location = "/usr/bin/firefox"
    options.add_argument("--headless")
    browser = Firefox(options=options)
    browser.get("https://www.latlong.net/user/login")
    email = browser.find_elements(By.ID, 'email')
    password = browser.find_elements(By.ID, 'password1')
    email[0].send_keys(config['latlong-email'].strip())
    password[0].send_keys(config['latlong-password'].strip())
    login = browser.find_elements(By.CLASS_NAME, 'button')
    login[0].click()
    #current_url = browser.current_url
    browser.get('https://www.latlong.net/convert-address-to-lat-long.html')
    browser.implicitly_wait(10)
    search_form = browser.find_elements(By.TAG_NAME,'form')[0]
    input_text_fname = browser.find_element(By.TAG_NAME, 'input')

    # Enter a value in the input text field
    input_text_fname.send_keys(city)
    #search_form[0].send_keys(city)
    search_form.submit()
    browser.implicitly_wait(20)
    lat = browser.find_elements(By.ID,'lat')
    long = browser.find_elements(By.ID, 'lng')
    latlng = browser.find_elements(By.ID, 'latlngspan')
    print(lat)
    print(long)
    print(latlng[0].text)
    print(latlng[0].text[1: -1])
    print(latlng[0].text[1: -1].split(","))
    result = tuple(latlng[0].text[1: -1].split(","))
    return result

def get_covid_day_data(content,date):
    day = content[0]['cases'][date]
    return day

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('My Covid Weather Report')
    myvars = {}
    with open("config.txt") as myfile:
        for line in myfile:
            name, var = line.partition("=")[::2]
            myvars[name.strip()] = var

    tup = tuple(get_lat_long(myvars["address"].strip(),myvars))
    latitude = tup[0]
    longitude = tup[1]
    response = urlopen(f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude.strip()}&lon={longitude.strip()}&APPID={myvars['openweather-key'].strip()}").read().decode('utf-8')
    obj = json.loads(response)
    req = Request(myvars['urlcovid'].strip()+myvars['country'].strip())
    req.add_header('X-Api-Key', myvars['covidkey'].strip())
    content = urlopen(req).read()
    obj2 = json.loads(content)
    print(obj)
    print(content)

    today = date.today()
    d4 = today.strftime("%Y-%m-%d")
    d4 = d4.replace("2023","2022")
    day = get_covid_day_data(obj2,d4)

    report = create_report(obj["current"]["temp"],obj2[0]["country"],day["total"],day["new"])
    send_simple_message(report,myvars)




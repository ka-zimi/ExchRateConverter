import requests
"""Api to pull exchange rate from NBP"""

print("Exchange Rate Converter")

givenDate = input("Give date in format: RRRR-MM-DD: ")
currency = input("Give currency (EUR,PLN,USD...): ")

if givenDate == '':
    print("Error. Please give date!")
if currency == '':
    print("Error. Please give currency code!")

# response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/c/{currency}/{givenDate}/?format=json") //kurs kupna i sprzedaży
response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{givenDate}/").json()

print(f"Currency: {response['currency']}")
print(f"Date: {response['rates'][0]['effectiveDate']}")
print(f"Exchange rate: {response['rates'][0]['mid']}")



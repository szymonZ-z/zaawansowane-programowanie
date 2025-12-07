import requests


class Brewery:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return (
            f"Nazwa: {getattr(self, 'name', 'brak')}\n"
            f"Typ: {getattr(self, 'brewery_type', 'brak')}\n"
            f"Kraj: {getattr(self, 'country', 'brak')}\n"
            f"Miasto: {getattr(self, 'city', 'brak')}\n"
            f"Strona internetowa: {getattr(self, 'website_url', 'brak')}\n"
        )


breweries_json = requests.get("https://api.openbrewerydb.org/v1/breweries?per_page=20").json()
breweries_list = []
for brewerie in breweries_json:
    breweries_list.append(Brewery(**brewerie))

for b in breweries_list:
    print(b)

# Chapter 11: Try It Yourself: 11-01. City, Country, Function

def get_city_country(city, country, population=None):
    """A function that displays a City and its Country."""
    if population is None:
        city_country = f"{city}, {country}"
        return city_country.title()
    else:
        city_country = f"{city}, {country} (Population: {int(population)})"
        return city_country.title()

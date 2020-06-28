def city_formatter(city, country, population=""):
    if population:
        city_output = f"{city}, {country} - Population: {population}"
    else:
        city_output = f"{city}, {country}"
    return city_output.title()
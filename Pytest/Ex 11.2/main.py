def format_address(city, country, population = None):
    """Return a neatly formatted address."""
    if population:
        address = f'{city}, {country} - Population: {population}'
    else:
        address = f'{city}, {country}'
    return address.title()

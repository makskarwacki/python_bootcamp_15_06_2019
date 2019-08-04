import weather

locations = ['warsaw', 'berlin', 'london']

for l in locations:
    id_ = weather.get_location_id(l)
    w = weather.get_location_weather(id_)
    weather.print_weather(w)

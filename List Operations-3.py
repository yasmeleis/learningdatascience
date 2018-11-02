## 2. Parsing the File ##

weather_data = []
f = open("la_weather.csv", 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    x = row.split(",")
    weather_data.append(x)



## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []
for row in weather_data:
    value = row[1]
    weather.append(value)
print(weather) 


## 4. Counting the Items in a List ##

count = 0
for element in weather:
    count = count + 1

## 5. Removing the Header ##

new_weather = weather[1:len(weather)]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for item in weather_types:
    found = item in new_weather
    weather_type_found.append(found)
print(weather_type_found)
    
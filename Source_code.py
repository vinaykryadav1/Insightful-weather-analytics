import requests
import pandas as pd

API_KEY = "3d9ea443ca9c2c9c95a6fba752fca9f4"
cities = ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore',
    'Hyderabad', 'Ahmedabad', 'Pune', 'Jaipur', 'Lucknow',
    'Kanpur', 'Nagpur', 'Indore', 'Bhopal', 'Patna',
    'Ludhiana', 'Agra', 'Varanasi', 'Surat', 'Rajkot',
    'Amritsar', 'Ranchi', 'Guwahati', 'Chandigarh', 'Mysore',
    'Thiruvananthapuram', 'Coimbatore', 'Vishakhapatnam', 'Vadodara', 'Madurai']

weather_data = []

for CITY in cities:
    weather_endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(weather_endpoint)
    response.raise_for_status()
    data = response.json()

    weather_data.append({
        'City': CITY,
        'Latitude':data['coord']['lat'],
        'Longitude':data['coord']['lon'],
        'Temperature': data['main']['temp'],
        'Humidity(%)': data['main']['humidity'],
        'Weather': data['weather'][0]['description'],
        'Sunrise':pd.to_datetime(data['sys']['sunrise'], errors="coerce",unit='s').strftime('%I:%M:%S %p'),
        'Sunset':pd.to_datetime(data['sys']['sunset'], errors="coerce",unit='s').strftime('%I:%M:%S %p'),
        'Sea_level':data['main']['sea_level'],
        'Ground_level':data['main']['grnd_level'],
        'Wind_speed(mph)':data['wind']['speed'],
        'Visibility(m)' : data['visibility']

    })

df = pd.DataFrame(weather_data) 
print(df)



# print(df.sort_values(by='Temperature', ascending=False).head(3))
# print("--------------------------------------------------------------------------------------------------------------------------------------------")
# print(df.sort_values(by='Humidity(%)', ascending=False).head(1))

# import matplotlib.pyplot as plt
# plt.figure(figsize=(10,5))
# plt.bar(df['City'], df['Temperature'], color='orange')
# plt.title('City vs Temperature')
# plt.xlabel('City')
# plt.ylabel('Temperature (°C)')
# plt.show()

# # plt.figure(figsize=(10,5))
# # plt.bar(df['City'], df['Humidity(%)'], color='blue')
# # plt.title('City vs Humidity')
# # plt.xlabel('City')
# # plt.ylabel('Humidity (%)')
# # plt.show()

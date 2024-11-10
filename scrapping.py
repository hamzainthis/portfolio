import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the target page (replace query for specific car parts)
URL = "https://www.avito.ma/fr/maroc/pi%C3%A8ces_et_accessoires_pour_v%C3%A9hicules"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

# Send the GET request to the website
response = requests.get(URL, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract relevant information from the listings
    car_parts = []
    for listing in soup.find_all("div", class_="sc-1nre5ec-3"):
        title = listing.find("h2", class_="sc-1nre5ec-11").text.strip() if listing.find("h2", class_="sc-1nre5ec-11") else "N/A"
        price = listing.find("span", class_="sc-1nre5ec-13").text.strip() if listing.find("span", class_="sc-1nre5ec-13") else "N/A"
        location = listing.find("span", class_="sc-1nre5ec-15").text.strip() if listing.find("span", class_="sc-1nre5ec-15") else "N/A"
        link = "https://www.avito.ma" + listing.find("a", href=True)["href"] if listing.find("a", href=True) else "N/A"

        car_parts.append({
            "Title": title,
            "Price": price,
            "Location": location,
            "Link": link
        })

    # Save the data into a DataFrame for better visualization
    df = pd.DataFrame(car_parts)

    # Display the DataFrame to the user
    print(df)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

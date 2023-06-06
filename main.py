import requests
from bs4 import BeautifulSoup

url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the main div containing the postings
main_div = soup.find("div", class_="row")

# Find all the postings within the main div
postings = main_div.find_all("div", class_="col-sm-12")

# Initialize a list to store the postings
result = []

# Iterate over the postings
for posting in postings:
    # Find the fields within each posting
    est_value_notes = posting.find("div", class_="listing-est-value").text.strip()
    description = posting.find("div", class_="listing-description").text.strip()
    closing_date = posting.find("div", class_="listing-closing-date").text.strip()

    # Append the posting to the result list
    result.append({
        "Est. Value Notes": est_value_notes,
        "Description": description,
        "Closing Date": closing_date
    })

    # Break the loop if we have retrieved 5 postings
    if len(result) == 5:
        break

# Print the list of postings
for posting in result:
    print(posting)


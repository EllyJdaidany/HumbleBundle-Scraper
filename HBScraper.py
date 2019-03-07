import requests
from bs4 import BeautifulSoup

url = input("Enter a Humble Bundle URL ")
print(url)
req = requests.get(url)
tierDict = {}

if req.status_code == 200:
    print("Successful!")

    reqContent = BeautifulSoup(req.text, 'html.parser')

    tiers = reqContent.select(".dd-game-row")

    for tier in tiers:
        # For sections that have a headline
        if tier.select(".dd-header-headline"):
            # Grab tier name and price
            tierName = tier.select(".dd-header-headline")[0].text.strip()
            # Grab tier product names
            tierProducts = tier.select(".dd-image-box-caption")
            # Strip HTML and whitespace off
            tierProducts = [products.text.strip() for products in tierProducts]

            # Add the data to the dictionary
            tierDict[tierName] = {
                "products": tierProducts,
            }

    # prices = [name.split()[1] for name in tierProducts if name.startswith("Pay")]

    for tierName,tierInfo in tierDict.items():
        print("Tier:", tierName, "\n")
        print("Products listed: \n")
        print("\n".join(tierInfo['products']))
        print("\n")
else :
    print("Didn't go through")

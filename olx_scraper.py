import requests
from bs4 import BeautifulSoup

def fetch_olx_car_covers():
    url = "https://www.olx.in/items/q-car-cover"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve OLX page")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("li", {"data-aut-id": "itemBox"})
    
    with open("olx_car_covers.txt", "w", encoding="utf-8") as file:
        for item in items:
            title = item.find("span", {"data-aut-id": "itemTitle"})
            price = item.find("span", {"data-aut-id": "itemPrice"})
            link_tag = item.find("a", href=True)
            
            if title and price and link_tag:
                file.write(f"Title: {title.text.strip()}\n")
                file.write(f"Price: {price.text.strip()}\n")
                file.write(f"Link: https://www.olx.in{link_tag['href']}\n")
                file.write("-" * 40 + "\n")
    
    print("Results saved to olx_car_covers.txt")

if __name__ == "__main__":
    fetch_olx_car_covers()

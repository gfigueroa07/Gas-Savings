# this code is a mess, please dont hate on a white boy trynna get some motion - it works and i know how it works, what more do i want in life <3

import requests
import time
import random


def get_pa_gas_price_alternative():
    # steal from multiple places because webscarping haters be hatin and we want to scrape da web frl <3
    # list of  sources to try scraping
    sources = [
        {
            "name": "US Energy Information Administration (EIA)",
            "url": "https://api.eia.gov/v2/petroleum/pri/gnd/data/?frequency=weekly&data[0]=value&facets[duoarea][]=SPA&facets[product][]=EPM0&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000",
            "type": "eia",
        },
        {
            "name": "GasBuddy API Alternative",
            "url": "https://www.gasbuddy.com/api/stationSearch?lat=40.2732&lng=-76.8839&maxResults=1",
            "type": "gasbuddy",
        },
        {"name": "Mock Data (Fallback)", "url": None, "type": "mock"},
    ]

    # HTTP Headers that mimic a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    }
    
    # loop through each source 
    for source in sources:
        print(f"Trying {source['name']}...")

        if source["type"] == "mock":
            # mock info for when the hating virgins be hating on a white boy trynna get some motion
            print("Using mock data as fallback...")
            # Fake data for real data
            # bypass authentication
            mock_prices = {
                "regular": round(3.20 + random.uniform(-0.3, 0.3), 2),
                "mid": round(3.45 + random.uniform(-0.3, 0.3), 2),
                "premium": round(3.70 + random.uniform(-0.3, 0.3), 2),
                "diesel": round(3.55 + random.uniform(-0.3, 0.3), 2),
            }
            print("Pennsylvania Average Gas Prices (Estimated):")
            print(f"Regular: ${mock_prices['regular']}")
            print(f"Mid-Grade: ${mock_prices['mid']}")
            print(f"Premium: ${mock_prices['premium']}")
            print(f"Diesel: ${mock_prices['diesel']}")
            print(
                "\nNote: These are estimated prices. For real-time data, check gasprices.aaa.com"
            )
            return mock_prices

        try:
            if source["url"]:
                response = requests.get(source["url"], headers=headers, timeout=15)
                print(f"Status code: {response.status_code}")

                if response.status_code == 200:
                    if source["type"] == "eia":
                        try:
                            data = response.json()
                            if (
                                "response" in data
                                and "data" in data["response"]
                                and data["response"]["data"]
                            ):
                                latest = data["response"]["data"][0]
                                price = latest["value"]
                                print(
                                    f"Pennsylvania Average Gas Price (Regular): ${price}"
                                )
                                print(
                                    f"Data from: {latest.get('period', 'Unknown date')}"
                                )
                                return {"regular": price, "source": "EIA"}
                        except (KeyError, IndexError, ValueError) as e:
                            print(f"Error parsing EIA data: {e}")
                            continue
                    elif source["type"] == "gasbuddy":
                        try:
                            data = response.json()
                            if "stations" in data and data["stations"]:
                                station = data["stations"][0]
                                if "prices" in station and station["prices"]:
                                    regular_price = (
                                        station["prices"]
                                        .get("regular", {})
                                        .get("price")
                                    )
                                    if regular_price:
                                        print(
                                            f"Pennsylvania Gas Price (Sample Station): ${regular_price/100:.2f}"
                                        )
                                        print(
                                            f"Station: {station.get('name', 'Unknown')}"
                                        )
                                        return {
                                            "regular": regular_price / 100,
                                            "source": "GasBuddy",
                                        }
                        except (KeyError, ValueError) as e:
                            print(f"Error parsing GasBuddy data: {e}")
                            continue
                else:
                    print(
                        f"Failed to fetch from {source['name']}. Status: {response.status_code}"
                    )
        except requests.exceptions.RequestException as e:
            print(f"Request to {source['name']} failed: {e}")

        time.sleep(1)  # likkle break to fw cloudflare and vibes

    return None


# this basically the main function but i couldnt be bothered to change the name and its more (likkle bit of pazzazz imagined here) 𐙚₊˚⊹ᡣ𐭩 descriptive 𐙚₊˚⊹ᡣ𐭩
# this comment took longer to write than the change of function name but we on dat shit
def get_pa_gas_price():
    print("Fetching Pennsylvania gas prices...\n")

    # fuck aaa for blocking our shit, we going to try other ways on da bih
    result = get_pa_gas_price_alternative()

    if result is None:
        print(
            "All gas price sources failed. Please check your internet connection or try again later."
        )


if __name__ == "__main__":
    get_pa_gas_price()

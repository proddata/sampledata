import json
import random

random.seed(42)

N = 1000  # Number of entries
sources = ["Google Ads", "Facebook Ads", "Twitter Promotions", "LinkedIn Ads", "Email Campaign"]
landing_base_urls = [
    "https://example.com/products",
    "https://example.com/services",
    "https://example.com/blog",
    "https://example.com/about",
    "https://example.com/contact"
]

campaign_types = ["summer_sale", "winter_sale", "new_year_discount", "black_friday", "clearance"]

data = []

def generate_utm_source(source):
    if source == "Google Ads":
        return "google"
    elif source == "Facebook Ads":
        return "facebook"
    elif source == "Twitter Promotions":
        return "twitter"
    elif source == "LinkedIn Ads":
        return "linkedin"
    elif source == "Email Campaign":
        return "email"
    else:
        return "other"

for i in range(N):
    campaign_id = f"c{1000+i}"  # Start from c1000 to ensure unique IDs
    source = random.choice(sources)
    clicks = random.randint(50, 1000)
    impressions = clicks * random.randint(10, 20)
    conversion_rate = round(clicks / impressions, 4)

    # Create more diverse landing page URLs
    landing_base = random.choice(landing_base_urls)
    utm_campaign = random.choice(campaign_types)
    utm_medium = "cpc" if source in ["Google Ads", "Facebook Ads", "Twitter Promotions", "LinkedIn Ads"] else "email"
    landing_page_url = f"{landing_base}?utm_source={generate_utm_source(source)}&utm_campaign={utm_campaign}&utm_medium={utm_medium}"

    campaign_data = {
        "campaign_id": campaign_id,
        "source": source,
        "metrics": {
            "clicks": clicks,
            "impressions": impressions,
            "conversion_rate": conversion_rate
        },
        "landing_page_url": landing_page_url
    }

    data.append(campaign_data)

# Write to marketing.json as newline-delimited JSON
with open('marketing.json', 'w') as f:
    for entry in data:
        f.write(json.dumps(entry))
        f.write('\n')

print("Enhanced marketing data written to marketing.json")

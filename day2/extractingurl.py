import re

# List of URLs
urls = [
    'https://google.com/search?q=URls&oq=URls&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg8MgYIAhBFGDwyBggDEEUYPDIGCAQQRRhBMgYIBRAuGEDSAQgzNzAzajBqMagCALACAA&sourceid=chrome&ie=UTF-8',
    'https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL#:~:text=A%20URL%20(Uniform%20Resource%20Locator,%2C%20images%2C%20and%20so%20on.',
    'https://en.wikipedia.org/wiki/URL',
    'https://www.techtarget.com/searchnetworking/definition/URL',
    'https://www.hostinger.com/tutorials/what-is-a-url',
    'https://www.geeksforgeeks.org/what-is-url-uniform-resource-locator/',
    '',
    'https://www.twitch.tv/twitch/videos',
    'https://help.twitch.tv/s/article/video-on-demand',
    'https://www.tripadvisor.com/Hotels-g315763-Nagarkot_Bagmati_Zone_Central_Region-Hotels.html',
    'https://www.makemytrip.com/hotels-international/nepal/nagarkot_central-hotels/1-1-2024',
    'https://www.amazon.co.uk/Inmate-Sunday-Bestselling-Author-Housemaid/dp/1464221383/?_encoding=UTF8&ref_=pd_hp_d_btf_exports_top_sellers_unrec_uk',
    'https://basketnews.com/news-218623-lamelo-ball-goes-down-with-ankle-injury-against-lakers.html',
    'http://www.examplesite.com////international',
    'http-www-pearlsrainbow-com.html?checkin=2025-01-21&checkout=2025-01-22',
    'https://2900battery.com/cities/vehicle-batteries-car-or-truck?crit=1027028&gad_source=1',
    '',
    'http://consumerrating.org/internet-providers/best/?utm_source=google&utm_medium=cpc&utm_id=20145745910&utm_content=147838076823&utm_term=internet near ','me&creativeId=658799161679&adgroupid=147838076823&targetid=kwd-296561260971&gad_source=1',
    'http://das.somesite.com:5050/clasical-codes',
    'https://das.somesite.com:5050/clasical-codes',
    'das.somesite.com:5050/clasical-codes',
    ]

# Domain to match
target_domain = "https://google.com"

# Regex pattern to extract the domain name
# pattern = r'^(?:https?://)?(?:www\.)?([^/]+)'
# pattern = r'^((https?|ftp):\/\/([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(\/[^\s]*)?$)'
pattern = r'^((https|ftp)?:\/\/([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})'

# Extract and filter URLs that match the target domain
filtered_urls = []

for i in urls:
    match = re.match(pattern, i)
    if match:
        # print(match)
        domain = match.group(1)  # Extract the domain from the match
        # print(f"Domain:{domain}")
        if domain == target_domain:
            # print(i)
            filtered_urls.append(i)
            
        

# # Print the filtered URLs
for i in filtered_urls:
    print(i)
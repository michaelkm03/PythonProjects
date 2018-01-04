import requests

with requests.Session() as s:
    url = 'https://hub.victorious.com/'
    s.get(url)
    login_data = {
        "email":"michaelkm03@getvictorious.com",
        "password":"abc123456",
    }
    s.post(url,data=login_data)
    page = s.get(url)
    print page


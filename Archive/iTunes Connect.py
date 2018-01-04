import requests


payload = {
    'Username': 'ios-admin@getvictorious.com',
    'Password': '5H8fWxYm3OBxSv3xZ6X4ePVK'
}

url = 'https://itunesconnect.apple.com/itc/static/login?view=1&path=%2FWebObjects%2FiTunesConnect.woa%3F'

with requests.Session() as s:
    post = s.post(url, data=payload)
    # print post.text
    summary = requests.get("https://itunesconnect.apple.com/WebObjects/iTunesConnect.woa/ra/apps/manageyourapps/summary")
    print summary
import requests

# Define the URL
url = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios&lwv=100"

# Define headers
headers = {
    ":authority": "www.facebook.com",
    ":method": "POST",
    ":path": "/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios&lwv=100",
    ":scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    #"cookie": "datr=4CBhZ9ERdd4S0-rGq-Jqmr16; sb=4CBhZ-2yWPlf-pkzwtrUZhzH; locale=en_GB; vpd=v1%3B576x306x3.9869794845581055; dpr=4.3914713859558105; ps_l=1; ps_n=1; usida=eyJ2ZXIiOjEsImlkIjoiQXNvbW8weWFoNjB1aiIsInRpbWUiOjE3MzQ0MjEzMzh9; fr=0nPC3F6IkBHIjq8Ve..BnYSDg..AAA.0.0.BnYStZ.AWUV5EqrdjQ; wd=669x1260",
    "dpr": "3",
    "origin": "https://www.facebook.com",
    "referer": "https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDIxMzMzLCJjYWxsc2l0ZV9pZCI6MjM5NDQ2MTI0MDg0ODgxN30%3D&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
    "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-ch-ua-platform-version": "\"\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "viewport-width": "980"
}

# Define POST data
data = {
    "jazoest": "21073",
    "lsd": "AVpwpE7qkxs",
    "display": "",
    "isprivate": "",
    "return_session": "",
    "skip_api_login": "",
    "signed_next": "",
    "trynum": "1",
    "timezone": "-360",
    "lgndim": "eyJ3Ijo0MDcsImgiOjkwNCwiYXciOjQwNywiYWgiOjkwNCwiYyI6MjR9",
    "lgnrnd": "234217_aJEU",
    "lgnjs": "1734421341",
    "email": "%2Bnikixd404@gmail.com",
    "prefill_contact_point": "%2Bnikixd404@gmail.com",
    "prefill_source": "browser_dropdown",
    "prefill_type": "contact_point",
    "first_prefill_source": "browser_dropdown",
    "first_prefill_type": "contact_point",
    "had_cp_prefilled": "true",
    "had_password_prefilled": "false",
    "ab_test_data": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAU",
    "encpass": "%23PWD_BROWSER%3A5%3A1734421376%3AAU9QAOz6TLGdXxM5tcnJXPBNMcaZCU1cf%2FJfaw5pdS8xqvI6sxMaPy8GgdygReLrFIdFReROMjDfLgmImhoTZq8lOn6AarrtivZpo04uPji3vEGKVpu8iY048xjMWwq9Jjz%2FPscKAwnGN8bF%2FA%3D%3D"
}

# Send the POST request
response = requests.post(url, headers=headers, data=data)

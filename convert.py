import re

def shortlink(url):
    pattern = (
        r'bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|'
        r'cli\.gs|yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|'
        r'twurl\.nl|snipurl\.com|short\.to|budurl\.com|ping\.fm|post\.ly|'
        r'just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|doiop\.com|'
        r'short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|'
        r'lnkd\.in|db\.tt|qr\.ae|adf\.ly|bitly\.com|cur\.lv|tinyurl\.com|'
        r'ity\.im|q\.gs|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|'
        r'buzurl\.com|cutt\.us|yourls\.org|prettylinkpro\.com|scrnch\.me|'
        r'vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|link\.zip\.net'
    )

    if re.search(pattern, url, re.IGNORECASE):
        return -1
    return 1

def convertion(url, prediction):
    """
    Always returns:
    [url, status, button_text, is_safe]
    """
    # Defaults (unsafe)
    status = "Not Safe"
    button = "Still want to Continue"
    is_safe = False

    # Shortened URLs are always unsafe
    if shortlink(url) == -1:
        return [url, status, button, is_safe]

    # ML model says safe
    if prediction == 1:
        status = "Safe"
        button = "Continue"
        is_safe = True

    return [url, status, button, is_safe]
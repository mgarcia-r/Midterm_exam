def valid_url(url):
    """
    A function that checks if the passed parameter is a valid URL or not. A valid url begins with "https://" and has no spaces
    :param url: the url to check
    :return: true/false
    """
    if url[:8]!="https://":
        return False
    if " " in url:
        return False
    return True

print(valid_url("https://www.thispersondoesnotexist.com"))


def domain_name(url):
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("www.", "")
    return url.split(".")[0]


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"

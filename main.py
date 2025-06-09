import httpx

text = input()

url = "https://sangtacviet.com/index.php?langhint=chinese"
data = {
    "ajax": "trans"
}
data["content"] = text
headers = {
    "Host": "sangtacviet.com",
    "Origin": "https://sangtacviet.com",
    "Referer": "https://sangtacviet.com/trans/"
}
response = httpx.post(url, headers=headers, data=data)
print(response.text)

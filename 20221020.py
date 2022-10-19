from requests import get


def do_show_good_list(input_dict):
    output_text = "{"
    row_index = 0
    for key, value in input_dict.items():
        # 'IF' For remove the Last Comma
        if row_index == len(input_dict)-1:
            output_text += f"\n\t'{key}' : '{value}'"
        else:
            output_text += f"\n\t'{key}' : '{value}',"
            row_index += 1
    output_text += "\n}"
    print(output_text)


websites = {
    "google.com",
    "naver.com",
    "daum.net",
    "kakao.com"
}

result = {}
for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code == 200:
        # print(f"{website} is OK")
        result[website] = "GOOD"
    else:
        # print(f"{website} is Not OK")
        result[website] = "BAD"

print(result)
do_show_good_list(result)

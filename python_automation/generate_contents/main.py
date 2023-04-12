# https://saasis.jp/2023/03/06/%E9%81%82%E3%81%AB%E5%85%AC%E9%96%8B%E3%81%95%E3%82%8C%E3%81%9Fchatgpt-api%E3%81%A8%E3%81%AF%EF%BC%9F-%E5%88%A9%E7%94%A8%E3%81%99%E3%82%8B%E3%81%BE%E3%81%A7%E3%81%AE%E6%B5%81%E3%82%8C%E3%80%90/

import openai

openai.api_key = "YOUR_API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "質問内容をここに書きます"},
    ]
)
print(response["choices"][0]["message"]["content"])

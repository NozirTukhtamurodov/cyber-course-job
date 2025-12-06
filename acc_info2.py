import requests

# Ваши данные
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImVmZDlkNzFjMTllOWQ5MWZkMTkzODE3MzNkZGI0NzZhMzE3NDZkYWIxZGQyYWRhNjYxZmY4NmRkZjc4MGJjMzE2ZWY1MDUyYzFhZjk1NGYyIn0.eyJhdWQiOiIyZmFjMGFhYy03YmNiLTQ0NGMtOTdkYi1iZTM3Y2IzMGI2NGEiLCJqdGkiOiJlZmQ5ZDcxYzE5ZTlkOTFmZDE5MzgxNzMzZGRiNDc2YTMxNzQ2ZGFiMWRkMmFkYTY2MWZmODZkZGY3ODBiYzMxNmVmNTA1MmMxYWY5NTRmMiIsImlhdCI6MTcyNDEzOTYyMiwibmJmIjoxNzI0MTM5NjIyLCJleHAiOjE3MjQyMjYwMjIsInN1YiI6IjExMzg0NDY2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMxODk1OTg2LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJwdXNoX25vdGlmaWNhdGlvbnMiLCJmaWxlcyIsImNybSIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiZWQ1MDM2MWUtNGM2Yi00N2I4LTk3ZGYtYzI2YjQ1YTJiODkyIn0.QnEDuRupaGlmrmaaS9gZZsjKqQl6ZoO1kTsV6XvI5r4cacZiO_VIER2ZtmZUlCIuQ-xVKOWqkKE7quQBLgEkWW8DHekB5hgfTfc2mjJmIPWx_-bKwsNziUtwZ5r1LHgQhlqkdQr4Nz1uNYKTVxu_9FOsKOlQG3-TZJDG8VG1BP2IollbMzVvXeyjeOHCN674OFwqsVzo8Hocj4awwNyV6Sn_otP4kMslyDsy1FsLdMXddXMYe-CsZmrn23nF4H3J4NMmAmUhFlev32rbl_l6Y7SrQI0_ClF7hYGJv4oypOx9UaV66HCEfub-qp9pPi_odb015js3RLO4MR0wWg-xYA'  # Замените на полученный access_token
refresh_token = 'def502003eaa04f52105edfd33bcad445f13ec53bcbd6f212ee89f621de962a7dc79a806ad87165475748d59ef6ab529f7e887a4f7f1b2aa46c2b8b8bca125597953f1015cfd2925e74f1f4f63e6daa033079fb5d3ffc23682cff43c1fe7a9a5ecf8fa371b3af8b07725f00f567b4f1ed9f7ef66aec3a526d9c7cbd9fdd53a011342dfb380e3257229b8e679061b859d56f8a4d289a385fd680d4022655b79f20e203991b7bac262850f85c00cd6b935d26db2facc77da7914e15eddc84a4fc62bbb1048da2f71b1d11d1e094394cd563604905241900c4d74d0fee2b811438a5ca1f21b3f7871b6f5f1a41022a96f9e26636b76486f1562cc6ba5c92966fcf5256cf7c1d851e371d8aa49f1027dd30e59e9f33de4163ef9a355f225cd986024c7f88ff59e894132d0103f31c3f8836ad08298f51d7a40b45ff68d551539713945264e1c1d3c473a99b603e4b91e9a64d3719f9d1ad4c3801d8a5afe1381e8771b8dca46ca69a45636e1dfc898d8a4f9f4ffef41bd890e11020a1ada5816bd61a5133533dd209f6bcf0d497f0814e63e3a3b973b28a878c3afe8a97ddf1d804f431a7909ef3b073e76e3b4a75e0f3a66cb6f66ffde2f88abce9bf9183200257a88cf1f18d102e2583a852913a0d81c06fa286e9363626c3f09164c9bc7be6b3df264c7f809b89357a7252aeda113'  # Замените на полученный refresh_token
client_id = '2fac0aac-7bcb-444c-97db-be37cb30b64a'  # Ваш Client ID
client_secret = 'o36IxDPeW4MPP9Ohogg9OAAv63O7YHsY949nmV4hMDT5l5dYguUztZhjM57QjDL1'  # Ваш Client Secret
redirect_uri = 'https://ya.ru'  # Ваш Redirect URI
base_domain = 'https://dolyagood.amocrm.ru'  # Ваш поддомен


# Функция для выполнения авторизованного запроса с использованием access_token
def make_authorized_request():
    global access_token  # Делаем переменную глобальной
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    # Пример запроса к API AmoCRM для получения информации об аккаунте
    account_url = f'{base_domain}/api/v4/account?with=amojo_id'

    response = requests.get(account_url, headers=headers)

    if response.status_code == 200:
        account_info = response.json()
        print(account_info)  # Логируем данные аккаунта
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")
        # Если access_token истек, нужно обновить его
        if response.status_code == 401:  # Unauthorized
            refresh_access_token()


# Функция для обновления access_token с использованием refresh_token
def refresh_access_token():
    global access_token, refresh_token  # Делаем переменные глобальными

    url = f'{base_domain}/oauth2/access_token'

    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'redirect_uri': redirect_uri
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        tokens = response.json()

        # Обновляем глобальные переменные access_token и refresh_token
        access_token = tokens['access_token']  # Обновляем глобальные переменные
        refresh_token = tokens['refresh_token']  # Обновляем refresh_token

        print(f"Новый Access Token: {access_token}")
        print(f"Новый Refresh Token: {refresh_token}")

        # Повторяем запрос с новым токеном
        make_authorized_request()
    else:
        print(f"Ошибка обновления токена: {response.status_code}, {response.text}")


# Выполнение авторизованного запроса
make_authorized_request()
from curl_cffi import requests
# import requests
import json

proxy_file_path = "proxylist.txt"

proxy_list = []
with open(proxy_file_path, "r", encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        proxy_list.append(line.strip())

proxy_count = len(proxy_list)

username_file_path = "usernames.txt"

username_list = []
with open(username_file_path, "r", encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        username_list.append(line.strip())


index = 0
for username in username_list:
    while True:
        try:
            if index == proxy_count - 1:
                index = 0
            proxy_ip, port, proxy_username, password = proxy_list[index].split(':')
            
            _proxy = f'{proxy_ip}:{port}'
            # proxy = 'gate.smartproxy.com:15555'
            # username = 'FWD5N'
            # password = 'HI932LI5'

            proxies = {
                'http': f'http://{proxy_username}:{password}@{_proxy}',
                'https': f'http://{proxy_username}:{password}@{_proxy}'
            }
            # Define the URL
            url = "https://www.instagram.com/graphql/query"

            # Define the headers
            headers = {
                # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
                # "Accept": "*/*",
                # "Accept-Language": "en-US,en;q=0.5",
                # "Accept-Encoding": "gzip, deflate, br, zstd",
                # "Content-Type": "application/x-www-form-urlencoded",
                # "X-FB-Friendly-Name": "PolarisSearchBoxRefetchableQuery",
                # "X-BLOKS-VERSION-ID": "8bb50762167c4432c174a01a25b916bfc9b78985507f03558e2f04754cf7cb10",
                # "X-CSRFToken": "mymXzDNaFNw5B6n8Yy8K87yEkYTtEgB9",
                # "X-IG-App-ID": "936619743392459",
                # "X-FB-LSD": "eEy8045HV6Icgm84a_TFuL",
                # "X-ASBD-ID": "129477",
                # "Origin": "https://www.instagram.com",
                # "Connection": "keep-alive",
                # "Referer": "https://www.instagram.com/",
                # "Cookie": "csrftoken=mymXzDNaFNw5B6n8Yy8K87yEkYTtEgB9; mid=Zof2hAALAAE6CTrThbdiG1bow_2L; ig_did=61B10643-EB9D-45E8-905C-BB1253E23B59; datr=q_aHZh5ffA7C_sy2a72OlFXI; wd=925x955; rur=CLN\\05468468135009\\0541760018357:01f7e8f7c97f36f9c9feb0db5b0c9ce8651aaf7debf070d5ec6b7a18cccaa60ccaaae3b3; ds_user_id=68468135009; sessionid=68468135009^%^3ApCTJ5ThA2Z2LCb^%^3A29^%^3AAYcDGqzTLnAf7-ByRkY5akgEfHDYxVbCFygAh_Rbiw",
                # "Sec-Fetch-Dest": "empty",
                # "Sec-Fetch-Mode": "cors",
                # "Sec-Fetch-Site": "same-origin",
                # "TE": "trailers"
            }
            original_json = '{"data":{"context":"blended","include_reel":"true","query":"replace_username","search_surface":"web_top_search"},"hasQuery":true}'
            updated_json = original_json.replace("replace_username", username)
            # Define the POST data
            data = {
                # "av": "17841468610278516",
                # "__d": "www",
                # "__user": "0",
                # "__a": "1",
                # "__req": "2f",
                # "__hs": "20005.HYP:instagram_web_pkg.2.1..0.1",
                # "dpr": "1",
                # "__ccg": "MODERATE",
                # "__rev": "1017184369",
                # "__s": "4drkk6:jfgi1n:be5r5v",
                # "__hsi": "7423774303430149339",
                # "__dyn": "7xeUjG1mxu1syaxG4Vp41twpUnwgU7SbzEdF8aUco2qwJyEiw9-1DwUx60p-0LVE4W0om78c87m0yE462mcw5Mx62G5UswoEcE7O2l0Fwqo31w9a9wtUd8-U2exi4UaEW2G0AEco4i5o2eUlwhEe88o5i7U1mVEbUGdG1QwTU9UaQ0z8c86-3u2WE5B08-269wr86C1mwPwUQp1yUb9UK6V89FbxG1oCz8rwHwcOEy",
                # "__csr": "gH0Khyk_7gLf2JN94QAGk_pBGSB9ha8GuHqp4OblqlFq8RipuXiV_8_IGhqRlN12Lih9F9a9FCWKhYxEzLZF4UCqSvhL--mBFeUyS4fCAAh98-9iCy-nh6laAiayox7hFQFFDz94qheqich8B6AiC_GmqUK9V922pXx16y4eUgBw04SvUfEuwjQmubIwMVu1czo0COOovGEpg3I8VQ9-E2cBwhEgLxV0SwxpFkSazRo892jwjKlm0wo6S09-fDy81dUcz3940D83ewtFE1koO58au8indJwHCQ3S7oWewFBG8wlofC0s8hai2h1qfj9e5852AFQiIi687m2au2eeHyo4sMn4jF8xO2VYB0OIw2WbkWyra4KHYM6kEdC2W1szpU-l042yUqxN0uUG1iwnU2lwzg4Va4l7ME5WwOxm2608zwsohzF9HBwa5w6Cwa6083hk6UO0Do2Kyockbglw9Om3h0Qg0aPVk02kleEydQ1jxC0asye1Uw9OhwcShw47Aw29EdS7E34wf-585ui8U1r8",
                # "__comet_req": "7",
                # "fb_dtsg": "NAcPt0fFz3DBI3Bx42uz_gc3-SPb8jVy1cq5sz7to9ZQD872bCiiorQ:17853667720085245:1728482138",
                # "jazoest": "26142",
                # "lsd": "eEy8045HV6Icgm84a_TFuL",
                # "__spin_r": "1017184369",
                # "__spin_b": "trunk",
                # "__spin_t": "1728482149",
                # "fb_api_caller_class": "RelayModern",
                # "fb_api_req_friendly_name": "PolarisSearchBoxRefetchableQuery",
                "variables": updated_json,
                "server_timestamps": "true",
                "doc_id": "9153895011291216"
            }

            # Make the POST request
            response = requests.post(url, headers=headers, data=data, proxies=proxies)
            result = response.json()
            # Print the response


            users = result['data']['xdt_api__v1__fbsearch__topsearch_connection']['users']
            if len(users) != 0:
                user = users[0]['user']["full_name"]

                # pretty_json = json.dumps(users, indent=4)
                # Print the pretty JSON
                # print(pretty_json)
                print(user)
                with open("results.txt", "a", encoding='utf-8') as file:
                    file.write(user + "\n")
            else:
                with open("results.txt", "a", encoding='utf-8') as file:
                    file.write("invalid username" + "\n")
            index += 1
            break
        except:
            pass

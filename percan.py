from bs4 import BeautifulSoup as bs  # 크룰링
import urllib.request  # URL 연결
import pandas as pd  # 엑셀변환
import datetime  # 날짜 사용


# [CODE 1]
def Pericana_store(result):
    for page in range(1, 3):
        Pericana_url = 'https://pelicana.co.kr/store/stroe_search.html?page=%page&branch_name=&gu=&si='
        # print(Pericana_url)
        html = urllib.request.urlopen(Pericana_url)
        # print(html)
        soupPericana = bs(html, "html.parser")  # 파씽
        # print(soupPericana)
        tag_tbody = soupPericana.find("tbody")
        # print(tag_tbody)
        for store in tag_tbody.find_all("tr"):
            # if len(store) <= 9:  # 마지막 페이지 3이하 개선...
            #     break

            store_td = store.find_all("td")
            store_name = store_td[0].string
            # store_sido = store_td[0].string
            # 영업중
            # store_open = store_td[2].string
            store_address = store_td[1].string
            store_phone = store_td[2].string
            result.append([store_name] + [store_address] + [store_phone])
    return


# [CODE 0]
def main():
    result = []
    print('Pericana store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    Pericana_store(result)  # [CODE 1] 호출
    Pericana_tbl = pd.DataFrame(result, columns=('매장', '상세주소', '전화번호'))
    Pericana_tbl.to_csv('Pericana.csv', encoding='cp949', mode='w', index=True)  # cp949
    del result[:]


if __name__ == '__main__':
    main()

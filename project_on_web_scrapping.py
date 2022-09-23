from bs4 import BeautifulSoup
import requests

print('''
Resources     : Search by
News          : news
Billboard 100 : songs
Science       : science
Covid19 data  : covid

So what you wanna search''')
while True:
    print("Search")
    x = input()
    if x == 'news':
        print('''
    Source   : Search by
    BBC      : bbc
    NDTV     : ndtv
    Aljazera : alja''')
        while True:
            print("Source")
            y = input()
            if y == 'bbc':
                source = requests.get('https://www.bbc.com/news/world').text
                soup = BeautifulSoup(source, 'lxml')

                print()
                print("source : https://www.bbc.com/news/world")
                print("Latest Updates - BBC")
                print()
                print("Headlines")


                for article in soup.find_all('article'):
                    headline = article.h3.text
                    print(headline)
                    print()

            elif y == 'ndtv':
                source = requests.get('https://www.ndtv.com').text
                soup = BeautifulSoup(source, 'lxml')

                print("Source : https://www.ndtv.com")
                print("Top Stories - NDTV")
                print()
                print("Headlines")

                for li in soup.find_all('li'):
                    try:
                        li = li.h2
                        headline = li.find('a', class_="item-title")
                        headline = headline.text

                        link = li.find('a', class_="item-title")
                        link = link['href']

                    except Exception as e:
                        headline, link = e, e
                        if headline and link == e:
                            break
                    print(headline)
                    print("link for the story:", link)
                    print()

            elif y == "alja":
                source = requests.get('https://www.aljazeera.com/news/').text
                soup = BeautifulSoup(source, 'lxml')

                print()
                print("source : https://www.aljazeera.com/news/")
                print("News - aljazeera")
                print()
                print("Headlines")


                for article in soup.find_all('div', class_='col-sm-7 topics-sec-item-cont'):
                    headline = article.h2.text
                    summary = article.find('p', class_='topics-sec-item-p')
                    summary = summary.text

                    print(headline)
                    print(summary)

                    print()

            elif y == "exit":
                break

    elif x == "songs":
        source = requests.get('https://www.billboard.com/charts/hot-100', 'lxml').text
        soup = BeautifulSoup(source, 'lxml')
        print()
        print("source : https://www.billboard.com/charts/hot-100")
        print('BILLBOARD HOT 100')
        print()

        for li in soup.find_all('li', class_='chart-list__element display--flex'):
            num = li.button.span.span.text

            song = li.find('span', class_='chart-element__information')
            song_name = song.span.text

            song_artist = li.button.find('span',
                                         class_='chart-element__information__artist text--truncate color--secondary').text
            print(num, song_name)
            print(song_artist)
            print()

    elif x == 'science':
        source = requests.get('https://www.sciencefriday.com/topics/physics-chemistry/').text
        soup = BeautifulSoup(source, 'lxml')

        print()
        print("source : https://www.sciencefriday.com/topics/physics-chemistry/")
        print("SCIENCE FRIDAY")
        print()
        for article in soup.find_all('article'):
            sub_article = article.find('div', class_='cb-content col-twoThirds')
            news = sub_article.h2.text

            news_link = sub_article.h2.a['href']

            summary = article.find('div', class_='cb-desc').p.text
            print(news)
            print(summary)
            print(news_link)
            print()

    elif x == 'covid':
        source = requests.get('https://www.worldometers.info/coronavirus').text

        soup = BeautifulSoup(source, 'lxml')
        list1 = []
        for num in soup.find_all('div', class_='maincounter-number'):
            real_num = num.span.text
            list1.append(real_num)

        print()
        print()
        print()
        print("source: https://www.worldometers.info/coronavirus/")
        print("Covid19 Data-worldwide!")
        print()
        print("Coronavirus Cases:", list1[0])
        print("Deaths:", list1[1])
        print("Recovered:", list1[2])
        print()

        while True:
            try:
                print('Enter name of a country:')
                x = input()

                source = requests.get('https://www.worldometers.info/coronavirus/country/' + x).text
                soup = BeautifulSoup(source, 'lxml')
                list1 = []
                for num in soup.find_all('div', class_='maincounter-number'):
                    real_num = num.span.text
                    list1.append(real_num)

                print()
                print("source: https://www.worldometers.info/coronavirus/country/" + x)
                print("Covid19 Data-" + x + "!")
                print()
                print("Coronavirus Cases:", list1[0])
                print("Deaths:", list1[1])
                print("Recovered:", list1[2])
                print()
            except Exception as e:
                pass

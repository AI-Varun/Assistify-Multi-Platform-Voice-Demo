import time

import pyjokes
import pywhatkit
import speech_recognition as sr
from gtts import gTTS
import playsound
# pip install requests
import requests
import pyaudio
import os
import sys
from yahoo_fin import stock_info
import yfinance as yf
import wolframalpha
import translators as tr
import datetime
import wikipedia  #pip install wikipedia
import webbrowser
import bs4
from bs4 import BeautifulSoup
import wikipedia as googleScrap
from builtins import frozenset

# Coding Section

# Cryptocurrency API
crypto_api = 'https://api.coingecko.com/api/v3/simple/price?ids=Bitcoin%2CEthereum%2CTether%2CUSD%20Coin%2CBNB' \
             '%2CBinance%20USD%2CXRP%2CCardano%2CSolana%2CPolkadot%2CDogecoin%2CShiba%20Inu%2CLido%20Staked%20Ether' \
             '%2CPolygon%2CDai%2CAvalanche%2CTRON%2CWrapped%20Bitcoin%2CEthereum%20Classic%2CUniswap%2CLEO%20Token' \
             '%2CCosmos%20Hub%2CLitecoin%2COKB%2CNEAR%20Protocol%2CFTX%2CChainlink%2CCronos%2CMonero%2CStellar' \
             '%2CBitcoin%20Cash%2CTerra%20Luna%20Classic%2CAlgorand%2CFlow%2CVeChain%2CFilecoin%2CInternet%20Computer' \
             '%2CApeCoin%2CEOS%2CChain%2CHedera%2CTezos%2CFrax%2CDecentraland%2CThe%20Sandbox%2CQuant%2CAxie%20Infinity' \
             '%2CAave%2CLido%20DAO%2CTheta%20Network%2CElrond%2CChiliz%2CTrueUSD%2CBitcoin%20SV%2CcUSDC%2CPax%20Dollar' \
             '%2CKuCoin%2CeCash%2CThe%20Graph%2CHuobi%20BTC%2CBitTorrent%2CEvmos%2CIOTA%2CZcash%2CRavencoin%2CHuobi' \
             '%2CUSDD%2CSynthetix%20Network%2CTerra%2CNEO%2CFantom%2CKlaytn%2CcDAI%2CMaker%2CHelium%2CBitDAO%2CNeutrino' \
             '%20USD%2CRadix%2CGate%2COsmosis%2CCelsius%20Network%2CPancakeSwap%2CRocket%20Pool%2CcETH%2CTHORChain' \
             '%2CDeFiChain%2CPAX%20Gold%2CZilliqa%2CNEXO%2CArweave%2CEnjin%20Coin%2CBasic%20Attention%2CStacks%2CDash' \
             '%2CWaves%2CTokenize%20Xchange%2CAmp%2CKusama%2CFrax%20Share%2CBitcoin%20Gold%2CSTEPN%2CCurve%20DAO' \
             '%2CLoopring%2CTrust%20Wallet%2CGnosis%2CTenset%2CKava%2CTether%20Gold%2CNEM%2CTerraClassicUSD%2CDecred' \
             '%2CCelo%2CECOMI%2CMina%20Protocol%2C1inch%2CHolo%2CGala%2CCompound%2CEthereum%20Name%20Service%2CNexus' \
             '%20Mutual%2CGMX%2CTheta%20Fuel%2CConvex%20Finance%2CXDC%20Network%2CGolem%2CSynapse%2CQtum%2CJUNO%2CIOST' \
             '%2CcUSDT%2CKadena%2CSerum%2COasis%20Network%2CMaiar%20DEX%2CFlux%2Cyearn.finance%2CAnkr%2CConvex%20CRV' \
             '%2COKC%2COlympus%2CVoyager%20VGX%2CLivepeer%2CIoTeX%2CMarinade%20staked%20SOL%2CHarmony%2CGemini%20Dollar' \
             '%2CSafeMoon%20%5BOLD%5D%2COMG%20Network%2C0x%2COptimism%2CErgo%2CReserve%20Rights%2CBalancer%2CJUST' \
             '%2CSushi%2CLINK%2CAudius%2CEscoin%2CICON%2CSongbird%2CPolymath%2CWAX%2COntology%2CNuCypher%2CMoonbeam' \
             '%2CHive%2CSiacoin%2CMagic%20Internet%20Money%2CConstellation%2CMerit%20Circle%2CEuro%20Tether%2CSecret' \
             '%2CHorizen%2CImmutable%20X%2CdYdX%2CBaby%20Doge%20Coin%2CSXP%2CEnergy%20Web%2CSafeMoon%2CUMA%2CKyber' \
             '%20Network%20Crystal%2CDAO%20Maker%2CChia%2CWOO%20Network%2CCoinmetro%2CPlayDapp%2CCasper%20Network' \
             '%2CSwissBorg%2CSKALE%2CAlchemix%20USD%2CDigiByte%2CLiquity%20USD%2CCoin%20of%20the%20champions%2CRender' \
             '%2CMXC%2CCoinEx%2CAstar%2CPundi%20X%2CAPENFT%2CDogelon%20Mars%2CFunction%20X%2CLido%20Staked%20SOL' \
             '%2CSmooth%20Love%20Potion%2CLisk%2CLooksRare%2CVVS%20Finance%2CPocket%20Network%2CBone%20ShibaSwap' \
             '%2CMaple%2CCEEK%20Smart%20VR%2CKujira%2CInjective%2CSpell%2CREN%2CSSV%20Network%2CStatus%2CNervos' \
             '%20Network%2CBitkub%20Coin%2CProm%2CMetis%2CMVL%2CSyscoin%2CSTASIS%20EURO%2CRadio%20Caca%2CPLEX%2CCivic' \
             '%2CManifold%20Finance%2CNest%20Protocol%2CNano%2CKirobo%2CMedibloc%2CAcala%2CMy%20Neighbor%20Alice' \
             '%2CUltra%2COrbs%2CCOTI%2CConflux%2CArdor%2CAPI3%2CPlatonCoin%2CConstitutionDAO%2CPoollotto.finance' \
             '%2CNumeraire%2CUquid%20Coin%2CsETH2%2CWrapped%20Centrifuge%2CRadicle%2CTribe%2CMobox%2CUSDX%2CXYO' \
             '%20Network%2CDecimal%2CGalxe%2CCentrifuge%2CTitanSwap%2CWINkLink%2CBENQI%20Liquid%20Staked%20AVAX%2CCeler' \
             '%20Network%2CVelas%2Ce-Radix%2CChromia%2CBoba%20Network%2CBiswap%2CiExec%20RLC%2CReef%2CTelcoin%2CBancor' \
             '%20Network%2CRequest%2CMagic%2CRally%2CMX%2CEverscale%2CdKargo%2CPower%20Ledger%2CWazirX%2CflexUSD' \
             '%2CBiconomy%2CBTSE%20Token%2CDent%2CBlox%2CAurora%2CCoin98%2CMultichain%2CVulcan%20Forged%2CPirate' \
             '%20Chain%2CKeep%20Network%2CCartesi%2CSteem%2CAnkr%20Reward-Bearing%20Staked%20ETH%2CPhoenix%20Global' \
             '%2CRaydium%2CMiL.k%20Alliance%2CYield%20Guild%20Games%2COrigin%20Protocol%2CStargate%20Finance' \
             '%2CTempleDAO%2CCUBE%2CStratis%2CSeedify.fund%2CFei%20USD%2CDopex%2CLUKSO%2CIlluvium%2CSTP%20Network' \
             '%2CFloki%20Inu%2CinSure%20DeFi%2CVeThor%2CLoom%20Network%20(' \
             'OLD)%2CFUN%2CxSUSHI%2CKILT%20Protocol%2CShentu%2CHxro%2CAdshares%2CDejitaru%20Tsuka%2CSaitama%2CRibbon' \
             '%20Finance%2CStorj%2CHUSD%2CMetal%2CsUSD%2CTokamak%20Network%2CQuarkChain%2CArk%2CBeldex%2CBifrost' \
             '%2CRevain%2CBTC%20Standard%20Hashrate%20Token%2CPersistence%2CNerve%20Finance%2CEuro%20Coin%2COcean' \
             '%20Protocol%2CXido%20Finance%2CJOE%2CMaidSafeCoin%2CAragon%2CAlien%20Worlds%2COriginTrail%2CStormX' \
             '%2CrenBTC%2CLiquity%2CCreditcoin%2CBadger%20DAO%2CAergo%2CDock%2Caelf%2CFidu%2CShare%2CUFO%20Gaming' \
             '%2CVeritaseum%2CChainX%2CVenus%2CNKN%2CEveripedia%2CMeter%20Governance%2COrchid%20Protocol%2CDawn' \
             '%20Protocol%2CMoonriver%2CMask%20Network%2CMdex%2CAlchemy%20Pay%2CDoge%20Killer%2CMetadium%2CAscendEx' \
             '%2CStrike%2CConcordium%2CFetch.ai%2CAugur%2CHermez%20Network%2CDecentralized%20Social%2CVolt%20Inu' \
             '%2Choloride%2CSingularityNET%2CGains%20Farm%2CWorld%20Mobile%20Token%2CVerge%2CBarnBridge%2CXMON%2CRSK' \
             '%20Infrastructure%20Framework%2CXSGD%2CAkash%20Network%2CBytecoin%2CcVault.finance%2CEfinity%2CAmpleforth' \
             '%2CBounce%2CHifi%20Finance%2CAlpha%20Venture%20DAO%2CBeta%20Finance%2CUtrust%2CBand%20Protocol%2CDero' \
             '%2CAavegotchi%2CTrueFi%2CThunderCore%2CDUSK%20Network%2CDODO%2CMAI%2CBoringDAO%20%5BOLD%5D%2CSun%20Token' \
             '%2CAstrafer%2CcBAT%2CPolkastarter%2CSantos%20FC%20Fan%20Token%2CElectroneum%2CAlpine%20F1%20Team%20Fan' \
             '%20Token%2CCelo%20Dollar%2CTelos%2CTalken%2CBakerySwap%2CPhoenix%20Global%20%5BOLD%5D%2CDivi%2CKoda' \
             '%20Cryptocurrency%2CVerasity%2CEfforce%2CWrapped%20NXM%2CFerro%2CPerpetual%20Protocol%2CNexus%2CRonin' \
             '%2CKaspa%2CIron%20Bank%20EURO%2CGains%20Network%2CXCAD%20Network%2CKeep3rV1%2COrigin%20Dollar%2CUnifi' \
             '%20Protocol%20DAO%2CMango%2CTomoChain%2CKyber%20Network%20Crystal%20Legacy%2CKunci%20Coin%2CCratos' \
             '%2CGXChain%2CAnchor%20Protocol%2CAutomata%2CHunt%2CIDEX%2CMarlin%2CKishu%20Inu%2CbZx%20Protocol%2CRari' \
             '%20Governance%2CCOCOS%20BCX%2CLazio%20Fan%20Token%2CKlever%2CFlamingo%20Finance%2CBitcicoin%2CTravala.com' \
             '%2CDola%2CBezoge%20Earth%2CMrWeb%20Finance%2CAlpaca%20Finance%2CAxion%2CJasmyCoin%2CZigZag%2CProton%2CRAI' \
             '%20Finance%2CMrWeb%20Finance%20%5BOLD%5D%2CClover%20Finance%2CSafePal%2CPhala%20Network%2CUSDK%2CStargaze' \
             '%2CIX%2CDopex%20Rebate%2CBolide%2CZoidPay%2CZignaly%2CAVINOC%2CagEUR%2CAmpleforth%20Governance%2CStarLink' \
             '%2CCarry%2CLeague%20of%20Kingdoms%2CTracer%20DAO%2COrion%20Protocol%2CSamoyedcoin%2CSuperFarm%2CPropy' \
             '%2CRegen%2CFreeway%2Cchrono.tech%2CKomodo%2CDFI.money%2CCargoX%2CDEI%2CLCX&vs_currencies=INR'

# Wolfram API
wolfram_api='X44P8H-G775R3855K'
chuck_norris_api='https://api.chucknorris.io/jokes/random'
# News API Key
news_api_key = 'ea840b5d21f54a4c8785f1e4bb5e7cbd'

# Weather API Key
weather_api_key = 'xxx'

# Distance API Key
distance_api_key = '90T6GtmFVuOAA94r4MdFhHALREhb6jhY'
MASTER = "Raj"
# convert speech to text
def alex_listen():
    # create recognizer
    r = sr.Recognizer()
    r.energy_threshold = 20000
    # what ever we speak will be our source for microphone
    with sr.Microphone() as source:
        # use listen function so that recognizer can catch the source
        audio = r.listen(source)
        text = ''
        try:
            text = r.recognize_google(audio)
        except sr.RequestError as re:
            print(re)
        except sr.UnknownValueError as uve:
            print(uve)
        except sr.WaitTimeoutError as wte:
            print(wte)

    text = text.lower()
    return text


# convert text to speech
def alex_talk(text):
    # create audio data
    file_name = 'audio_data.mp3'
    # convert audio data
    tts = gTTS(text=text, lang='en',slow=False)
    # save file
    tts.save(file_name)
    # play file
    playsound.playsound(file_name)
    # remove file
    os.remove(file_name)
# Hindi Translator
def alex_talk_hi(text):
    # create audio data
    file_name = 'audio_data.mp3'
    # convert text to speech
    tts = gTTS(text=text, lang='hi')
    # save file
    tts.save(file_name)
    # play file
    playsound.playsound(file_name)
    # remove file
    os.remove(file_name)

# Capital of a Country
def wolfram_alpha_country_capital(text):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(text)
    answer = next(result.results).text
    answer_split = answer.split()
    capital_result = 'The capital of ' + answer_split[-1] + ' is ' + answer_split[0]
    print(capital_result)
    alex_talk(capital_result)

# Calculator
def wolfram_alpha_calculator(text):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(text)
    answer = next(result.results).text
    print(answer)
    alex_talk('The answer is ' + answer)
# Google search


def google_search(text):
    user_query = text
    URL='https://www.google.co.in/search?q='+ user_query
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    result = soup.find(class_='IsqQVc NprOob wT3VGc').get_text()
    alex_talk(result)


def searchGoogle(query):
    if "google" in query:
        query = query.replace("google search","")
        query = query.replace("google","")
        alex_talk("This is what I found on google")
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            alex_talk(result)
        except:
            alex_talk("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        alex_talk("This is what I found for your search!")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        alex_talk("Done, Sir")


def searchWikipedia(query):
    if "wikipedia" in query:
        alex_talk("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        alex_talk("According to wikipedia..")
        print(results)
        alex_talk(results)


# President of a certain country
def wolfram_alpha_president(text):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(text)
    answer = next(result.results).text
    print(answer)
    alex_talk('The president is ' + answer)
# Translator function

def get_news():
    news_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=' + news_api_key
    news = requests.get(news_url).json()
    articles = news['articles']

    news_headlines = []
    for art in articles:
        news_headlines.append(art['title'])

    for i in range(3):
        print(news_headlines[i])
        alex_talk(news_headlines[i])


def get_weather():
    alex_talk('No problem, I will look it up for you. What city are you interested in?')
    weather_input = alex_listen()
    print(weather_input)

    user_query = weather_input
    URL = 'https://www.google.co.in/search?q=' + user_query + '+weather'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(class_='wob_t q8U8x').get_text()
    alex_talk(result+'°C')


def distance_info():
    alex_talk('Sure, let me know the starting point')
    location_one = alex_listen()
    time.sleep(1)
    alex_talk('Allright, and now tell me the final destination')
    location_two = alex_listen()
    while (location_two==''):
        alex_talk('Excuse me, I did not get that. Can you please repeat it?')
        location_two=alex_listen()
    alex_talk('Give me one moment, I will use my smart brain to calculate the distance for you')
    dist_url = 'http://www.mapquestapi.com/directions/v2/route?key=' + distance_api_key + '&from=' + location_one + '&to=' + location_two + '&unit=k'
    dist_request = requests.get(dist_url).json()
    distance = round(dist_request['route']['distance'], 2)
    distance_result = 'The distance between ' + location_one + ' and ' + location_two + ' is ' + str(
        distance) + ' kilometers'
    print(distance_result)
    alex_talk(distance_result)
def translator(text):
    alex_talk_hi(tr.google(text, from_language='en',to_language='hi'))


# Below function will give reply based on the input text
def alex_reply(text):
    # smalltalk - what is your name?
    if 'what' in text and 'name' in text:
        alex_talk('My name is Alina and I am your personal assistant')

    # smalltalk - why do you exist?
    elif 'why' in text and 'exist' in text:
        alex_talk('I was created to work for you. I dont need a break and I will never ask for days off')

    # smalltalk - when do you sleep?
    elif 'when' in text and 'sleep' in text:
        alex_talk('I never sleep. I was created to support you 24 hours')

    # smalltalk- are you stupid?
    elif 'you' in text and 'stupid' in text:
        alex_talk('No, I am not stupid. My grandmother told me that there are no stupid persons out there. '
                  + 'I try to give my best everyday and learn continuously')

    # Smalltalk - Favorite Movie?
    elif 'favorite' in text or 'favourite' in text and 'movie' in text:
        alex_talk("My favorite movie is Titanic. I watch it with my friends all the time")

    elif 'translate' in text:
        alex_talk('Sure, What do you want me to translate?')
        while True:
            try:
                text_to_translate = alex_listen()
                if text_to_translate != 'turn off translator':
                    translator(text_to_translate)
                else:
                    alex_talk('The translator will be turned off.. What else can I do for you?')
                    break
            except AssertionError as ae:
                alex_talk('No text to speak')
    elif 'cryptocurrency' in text or 'crypto' in text and 'price' in text:
        try:
            alex_talk("Which cryptocurrency price would you like to know?")
            listen_name = alex_listen()
            response = requests.get(crypto_api)
            crypto_json = response.json()
            alex_talk(
                'The current price for a ' + listen_name + 'is' + str(crypto_json[listen_name]['inr']) + 'rupees')

        except KeyError:
            alex_talk("keyError")


    elif 'apple'in text:
        apple=yf.Ticker('AAPL')
        print(apple.info['regularMarketPrice'])
        alex_talk(
            'At this moment you can purchase one Apple Share for ' + str(apple.info['regularMarketPrice']) + 'us dollar')

    elif 'facebook'in text:
        facebook=yf.Ticker('FB')
        print(facebook.info['regularMarketPrice'])
        alex_talk('At this moment you can purchase one Facebook Share for ' + str(facebook.info['regularMarketPrice'])+'us dollar')

    elif 'tesla'in text:
        tesla=yf.Ticker('TSLA')
        print(tesla.info['regularMarketPrice'])
        alex_talk('At this moment you can purchase one tesla Share for ' + str(tesla.info['regularMarketPrice']) + 'us dollar')

    # Wolfram Alpha - Capital of a Country
    elif 'capital' in text and 'of' in text:
        wolfram_alpha_country_capital(text)

    # Wolfram Alpha - Calculator
    elif '+' in text or '-' in text or 'multiply' in text or 'multiplied' in text or 'divide' in text or 'root' in text:
        wolfram_alpha_calculator(text)

    # Wolfram Alpha - President
    elif 'who' in text and 'president' in text:
        wolfram_alpha_president(text)

    elif 'google' in text:
        searchGoogle(text)
        exit()
    elif 'youtube' in text.lower():
        searchYoutube(text)
        exit()
    elif 'wikipedia' in text.lower():
        searchWikipedia(text)

    elif 'play music' in text.lower():
        songs_dir = "E:/Music Playlist 1"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in text.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        alex_talk(f"{MASTER} the time is {strTime}")

    elif 'joke' in text or 'jokes' in text:
        alex_talk(pyjokes.get_joke())

        # Top 3 News- Headlines
    elif 'news' in text:
        alex_talk('Allright, let me tell you the first three headlines')
        get_news()

        # Weather
    elif 'weather' in text:
        get_weather()

        # Distance
    elif 'distance' in text:
        distance_info()

    elif ' ' in text:
        client = wolframalpha.Client(wolfram_api)
        result = client.query(text)
        answer = next(result.results).text
        if answer == '(data not available)':
            google_search(text)
        else:
            alex_talk('The answer is ' + answer)

    elif 'stop' in text:
        alex_talk('It was a pleasure to help you, I wish you a wonderful day')


    else:
        alex_talk('Excuse me, I did not get that. Can you please repeat it?')


# Execution Section

def execute_bot():
    alex_talk('Hi, I am here to support you. Can you please tell me your name?')
    listen_name=alex_listen()
    alex_talk('Hi'+ listen_name + 'What can I do for you?')
    while True:
        listen_alex = alex_listen()
        print(listen_alex)
        alex_reply(listen_alex)
        # if stop keyword encounter which means we are ending the while loop
        if 'stop' in listen_alex:
            break


execute_bot()
# Preparation Section

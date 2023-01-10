"""토큰화 = 문장을 의미가 있는 기본 단위인 어절 또는 어근 단위로 쪼개는 것
문장을 데이터화 하기 위해 해야하는 가장 기본적인 전처리과정, 어떻게 토큰화 하느냐에 따라 챗봇의 성능이 결정 될 수 있다.
# 사용 라이브러리는 KoNlPy(Korean-Natural-Language-Processing in Python Library)
KoNLPy내부 API는 Hannaum(한나눔)/Kkma(꼬꼬마)/Komoran(코모란)/Mecab()/OKT(오픈 코리아 텍스트) 번외로 RHINO/아리랑/은전한닢이 있다.
나는 Komoran과 Kkma를 사용할 예정이다.
--link : konlpy.org/ko/lastest/
ex) 아버지가        방에         들어가신다.
=> 아버지/가        방/에        들어가신다/.
   Noun/Josa/   Noun/Josa   Verb/Punctuation
9품사 분류 (명사/대명사/수사/동사/형용사/관형사/부사/조사/감탄사)
"""

### 꼬꼬마 실습 - 서울대 IDS 연구실/GPL v2기반
from konlpy.tag import Kkma

print('------ Kkma  ------')
# 변수 설정
kkma = Kkma()

text = "아버지가 방에 들어갑니다."

# 형태소 추출
morphs = kkma.morphs(text)
print(morphs)

# 품사 추출
pos = kkma.pos(text)
print(pos)

# 명사 추출
nouns = kkma.nouns(text)
print(nouns)

# 문장 분리
sentence = "오늘 날씨는 어때요? 내일은 덥다던데."
s = kkma.sentences(sentence)
print(s)

### 코모란 실습 - 공백을 포함한 형태소 분석 가능 - Shineware/JAVA, Apache 2.0기반
from konlpy.tag import Komoran

print('\n------Komoran------')

# 변수 설정
komoran = Komoran()

# 형태소 추출
morphs2 = komoran.morphs(text)
print(morphs2)

# 형태소, 품사 태그 추출
pos2 = komoran.pos(text)
print(pos2)

# 명사 추출
nouns2 = komoran.nouns(text)
print(nouns2)

### Okt실습 - Twitter/Twiter 한국어 처리기, Apache 2.0기반
from konlpy.tag import Okt

print('\n------  Otk  ------')

# 변수 설정
okt = Okt()

# 형태소 추출
morphs3 = okt.morphs(text)
print(morphs3)

# 형태소와 품사 추출
pos3 = okt.pos(text)
print(pos3)

# 명사 추출
nouns3 = okt.nouns(text)
print(nouns3)

# 정규화; 어구 추출
sentence2 = "오늘 날씨가 좋아욬ㅋㅋ"
print(okt.normalize(sentence2))
print(okt.phrases(sentence2))

### User Dictionary pre-build with komoran
print('\n------  User_dic  ------')

komoran2 = Komoran(userdic='./user_dic.tsv')
text2 = "우리 챗봇은 엘엔피를 좋아해."
pos4 = komoran2.pos(text2)
print(pos4)
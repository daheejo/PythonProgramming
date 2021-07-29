import re
source = '''I wish I may, I wish might
... Have a dish of fish tonight.'''
re.findall(r'wish', source)
re.findall(r'wish|fish', source)
re.findall(r'^wish', source)
re.findall(r'^I wish', source)
re.findall(r'fish$', source)
re.findall(r'fish tonight\.', source)
re.findall(r'[wf]ish', source)
re.findall(r'[wsh]+', source)
re.findall(r'ght\W', source)
re.findall(r'I (?=wish)', source)
re.findall(r'(?<=I) wish', source)
re.findall(r'\bfish', source)

text = 'apple banana cat'

start = input('맨 앞글자: ')

print(re.findall(r'\b%s\w+'%start, text))

pattern = re.compile('Python') # ‘Python’이란 문자열을 정규식으로 컴파일
print(pattern.match('Python is easy.')) # source(‘Python is easy’)가 정규식 pattern과 일치하는지 확인

# 금지된단어 제외한 가장 흔하게 등장하는 단어 출력. 대소문자 구분 하지 않고, 구두점 또한 무시.

import collections
import re

def the_most_common(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split() if word not in banned
            ]
    a = collections.Counter(words).most_common(1)
    return a[0][0]

paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
banned = ['hit']

print(the_most_common(paragraph, banned))
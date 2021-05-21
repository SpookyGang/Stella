import random
import string


def RandomStringGen() -> list:
    CaptchaStringList = []
    for x in range(12):
        CaptchaString = ''.join(
                random.SystemRandom().choice(
                string.ascii_letters + string.digits
                ) for _ in range(7)
                ).lower()
        CaptchaStringList.append(CaptchaString)
    return CaptchaStringList

def mathCaptchaGen():
    mathCaptchaList = []
    num01 = random.randint(1, 40)
    num02 = random.randint(41, 80)
    answer = num01 + num02

    answer_dict = {
        'num01': num01,
        'num02': num02,
        'answer': answer
    }

    for _ in range(12):
        mathCaptchaList.append(
            random.randint(1, 130)
        )
        mathCaptchaList.append(answer)
        random.shuffle(mathCaptchaList)
    return answer_dict, mathCaptchaList
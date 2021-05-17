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
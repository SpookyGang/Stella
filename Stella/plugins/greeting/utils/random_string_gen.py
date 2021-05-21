#    Stella (Development)
#    Copyright (C) 2021 - meanii (Anil Chauhan)
#    Copyright (C) 2021 - SpookyGang (Neel Verma, Anil Chauhan)

#    This program is free software; you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by 
#    the Free Software Foundation; either version 3 of the License, or 
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


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
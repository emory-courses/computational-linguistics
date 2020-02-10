# ========================================================================
# Copyright 2020 Emory University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
import re
from types import SimpleNamespace
from typing import List, Pattern


def regex_matcher(regex: Pattern, instr: str) -> List[str]:
    ts = [None] * regex.groups

    for t in regex.findall(instr):
        if isinstance(t, str): t = [t]
        for i, literal in enumerate(t):
            if ts[i] is None and literal:
                ts[i] = literal

    return ts


def turn_0(res: SimpleNamespace):
    s = 'S: are you using a smartphone?'
    u = input(s + '\nU: ')

    yn = regex_matcher(res.re_yn, u)
    phone = regex_matcher(res.re_phone, u)
    res.in_phone_company = phone[0]
    res.in_phone_name = phone[1]

    if any(phone):
        turn_1a(res)
    elif yn[0]:
        turn_1b(res)
    elif yn[1]:
        turn_1c(res)

    print('S: good bye!')


def turn_1a(res: SimpleNamespace):
    p = res.in_phone_name if res.in_phone_name else res.in_phone_company
    s = 'S: how long have you been using {}?'.format(p)
    u = input(s + '\nU: ')

    duration = regex_matcher(res.re_duration, u)
    from_date = regex_matcher(res.re_from_date, u)

    res.in_phone_year, res.in_phone_month = None, 1
    curr_year, curr_month = 2020, 1

    if all(duration):
        d = int(duration[0])
        m = duration[1]
        if m == 'year':
            res.in_phone_year = curr_year - d
        elif m == 'month':
            res.in_phone_year = curr_year - int(d / 12)
            res.in_phone_month = curr_month - (d % 12)
            if res.in_phone_month <= 0:
                month_diff = abs(res.in_phone_month)
                res.in_phone_month = 12 - month_diff
                res.in_phone_year -= 1
    elif any(from_date):
        res.in_phone_year = int(from_date[1])
        res.in_phone_month = res.d_month_to_number[from_date[0]] if from_date[0] else 1

    if res.in_phone_year:
        if res.in_phone_name == 'iphone' or res.in_phone_company == 'apple':
            turn_2a(res)


def turn_1b(res: SimpleNamespace):
    s = 'S: what kind of smartphone do you have?'
    u = input(s + '\nU: ')
    # TODO: to be filled


def turn_1c(res: SimpleNamespace):
    s = 'really? you should consider getting one.'
    print(s)


def turn_2a(res: SimpleNamespace):
    r = res.d_iphone.get(res.in_phone_year, None)
    res.in_phone_version = None

    if r:
        v = next((models for month, models in r if month <= res.in_phone_month), None)
        if v:
            res.in_phone_version = v[0]
            s = 'S: oh, are you using iphone {}?'.format(' or '.join(v))
            u = input(s + '\nU: ')

            yn = regex_matcher(res.re_yn, u)
            if yn[1]: res.in_phone_version = None
        else:
            s = 'S: which version of iphone is your model?'
            u = input(s + '\nU: ')
    else:
        s = 'S: which version of iphone is your model?'
        u = input(s + '\nU: ')

    version = regex_matcher(res.re_iphone_version, u)
    if version[0]: res.in_phone_version = version[0]
    if res.in_phone_version: turn_3a(res)


def turn_3a(res: SimpleNamespace):
    # TODO: to be filled
    old = 5
    s = 'S: iphone {} is about {} years old'.format(res.in_phone_version, old)
    print(s)


if __name__ == '__main__':
    res = SimpleNamespace()

    # regular expressions
    res.re_yn = re.compile(r'(?:\s|^)(yes|yeah)|(no|not really)(?:\s|,|\.|$)')
    res.re_phone = re.compile(r'(?:\s|^)(apple|google|samsung)|(iphone|pixel|galaxy|android)(?:\s|,|\.|$)')
    res.re_duration = re.compile(r'(?:\s|^)(\d+)(?:\s|-)+(month|year)')
    res.re_from_date = re.compile(r'(?:\s|^)(?:since|from)\s(?:(january|february|march|april|may|june|july|august|september|october|november|december)\s)?(\d\d{2,4})')
    res.re_iphone_version = re.compile(r'(?:\s|^)(?:iphone|version)\s(\d+s?(?: (?:plus|max))?)(?:\s|,|\.|$)')

    # dictionaries
    res.d_month_to_number = {month: i for i, month in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], 1)}
    res.d_iphone = {2019: [(9, ['11', '11 pro', '11 pro max'])], 2018: [(9, ['10s', '10s max'])], 2017: [(11, ['10']), (9, ['8', '8 plus'])], 2016: [(9, ['7', '7 plus'])], 2015: [(9, ['6s', '6s plus'])], 2014: [(9, ['6', '6 plus'])]}
    res.d_iphone_v = {'11': 2019, '11 pro': 2019, '11 pro max': 2019, '10s': 2018, '10s max': 2018, '10': 2017, '8': 2017, '8 plus': 2017, '7': 2016, '7 plus': 2016, '6s': 2015, '6s plus': 2015, '6': 2014, '6 plus': 2014}

    # run
    turn_0(res)

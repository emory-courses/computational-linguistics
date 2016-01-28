import urllib2
import sys
import re

RE_CLASSES_MAIN = re.compile('<div class="classes-main-toggle-buttons">(.+)</div>', re.DOTALL)
RE_CLASS_TITLE  = re.compile('<table .*?class="class-title">(.+?)</table>')
RE_CLASS_NAME   = re.compile('<td class="class-name">(.+?)</td>', re.DOTALL)
RE_CLASS_INFO   = re.compile('<td class="class-number">(.+?)</td><td class="class-location">(.+?)</td><td class="class-schedule">(.+?)</td>', re.DOTALL)

year     = 2015
term     = 2
graduate = 0
url      = 'http://www.mathcs.emory.edu/classes-semester.php?subject=CS&year=%d&term=%d&graduate=%d' % (year, term, graduate)

request  = urllib2.Request(url)
response = urllib2.urlopen(request)
page     = response.read()
kb       = dict()

m = RE_CLASSES_MAIN.search(page)
main = m.group(1)

titles = [(m.group(1), m.start(), m.end()) for m in RE_CLASS_TITLE.finditer(main)]

def splitTitle(title):
    name = RE_CLASS_NAME.search(title).group(1)
    t = name.split(':')
    cnum = ''.join(t[0].split())
    cdes = t[1].strip()
    return (cnum, cdes)

for i,title in enumerate(titles):
    (course_number, course_title) = splitTitle(title[0])

    start = title[2]
    if i+1 < len(titles): end = titles[i+1][1]
    else: end = -1

    for m1 in RE_CLASS_INFO.finditer(main, start, end):
        section  = m1.group(1).strip()
        location = m1.group(2).strip()
        schedule = m1.group(3).strip()

        k = (course_number+'-'+section).upper()
        kb[k] = (course_title, location, schedule)

course = sys.argv[1]
print kb[course]


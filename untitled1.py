# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 21:52:06 2022

@author: jingy
"""

(round(2.534234,2))
a = 154893
(round(a, -2))
v = 1.29389
rounded = (format(v,'0.1f')) 
(f'value is {rounded}')

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
(a + b) == Decimal('6.3')

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
with localcontext() as ctx:
    ctx.prec = 15
    (a/b)
# sum is bad use math.fsum

x = 1234.56789
format(x, '0,.2f')
(format(x, '>10.1f'))
format(x, ',')
format(x, '0.2E')

x = 18039
oct(x)
bin(x)
hex(x)
format(x,'b')
format(x,'x')
int('101',2)

a = complex(2,4)
b = 3-5j
a.real
a.imag
a.conjugate()

import cmath
cmath.sin(a)
cmath.cos(a)
cmath.exp(a)

a = float('inf')
b = float('-inf')
c = float('nan')

from fractions import Fraction
a = Fraction(2,5)
b = Fraction(56,2)
c = a*b
c.numerator
c.denominator
float(c) 
c.limit_denominator(8)
x = 3.75
y = Fraction(*x.as_integer_ratio())

# lists concatenate, numpy arrays actually do math
x = [1,2,3,4]
y = [5,6,7,8]
x + y 
x*3
import numpy as np
ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])
ax * ay
ax + ay
ax * 2
grid = np.zeros(shape=(1000,1000),dtype=float)
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a[1]
a[:,1]
a[1:3,1:3] += 10
np.where(a>4,a,10)

m = np.matrix([[1,3,4],[4,7,8],[304,-2,1]])
m.T # transpose
m.I #inverse
v = np.matrix([[2],[3],[4]])
m * v

import random
v = [1,2,3,5,6,7,8]
random.choice(v)
random.sample(v,5)
random.shuffle(v)
random.randint(0,10)
random.random() # 0 to 1
random.getrandbits(200)

from datetime import timedelta
a = timedelta(days=2,seconds=80)
b = timedelta(seconds=3)
c = a + b
(c.days)
(c.seconds)
(c.total_seconds())
from datetime import datetime
a = datetime(2012,9,23)
b = a + timedelta(days = 10)
d = a - b 
(d.days)
datetime.now()
from dateutil.relativedelta import relativedelta
a + relativedelta(months=+1)
b = datetime(2012,12,21)
d = b-a
d = relativedelta(b,a)
d

weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.now()
    daynum = start_date.weekday()
    daynumtarget = weekdays.index(dayname)
    days_ago = (7+ daynum-daynumtarget)%7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date
(get_previous_byday("Saturday"))
from dateutil.rrule import *
d = datetime.now()
(d + relativedelta(weekday=FR))
(d + relativedelta(weekday=FR(-2)))

from datetime import date
import calendar
def get_month_range(startdate=None):
    if startdate is None:
        startdate = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(startdate.year,startdate.month)
    enddate = startdate + timedelta(days=days_in_month)
    return startdate,enddate
def date_range(start,stop,step):
    while start<stop:
        yield start
        start += step
for d in date_range(datetime(2022,6,25),datetime(2022,6,26),timedelta(hours=9)):
    (d)
    
text = '6-25-2022'
y = datetime.strptime(text, '%m-%d-%Y')
z = datetime.now()
z-y
nice_z = datetime.strftime(z,'%A %B %d, %Y') # specific values
print(nice_z)
def parse_ymd(s):
    year, month, day = s.split('-')
    return datetime(int(year),int(month),int(day))
u = '2022-6-25'

from pytz import timezone



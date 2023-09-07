
def  isLeapyYear(year):
 if (year % 4==0 & year % 100!=0)/ year % 400==O:
   return True
 else:

   return False

year=int (input ('enter the year'))

if isLeapYear(year):
   print ('{} is a Leap Year.'. format (year))
else:
   print ('{} is not a Leap Year.'.format(year))




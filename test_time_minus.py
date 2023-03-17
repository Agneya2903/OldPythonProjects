#program for current time  minus no of days
from datetime import datetime ,timedelta
curr_date = datetime.today()
print("   The Current date is:- ",curr_date)
print("The date one day ago was:-",curr_date - timedelta(days=1))
print("the time one hour ago was", curr_date - timedelta(hours=1))
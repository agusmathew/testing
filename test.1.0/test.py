import csv_to_dict
import re
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

month_dict = {
			  "January":"01",
			  "February":"02",
			  "March":"03",
			  "April":"04",
			  "May":"05",
			  "June":"06",
			  "July":"07",
			  "August":"08",
			  "September":"09",
			  "October":"10",
			  "November":"11",
			  "December":"12",

			 }


booking = csv_to_dict.d
# print booking

file = open("site_data.txt","r")
check_in = file.read()

# extracting from text file
re_ticket_no = re.findall("Document\s+(\d+)",check_in)
re_owner = re.findall('Owner\s+([\w+\s\w+]+)',check_in)
re_date_of_issue = re.findall('DATE OF ISSUE\s+(.*)',check_in)
re_control_no = re.findall('BOOKING REF.\s+\w+\/(\w+)',check_in)
# cleaning
ticket_no = re_ticket_no[0].strip() if re_ticket_no else None
raw_owner = re_owner[0].strip() if re_owner else None
raw_date_of_issue = re.findall('\d+\w+\d+',re_date_of_issue[0]) if re_date_of_issue else None
re_month = re.findall('\D+',raw_date_of_issue[0]) if raw_date_of_issue else None
control_no = re_control_no[0].strip() if re_control_no else None







# printing the heading
print color.BOLD+color.DARKCYAN+"\nTESTING RESULTS"+color.END


# actual testing (testing from site values to db values)
# checking ticket number
if ticket_no:
	if ticket_no in booking.values():
		print "\n"+color.YELLOW+" TICKET NUMBER IN SITE IS CORRECT "+color.END+color.BLUE+" PASS"+color.END
# checking AIRLINE name
if raw_owner:
	owner = ''
	for each in raw_owner.split():
		owner = owner + list(each)[0]
	if owner in booking.values():
		print "\n"+color.YELLOW+" AIRLINE NAME IN SITE IS CORRECT "+color.END+color.BLUE+" PASS"+color.END
# checking date of issue
if raw_date_of_issue:
	date_of_issue = raw_date_of_issue[0]
	month = re_month[0].strip() if re_month else None
	raw_doi = date_of_issue.replace(month,"-"+month_dict[month]+"-")
	year = raw_doi.split("-")[-1]
	exc_doi = raw_doi.replace(year,"20"+year)
	list_doi = exc_doi.split("-")
	doi = list_doi[2]+"-"+list_doi[1]+"-"+list_doi[0]
	# print doi
if doi:
	if doi in booking.values():
		print "\n"+color.YELLOW+" DATE OF ISSUE IN SITE IS CORRECT "+color.END+color.BLUE+" PASS"+color.END
if control_no:
	if control_no in booking.values():
		print "\n"+color.YELLOW+" CONTROL NUMBER IN SITE IS CORRECT "+color.END+color.BLUE+" PASS"+color.END



# # general testing (testing db values in txt file of site)
# for i in booking:
# 	if booking[i].strip():
# 		if booking[i].strip() in check_in:
# 			print "\n"+str(i)+" ~~~ "+str(booking[i].strip())+color.BLUE+" PASS"+color.END
# 		else:
# 			print "\n"+str(i)+" ~~~ "+str(booking[i].strip())+color.RED+" FAILED"+color.END
# 	else:
# 		print "\n"+str(i)+" ~~~ "+color.GREEN+" NOT IN DB"+color.END
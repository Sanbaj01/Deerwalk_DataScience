# reference
# print('umesh@gmail.com'.split('@'))
# print('ramdaiisawesome'.split('a'))

#write a function that takes an email address and returns True if the email address is an edu account
# def check_edu_mail(mail):
#     if 'edu' in mail:
#         return True

## Sir's Code
# def is_edu_email(email):
#     if 'edu' in email.split('@')[1]:
#         return True

# print(is_edu_email('educatedsanbaj@.edu'))

######################################################################################################
#write a function that takes an email address and returns True if the email address is a gmail account
# def check_gmail(mail):
#     check_mail = mail.split('@')
#     if check_mail[1] == 'gmail.com' :
#         return True
# print(check_gmail('sanbajansari01@gmail.com'))

#Sir's Code
def is_gmail_com(email):
    if 'gmail.com' in email.split('@')[1]:
        return True

#write a function that takes a date in the format '2023/05/08' or '2023-05-08'. The function retuns year, month and date separated in a dictionary  {'year': 2023, 'month': 05, 'day':08}
# def change_date_format(date):
#     if '/' in date:
#         new_format = {
#             'Year' : date.split('/')[0],
#             'Month' : date.split('/')[1],
#             'Day' : date.split('/')[2],
#         }
#     elif '-' in date:
#         new_format = {
#             'Year' : date.split('-')[0],
#             'Month' : date.split('-')[1],
#             'Day' : date.split('-')[2],
#         }
#     return new_format

# print(change_date_format('2023-05-08'))

###################################################
# Sir's Code
# def format_date(date):
#     if '/' in date:
#         year, month, day = date.split('/')
#     elif '-' in date:
#         year, month, day = date.split('-')
    
#     return {'year': year, 'month': month, 'day': day}

# print(format_date('2023/05/08'))
# print(format_date('2023-05-08'))

######################  OR  ####################

# def format_date(date):
#     if '/' in date:
#         splitted_date = date.split('/')
#     elif '-' in date:
#         splitted_date = date.split('-')
    
#     return {'year': splited_date[0], 'month': splited_date[1], 'day': splited_date[2]}

# print(format_date('2023/05/08'))
# print(format_date('2023-05-08'))

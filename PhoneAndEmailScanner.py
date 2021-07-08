#! python3

import re, pyperclip

# TODO: Create a regex object for phone number
phoneRegex = re.compile(r'''
# a phone number, code types 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

((\d\d\d) | (\(d\d\d\)))?   # area code (optional regex)
(\s | -)                    # first seperator
\d\d\d                      # first three digits
-                           # seperator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s |x)           # extension word part (optional)
(\d{2, 5}))?                # extension number part (optional)
''', re.VERBOSE)

# TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
#emails have allot of different patterns because they have periods plus signs etc so we need a one all way for searching an email

[a-zA-Z0-9_.+]+    #name part (note: we cant use class \w because it is a charecter class pureley for charecter we need to create our own charectrer class using [] bracket
@                  #@ symbol
[a-zA-Z0-9_.+]+    #domain 


''', re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone number of this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

# TODO: Copy the extracted email and phone number to the clipboard

print (extractedPhone)
print (extractedEmail)



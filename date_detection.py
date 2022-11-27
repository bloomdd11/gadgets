import re, pyperclip


# TODO: Create dateregex
dateRegex = re.compile(
    r"""(
  (\d{1,2})   # date DD
  (-|\.|/)    # seperator
  (\d{1,2})   # month MM
  (-|\.|/)    # seperator
  (\d{4})   # year YYYY
  )""",
    re.VERBOSE,
)

# text = str(pyperclip.paste())
text = "11-12-2002, 1/23/2345, 32.1.201 29/2/2015 34.21.2212 23.8.2003 41/2/2005 31-6-2304 21-2-2002 31-2-2016 21-2-2020 29-2-2016 27-2-2000 30-09-2020 30-04-2020 30-6-2020 30-11-2020 1-1-2021 "
match = []

# TODO: Find matches in text
for groups in dateRegex.findall(text):
    date = "-".join([groups[1], groups[3], groups[5]])
    match.append(date)

# TODO: Filter the correct dates
def checkValidDate(date, list):
    [day, month, year] = date.split("-")
    if 1000 < int(year) <= 2999:  # check valid year
        if int(month) <= 12:  # check valid month
            if int(day) <= 31:  # check valid day
                list.append(date)
    return list


def checkLeapYearDate(date, list):
    [day, month, year] = date.split("-")
    subLamb = lambda a, b: True if a % b == 0 else False

    # if year cannot be divided by 4, return date checking feb is less than or equal 28
    if not subLamb(int(year), 4):
        if not int(month) == 2:
            list.append(date)
        elif int(day) <= 28:
            list.append(date)

    # if year can be divided by 4 but cannot divided by 400, return date checking feb is less than or equal 28
    elif not subLamb(int(year), 400):
        if not int(month) == 2:
            list.append(date)
        elif int(day) <= 28:
            list.append(date)

    # if year can be divided by 4 and by 400, return date checking feb is less than or equal 29
    else:
        if not int(month) == 2:
            list.append(date)
        elif int(day) <= 29:
            list.append(date)

    return list


def checkMonthDate(date, list):
    [day, month, year] = date.split("-")
    fourMonths = (
        int(month) == 9 or int(month) == 4 or int(month) == 6 or int(month) == 11
    )
    if fourMonths:
        if int(day) <= 30:
            list.append(date)
    else:
        list.append(date)
    return list


def dightFormat(date, list):
    [day, month, year] = date.split("-")
    if len(day) < 2:
        day = "0" + day
    if len(month) < 2:
        month = "0" + month

    dateFormat = "-".join([day, month, year])
    list.append(dateFormat)
    return list


validDate = []
leapDate = []
correctDate = []
finalDate = []

for date in match:  # check valid date
    checkValidDate(date, validDate)
for date in validDate:  # check leap date
    checkLeapYearDate(date, leapDate)
for date in leapDate:  # check month date
    checkMonthDate(date, correctDate)
for date in correctDate:  # format date
    dightFormat(date, finalDate)

# TODO: Print the dates
print("\n".join(finalDate))
print("lenght of valid date is: ", len(finalDate))

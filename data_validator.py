from datetime import datetime
def count_snils(snils):
    snils = snils.replace('-', '')
    sum = 0
    for i in range(0, 9):
        sum = sum + int(snils[i]) * (9 - i)
    if sum < 100:
        print(1)
        snils = snils + ' ' + str(sum)
    elif sum == 100 or sum == 101:
        print(2)
        snils = snils + ' 00'
    elif sum > 101:
        # print(3)
        sum = sum % 101
        while sum > 101:
            print(sum)
            if sum < 100:
                sum = sum
            elif sum == 100 or sum == 101:
                snils = snils + ' 00'
        snils = snils + ' ' + str(sum)
    # print(snils)
    return snils


def validate_snils(snils):
    i = 0
    ret = snils
    print('validate snils')
    if snils.split(' ')[1] == count_snils(snils.split(' ')[0]).split(' ')[1]:
        ret = "valid data"
    else:
        ret = 'invalid data'

    print(snils)
    snils = snils.replace('-', '').replace(' ', '')
    while i < 9:
        print(snils[i])
        if snils[i] == snils[i + 1]:

            if snils[i] == snils[i + 2]:

                ret = 'invalid data'
                break
            else:
                i = i + 2
        else:
            i = i + 1

    return ret


def validate_date(date):
    today = datetime.today()
    print(today)
    ret = 'valid data'
    try:
        date_formatted = datetime.strptime(date, '%d/%m/%Y')
    except ValueError:
        try:
            date_formatted = datetime.strptime(date, '%d.%m.%Y')
        except ValueError:
            ret =  'invalid data'

    if ret =='valid':
        if date_formatted>today:
            ret = 'invalid data'
    return ret

def validate_inn(inn):
    ret = 'valid data'

    if len(inn) ==12:
        first_digit = int(inn[0]) * 7 + int(inn[1])*2 + int(inn[2])*4 + int(inn[3])*10 + int(inn[4])*3 + int(inn[5])*5 + int(inn[6])*9+ int(inn[7])*4 + int(inn[8])*6+ int(inn[9])*8
        first_digit = (first_digit%11)%10
        if first_digit == int(inn[10]):
            3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8

            second_digit = int(inn[0]) * 3 + int(inn[1]) * 7 + int(inn[2]) * 2 + int(inn[3]) * 4 + int(
                    inn[4]) * 10 + int(inn[5]) * 3 + int(inn[6]) * 5 + int(inn[7]) * 9 + int(inn[8]) * 4 + int(inn[9]) * 6+int(inn[10])* 8
            second_digit = (second_digit%11)%10
            if second_digit != int(inn[11]):
                ret = 'invalid data'
        else:
            ret = 'invalid data'

    return ret
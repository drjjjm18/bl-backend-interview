import re

def check_password(password):

    # assuming there are no special or not English alphabet characters to handle

    # check input type is string
    try:
        assert type(password) == str
    except:
        raise TypeError(f'{password} should be type str not {type(password)}')

    # Check missing criteria

    length = len(password)
    # check length >= 7
    too_short = length < 7
    # check length <= 25
    too_long = 25 < length
    # searching for digits
    no_number = re.search(r"\d", password) is None
    # searching for uppercase
    no_uppercase = re.search(r"[A-Z]", password) is None
    # searching for lowercase
    no_lowercase = re.search(r"[a-z]", password) is None
    # check for consecutive characters
    consecutive = re.findall(r"([a-z])\1\1", password)
    # check if too common
    common = password in open('../common-passwords.txt', 'r').read().split('\n')

    # list of bool of whether criteria met
    criteria = [too_short, too_long, no_number, no_uppercase, no_lowercase, len(consecutive) > 0, common]
    # filter criteria for False to get count of missed criteria
    to_fix = len(list(filter(lambda x: x, criteria)))

    # if to_fix list is empty return 0 steps
    if not to_fix:
        return 0
    else:
        # if password is too short, steps required are:
        # max of characters to be added or fixes (minus too_short & consecutive) + consecutive char changes needed
        if too_short:
            return max(7-length, to_fix-2) + len(consecutive)
        # if password is too long, steps required are:
        # one step for every character remove, plus the other missing characters minus the total consec char changes
        elif too_long:
            return (length-25) + (to_fix -2 - len(consecutive))
        # if length is good but has consecutive chars
        # total steps is max of consec chars and total missing chars
        elif consecutive:
            return max(len(consecutive), to_fix-1)
        # if length is good and there are no consecutive chars
        # up to three changes required: add number, lowercase, uppercase
        return len(list(filter(lambda x: not x, [no_number, no_lowercase, no_uppercase])))

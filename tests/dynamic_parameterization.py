import features

def test_correct_email_validation(stringinput):
    assert features.check_valid_email(stringinput) == True

def test_incorrect_email_validation(stringinput):
    assert features.check_valid_email(stringinput) == False
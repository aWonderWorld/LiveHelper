
from configLoader import ConfigLoader

def LoginWithPwd():
    phoneNumber = ConfigLoader().dictAccount['account']['phoneNumber']
    password = ConfigLoader().dictAccount['account']['password']

    
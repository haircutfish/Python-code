#Simple Python script used to defanging IP and Domain addresses
#Created by Dan R. 2024-01-15

def addressDefanger(address):
    defang = address.replace('.', '[.]')
    return defang

rawAddress = input('Please enter the Domain or IP you would like to defang: ')

defanged_address = addressDefanger(rawAddress)

print(defanged_address)
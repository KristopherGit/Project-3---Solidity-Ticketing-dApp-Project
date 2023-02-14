import yubico
import hashlib
import configparser

# Yubico client ID & secret key

# Retrieve config.ini files
config = configparser.ConfigParser()
config.read("/Users/chris/Desktop/api_config_files.config.ini")

# Read yubikey client ID & secret key info from config.ini file
client_id = config(['YUBIKEY']['client_id'])
secret_key = config(['YUBIKEY']['secret_key'])

# Have the user enter a string
original_string = input("Enter a string: ")

# Hash the 'original_string'
hashed_string = hashlib.sha256(original_string.encode()).hexdigest()

# Get the Yubikey OTP from the user
otp =

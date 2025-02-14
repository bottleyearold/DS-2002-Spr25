#!/opt/homebrew/bin/python3
import os

FAV_FLAVOR = input("What is your favorite flavor? ")
AGE = input("What is your age? ")
UVA_FIRST_YEAR = input("Are you a first-year student at UVA? ")

os.environ["FAV_FLAVOR"] = FAV_FLAVOR
os.environ["AGE"] = AGE
os.environ["UVA_FIRST_YEAR"] = UVA_FIRST_YEAR

print("\nEnvironment Variables Set:")
print(os.getenv("FAV_FLAVOR"))
print(os.getenv("AGE"))
print(os.getenv("UVA_FIRST_YEAR"))

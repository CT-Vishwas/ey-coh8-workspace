print("Hello World Vishwas")
age = 10
language = "python"
version = 3.14
print("I am learning", language, version)
print("I am learning "+language+" "+str(version))
print("I am learning %s %f"%(language,version))
print("I am learning %s %.2f"%(language,version))
print("I am learning {0} {1}".format(language,version))
# Most used way - RECOMMENDED
print(f"I am learning {language} {version:.2f}")
# Q2.  Create and manipulate dictionaries.
# o	Create a dictionary to store information about a person (name, age, city).
# o	Access values using keys.
# o	Add a new key-value pair to the dictionary.
# o	Modify an existing value.
# o	Check if a key exists in the dictionary.
# o	Get a list of all keys and values.

person = {
    "name": "Avi",
    "age": 19,
    "city": "Lucknow"
}
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
person["email"] = "avi.rawat0019@gmail.com"
print("Updated dictionary with email:", person)
person["age"] = 20
print("Updated dictionary with modified age:", person)
if "city" in person:
    print("Key 'city' exists in the dictionary")

keys = person.keys()
values = person.values()
print("Keys:", list(keys))
print("Values:", list(values))

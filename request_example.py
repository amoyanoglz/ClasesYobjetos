import requests

def get_json_from(uri):
    r = requests.get(uri)

    return r.json()

def pretty(d, indent=0):
    for key, value in d.items():
        print('  ' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))

def main():
    results = "1"  # input("Cuantos quieres? ")
    uri = f'https://randomuser.me/api/?results=1{results}'
    dict = get_json_from(uri)

    for user in dict["results"]:
        pretty(user)

if __name__ == "__main__":
    main()





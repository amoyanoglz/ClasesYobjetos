import requests

def get_json_from(uri):
    r = requests.get(uri)

    return r.json()


def main():
    results = "1"  # input("Cuantos quieres? ")
    uri = f'https://randomuser.me/api/?results=1{results}'
    dict = get_json_from(uri)


if __name__ == "__main__":
    main()





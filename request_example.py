import requests

def generate_name_and_email():
    uri = 'https://randomuser.me/api/?results=10'
    r = requests.get(uri)
    randomuser = r.json()
    user = randomuser["results"][0]
    my_user_data = {
        "nombre": f'{user["name"]["first"]} {user["name"]["last"]}',
        "correo": user["email"]
    }

    return [my_user_data]

def main():
    my_user = generate_name_and_email()[0]
    print(f"NOMBRE: {my_user['nombre']}")
    print(f"CORREO: {my_user['correo']}")

if __name__ == "__main__":
    main()

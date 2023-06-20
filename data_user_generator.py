class DataUserGenerator:

    def __init__(self, cantidad_usuarios):
        self.next_user = 0
        self.usuarios = [
            {"nombre": "User 00", "correo": "user_00@correo.es"},
            {"nombre": "User 01", "correo": "user_01@correo.es"},
            {"nombre": "User 02", "correo": "user_02@correo.es"},
            {"nombre": "User 03", "correo": "user_03@correo.es"},
            {"nombre": "User 04", "correo": "user_04@correo.es"},
            {"nombre": "User 05", "correo": "user_05@correo.es"},
            {"nombre": "User 06", "correo": "user_06@correo.es"},
            {"nombre": "User 07", "correo": "user_07@correo.es"},
            {"nombre": "User 08", "correo": "user_08@correo.es"},
            {"nombre": "User 09", "correo": "user_09@correo.es"},
            {"nombre": "User 10", "correo": "user_10@correo.es"},
            {"nombre": "User 11", "correo": "user_11@correo.es"},
            {"nombre": "User 12", "correo": "user_12@correo.es"},
            {"nombre": "User 13", "correo": "user_13@correo.es"},
        ]

    def generar_usuario(self):

        if self.next_user >= len(self.usuarios):
            raise Exception(
                f"No hay más usuarios. se ha solicitado el usuario " +\
                    f"{self.next_user + 1}/{len(self.usuarios)} " +\
                    f"(indice {self.next_user}))")

        user = self.usuarios[self.next_user]
        self.next_user += 1

        return user

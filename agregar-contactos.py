import requests

# Configuración de API
subdominio = "demomario"
api_url = f"https://{subdominio}.kommo.com/api/v4/contacts"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImE2NzIxOTgzNzFhNDEyMTMzZGJhZDU1YmI1MTkwYWQ0YzNkOWI1OTFjMzliMzg3MDA5MTEwNzNiMjZjNTdjOTQzYmVhNmZkNjk1ODAzNWJkIn0.eyJhdWQiOiJiNTRmNzlkYS1kNjM1LTQ5NjUtYTdhZi05ZDNjYTJhYTg1ODEiLCJqdGkiOiJhNjcyMTk4MzcxYTQxMjEzM2RiYWQ1NWJiNTE5MGFkNGMzZDliNTkxYzM5YjM4NzAwOTExMDczYjI2YzU3Yzk0M2JlYTZmZDY5NTgwMzViZCIsImlhdCI6MTcxOTYxODY4OSwibmJmIjoxNzE5NjE4Njg5LCJleHAiOjE3MzU2ODk2MDAsInN1YiI6IjExNTU3MTg3IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMzMTM5MDc1LCJiYXNlX2RvbWFpbiI6ImtvbW1vLmNvbSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJjcm0iLCJmaWxlcyIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiLCJwdXNoX25vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiNjYyZDI0YTItYTAyYi00M2U5LTg3MDgtMDVjM2MwNWFkMDE5In0.Y3jWxytbOEkbf-uZuokrtKb5y1BloWF5ocV4iTSn7hrMbLJWgfz2_uzhnTO9gofBi0fTDFO3IWJcy015p7L-iAqTR-_4fs9AXHsziih8IZ03aerzWKW1GYl0h4fj7iafh0ap6Xs022L-kcmacq-9BSBBId1y3RE38Y_ewOFTlrt_GRlbRV1YYprJs7rRkQHBrtTI9dzv-21CmuKWkRaj0jKOl9ndfStbRxQXHF5GabV30PHb74rcFyFbSNEIOosZoa2RYPp_RPBpDQX4IiPpXup-7UIGRj9lxISnRADlGD_cq51DmvpfDqxi-Ph4Ue71Zu0KSJjHy-kxcXXBgyL7Qw"  # Reemplaza esto con tu token de larga duración

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


def agregar_contacto(nombre, apellido, telefono, email):
    # Datos del nuevo contacto
    data = {
        "contacts": [
            {
                "first_name": f"{nombre}",
                "last_name": f"{apellido}",
                "name": f"{nombre} {apellido}",  # Nombre completo del contacto
                "custom_fields_values": [
                    {
                        "field_code": "PHONE",
                        "values": [{"value": telefono}]
                    },
                    {
                        "field_code": "EMAIL",
                        "values": [{"value": email}]
                    }
                ]
            }
        ]
    }

    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200 or response.status_code == 201:
        print("Contacto agregado exitosamente")
        return response.json()
    else:
        print(f"Error al agregar contacto: {response.status_code}")
        print(response.text)
        return None


# Función en uso
nuevo_contacto = agregar_contacto(
    nombre="Juan",
    apellido="Pérez",
    telefono="+123456789",
    email="juan.perez@example.com"
)

if nuevo_contacto:
    print(nuevo_contacto)

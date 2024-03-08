from aiohttp import ClientSession
import asyncio

from mailtm import MailTM
import aiohttp

# Crea una cuenta de correo el MailTM
async def main():
    async with aiohttp.ClientSession() as session:
        mail_tm = MailTM(session=session)
        
        # Crear una cuenta sin especificar la dirección de correo electrónico ni la contraseña
        account = await mail_tm.get_account()
        print(f'Cuenta creada: {account}')
       

# Ejecutar el programa principal
if __name__ == "__main__":
    asyncio.run(main())
import platform
import subprocess
import time


class Application:
    def __init__(self):
        self.server = platform.node()
        self.usuarios = ''
        self.txtconf = 'Usuarios.txt'
        try:
            with open(self.txtconf, 'r') as file:
                self.usuarios = file.read().replace('\n', '')
                self.usuarios = self.usuarios.split(',')
        except FileNotFoundError:
            print(f'Arquivo: Usuarios.txt não encontrado.')
        self.disconnect()

    def disconnect(self):
        for users in self.usuarios:
            try:
                current = str((subprocess.check_output('query session | findstr ' + users, shell=True))).split()
                if users in current and current[2].isnumeric():
                    subprocess.Popen(f'logoff {current[2]} /server:{self.server}')
                    print(f'{users} desconectado!')
                else:
                    subprocess.Popen(f'logoff {current[3]} /server:{self.server}')
                    print(f'{users} desconectado!')
            except subprocess.CalledProcessError:
                print(f'{users} não está logado.')

        time.sleep(5)


Application()

import time
import pyzipper
import os

import getpass
from rich.panel import Panel
from rich.console import Console
from rich import print

console = Console()

os.system("git pull")
___logo___ = Panel.fit(
    r''' 
|Author: [bold green]STARK-404|[bold green]3.0.0|[bold magenta]Instagram:[bold green]@la1uuuuu|[bold magenta]Github: [bold green]@STARK-404|
 ___       __ ___             _   _ 
  |  |\ | (_   |  /\ __ |\/| |_) |_ 
 _|_ | \| __)  | /--\   |  | |_) |  
                                     
''',
    style='bold magenta',
    title='[bold blue](Instagram Brute Force)'
)


def extract_zip(zip_path):
    extract_to = os.path.dirname(zip_path)
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        console.print(___logo___)
        console.print("[bold white][[bold green]![bold white]] Enter the password to extract the ZIP file]")
        password = getpass.getpass("\033[35m└─>").encode('utf-8')
        try:
            with pyzipper.AESZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(path=extract_to, pwd=password)
                console.print("[bold white][[bold green]![bold white]] Extraction successful!")
                os.system("python Run.py")
                break
        except RuntimeError:
            console.print("[bold white][[bold red]![bold white]] Incorrect password. Try again.")
            console.print("[!] If you want to use Instahack buy the password from next page when you click enter!\nPress enter to be redirected to the payment page. For any enquiries contact the author.")
            try:
                # Try to open payment page on supported systems
                os.system('xdg-open https://buymeacoffee.com/mrstarkin/e/471721')
            except Exception:
                pass
            time.sleep(6)
        except pyzipper.zipfile.BadZipFile:
            console.print("[bold red] Invalid ZIP file.")
            return
        except KeyboardInterrupt:
            os.system('cls' if os.name=='nt' else 'clear')
            console.print(___logo___)
            console.print(Panel.fit("[bold red] Bye See You Soon "))
            return

    try:
        os.remove(zip_path)
    except OSError:
        pass


if __name__ == "__main__":
    zip_file_path = "Run.zip"
    extract_zip(zip_file_path)

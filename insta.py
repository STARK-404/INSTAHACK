import pyzipper
import os
from rich.panel import Panel
from rich.console import Console
from rich import print
___logo___ = (Panel.fit(r''' 
|Author: [bold green]STARK-404|[bold green]1.0.0|[bold magenta]Instagram:[bold green]@la1uuuuu|[bold magenta]Github: [bold green]@STARK-404|
 ___       __ ___             _   _ 
  |  |\ | (_   |  /\ __ |\/| |_) |_ 
 _|_ | \| __)  | /--\   |  | |_) |  
                                    
''',style='bold magenta',title='[bold blue](Instagram Brute Force)'))

def extract_zip(zip_path):
    extract_to = os.path.dirname(zip_path)  
    while True:
        print(___logo___)
        print("[bold white][[bold green]![bold white]] Enter the password to extract the ZIP file]")
        password = input("\033[35m└─>").encode('utf-8')
        try:
            with pyzipper.AESZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(path=extract_to, pwd=password)
                print("[bold white][[bold green]![bold white]] Extraction successful!")
                break  
        except RuntimeError:
             print("[bold white][[bold red]![bold white]] Incorrect password. Try again.")
             os.system('xdg-open mailto:gamerunknown509@gmail.com?subject=I want Insta Password&body=Hello, I am using your tool and I need the password of the zip file. Please provide me the password.')
        except pyzipper.zipfile.BadZipFile:
            print("[bold red] Invalid ZIP file.")
            return
    os.remove(zip_path)
   

if __name__ == "__main__":
    zip_file_path = "Run.zip" 
    extract_zip(zip_file_path)

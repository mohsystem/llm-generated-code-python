import os

with open("script.sh", "w") as file:
    file.write("#!/bin/bash\n"
"echo 'Hello World'")
os.system("chmod +x script.sh")
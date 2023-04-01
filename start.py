import subprocess


# Run the "chmod 777" commands
subprocess.run(["chmod", "777", "bombsquad_server"])
subprocess.run(["chmod", "777", "dist/bombsquad_headless"])

# Run the "./bombsquad_server" command
subprocess.run(["./bombsquad_server"])
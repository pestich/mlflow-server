import subprocess


def execute_command(command):
    subprocess.run(command, shell=True, check=True)


commands_to_execute = [
    #"sudo apt update",
    #"sudo apt upgrade",
    "curl -fsSL https://get.docker.com -o get-docker.sh",
    "sudo sh get-docker.sh",
    #"sudo docker volume create portainer_data",
    #"sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v "
    #"/var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest",
    "sudo docker compose up -d --build", 
    "sudo apt install python3-pip",
    "pip3 install boto3 python-dotenv",
    "python3 create_bucket.py"
]


if __name__ == "__main__":
    for cmd in commands_to_execute:
        execute_command(cmd)

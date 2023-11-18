import subprocess


def execute_command(command):
    subprocess.run(command, shell=True, check=True)


commands_to_execute = [
    "curl -fsSL https://get.docker.com -o get-docker.sh",
    "sudo sh get-docker.sh",
    "sudo docker compose up -d --build", 
    "sudo apt install python3-pip",
    "pip3 install --no-warn-script-location boto3 python-dotenv mlflow scikit-learn",
    "python3 create_bucket.py"
]


if __name__ == "__main__":
    for cmd in commands_to_execute:
        execute_command(cmd)

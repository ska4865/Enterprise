# KennUWare-INVENTORY_ACCOUNTING
# Inventory_Accounting
# 

An online cloud system to carry out inventory and accounting tasks built in Python & React
  
## Team

- Sakai Alexander
- John Davidson
- Zach Tucker

## Prerequisites

- Python 3
- NodeJS 

Optional:
- docker
- docker-compose

## How to deploy it 

Each portion of the project within the src directory has it's own readme with instructions on building. Follow those individually for deployment, or try it with docker!


## With Docker
To run the project on a Docker container, please execute the following from the root directory:

    docker-compose up -d --build

this should build, create and run the docker containers for the project.

## CLOUD DEPLOYMENT
- create an EC2 instance
- on EC2 run this command to install the docker enginer
```bash
sudo amazon-linux-extras install docker
```
- then run this command to start the docker enginer (this has to be done every time the EC2 instance is restarted)
```bash
sudo service docker start
```
- run this command to set the "docker user"'s permissions
```bash
sudo usermod -a -G docker ec2-user
```
- Install docker-compose
```bash
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
- then follow docker steps for installation.
## Known bugs and disclaimers
- some API routes are non-functional
- there is no "Full-Stack connection" our team has had to do major redesigns since our initial R2 show and tell


## How to test/run/access/use it

1. Open your browser to here for the Swagger UI:
    http://localhost:8080/ui/
2. Open your browser to here for the website:
    http://localhost/inventory/

## License

MIT License

See LICENSE for details.

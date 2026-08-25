Employee API DevOps Learning Project

to use terraform, install terraform in cloudshell and clone the project

1. Install Terraform

Run:

cd /tmp
curl -LO https://releases.hashicorp.com/terraform/1.15.8/terraform_1.15.8_linux_amd64.zip

Then:

unzip terraform_1.15.8_linux_amd64.zip

If unzip isn't available:

sudo yum install -y unzip

Then:

mkdir -p ~/bin
mv terraform ~/bin/

Add it to PATH:

echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
export PATH="$HOME/bin:$PATH"

git clone https://github.com/nimeshgaria/Employee-API-project.git
cd /Em/terraform

terraform init
terraform apply


In EC2 
git clone https://github.com/nimeshgaria/Employee-API-project.git

cd Empl

sudo docker compose pull
sudo docker compose up -d

Put the public key on EC2
cat employee-api-github-actions.pub

mkdir -p ~/.ssh
chmod 700 ~/.ssh

vim ~/.ssh/authorized_keys

enter - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMBxaRlC4Fnsfck33hZyUreDVnMq/vrQDv0gXf5t+GqI github-actions-employee-api

chmod 600 ~/.ssh/authorized_keys


Employee API DevOps Learning Project

to use terraform, install terraform in cloudshell and clone the project

1. Install Terraform

Run:

cd ~
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
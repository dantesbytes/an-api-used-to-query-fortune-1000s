provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "my_instance" {
  ami           = "ami-0c55b159cbfafe1f0" // Ubuntu 18.04 LTS
  instance_type = "t2.micro"
  tags = {
    Name = "MyEC2Instance"
  }
}

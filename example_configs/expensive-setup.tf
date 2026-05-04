# Example: Expensive/Sub-optimal Terraform Configuration

provider "aws" {
  region = "us-east-1"
}

# Expensive: Large instance when smaller would work
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "m5.2xlarge"  # EXPENSIVE - overkill for small app

  # Expensive: No auto-shutdown
  tags = {
    Name = "web-server"
  }
}

# Expensive: No caching
resource "aws_db_instance" "main" {
  allocated_storage    = 1000  # EXPENSIVE - very large storage
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.r5.4xlarge"  # EXPENSIVE - oversized
  username             = "admin"
  password             = "hardcoded-password"  # SECURITY ISSUE
  publicly_accessible  = true  # SECURITY ISSUE
  skip_final_snapshot  = true

  tags = {
    Name = "database"
  }
}

# Expensive: Single NAT Gateway (could be optimized)
resource "aws_nat_gateway" "main" {
  allocation_id = aws_eip.main.id
  subnet_id     = aws_subnet.public.id

  tags = {
    Name = "nat"
  }
}

resource "aws_eip" "main" {
  domain = "vpc"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}

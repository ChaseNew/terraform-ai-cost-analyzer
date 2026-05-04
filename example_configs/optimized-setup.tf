# Example: Optimized Terraform Configuration

provider "aws" {
  region = "us-east-1"
}

# OPTIMIZED: Right-sized instance with auto-shutdown
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"  # Cost-effective, right-sized

  # Auto-shutdown to prevent idle charges
  instance_initiated_shutdown_behavior = "terminate"

  tags = {
    Name        = "web-server"
    CostCenter  = "engineering"
    Environment = "production"
  }
}

# OPTIMIZED: Right-sized database with encryption
resource "aws_db_instance" "main" {
  allocated_storage   = 20  # Right-sized for actual needs
  engine              = "mysql"
  engine_version      = "8.0"
  instance_class      = "db.t3.micro"  # Cost-effective
  username            = var.db_username
  password            = random_password.db_password.result
  publicly_accessible = false  # Security best practice

  # Encryption for security
  storage_encrypted = true

  # Automated backups
  backup_retention_period = 7
  skip_final_snapshot     = false

  tags = {
    Name = "database"
  }
}

# Variables for security (not hardcoded)
variable "db_username" {
  type        = string
  sensitive   = true
  description = "Database admin username"
}

resource "random_password" "db_password" {
  length  = 16
  special = true
}

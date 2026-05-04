"""
Terraform Configuration Parser

Reads and parses Terraform .tf files to extract:
- Resources
- Variables
- Outputs
- Configuration details
"""

import os
from pathlib import Path


class TerraformParser:
    """Parse Terraform configuration files."""

    def __init__(self, config_path):
        """
        Initialize parser with path to Terraform config.

        Args:
            config_path: Path to .tf file or directory containing .tf files
        """
        self.config_path = Path(config_path)
        self.configs = {}

    def read_config(self):
        """
        Read Terraform configuration files.

        Returns:
            dict: Raw Terraform configuration content
        """
        if self.config_path.is_file():
            # Single file
            return self._read_file(self.config_path)
        elif self.config_path.is_dir():
            # Directory - read all .tf files
            all_content = ""
            for tf_file in self.config_path.glob("*.tf"):
                all_content += self._read_file(tf_file)
                all_content += "\n\n"
            return all_content
        else:
            raise FileNotFoundError(f"Path not found: {self.config_path}")

    def _read_file(self, file_path):
        """Read a single Terraform file."""
        with open(file_path, 'r') as f:
            return f.read()

    def extract_summary(self):
        """
        Extract high-level information from Terraform config.

        Returns:
            dict: Summary of resources, providers, etc.
        """
        content = self.read_config()

        # Count resource types
        resource_types = {}
        for line in content.split('\n'):
            if line.strip().startswith('resource "'):
                # Extract resource type
                # Example: resource "aws_ec2_instance" "example" {
                parts = line.strip().split('"')
                if len(parts) >= 2:
                    resource_type = parts[1]
                    resource_types[resource_type] = resource_types.get(resource_type, 0) + 1

        return {
            "total_lines": len(content.split('\n')),
            "resource_count": sum(resource_types.values()),
            "resource_types": resource_types,
            "raw_content": content
        }

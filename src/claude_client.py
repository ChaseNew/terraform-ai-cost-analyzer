"""
Claude AI Client

Handles all communication with the Anthropic Claude API.
Sends Terraform configurations for analysis and receives recommendations.
"""

import os
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv


class ClaudeAnalyzer:
    """Analyze Terraform configs using Claude AI."""

    def __init__(self):
        """Initialize Claude client with API key from environment."""
        # Load .env from project root (one level up from src/)
        env_path = Path(__file__).parent.parent / ".env"
        load_dotenv(dotenv_path=env_path)
        self.api_key = os.getenv("ANTHROPIC_API_KEY")

        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY not found in environment. "
                "Please create a .env file with your API key."
            )

        self.client = Anthropic(api_key=self.api_key)
        self.model = "claude-3-5-sonnet-20241022"

    def analyze_terraform(self, terraform_config: str) -> str:
        """
        Analyze Terraform configuration and return recommendations.

        Args:
            terraform_config: Raw Terraform configuration as string

        Returns:
            str: Claude's analysis and recommendations
        """
        system_prompt = """You are an expert cloud infrastructure engineer specializing in AWS and Azure.

Your job is to analyze Terraform configurations and provide:
1. **Cost Optimization** - Identify ways to reduce AWS/Azure spending
2. **Security Improvements** - Spot security vulnerabilities or best practice violations
3. **Architecture Recommendations** - Suggest better design patterns
4. **Automation Opportunities** - Identify automation improvements

Provide specific, actionable recommendations. Include estimated cost savings where possible.

Format your response as:
## Cost Optimization
[recommendations]

## Security Improvements
[recommendations]

## Architecture Recommendations
[recommendations]

## Automation Opportunities
[recommendations]

## Summary
[brief summary of key findings]
"""

        message = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": f"Please analyze this Terraform configuration:\n\n{terraform_config}"
                }
            ]
        )

        return message.content[0].text

    def cost_estimate(self, terraform_config: str) -> str:
        """
        Estimate AWS/Azure costs based on Terraform config.

        Args:
            terraform_config: Raw Terraform configuration as string

        Returns:
            str: Cost estimation and recommendations
        """
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system="You are a cloud cost expert. Estimate monthly AWS/Azure costs based on Terraform configurations.",
            messages=[
                {
                    "role": "user",
                    "content": f"Estimate the monthly cost for this infrastructure:\n\n{terraform_config}"
                }
            ]
        )

        return message.content[0].text

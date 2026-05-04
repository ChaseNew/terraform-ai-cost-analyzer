# Terraform AI Cost Analyzer

An intelligent tool that analyzes Terraform configurations using Claude AI to identify cost optimization opportunities, security improvements, and architectural recommendations.

## Features

✨ **AI-Powered Analysis** — Uses Claude API to provide intelligent recommendations
💰 **Cost Optimization** — Identifies expensive configurations and suggests cost-saving alternatives
🔒 **Security Review** — Spots security vulnerabilities and best practice violations
🏗️ **Architecture Insights** — Recommends better design patterns and infrastructure approaches
⚡ **Automation Opportunities** — Suggests ways to improve infrastructure automation

## Quick Start

### Prerequisites
- Python 3.9+
- Claude API key (get one at https://console.anthropic.com)

### Installation

```bash
# Clone repository
git clone https://github.com/ChaseNew/terraform-ai-cost-analyzer.git
cd terraform-ai-cost-analyzer

# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
echo "ANTHROPIC_API_KEY=your-key-here" > .env
```

### Usage

```bash
# Analyze a single Terraform file
python src/main.py path/to/your/config.tf

# Analyze all .tf files in a directory
python src/main.py path/to/terraform/directory

# Try the included examples
python src/main.py example_configs/expensive-setup.tf
```

## Example Output

The tool analyzes your Terraform configuration and provides:

- **Resource Summary** — Total resources and types detected
- **Cost Optimization** — Specific ways to reduce spending (with estimated savings)
- **Security Improvements** — Vulnerabilities and best practice violations
- **Architecture Recommendations** — Better design patterns
- **Automation Opportunities** — Ways to improve infrastructure-as-code
- **Cost Estimation** — Estimated monthly AWS/Azure costs

## Project Structure

```
terraform-ai-cost-analyzer/
├── src/                          # Main application code
│   ├── main.py                  # Entry point
│   ├── terraform_parser.py       # Reads .tf files
│   ├── claude_client.py          # Claude API integration
│   └── analyzer.py              # Analysis orchestrator
├── example_configs/              # Sample Terraform files
│   ├── expensive-setup.tf       # Example of sub-optimal config
│   └── optimized-setup.tf       # Example of optimized config
├── docs/                         # Documentation
├── tests/                        # Unit tests
├── requirements.txt              # Python dependencies
├── .env                         # API key (not in git)
└── README.md                    # This file
```

## How It Works

1. **Parse Terraform** — Reads and extracts configuration details
2. **Send to Claude** — Submits configuration to Claude API with analysis prompts
3. **Get Recommendations** — Claude analyzes and provides structured recommendations
4. **Display Results** — Formats and presents findings to the user

## Use Cases

- 💼 **Portfolio Projects** — Optimize costs before deployment
- 🔍 **Code Reviews** — Get a second opinion on infrastructure design
- 📚 **Learning** — Understand best practices from AI feedback
- 🚀 **Optimization** — Find cost savings in existing infrastructure
- 🛡️ **Security** — Identify security issues before they become problems

## Example: Expensive Config Analysis

Try analyzing the included expensive configuration:

```bash
python src/main.py example_configs/expensive-setup.tf
```

This example includes:
- Oversized EC2 instances (m5.2xlarge when t3.micro would work)
- Oversized database (db.r5.4xlarge when db.t3.micro is sufficient)
- Hardcoded passwords
- Publicly accessible database
- No encryption

Claude will identify all of these and suggest improvements with cost estimates.

## Technologies

- **Python 3.9+** — Core language
- **Anthropic Claude API** — AI analysis engine
- **python-dotenv** — Environment variable management

## Installation Requirements

```
anthropic>=0.7.0
python-dotenv>=1.0.0
```

## Future Enhancements

- [ ] Multi-file analysis with dependency mapping
- [ ] Historical comparison (track improvements over time)
- [ ] Integration with Terraform Cloud/Enterprise
- [ ] Cost projection over time
- [ ] Automated fix suggestions
- [ ] Custom analysis templates
- [ ] Web interface

## Contributing

This is a portfolio project, but contributions are welcome! Feel free to:
- Suggest new features
- Report issues
- Improve documentation
- Optimize code

## License

This project is open source and available under the MIT License.

## About

Built with Claude API to demonstrate:
- AI integration in cloud tools
- Terraform automation
- Python best practices
- Cloud cost optimization

Learn more about Claude at https://claude.ai

---

**Created by:** Chase Newman  
**GitHub:** https://github.com/ChaseNew  
**Contact:** chase@newfolio.com
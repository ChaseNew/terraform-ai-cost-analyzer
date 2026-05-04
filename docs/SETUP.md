# Setup Instructions

## Prerequisites

- Python 3.9+
- Claude API key (from https://console.anthropic.com)
- Git

## Installation Steps

1. **Clone the repository**
   ```
   git clone https://github.com/ChaseNew/terraform-ai-cost-analyzer.git
   cd terraform-ai-cost-analyzer
   ```

2. **Create virtual environment**
   ```
   python -m venv venv
   ```

3. **Activate virtual environment**
   - Windows: `.\venv\Scripts\Activate.ps1`
   - Mac/Linux: `source venv/bin/activate`

4. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

5. **Create .env file**
   Create a file named `.env` in the project root with:
   ```
   ANTHROPIC_API_KEY=your-api-key-here
   ```

6. **Run the tool**
   ```
   python src/main.py example_configs/expensive-setup.tf
   ```

## Usage

### Analyze a single Terraform file
```
python src/main.py path/to/your/file.tf
```

### Analyze all Terraform files in a directory
```
python src/main.py path/to/directory
```

### Example
```
python src/main.py example_configs/expensive-setup.tf
```

## Output

The tool will display:
1. Resource summary
2. Cost optimization recommendations
3. Security improvements
4. Architecture recommendations
5. Automation opportunities
6. Cost estimation

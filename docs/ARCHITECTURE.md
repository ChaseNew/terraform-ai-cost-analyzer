# Architecture Overview

## How It Works

```
User runs program
    ↓
main.py receives Terraform file path
    ↓
TerraformParser reads the file
    ↓
ClaudeAnalyzer sends to Claude API
    ↓
Claude analyzes and returns recommendations
    ↓
Results displayed to user
```

## Component Details

### TerraformParser
- **Job:** Read Terraform files and extract information
- **Methods:**
  - `read_config()` - Read single file or directory
  - `extract_summary()` - Count resources, identify types

### ClaudeAnalyzer
- **Job:** Talk to Claude API
- **Methods:**
  - `analyze_terraform()` - Full analysis (cost, security, architecture)
  - `cost_estimate()` - Just cost estimation

### AnalysisOrchestrator
- **Job:** Coordinate the workflow
- **Methods:**
  - `run_full_analysis()` - Run everything
  - `display_results()` - Format output nicely

### main.py
- **Job:** Entry point, handle command-line arguments
- Parses user input
- Calls orchestrator
- Shows results

## Data Flow

1. **Input:** User provides path to Terraform file(s)
2. **Parsing:** Extract configuration content
3. **API Call:** Send to Claude with system prompt
4. **Analysis:** Claude returns structured recommendations
5. **Output:** Display results to user

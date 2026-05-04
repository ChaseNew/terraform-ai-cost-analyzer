"""
Terraform AI Cost Analyzer - Main Entry Point

Usage:
    python main.py <path-to-terraform-file-or-directory>

Examples:
    python main.py ../example_configs/expensive-setup.tf
    python main.py ../example_configs
"""

import sys
from pathlib import Path
from analyzer import AnalysisOrchestrator


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python main.py <path-to-terraform-config>")
        print("\nExamples:")
        print("  python main.py ../example_configs/expensive-setup.tf")
        print("  python main.py ../example_configs")
        sys.exit(1)

    config_path = sys.argv[1]

    # Verify path exists
    if not Path(config_path).exists():
        print(f"[ERROR] Path not found: {config_path}")
        sys.exit(1)

    try:
        orchestrator = AnalysisOrchestrator(config_path)
        results = orchestrator.run_full_analysis()
        orchestrator.display_results(results)

        # Also run cost analysis
        print("\nCOST ESTIMATION")
        print("=" * 80)
        cost_analysis = orchestrator.run_cost_analysis()
        print(cost_analysis)

    except Exception as e:
        print(f"[ERROR] {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

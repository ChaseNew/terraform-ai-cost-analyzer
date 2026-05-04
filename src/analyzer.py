"""
Main Analysis Orchestrator

Coordinates:
1. Reading Terraform files (TerraformParser)
2. Sending to Claude (ClaudeAnalyzer)
3. Formatting and displaying results
"""

from terraform_parser import TerraformParser
from claude_client import ClaudeAnalyzer


class AnalysisOrchestrator:
    """Coordinate the full analysis workflow."""

    def __init__(self, config_path):
        """
        Initialize analyzer.

        Args:
            config_path: Path to Terraform file or directory
        """
        self.parser = TerraformParser(config_path)
        self.claude = ClaudeAnalyzer()

    def run_full_analysis(self):
        """
        Run complete analysis pipeline.

        Returns:
            dict: Complete analysis results
        """
        print("[*] Reading Terraform configuration...")
        config_content = self.parser.read_config()
        summary = self.parser.extract_summary()

        print(f"[+] Found {summary['resource_count']} resources")
        print("\n[*] Analyzing with Claude AI...")

        # Get analysis
        analysis = self.claude.analyze_terraform(config_content)

        print("[+] Analysis complete\n")

        return {
            "summary": summary,
            "analysis": analysis,
            "config_path": str(self.parser.config_path)
        }

    def run_cost_analysis(self):
        """
        Run cost estimation analysis.

        Returns:
            str: Cost analysis results
        """
        print("[*] Analyzing costs...")
        config_content = self.parser.read_config()
        cost_estimate = self.claude.cost_estimate(config_content)
        print("[+] Cost analysis complete\n")
        return cost_estimate

    def display_results(self, results):
        """
        Display analysis results in formatted output.

        Args:
            results: Results dict from run_full_analysis()
        """
        print("=" * 80)
        print("TERRAFORM ANALYSIS REPORT")
        print("=" * 80)
        print(f"\nConfiguration: {results['config_path']}")
        print(f"Summary:")
        print(f"   - Total resources: {results['summary']['resource_count']}")
        print(f"   - Resource types: {len(results['summary']['resource_types'])}")

        print("\n" + "=" * 80)
        print("ANALYSIS")
        print("=" * 80)
        print(results['analysis'])
        print("\n" + "=" * 80)

import argparse
from log_processor import LogProcessor
from report_generator import ReportGenerator
from output_formatter import OutputFormatter

class LogAnalyzer:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='for processing log files and generating reports')
        self.parser.add_argument('--file', required=True, help='path to log file')
        self.parser.add_argument('--report', required=True, help='report type')
        self.parser.add_argument('--date', help='filter logs by date (YYYY-MM-DD)')
        self.args = self.parser.parse_args()

    def run(self):
        log_processor = LogProcessor(self.args.file, self.args.date)
        logs = log_processor.parse_logs()

        if self.args.report == 'average':
            report = ReportGenerator.generate_average_report(logs)
        else:
            raise ValueError(f'unknown report type: {self.args.report}')
        
        OutputFormatter.format_report(report, self.args.report)

if __name__ == '__main__':
    analyzer = LogAnalyzer()
    analyzer.run()
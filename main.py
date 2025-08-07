import json 
import tabulate
import argparse

def process_log(file_paths, report_type):
    endpoints = {}

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    log = json.loads(line)
                except Exception:
                    continue
                endpoint = log.get('url')
                response_time = log.get('response_time')
                if endpoint and response_time is not None:
                    if endpoint not in endpoints:
                        endpoints[endpoint] = {'count': 0, 'total_time': 0}
                    endpoints[endpoint]['count'] += 1
                    endpoints[endpoint]['total_time'] += response_time

    if report_type == 'average':
        report = []
        for endpoint, data in endpoints.items():
            avg_time = data['total_time'] / data['count']
            report.append([endpoint, data['count'], round(avg_time, 4)])
        print(tabulate.tabulate(report, headers=['Endpoint', 'Requests', 'Avg Response Time (s)']))
    else:
        print(f"Unknown report type: {report_type}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log file analyzer")
    parser.add_argument('--file', nargs='+', required=True, help='Path(s) to log file(s)')
    parser.add_argument('--report', required=True, help='Report type (e.g., average)')
    args = parser.parse_args()
    process_log(args.file, args.report)
            

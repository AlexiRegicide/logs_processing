from collections import defaultdict
import re

class ReportGenerator:
    @staticmethod
    def generate_average_report(logs):
        endpoints = {}
        for log in logs:
            endpoint = log.get('url')
            response_time = log.get('response_time')
            if endpoint and response_time is not None:
                if endpoint not in endpoints:
                    endpoints[endpoint] = {'count': 0, 'total_time': 0}
                endpoints[endpoint]['count'] += 1
                endpoints[endpoint]['total_time'] += response_time

        report = []
        for endpoint, data in endpoints.items():
            avg_time = data['total_time'] / data['count']
            report.append([endpoint, data['count'], avg_time])
        
        return report
    
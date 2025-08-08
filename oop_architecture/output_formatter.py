import tabulate 

class OutputFormatter:
    @staticmethod
    def format_report(report, report_type):
        if report_type == 'average':
            headers = ['endpoint', 'requests', 'average response time']
        else:
            raise ValueError(f"unknown report type {report_type}")
        
        print(tabulate.tabulate(report, headers=headers))
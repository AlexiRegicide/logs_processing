import json

class LogProcessor:
    def __init__(self, file_path, date_filter=None):
        self.file_path = file_path
        self.date_filter = date_filter

    def parse_logs(self):
        logs = []
        with open(self.file_path, 'r') as file:
            for line in file:
                try:
                    logs.append(json.loads(line))
                except:
                    continue
        
        if self.date_filter:
            logs = [log for log in logs if log['@timestamp'].startswith(self.date_filter)]

        return logs
    
    
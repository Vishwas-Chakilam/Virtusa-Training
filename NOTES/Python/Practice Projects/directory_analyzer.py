import os
import sys

class DirectoryAnalyzer:
    def __init__(self, path):
        self.path = path
        self.stats = {"files": 0, "dirs": 0, "size_bytes": 0}

    def analyze(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError("Directory not found")
            
        for root, dirs, files in os.walk(self.path):
            self.stats["dirs"] += len(dirs)
            self.stats["files"] += len(files)
            for f in files:
                try:
                    fp = os.path.join(root, f)
                    self.stats["size_bytes"] += os.path.getsize(fp)
                except OSError:
                    pass

    def report(self):
        mb = self.stats["size_bytes"] / (1024 * 1024)
        print(f"Analysis for: {self.path}")
        print(f"Directories: {self.stats['dirs']}")
        print(f"Files: {self.stats['files']}")
        print(f"Total Size: {mb:.2f} MB")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    analyzer = DirectoryAnalyzer(target)
    try:
        analyzer.analyze()
        analyzer.report()
    except Exception as e:
        print(f"Error: {e}")
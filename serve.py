#!/usr/bin/env python3
"""Local server cho site Ethan — hỗ trợ clean URL (/gioi-thieu -> gioi-thieu.html).
Chạy: python3 serve.py [port]   (mặc định 8000)
"""
import os, sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))

class CleanURLHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        full = super().translate_path(path)
        # /duong-dan không có đuôi -> thử duong-dan.html
        if not os.path.exists(full):
            base = full.rstrip("/")
            if os.path.isfile(base + ".html"):
                return base + ".html"
        return full

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    os.chdir(ROOT)
    print(f"→ http://localhost:{port}/  (Ctrl+C để dừng)")
    ThreadingHTTPServer(("", port), CleanURLHandler).serve_forever()

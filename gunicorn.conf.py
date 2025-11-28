# Gunicorn configuration for Railway deployment
import os

# Bind to the port Railway provides
bind = f"0.0.0.0:{os.environ.get('PORT', 8000)}"

# Number of worker processes
workers = int(os.environ.get('WEB_CONCURRENCY', 2))

# Number of threads per worker
threads = int(os.environ.get('DJANGO_THREADS', 4))

# Timeout for worker processes
timeout = 30

# Keepalive timeout
keepalive = 5

# Maximum number of simultaneous connections
max_requests = 1000
max_requests_jitter = 100

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process naming
proc_name = "mi_proyecto"

# Worker class
worker_class = "sync"

# Preload the application
preload_app = True

# Graceful timeout
graceful_timeout = 30

# Worker connections (for eventlet/gevent workers)
worker_connections = 1000

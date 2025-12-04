#!/usr/bin/env python3
from pyngrok import ngrok

# Start ngrok tunnel
public_url = ngrok.connect(8000)
print(f"\nPublic URL: {public_url}")
print(f"\nAccess your Django app at: {public_url}")
print("\nPress Ctrl+C to stop the tunnel\n")

try:
    # Keep the tunnel open
    import time
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nShutting down tunnel...")
    ngrok.kill()

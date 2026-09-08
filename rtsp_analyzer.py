#!/usr/bin/env python3
"""
RTSP Protocol Analyzer
Tests RTSP endpoints for vulnerabilities and misconfigurations
"""

import socket
import sys

def test_rtsp_endpoint(host, port=554, timeout=3):
    """Test RTSP endpoint for accessibility and authentication"""
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((host, port))
        
        # Send OPTIONS request
        request = b'OPTIONS * RTSP/1.0\r\nCSeq: 1\r\nConnection: close\r\n\r\n'
        s.send(request)
        
        response = s.recv(4096).decode('utf-8', errors='ignore')
        s.close()
        
        # Analyze response
        if '200' in response:
            print(f"[+] {host}:{port} - RTSP endpoint accessible")
        elif '401' in response or '407' in response:
            print(f"[-] {host}:{port} - Authentication required (401/407)")
        else:
            print(f"[?] {host}:{port} - Unknown response")
            
        return response
        
    except socket.timeout:
        print(f"[-] {host}:{port} - Connection timeout")
    except ConnectionRefusedError:
        print(f"[-] {host}:{port} - Connection refused")
    except Exception as e:
        print(f"[!] {host}:{port} - Error: {e}")
    
    return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 rtsp_analyzer.py <host> [port]")
        sys.exit(1)
    
    host = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 554
    
    test_rtsp_endpoint(host, port)

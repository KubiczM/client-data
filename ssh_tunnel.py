"""
SSH Tunnel Management.

Provides a function to establish a secure SSH tunnel for database connections.
"""


from sshtunnel import SSHTunnelForwarder
from config import SSH_HOST, SSH_PORT, SSH_USER, SSH_PASSWORD, DB_HOST, DB_PORT

LOCAL_PORT = 3307

def start_ssh_tunnel():
    tunnel = SSHTunnelForwarder(
        (SSH_HOST, SSH_PORT),
        ssh_username=SSH_USER,
        ssh_password=SSH_PASSWORD,
        remote_bind_address=(DB_HOST, DB_PORT),
        local_bind_address=("127.0.0.1", LOCAL_PORT),
    )
    tunnel.start()
    print(f"SSH Tunnel established: {tunnel.local_bind_address}")
    return tunnel, LOCAL_PORT

def stop_ssh_tunnel(tunnel):
    if tunnel:
        tunnel.stop()
        print("SSH Tunnel stopped")


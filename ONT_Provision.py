from paramiko import SSHClient
import paramiko

class SSH:
   def __init__(self):
      self.ssh = SSHClient()
      self.ssh.load_system_host_keys()
      self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      self.ssh.connect(hostname='10.10.200.120',username='root',password='root')

   def exec_cmd(self,cmd):
      stdin,stdout,stderr = self.ssh.exec_command(cmd)
      if stderr.channel.recv_exit_status() != 0:
         print stderr.read()
      else:
         print stdout.read()

if __name__ == '__main__':
   ssh = SSH()
   ssh.exec_cmd("apt-get update"a)

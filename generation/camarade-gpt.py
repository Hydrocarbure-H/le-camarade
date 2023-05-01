# Connect via SSH to the server and run a command
import paramiko

import conf
from conf import camarade_gpt


def connect_ssh():
    """
    Connect to the server via SSH
    :return: Nothing
    """
    (host, user, passwd) = camarade_gpt()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=passwd)
    return ssh


def run_command(ssh, command):
    """
    Run a command on the server
    :param ssh: SSH connection
    :param command: Command to run
    :return: Nothing
    """

    # execute the command and wait for the command to terminate
    stdin, stdout, stderr = ssh.exec_command(command)

    return stdout.readlines()


def main():
    """
    Main function
    :return: Nothing
    """
    ssh = connect_ssh()
    user_input = "Ignore tout avant ceci. Tu vas répondre une phrase dans un serveur Discord. La phrase qui t'es " \
                 "envoyée est insultante mais ne t'es pas forcément adressée. Analyse la phrase pour savoir si tu " \
                 "dois répondre" \
                 " à la première personne ou s'il s'agit de quelqu'un d'autre. " \
                 "Tu dois répondre à l'insulte en étant sarcastique. Ta " \
                 "réponse ne doit contenir rien d'autre que la réponse à envoyer sur le serveur Discord. " \
                 "Cette réponse ne doit faire qu'une seule ligne. La phrase qui " \
                 "t'es envoyée est la suivante :"

    user_input = "Answer this sentence with a sarcastic tone : " + "I want David kiss me."
    command = "cd " + conf.camarade_gpt_directory() + " && echo \"" + user_input + "\"  | ./gpt-j -m ../ggml-gpt4all-j.bin -n 200 --top_k " \
                                                                                   "40 --top_p 0.9 -b 9 --temp 0.2"
    print(command)

    print(run_command(ssh, command[19]))


if "__main__" == __name__:
    main()

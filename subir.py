import subprocess

comandos= [
    ["git", "add", "."],
    ["git", "commit", "-m", "secondcommit"],
    ["git", "branch", "-M", "main"],
    ["git", "push"]
    ]
for comando in comandos:
    subprocess.run(comando, capture_output=True, text=True)
print("Subida de cambios exitosa")
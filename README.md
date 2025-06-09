Utilizando Python 3.12 em conjunto com as bibliotecas do Python “Flask” e “Request”:
-> No Prompt de Comando digitar ambas as linhas separadamente para a instalação das bibliotecas:

# AMBIENTE VIRTUAL

---

py -m venv ./Conceissionaria
pip install flask  
pip install requests

# OR

py -m venv ./Conceissionaria
pip install -r .\requirements\requirements.txt

---

# MAQUINA GLOBAL

---

pip install flask  
pip install requests

# OR

## pip install -r .\requirements\requirements.txt

===========================================================================================================================
Rode o primeiro o comando (caso isso nao seja feito, vai tomar erro de compilacao):
flask --app .\routes\provedor\concessionaria_provedor.py run
===========================================================================================================================

===========================================================================================================================
Logo em seguida, em outro cmd ou manualmente faca:
py .\api\consumidor\concessionaria_consumidor.py

ou

comandos curls manuais.

Verifique se o Visual Code Studio está apto a rodar programas com Web Service
Apenas testar se o código segue funcionando sem mais problemas.

FROM python:3.9-buster
WORKDIR /app
ADD . .
RUN pip install -r requirements.txt
#Caso a aplicação tenha contexto00
#ENV SERVER_CONTEXT_PATH=/cobertura/
ENTRYPOINT python cobertura.py
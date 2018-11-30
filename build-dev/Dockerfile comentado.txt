FROM python:3.6
LABEL maintainer 'Ricardo Resende official maintainer <ricardovmr at github.com>'

RUN useradd www && \
	mkdir /app && \
	mkdir /log && \
	chown www /log   #Dono da pasta /log vai ser o www

USER www #usuario logado quando os processos dentro do container forem iniciados/executados

VOLUME /log    #volume que ira apontar para a pasta /log
WORKDIR /app   #diretório de trabalho
EXPOSE 8000    #porta exposta e que nosso servidor irá escutar

ENTRYPOINT ["/usr/local/bin/python"]  #ponto de entrada ou processo que será executado quando o container for iniciado. Aqui está apontando para a pasta onde o python está. instalado

CMD ["run.py"]  #parâmetro que será passado para o ENTRYPOINT. Este comando irá chamar o nosso arquivo do servidor e executá-lo





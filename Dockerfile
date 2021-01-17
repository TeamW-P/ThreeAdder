FROM continuumio/anaconda3

WORKDIR /three_adder

COPY . .

RUN chmod +x boot.sh
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "adder_env", "/bin/bash", "-c"]


EXPOSE 5003

ENTRYPOINT ["conda", "run", "-n", "adder_env", "./boot.sh"]
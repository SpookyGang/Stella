WORKDIR /rikudo

RUN chmod 777 /rikudo

#sorry for noob dockerfile

RUN sudo apt-get update
RUN sudo apt install upgrade 
RUN sudo apt install python3-pip
RUN git clone https://github.com/SpookyGang/Stella.git
RUN cd Stella
RUN pip3 install --no-cache-dir -U -r requirements.txt

#fuck I'm noob in docker 

CMD ["python3", "-m", "Stella"]

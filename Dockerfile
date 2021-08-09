RUN sudo apt-get update
RUN sudo apt install upgrade 
RUN sudo apt install python3-pip
RUN git clone https://github.com/SpookyGang/Stella.git
RUN cd Stella
RUN pip3 install -r requirements.txt
RUN python3 -m Stella

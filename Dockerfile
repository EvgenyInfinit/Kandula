FROM --platform=linux/amd64 python:3.9-slim

# TODO: You need to copy the project files to the Docker and install the dependencies
#RUN mkdir /kandula
WORKDIR /kandula
COPY . /kandula/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#ENV FLASK_ENV=development
# RUN <<EOF
# FLASK_APP=run.py FLASK_DEBUG=1 flask run
# EOF
ENV FLASK_APP=run.py 
ENV FLASK_DEBUG=1

#ENTRYPOINT ["/bin/bash"]
#CMD ["python" , "run.py"]
CMD ["/bin/bash", "bin/run"]

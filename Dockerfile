#base image
FROM python
COPY . /python-docker
WORKDIR /python-docker
RUN pip install numpy
CMD python solve.py
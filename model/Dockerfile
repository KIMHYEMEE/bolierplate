FROM python:3.9

WORKDIR /code

RUN export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
RUN export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
RUN pip install --upgrade pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
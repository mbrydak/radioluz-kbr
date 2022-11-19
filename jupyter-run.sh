#!/bin/env bash

HOST_USER=$(who | awk '{print $1}')
HOST_UID=$(id -u)
HOST_GID=$(id -g)


podman run --rm  --privileged -p 8888:8888 --name jupyter -v $(pwd)/data:/home/jovyan/work jupyter/base-notebook

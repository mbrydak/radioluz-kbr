#!/bin/env bash

podman run --privileged -it --rm -v $(pwd)/data/data_raw:/app/data kbr-scraper

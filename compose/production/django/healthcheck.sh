#!/bin/bash
curl localhost:5000/healthz/ || (echo 'Health check failed' && exit 1)

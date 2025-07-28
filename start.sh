#!/bin/bash
echo "Starting Essanbot..."
uvicorn main:app --host 0.0.0.0 --port 8000

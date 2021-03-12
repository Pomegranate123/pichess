#!/bin/sh
cd frontend
npm install && npm run build && docker-compose build

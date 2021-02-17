#!/bin/sh
cd frontend
npm run build && docker-compose build

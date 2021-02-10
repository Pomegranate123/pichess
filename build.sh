#!/bin/sh

rm build
mkdir build

# Compile backend
cd backend/pichess || exit
python manage.py runserver || exit

cd .. || exit
cd .. || exit
#cp backend/target/debug/server build/

# Make database
#./backend/target/debug/db init build/db.sqlite || exit

# Compile frontend
cd frontend || exit

npm run build || exit

cd .. || exit

cp -r frontend/dist build

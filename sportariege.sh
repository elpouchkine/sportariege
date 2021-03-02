#!/bin/sh
function baseDonnees
{
echo "hello"
}

function server
{
cd sportariege
. ariege/bin/activate
cd sportariege
./manage.py runserver
}

server

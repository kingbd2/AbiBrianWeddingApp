#!/usr/bin/env bash
gnome-terminal -- python3 manage.py livereload 
gnome-terminal -- python3 manage.py runserver localhost:8000 
gnome-terminal -- yarn run dev 
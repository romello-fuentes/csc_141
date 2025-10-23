# imports_demo.py

import greetings
greetings.greet_user('Alice')

from greetings import greet_user
greet_user('Bob')

from greetings import greet_user as gu
gu('Charlie')

import greetings as gr
gr.greet_user('Dana')

from greetings import *
greet_user('Eli')

# GDG-HackFest
Repository for GDG HackFest @ KIIT Bhubaneswar

## Problem Statement
Make an application which can read data from a PDF ( example voter list, bill) and push the data items to a structured database (you can choose any database, firebase is good too)

## Aproach

The program uses `pdfminer.six` to convert the pdf into a `xml file`, which is parsed according to a templating rule written in `yaml` to create the final `json object` that will be sent to the database

## Dependencies and Modules used

- pdfminer.six
- pyyaml
- pyrebase
- os
- Framework: Django


## Contributors

A group of students from ITER, SOA Deemed to be University
- Debashish Mishra
- Pulak Kumar Das
- Ritvik Menon
- Syed Salif Moin
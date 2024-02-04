# Projet: data filter

## Description

The aim of this project is to create a program for loading, saving, filtering,
sort and display data from files in CSV Json XML or yaml format.

## Requirements

```
cat requirements/requirement.txt
```

## Installation

#### If you don't have `python3`, `pip`, `venv`, `git`:

```
sudo apt install python3 python3-pip python3-venv git       # Ubuntu/debian 
```
```
sudo dnf install python3 python3-pip python3-venv git       # red hat
```

 #### Clone Repository 

```
git clone git@github.com:yahia-adam/DataFilter.git          # Clone Repository 

cd DataFilter                                               # Change to project Root Directory

python3 -m venv env                                         # Create python virtual envirements 

pip install -r ./requirements/dependencies.txt              # Install project dependencies
```

## Usage

```
python3 src/main.py
```

## Directory structure

```
|-- datas                       <- Project datas
|   |-- inputs                  <- Input datas
|   |-- outputs                 <- Output datas
|-- src                         <- Source files
|-- requirements                <- Project requirements
|   |-- dependencies.txt        <- python dependencies
|   |-- sys_requirement.txt     <- system requirements
|-- Sujet                       <- project details
|   |-- Sujet.pdf               <- Project Sujet
|   |-- Syllabus.pdf            <- Project Syllabus
|-- README                      <- Project README
```

# Projet: data filter

## Description

Le but de ce projet est de créer un programme permettant de charger, sauvegarder, filtrer,
trier et afficher des données depuis des fichiers au format CSV Json XML ou yaml.

## Requirements

```
cat requirements/requirement.txt
```

## Installation

Make sure you have `python3`, `pip`, `venv` if not:

    ```
    sudo apt install python3 python3-pip python3-venv               # Ubuntu/debian 
    ```
    ```
    sudo dnf install python3 python3-pip python3-venv               # red hat
    ```

```
git clone git@github.com:yahia-adam/DataFilter.git          #Clone Repository 

cd DataFilter                                               #Change to project Root Directory

python3 -m venv env                                         #Create python virtual envirements 

pip install -r ./requirements/dependencies.txt               #Install project dependencies
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
import shutil
import zipfile
import io
import argparse
import re
import xml.etree.ElementTree as ET
import zipfile
import os
import sys
from pathlib import Path

doc_name = "temp/word/document.xml"
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


def extract_all(file):

    print("Path: " + file)
    zip = zipfile.ZipFile(file)
    zip.extractall("temp")



def read_doc(old, new):
    file=open(doc_name,'r',encoding='utf8',errors="ignore")
    xml_text = file.read()
    file.close()
    
    replaced = xml_text.replace(old, new)
    save_text(replaced)
    print("replaced: " + old + " with: " + new )

def save_text(text):
    file=open(doc_name, 'w', encoding='utf-8', errors='ignore')
    file.write(text)
    file.close()
    print("File saved")

def create_new_docx():

    shutil.make_archive('final.docx', 'zip', 'temp')


def replace_docx(old, new, file, name):
    
    extract_all(file)
    read_doc(old, new)
    create_new_docx()
    os.rename('final.docx.zip', name+".docx")
    
    


def generate(file_path, items, key):
    if os.path.isfile("final.docx.zip"):
        os.remove("final.docx.zip")
    for value in items:
        print(value)
        replace_docx(key, value, file_path, value)

script_location = Path(__file__).absolute().parent
os.chdir(script_location)


















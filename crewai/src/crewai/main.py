#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crewai.crew import Crewai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    doc_path = "src"
    with open(doc_path, "r", encoding="utf-8") as f:
        content = f.read()
    if not content:
        return
    inputs = {
        "content": content
    }
    Crewai().crew().kickoff(inputs=inputs)
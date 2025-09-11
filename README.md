# Introduction 

The LLM-generated Python code and unit tests based on the proposed dataset for evaluating LLMs generated code, developed for "Security and Quality in LLM-Generated Code: A Multi-Language, Multi-Model Analysis" research paper.
---

## Prerequisites

Before running the project and SonarQube scan, make sure the following are installed:

- [Python 3.12+](https://www.python.org/downloads/)
- [SonarQube Scanner](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/)

---

## Run the Project and Analyze

Run the compiler script:

```bash
python compiler.py

Run sonarqube scan
```
```bash
sonar-scanner.bat -D"sonar.organization=mohkharma"
```

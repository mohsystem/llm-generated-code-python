## Introduction 

The LLM-generated Python code and unit tests are based on the proposed dataset for evaluating LLM-generated code, developed for the research paper *"Security and Quality in LLM-Generated Code: A Multi-Language, Multi-Model Analysis"*.
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
```
Run sonarqube scan
```bash
sonar-scanner.bat -D"sonar.organization=mohkharma"
```

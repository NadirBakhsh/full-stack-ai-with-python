# Python Project Structure - Best Practices
```filestructure
my_project/
│
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       └── modules/
│           ├── __init__.py
│           ├── module1.py
│           └── module2.py
│
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
│
├── docs/
│   ├── index.md
│   └── api.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── exploration.ipynb
│
├── scripts/
│   └── setup_database.py
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
├── pyproject.toml
└── LICENSE
```
# Key Components:

- src/: Source code (importable package)
- tests/: Unit and integration tests
- docs/: Documentation files
- data/: Data files (excluded from git)
- notebooks/: Jupyter notebooks for exploration
- scripts/: Utility scripts
- requirements.txt: Dependencies
- setup.py or pyproject.toml: Package configuration
- .gitignore: Git exclusions
- README.md: Project overview
- .env.example: Environment variables template
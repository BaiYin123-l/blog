@echo off

pip-licenses.exe -sau --format=json > .\static\python-depends.json

.\node_modules\.bin\license-checker --production --json --out .\static\node-depends.json

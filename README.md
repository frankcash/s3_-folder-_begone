# S3 $folder$ Remove

Utility to remove $folder$ files from a desired S3 bucket.  Supports multiple paths.

## Running

Install deps in virtualenv:

```
virtualenv -p `which python3` venv
source venv/bin/activate
pip install -r requirements.txt
```

Then copy `config.sample.yaml` to `config.yaml` and update values.

Then run `python main.py`
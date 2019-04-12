# Helm YAML Template Linter


I wanted to lint some YAML templates for a
[Helm](https://helm.sh/docs/developing_charts/) chart, but `yamllint` doesn't
play nicely with the template syntax. So I wrote a small script to render
the templates and then run `yamllint` on those instead.

## Usage

This will:

1. Render all templates in the helm chart
2. Create a `rendered` directory to store files neatly.
3. Save them locally as `rendered/rendered-<template-filename>.yaml`
4. Run `yamllint` on each rendered template and output the results.
    - The linter was relaxed to make lines over length 80 just a warning
      instead of an error, due to potentially long template subsitutions.

```bash
python3 helm_template_linter.py <CHART>
```

Example linting errors:

```bash
$ python3 helm_template_linter.py stable/wordpress

rendered-nomadic-boxer-credentials-test
  11:3      error    wrong indentation: expected 4 but found 2  (indentation)
  28:81     warning  line too long (148 > 80 characters)  (line-length)
rendered-nomadic-boxer-mariadb-test-4funy
  21:7      error    wrong indentation: expected 8 but found 6  (indentation)
  35:7      error    wrong indentation: expected 8 but found 6  (indentation)
  41:3      error    wrong indentation: expected 4 but found 2  (indentation)
  48:1      error    too many blank lines (1 > 0)  (empty-lines)
rendered-master-configmap.yaml
  28:1      error    trailing spaces  (trailing-spaces)
  33:1      error    trailing spaces  (trailing-spaces)
rendered-tests.yaml
  10:81     warning  line too long (89 > 80 characters)  (line-length)
rendered-master-svc.yaml
  16:3      error    wrong indentation: expected 4 but found 2  (indentation)
rendered-deployment.yaml
  26:7      error    wrong indentation: expected 8 but found 6  (indentation)
  28:9      error    wrong indentation: expected 10 but found 8  (indentation)
  30:7      error    wrong indentation: expected 8 but found 6  (indentation)
  34:9      error    wrong indentation: expected 10 but found 8  (indentation)
  69:9      error    wrong indentation: expected 10 but found 8  (indentation)
  82:1      error    trailing spaces  (trailing-spaces)
  92:1      error    trailing spaces  (trailing-spaces)
  94:9      error    wrong indentation: expected 10 but found 8  (indentation)
  107:1     error    trailing spaces  (trailing-spaces)
  108:15    error    trailing spaces  (trailing-spaces)
  109:7     error    wrong indentation: expected 8 but found 6  (indentation)
rendered-master-statefulset.yaml
  37:11     error    wrong indentation: expected 12 but found 10  (indentation)
  45:7      error    wrong indentation: expected 8 but found 6  (indentation)
  49:9      error    wrong indentation: expected 10 but found 8  (indentation)
  64:9      error    wrong indentation: expected 10 but found 8  (indentation)
  68:81     warning  line too long (91 > 80 characters)  (line-length)
  76:81     warning  line too long (91 > 80 characters)  (line-length)
  84:1      error    trailing spaces  (trailing-spaces)
  86:9      error    wrong indentation: expected 10 but found 8  (indentation)
```

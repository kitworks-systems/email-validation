# Known issues

## Web validation form raises AttributeError on every non-empty email

Status: not fixed. Waiting for a decision on which message the form must show.

Modules: `kw_email_validation_web`, `kw_email_validation`.

Present in branches: 16.0, 17.0, 18.0, 19.0, 20.0 (the 20.0 branch has no `origin/20.0` yet; checked in the local 20.0 at 99d12c8).

### Symptom

On `/email_validation/validate` the validation of any non-empty address fails:

- the AJAX route `/email_validation/validate_ajax` returns a JSON-RPC error;
- the batch route `/email_validation/validate_batch` returns a server error;
- the page shows the row "Error - Failed to validate address"
  (`kw_email_validation_web/views/templates/email_validation_templates.xml:142`).

Empty input is handled before the failing line, so it works.

### Cause

`kw_email_validation_web/controllers/main.py` reads `validation.message`:

- line 48 and line 59 in `validate_email_batch` (specific validator and automatic selection);
- line 95 in `validate_email_ajax`.

`validation` is a `kw.email.validation` record. That model
(`kw_email_validation/models/email_validation.py`) has no `message` field.
`message` is defined on `kw.email.validation.result`
(`kw_email_validation/models/email_validation_result.py:25`), which is linked
through `kw.email.validation.result_ids`. Reading the missing attribute raises `AttributeError`.

### Open decision

Which text the form must show in the `message` column: the message of the
latest result, the messages of all results joined together, or a computed
field on `kw.email.validation`.

### Tests

`kw_email_validation_web/tests/test_controller.py` covers only the empty-email
paths (`test_batch_page_without_emails`, `test_ajax_empty_email`) and the form
page. There is no test for a non-empty address, because it would fail until the bug is fixed.

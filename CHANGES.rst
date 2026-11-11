Changelog
=========

0.0.9 (2026-11-11)
------------------

- added the `log_format_env_var` parameter to `init_logging` that allows overriding the logging format
  via this environment variable, to make it easy to change the format a runtime, e.g., for temporary
  debugging
- added the `filename_env_var` parameter to `init_logging` for overriding the filename to redirect the
  logging output to, e.g., for temporary turning on debugging output


0.0.8 (2026-07-23)
------------------

- added `log` method for outputting message via logger and to a specific log file (independent of logger setup)


0.0.7 (2026-07-16)
------------------

- added level `FATAL`
- added `logging_level_to_str` to turn int level into string representation


0.0.6 (2026-06-29)
------------------

- `add_logging_level` method now allows specifying the `default_level`


0.0.5 (2025-08-25)
------------------

- `add_logging_level` method now allows specifying the `destination` in the parsed namespace
- `add_logger_name` method now allows specifying the `destination` in the parse namespace,
  and either short or long option flag can be specified


0.0.4 (2025-08-25)
------------------

- `add_logging_level` method no longer requires short and long option flag to be specified together,
  one of them can be omitted (ie None)


0.0.3 (2025-01-14)
------------------

- using underscore in project name now


0.0.2 (2025-01-14)
------------------

- `init_logging` now supports specifying `stream` or `filename` or `handlers` as well as the `log_format`


0.0.1 (2023-11-30)
------------------

- initial release


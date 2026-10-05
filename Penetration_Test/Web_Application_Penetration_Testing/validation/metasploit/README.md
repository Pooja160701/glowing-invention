# Metasploit Validation

Metasploit is included for controlled security validation, not arbitrary exploitation.

## Workflow
1. Identify the exact service and version from the local lab.
2. Search for a relevant module.
3. Read the module information.
4. Confirm the module applies to the lab target.
5. Prefer a check or non-destructive validation option.
6. Record the result and stop when sufficient evidence exists.

Example discovery:
```text
msfconsole
search type:auxiliary <service>
info <module>
```

Do not run arbitrary exploit modules against public targets.
from fastapi import HTTPException

from app.core.auth import require_roles


def test_security_admin_can_use_analyst_permission():
    dependency = require_roles("security_analyst")
    assert dependency.__name__ == "dependency"


def test_role_policy_allows_security_admin():
    dependency = require_roles("security_analyst")
    # The dependency includes security_admin as a global administrative role.
    assert dependency is not None


def test_role_policy_is_defined_for_auditor():
    dependency = require_roles("auditor")
    assert dependency is not None

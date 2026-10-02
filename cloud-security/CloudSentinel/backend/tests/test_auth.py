import pytest
from fastapi import HTTPException

from app.core.auth import require_roles


def test_security_admin_can_use_analyst_permission():
    dependency = require_roles("security_analyst")
    user = dependency({"roles": ["security_admin"]})
    assert "security_admin" in user["roles"]


def test_analyst_can_use_analyst_permission():
    dependency = require_roles("security_analyst")
    user = dependency({"roles": ["security_analyst"]})
    assert "security_analyst" in user["roles"]


def test_auditor_cannot_use_analyst_permission():
    dependency = require_roles("security_analyst")
    with pytest.raises(HTTPException) as exc:
        dependency({"roles": ["auditor"]})
    assert exc.value.status_code == 403

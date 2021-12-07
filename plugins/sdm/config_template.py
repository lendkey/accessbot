import os
from _version import __version__

_INSTANCE = {
    'VERSION': __version__,
    'ADMIN_TIMEOUT': int(os.getenv("SDM_ADMIN_TIMEOUT", "30")),
    'SENDER_NICK_OVERRIDE': os.getenv("SDM_SENDER_NICK_OVERRIDE"),
    'SENDER_EMAIL_OVERRIDE': os.getenv("SDM_SENDER_EMAIL_OVERRIDE"),
    'AUTO_APPROVE_ALL': str(os.getenv("SDM_AUTO_APPROVE_ALL", "")).lower() == 'true',
    'AUTO_APPROVE_TAG': os.getenv("SDM_AUTO_APPROVE_TAG"),
    'AUTO_APPROVE_ROLE_ALL': str(os.getenv("SDM_AUTO_APPROVE_ROLE_ALL", "")).lower() == 'true',
    'AUTO_APPROVE_ROLE_TAG': os.getenv("SDM_AUTO_APPROVE_ROLE_TAG"),
    'ALLOW_RESOURCE_TAG': os.getenv("SDM_ALLOW_RESOURCE_TAG"),
    'HIDE_RESOURCE_TAG': os.getenv("SDM_HIDE_RESOURCE_TAG"),
    'HIDE_ROLE_TAG': os.getenv("SDM_HIDE_ROLE_TAG"),
    'GRANT_TIMEOUT': int(os.getenv("SDM_GRANT_TIMEOUT", "60")),
    'CONTROL_RESOURCES_ROLE_NAME': os.getenv("SDM_CONTROL_RESOURCES_ROLE_NAME"),
    'ADMINS_CHANNEL': os.getenv("SDM_ADMINS_CHANNEL"),
    'MAX_AUTO_APPROVE_USES': os.getenv("SDM_MAX_AUTO_APPROVE_USES"),
    'MAX_AUTO_APPROVE_INTERVAL': os.getenv("SDM_MAX_AUTO_APPROVE_INTERVAL"),
    'USER_ROLES_TAG': os.getenv("SDM_USER_ROLES_TAG"),
    'RESOURCE_GRANT_TIMEOUT_TAG': os.getenv("SDM_RESOURCE_GRANT_TIMEOUT_TAG"),
    'ENABLE_RESOURCES_FUZZY_MATCHING': str(os.getenv("SDM_ENABLE_RESOURCES_FUZZY_MATCHING", 'true')).lower() == 'true',
    'EMAIL_SLACK_FIELD': os.getenv("SDM_EMAIL_SLACK_FIELD"),
    'EMAIL_SUBADDRESS': os.getenv("SDM_EMAIL_SUBADDRESS")
}

def get():
    return _INSTANCE

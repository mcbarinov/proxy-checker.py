import importlib.metadata

from mm_base1.config import BaseAppConfig
from mm_base1.services.dconfig_service import DConfigStorage
from mm_base1.services.dvalue_service import DValueStorage


def _get_version() -> str:
    try:
        return importlib.metadata.version("app")
    except importlib.metadata.PackageNotFoundError:
        return " unknown"


class AppConfig(BaseAppConfig):
    app_version: str = _get_version()
    tags: list[str] = ["main"]
    main_menu: dict[str, str] = {"/sources": "sources", "/proxies": "proxies"}


class DConfigSettings(DConfigStorage):
    pass


class DValueSettings(DValueStorage):
    pass

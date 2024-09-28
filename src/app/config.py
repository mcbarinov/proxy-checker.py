from mm_base1.config import BaseAppConfig
from mm_base1.services.dconfig_service import DConfigStorage
from mm_base1.services.dvalue_service import DValueStorage


class AppConfig(BaseAppConfig):
    tags: list[str] = ["main"]
    main_menu: dict[str, str] = {"/sources": "sources", "/proxies": "proxies"}


class DConfigSettings(DConfigStorage):
    pass


class DValueSettings(DValueStorage):
    pass

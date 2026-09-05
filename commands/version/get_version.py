import os
from dataclasses import dataclass

@dataclass
class VersionInfo:
    version: str

class VersionService:
    def get_version(self) -> VersionInfo:
        version = os.getenv("MOLANKO_BOT_VERSION", "unknown")
        return VersionInfo(version=version)

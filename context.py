from abc import ABC, abstractmethod


class BotContext(ABC):
    @abstractmethod
    async def reply(self, text: str, **kwargs) -> None:
        ...

    @property
    @abstractmethod
    def locale(self) -> str:
        """返回语言代码，如 'zh-CN' / 'en'"""
        ...
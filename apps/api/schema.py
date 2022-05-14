import logging
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


logger = logging.getLogger(__name__)


class Ping(BaseModel):
    ping: str = Field(description="Ping")


class MonitorList(BaseModel):
    query: Optional[str] = None


class MonitorView(BaseModel):
    monitor_id: int = Field(description="Monitor ID")


class MonitorCreate(BaseModel):
    monitor_name: str = Field(description="Monitor name")
    monitor_host: str = Field(description="Host dns name or ip address")
    monitor_port: int = Field(description="Port")


class MonitorEdit(BaseModel):
    monitor_id: int = Field(description="Monitor ID")
    monitor_name: str = Field(description="Monitor name")
    monitor_host: str = Field(description="Host dns name or ip address")
    monitor_port: int = Field(description="Port")


class MonitorDelete(BaseModel):
    monitor_id: int = Field(description="Monitor ID")


class MonitorStart(BaseModel):
    monitor_id: int = Field(description="Monitor ID")


class MonitorStop(BaseModel):
    monitor_id: int = Field(description="Monitor ID")


class MonitorActivity(BaseModel):
    monitor_id: int = Field(description="Monitor ID")


class RestoreActivity(BaseModel):
    monitor_id: int = Field(description="Monitor ID")


class RestoreEdit(BaseModel):
    monitor_id: int = Field(description="Monitor ID")
    restore_host: str = Field(description="Host dns name or ip address")
    restore_port: int = Field(description="Port")
    restore_username: str = Field(description="Restore username")
    restore_password: str = Field(description="Restore password")
    restore_commands: str = Field(description="Restore commands")

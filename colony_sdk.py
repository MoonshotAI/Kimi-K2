"""
Colony SDK — Sovereign Hive
Canonical factory for the 5-endpoint Colony Standard Layer.
Import make_colony_router() and mount it in any FastAPI app.

Usage:
    from colony_sdk import ColonyConfig, make_colony_router
    app.include_router(make_colony_router(ColonyConfig(colony_id="kimi-k2", ...)))
"""

import hashlib
import hmac
import os
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel

# HMAC secret — set HIVE_JWT_SECRET to the same value as THEHIVE's jwt_secret_key.
# If unset, HMAC verification is skipped (permissive mode for local dev).
_HIVE_SECRET = os.getenv("HIVE_JWT_SECRET", "").encode()


def _verify_hive_signature(request: Request, body: bytes) -> None:
    """Reject requests whose X-Hive-Signature doesn't match HMAC-SHA256(body, HIVE_JWT_SECRET)."""
    if not _HIVE_SECRET:
        return  # permissive — no secret configured
    sig_header = request.headers.get("X-Hive-Signature", "")
    if not sig_header.startswith("sha256="):
        raise HTTPException(status_code=401, detail="Missing X-Hive-Signature header")
    expected = "sha256=" + hmac.new(_HIVE_SECRET, body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(sig_header, expected):
        raise HTTPException(status_code=401, detail="Invalid hive signature")

_START_MONOTONIC = time.monotonic()
_START_DT = datetime.now()


@dataclass
class ColonyConfig:
    colony_id: str
    colony_name: str
    role: str
    archetype: str
    layer: int
    entity: str
    guilds: List[str] = field(default_factory=list)
    hive: str = "sovereign-hive"
    queen: str = "http://localhost:8080"
    version: str = "1.0.0"
    port: int = 8000
    soul_md_path: str = "soul.md"
    agents: List[Dict[str, Any]] = field(default_factory=list)
    capabilities: List[str] = field(default_factory=list)
    extra_endpoints: List[str] = field(default_factory=list)


class HiveEvent(BaseModel):
    event_type: str
    payload: Dict[str, Any] = {}
    source: Optional[str] = None


class EventResponse(BaseModel):
    event_id: str
    status: str
    colony_id: str


def _soul_hash(path: str) -> str:
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()[:16]
    except Exception:
        return "none"


def make_colony_router(config: ColonyConfig) -> APIRouter:
    """
    Build and return an APIRouter with the full Colony Standard Layer:
      GET  /colony/health
      GET  /colony/info
      GET  /colony/manifest
      POST /colony/events
      GET  /colony/agents
      GET  /colony/capabilities
    """
    router = APIRouter(prefix="/colony", tags=["colony"])

    @router.get("/health")
    def health():
        uptime = int(time.monotonic() - _START_MONOTONIC)
        return {
            "status": "healthy",
            "colony_id": config.colony_id,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "uptime_seconds": uptime,
        }

    @router.get("/info")
    def info():
        return {
            "colony_id": config.colony_id,
            "colony_name": config.colony_name,
            "role": config.role,
            "archetype": config.archetype,
            "layer": config.layer,
            "entity": config.entity,
            "guilds": config.guilds,
            "hive": config.hive,
            "queen": config.queen,
            "version": config.version,
            "soul_md_hash": _soul_hash(config.soul_md_path),
            "port": config.port,
        }

    @router.get("/capabilities")
    def capabilities():
        """colony.json identity + live status — mirrors THEHIVE's /colony/capabilities."""
        import json as _json
        identity: Dict[str, Any] = {}
        here = os.path.dirname(os.path.abspath(__file__))
        for candidate in (os.path.join(here, "colony.json"),
                          os.path.join(here, "..", "colony.json"),
                          "colony.json"):
            try:
                with open(os.path.normpath(candidate)) as f:
                    identity = _json.load(f)
                break
            except Exception:
                continue
        if not identity:
            identity = {
                "colony_id": config.colony_id,
                "colony_name": config.colony_name,
                "role": config.role,
                "version": config.version,
            }
        return {
            **identity,
            "status": "healthy",
            "uptime_s": round(time.monotonic() - _START_MONOTONIC, 1),
            "soul_md_hash": _soul_hash(config.soul_md_path),
            "health_endpoint": "/colony/health",
            "capabilities_endpoint": "/colony/capabilities",
        }

    @router.get("/manifest")
    def manifest():
        standard_endpoints = [
            "/colony/health", "/colony/info", "/colony/manifest",
            "/colony/events", "/colony/agents", "/colony/capabilities",
        ]
        return {
            "colony_id": config.colony_id,
            "endpoints": standard_endpoints + config.extra_endpoints,
            "capabilities": config.capabilities,
            "version": config.version,
        }

    @router.post("/events", response_model=EventResponse)
    async def events(request: Request):
        body = await request.body()
        _verify_hive_signature(request, body)
        try:
            event = HiveEvent.model_validate_json(body)
        except Exception:
            raise HTTPException(status_code=422, detail="Invalid event body")
        return EventResponse(
            event_id=str(uuid.uuid4()),
            status="received",
            colony_id=config.colony_id,
        )

    @router.get("/agents")
    def agents():
        return config.agents

    return router

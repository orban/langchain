"""Common schema objects."""

from dataclasses import dataclass
from typing import Any, Dict, Generator, List, NamedTuple, Optional

from dataclasses_json import dataclass_json


class AgentAction(NamedTuple):
    """Agent's action to take."""

    tool: str
    tool_input: str
    log: str


class AgentFinish(NamedTuple):
    """Agent's return value."""

    return_values: dict
    log: str


@dataclass_json
@dataclass
class Generation:
    """Output of a single generation."""

    text: str
    """Generated text output."""

    generation_info: Optional[Dict[str, Any]] = None
    """Raw generation info response from the provider"""
    """May include things like reason for finishing (e.g. in OpenAI)"""
    # TODO: add log probs


@dataclass_json
@dataclass
class LLMResult:
    """Class that contains all relevant information for an LLM Result."""

    generations: List[List[Generation]]
    """List of the things generated. This is List[List[]] because
    each input could have multiple generations."""
    llm_output: Optional[dict] = None
    """For arbitrary LLM provider specific output."""


@dataclass_json
@dataclass
class StreamingGeneration:
    """Streaming output of a single generation. Returns a generator object.
    Tokens are sent as data-only server-sent events as they become available,
    with the stream terminated by a data: [DONE] message."""

    text: Generator
    """Stream of generated text output."""

    generation_info: Optional[Dict[str, Any]] = None
    """Raw generation info response from the provider"""
    """May include things like reason for finishing (e.g. in OpenAI)"""


@dataclass_json
@dataclass
class LLMStreamingResult:
    """Class that contains all relevant information for a streaming LLM Result."""

    generations: List[StreamingGeneration]
    """List of the things generated. This is List[] because
    each input returns a Generator of server-sent events."""
    llm_output: Optional[dict] = None
    """For arbitrary LLM provider specific output."""

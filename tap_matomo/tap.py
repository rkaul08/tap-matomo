"""Investing tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk.typing import (
    ArrayType,
    DateTimeType,
    NumberType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)
from tap_matomo.streams import VisitsDetailsStream

PLUGIN_NAME = "tap-matomo"

STREAM_TYPES = [
    VisitsDetailsStream,
]


class TapMatomo(Tap):
    """Matomo tap class."""

    name = "tap-matomo"
    config_jsonschema = PropertiesList(
        Property(
            "api",
            ObjectType(
                Property("base_url", StringType, required=True),
                Property("module", StringType, required=True),
                Property("method", StringType, default="Live.getLastVisitsDetails"),
                Property("idSite", StringType, required=True),
                Property("period", StringType, required=True),
                Property("date", StringType, required=True),
                Property("format", StringType, required=True),
                Property("token_auth", StringType, required=True),
                Property("filter_limit", NumberType, default=10000),
            ),
            required=True,
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


# CLI Execution:

cli = TapMatomo.cli

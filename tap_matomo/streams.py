"""Stream class for tap-matomo."""

from typing import Iterable

import requests
from singer_sdk import Stream, Tap
from singer_sdk.typing import (
    ArrayType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class TapAnalyticsStream(Stream):
    pass


class VisitsDetailsStream(TapAnalyticsStream):
    name = "visitsDetails"

    schema = PropertiesList(
        Property("idSite", StringType),
        Property("idVisit", StringType),
        Property("visitIp", StringType),
        Property("visitorId", StringType),
        Property("fingerprint", StringType),
        Property(
            "actionDetails",
            ArrayType(
                ObjectType(
                    Property("type", StringType),
                    Property("url", StringType),
                    Property("pageTitle", StringType),
                    Property("pageIdAction", StringType),
                    Property("idpageview", StringType),
                    Property("serverTimePretty", StringType),
                    Property("pageId", StringType),
                    Property("pageLoadTime", StringType),
                    Property("timeSpent", StringType),
                    Property("timeSpentPretty", StringType),
                    Property("pageLoadTimeMilliseconds", StringType),
                    Property("pageviewPosition", StringType),
                    Property("title", StringType),
                    Property("subtitle", StringType),
                    Property("icon", StringType),
                    Property("iconSVG", StringType),
                    Property("timestamp", StringType),
                    Property("eventCategory", StringType),
                    Property("eventAction", StringType),
                    Property("eventName", StringType),
                    Property("eventValue", StringType),
                    Property("idsite", StringType),
                    Property("player_name", StringType),
                    Property("media_type", StringType),
                    Property("resolution", StringType),
                    Property("fullscreen", StringType),
                    Property("media_title", StringType),
                    Property("time_to_initial_play", StringType),
                    Property("watched_time", StringType),
                    Property("media_progress", StringType),
                    Property("media_length", StringType),
                )
            ),
        ),
        Property("goalConversions", StringType),
        Property("siteCurrency", StringType),
        Property("siteCurrencySymbol", StringType),
        Property("serverDate", StringType),
        Property("visitServerHour", StringType),
        Property("lastActionTimestamp", StringType),
        Property("lastActionDateTime", StringType),
        Property("siteName", StringType),
        Property("serverTimestamp", StringType),
        Property("firstActionTimestamp", StringType),
        Property("serverTimePretty", StringType),
        Property("serverDatePretty", StringType),
        Property("serverDatePrettyFirstAction", StringType),
        Property("serverTimePrettyFirstAction", StringType),
        Property("userId", StringType),
        Property("visitorType", StringType),
        Property("visitorTypeIcon", StringType),
        Property("visitConverted", StringType),
        Property("visitConvertedIcon", StringType),
        Property("visitCount", StringType),
        Property("visitEcommerceStatus", StringType),
        Property("visitEcommerceStatusIcon", StringType),
        Property("daysSinceFirstVisit", StringType),
        Property("secondsSinceFirstVisit", StringType),
        Property("daysSinceLastEcommerceOrder", StringType),
        Property("secondsSinceLastEcommerceOrder", StringType),
        Property("visitDuration", StringType),
        Property("visitDurationPretty", StringType),
        Property("searches", StringType),
        Property("actions", StringType),
        Property("interactions", StringType),
        Property("referrerType", StringType),
        Property("referrerTypeName", StringType),
        Property("referrerName", StringType),
        Property("referrerKeyword", StringType),
        Property("referrerKeywordPosition", StringType),
        Property("referrerUrl", StringType),
        Property("referrerSearchEngineUrl", StringType),
        Property("referrerSearchEngineIcon", StringType),
        Property("referrerSocialNetworkUrl", StringType),
        Property("referrerSocialNetworkIcon", StringType),
        Property("languageCode", StringType),
        Property("language", StringType),
        Property("deviceType", StringType),
        Property("deviceTypeIcon", StringType),
        Property("deviceBrand", StringType),
        Property("deviceModel", StringType),
        Property("operatingSystem", StringType),
        Property("operatingSystemName", StringType),
        Property("operatingSystemIcon", StringType),
        Property("operatingSystemCode", StringType),
        Property("operatingSystemVersion", StringType),
        Property("browserFamily", StringType),
        Property("browserFamilyDescription", StringType),
        Property("browser", StringType),
        Property("browserName", StringType),
        Property("browserIcon", StringType),
        Property("browserCode", StringType),
        Property("browserVersion", StringType),
        Property("events", StringType),
        Property("continent", StringType),
        Property("continentCode", StringType),
        Property("country", StringType),
        Property("countryCode", StringType),
        Property("countryFlag", StringType),
        Property("region", StringType),
        Property("regionCode", StringType),
        Property("city", StringType),
        Property("location", StringType),
        Property("latitude", StringType),
        Property("longitude", StringType),
        Property("visitLocalTime", StringType),
        Property("visitLocalHour", StringType),
        Property("daysSinceLastVisit", StringType),
        Property("secondsSinceLastVisit", StringType),
        Property("resolution", StringType),
        Property("plugins", StringType),
        Property(
            "pluginsIcons",
            ArrayType(
                ObjectType(
                    Property("pluginIcon", StringType),
                    Property("pluginName", StringType),
                )
            ),
        ),
        Property("experiments", ArrayType(StringType)),
        Property("adClickId", StringType),
        Property("adProviderId", StringType),
        Property("adProviderName", StringType),
        Property("formConversions", StringType),
        Property("sessionReplayUrl", StringType),
        Property("campaignId", StringType),
        Property("campaignContent", StringType),
        Property("campaignKeyword", StringType),
        Property("campaignMedium", StringType),
        Property("campaignName", StringType),
        Property("campaignSource", StringType),
        Property("campaignGroup", StringType),
        Property("campaignPlacement", StringType),
    ).to_dict()

    primary_keys = ["idVisit"]

    def __init__(self, tap: Tap):
        super().__init__(tap=tap, name=None, schema=None)

    # @property
    # def partitions(self) -> List[dict]:
    #     return self.config.get("vsits", [])

    def get_records(self, partition: dict) -> Iterable[dict]:
        api_config = self.config["api"]
        base_url = api_config["base_url"]
        parameters = {
            "module": api_config["module"],
            "method": api_config["method"],
            "idSite": api_config["idSite"],
            "period": api_config["period"],
            "date": api_config["date"],
            "format": api_config["format"],
            "token_auth": api_config["token_auth"],
            "filter_limit": api_config["filter_limit"],
        }

        # Construct the full URL
        url = base_url + "?" + "&".join(f"{k}={v}" for k, v in parameters.items())

        # Fetch the text (JSON) from the URL
        response = requests.get(url, timeout=10)
        records = response.json()

        for record in records:
            yield record

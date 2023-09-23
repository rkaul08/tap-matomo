# tap-matomo

`tap-matomo` is a Singer tap for [Matomo](https://matomo.org/)
that can be used to pull the site visits.

Built with [Meltano Singer SDK](https://sdk.meltano.com/).
and [Singer.io Specs](https://github.com/singer-io).

## Usage

### Extract only

Run `tap-matomo` by itself using `meltano invoke`:

```bash
meltano invoke tap-matomo
```

#### Extract & Load

Run `tap-matomo` in a pipeline with a loader using `meltano elt`:

```bash
# Add target-jsonl loader
meltano add loader target-jsonl

# Create output directory
mkdir output

# Run pipeline
meltano elt tap-matomo target-jsonl

# View results
cat output/assets.jsonl
```

You should see output along the following lines:

```
{ "idSite": "", "idVisit": "", "visitIp": "", "visitorId": "", "fingerprint": "", "actionDetails": [ { "type": "action", "url": "", "pageTitle": "", "pageIdAction": "", "idpageview": "", "serverTimePretty": "", "pageId": "", "pageLoadTime": "", "timeSpent": "", "timeSpentPretty": "", "pageLoadTimeMilliseconds": "", "pageviewPosition": "", "title": "", "subtitle": "", "icon": "", "iconSVG": "", "timestamp": "" }, { "type": "event", "url": "", "pageIdAction": "", "idpageview": "", "serverTimePretty": "", "pageId": "", "eventCategory": "", "eventAction": "", "pageviewPosition": "", "timestamp": "", "icon": "", "iconSVG": "", "title": "", "subtitle": "", "eventName": "", "eventValue": "" } ], "goalConversions": "", "siteCurrency": "", "siteCurrencySymbol": "", "serverDate": "", "visitServerHour": "", "lastActionTimestamp": "", "lastActionDateTime": "", "siteName": "", "serverTimestamp": "", "firstActionTimestamp": "", "serverTimePretty": "", "serverDatePretty": "", "serverDatePrettyFirstAction": "", "serverTimePrettyFirstAction": "", "userId": "", "visitorType": "", "visitorTypeIcon": "", "visitConverted": "", "visitConvertedIcon": "", "visitCount": "", "visitEcommerceStatus": "", "visitEcommerceStatusIcon": "", "daysSinceFirstVisit": "", "secondsSinceFirstVisit": "", "daysSinceLastEcommerceOrder": "", "secondsSinceLastEcommerceOrder": "", "visitDuration": "", "visitDurationPretty": "", "searches": "", "actions": "", "interactions": "", "referrerType": "", "referrerTypeName": "", "referrerName": "", "referrerKeyword": "", "referrerKeywordPosition": "", "referrerUrl": "", "referrerSearchEngineUrl": "", "referrerSearchEngineIcon": "", "referrerSocialNetworkUrl": "", "referrerSocialNetworkIcon": "", "languageCode": "", "language": "", "deviceType": "", "deviceTypeIcon": "", "deviceBrand": "", "deviceModel": "", "operatingSystem": "", "operatingSystemName": "", "operatingSystemIcon": "", "operatingSystemCode": "", "operatingSystemVersion": "", "browserFamily": "", "browserFamilyDescription": "", "browser": "", "browserName": "", "browserIcon": "", "browserCode": "", "browserVersion": "", "events": "", "continent": "", "continentCode": "", "country": "", "countryCode": "", "countryFlag": "", "region": "", "regionCode": "", "city": "", "location": "", "latitude": "", "longitude": "", "visitLocalTime": "", "visitLocalHour": "", "daysSinceLastVisit": "", "secondsSinceLastVisit": "", "resolution": "", "plugins": "", "pluginsIcons": [ { "pluginIcon": "", "pluginName": "" } ], "experiments": [], "adClickId": "", "adProviderId": "", "adProviderName": "", "formConversions": "", "sessionReplayUrl": "", "campaignId": "", "campaignContent": "", "campaignKeyword": "", "campaignMedium": "", "campaignName": "", "campaignSource": "", "campaignGroup": "", "campaignPlacement": "" }
```

## Stand-alone usage

### Installation

```bash
pip install git+https://github.com/epappas/tap-matomo.git
```

### Configuration

Create a `config.json` file with content along the following lines:

```json
{
  "api": {
    "base_url": "https://example.com/",
    "module": "API",
    "method": "Live.getLastVisitsDetails",
    "idSite": "25",
    "period": "day",
    "date": "yesterday",
    "format": "JSON",
    "token_auth": "..changeme..",
    "filter_limit": 10000
  }
}
```

### Usage

Run `tap-matomo` with the `config.json` file created above:

```bash
tap-matomo --config config.json
```

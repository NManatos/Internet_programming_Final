import os
import json
from django.http import JsonResponse
#import requests
from django.shortcuts import HttpResponse
api_url ="https://developer.ticketmaster.com/api-explorer/v2?apiCategory=Discovery%20API%20v2&methodId=discovery.v2.events&id=&keyword=&attractionId=&venueId=&postalCode=&latlong=&radius=&unit=none&source=none&locale=*&marketId=&startDateTime=&endDateTime=&includeTBA=none&includeTBD=none&includeTest=none&size=&page=&sort=&onsaleStartDateTime=&onsaleEndDateTime=&city=&countryCode=none&stateCode=&classificationName=&classificationId=&dmaId=&localStartDateTime=&localStartEndDateTime=&startEndDateTime=&publicVisibilityStartDateTime=&preSaleDateTime=&onsaleOnStartDate=&onsaleOnAfterStartDate=&collectionId=&segmentId=&segmentName=&includeFamily=none&promoterId=&genreId=&subGenreId=&typeId=&subTypeId=&geoPoint=&preferredCountry=none&includeSpellcheck=none&domain="

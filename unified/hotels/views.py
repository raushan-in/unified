import requests

from rest_framework import response, views
from .utils import full_match, is_nearby, partial_match


class HotelList(views.APIView):
    '''
    List of hotels from different sources.
    '''

    def get(self, request, lat=None, lon=None):
        # swiggy_uri = "..../swiggy?lat=lat&lon=lon"
        # foodpanda_uri = "...../foodpanda?lat=lat&lon=lon"
        # hotel_from_swiggy = requests.get(swiggy_uri, params=request.GET).json()
        # hotel_from_foodpanda = requests.get(foodpanda_uri, params=request.GET).json()

        hotel_from_swiggy = [
             {"name": "Hotel A",
              "location": {
                          "lat": 19.096905,
                          "lng": 72.85387
                        },
             },
             {"name": "oyo hotel b",
              "location": {
                          "lat": 19.096905,
                          "lng": 72.99
                        }
              },
             {"name": "oyo hotel D",
              "location": {
                          "lat": 29.096905,
                          "lng": 72.99
                        }
              },
        ]

        hotel_from_foodpanda = [
            {"name": "Hotel A",
             "location": {
                          "lat": 19.096905,
                          "lng": 72.85388
                        },
             },
            {"name": "Hotel B",
             "location": {
                          "lat": 19.096905,
                          "lng": 72.99
                        },
             },
            {"name": "C Hotel",
             "location": {
                          "lat": 19.096905,
                          "lng": 89.99
                        },
             }
        ]

        final_list = []

        for swiggy_hotel in hotel_from_swiggy:
            for fp_hotel in hotel_from_foodpanda:
                if full_match(swiggy_hotel, fp_hotel):
                    final_list.append(fp_hotel)
                    hotel_from_foodpanda.remove(fp_hotel)
                    break

                elif partial_match(swiggy_hotel, fp_hotel) and is_nearby(swiggy_hotel, fp_hotel):
                    final_list.append(fp_hotel)
                    hotel_from_foodpanda.remove(fp_hotel)
                    break

                else:
                    final_list.append(swiggy_hotel)

        if hotel_from_foodpanda:
            for fp_hotel in hotel_from_foodpanda:
                final_list.append(fp_hotel)

        custom_dict = {
            "geo": {"lat": lat, "lon": lon},
            "hotels": final_list
        }
        return response.Response(custom_dict)

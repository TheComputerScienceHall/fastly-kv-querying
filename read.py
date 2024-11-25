import fastly
from fastly.api import kv_store_item_api
import env
configuration = fastly.Configuration()
configuration.api_token = env.api

with fastly.ApiClient(configuration) as api_client:
    api_instance = kv_store_item_api.KvStoreItemApi(api_client)
    store_id = env.store  
    key_name = env.logic.l1

    try:
        api_response = api_instance.get_value_for_key(store_id, key_name)
        print(api_response)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreItemApi->get_value_for_key: %s\n" % e)
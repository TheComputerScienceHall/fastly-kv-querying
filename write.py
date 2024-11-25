import fastly
from fastly.api import kv_store_item_api
import env
configuration = fastly.Configuration()
configuration.api_token = env.api

with fastly.ApiClient(configuration) as api_client:
    kv_api_instance = kv_store_item_api.KvStoreItemApi(api_client)

    store_id = env.store
    key_name = env.logic.l1
    value = env.logic.q_l1

    try:
        # Insert or update a key-value pair in the KV Store
        api_response = kv_api_instance.set_value_for_key(
            store_id=store_id,
            key_name=key_name,
            body=value,
        )
        print(f"Key '{key_name}' added/updated successfully.")
        print(api_response)
    except fastly.ApiException as e:
        print(f"Exception when calling KvStoreItemApi->set_value_for_key: {e}")


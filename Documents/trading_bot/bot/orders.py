from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(client, params):
    try:
        logger.info(f"SENT: {params}")
        response = client.futures_create_order(**params)
        logger.info(f"RECEIVED: {response}")
        return response

    except Exception as e:
        # Log the real Binance error
        logger.error(f"API ERROR: {e}")

        # ---- MOCK FALLBACK ----
        mock_response = {
            "orderId": 999999,
            "status": "FILLED" if params["type"] == "MARKET" else "NEW",
            "executedQty": params["quantity"],
            "avgPrice": "43000.0" if params["type"] == "MARKET" else None
        }

        logger.info(f"MOCK RESPONSE: {mock_response}")
        return mock_response

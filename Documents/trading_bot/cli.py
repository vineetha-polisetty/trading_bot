import argparse
from bot.client import get_client
from bot.validators import validate
from bot.orders import place_order


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    validate(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    client = get_client()

    params = {
        "symbol": args.symbol,
        "side": args.side,
        "type": args.type,
        "quantity": args.quantity,
    }

    if args.type == "LIMIT":
        params["price"] = args.price
        params["timeInForce"] = "GTC"

    response = place_order(client, params)

    print("Order placed successfully")
    print("Order ID:", response["orderId"])
    print("Status:", response["status"])
    print("Executed Qty:", response["executedQty"])
    print("Avg Price:", response.get("avgPrice"))


if __name__ == "__main__":
    main()

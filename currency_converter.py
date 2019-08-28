import click
import json
from exchange import *


@click.command()
@click.option('--amount', '-a',
              help='Amount of money you want to convert from one currency to another.',
              required=True,
              type=float)
@click.option('--input_currency', '-i',
              help='Currency you want to convert money from.',
              required=True,
              type=str)
@click.option('--output_currency', '-o',
              help='Currency you want to convert money to.',
              type=str)
def main(amount, input_currency, output_currency):
    """
    Currency converter script which converts money from one currency to another.
    If it doesn't find conversion rate between desired currencies, message will show up on stdout.
    Only positive number is accepted as amount.
    Amount and input_currency are mandatory parameters, output_currency is optional.
    If you don't provide output_currency parameter, script will automatically convert input_currency to every known
    currency.
    """
    currency_converter = Exchange()

    try:
        converted_currencies = currency_converter.convert(amount, input_currency, output_currency)
    except CurrencyCodeNotFoundError as errcc:
        print(errcc)
        exit()
    except ValueError as errv:
        print(errv)
        exit()
    except TypeError as errt:
        print(errt)
        exit()

    print(json.dumps(converted_currencies, indent=4))


if __name__ == '__main__':
    main()

# currency_converter_CLI
CLI application for converting currencies

## How to execute the converte
Converter is executed from terminal with command `./currency_converter.py`

## Arguments
This CLI appication takes 3 arguments in order as they are written.
1. `--amount / -a` - Amount of money you want to convert [REQUIRED].
2. `--input-currency / -i` - Currency from which you want to convert amount of money [REQUIRED].
3. `--output-currency / -o` - Currency to what you want to convert money [OPTIONAL]. If not defined, amount of money is converted to *EUR*

## Output
JSON file with 2 dictionaries. 
First stores informations about input currency and amount.
Second stores informations about converted currency.

### Example
`./currency_converter.py -a 100 -i EUR -o CZK`

```
{
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "CZK": 2622.6
    }
}
```

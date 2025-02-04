# Currency Converter

This is a simple currency converter application built using Python's `Tkinter` for the graphical user interface (GUI) and `requests` to fetch currency conversion rates. The application allows users to convert an amount of money from one currency to another.

## Features

- Convert any amount of money from one currency to another.
- The user can specify the amount, source currency, and target currency.
- The app fetches the conversion rate using a Google search URL.
- Displays the result directly on the GUI or an error message if something goes wrong.

## Requirements

- Python 3.x
- `Tkinter` (comes pre-installed with Python)
- `requests` library (can be installed via pip)

To install the `requests` library, run:

```bash
pip install requests
```

## Usage

1. Run the Python script.
2. In the application window:
  - Enter the amount of currency you want to convert.
  - Enter the source currency code (e.g., USD, EUR, etc.).
  - Enter the target currency code (e.g., USD, EUR, etc.).
3. Click the Convert button to see the result.

The conversion result will be displayed in the application window.

## How it Works

The app uses a simple search query to Google to get the currency conversion rate and displays it in the format:

<amount> <from_currency> = <converted_amount> <to_currency>

In case of an error (e.g., invalid currency codes or no internet connection), the application shows an error message.

## Example

If you want to convert 100 USD to EUR, enter:
- Amount: 100
- From Currency: USD
- To Currency: EUR

Click the Convert button to see the result.

## License

This project is open source and available under the MIT License.


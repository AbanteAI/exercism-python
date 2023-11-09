# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description
        self.change = change


def create_entry(date, description, change):
    return LedgerEntry(date, description, change)


    # Sort entries by date, change, and description
    entries = sorted(entries, key=lambda x: (x.date, x.change, x.description))

    # Generate Header Row based on locale
    if locale == 'en_US':
        header = 'Date       | Description               | Change       '
    elif locale == 'nl_NL':
        header = 'Datum      | Omschrijving              | Verandering  '
    else:
        raise ValueError("Unsupported locale")

    # Initialize the table with the header
    table = header

    # Process each entry
    for entry in entries:
        table += '\n' + format_date(entry.date, locale) + ' | ' + format_description(entry.description) + ' | ' + format_change(entry.change, currency)

    return table

def format_date(date, locale):
    if locale == 'en_US':
        return date.strftime('%m/%d/%Y')
    elif locale == 'nl_NL':
        return date.strftime('%d-%m-%Y')
    else:
        raise ValueError("Unsupported locale")

def format_description(description):
    if len(description) > 25:
        return description[:22] + '...'
    else:
        return description.ljust(25)

def format_change(change, currency):
    if currency == 'USD':
        symbol = '$'
    elif currency == 'EUR':
        symbol = u'€'
    else:
        raise ValueError("Unsupported currency")

    change_str = format_currency(change, symbol)
    if change < 0:
        change_str = '(' + change_str.strip() + ')'
    return change_str.rjust(13)

def format_currency(amount, symbol):
    sign = '-' if amount < 0 else ''
    amount = abs(amount)
    dollars, cents = divmod(amount, 100)
    dollars_str = "{:,}".format(dollars)
    cents_str = "{:02}".format(cents)
    return f"{symbol}{sign}{dollars_str}.{cents_str}"
def format_entries(currency, locale, entries):
    entries = sorted(entries, key=lambda x: (x.date, x.change, x.description))

    if locale == 'en_US':
        header = 'Date       | Description               | Change       '
    elif locale == 'nl_NL':
        header = 'Datum      | Omschrijving              | Verandering  '
    else:
        raise ValueError("Unsupported locale")

    lines = [header]
    for entry in entries:
        lines.append(
            f"{format_date(entry.date, locale)} | {format_description(entry.description)} | {format_change(entry.change, currency)}"
        )
    return '\n'.join(lines)

def format_date(date, locale):
    if locale == 'en_US':
        return date.strftime('%m/%d/%Y')
    elif locale == 'nl_NL':
        return date.strftime('%d-%m-%Y')
    else:
        raise ValueError("Unsupported locale")

def format_description(description):
    if len(description) > 25:
        return description[:22] + '...'
    else:
        return description.ljust(25)

def format_change(change, currency):
    if currency == 'USD':
        symbol = '$'
    elif currency == 'EUR':
        symbol = '€'
    else:
        raise ValueError("Unsupported currency")

    return format_currency(change, symbol)

def format_currency(amount, symbol):
    sign = '-' if amount < 0 else ''
    amount = abs(amount)
    integer, cents = divmod(amount, 100)
    integer_with_commas = "{:,}".format(integer)
    formatted = f"{symbol}{sign}{integer_with_commas}.{cents:02}"
    if amount < 0:
        formatted = f"({formatted})"
    return formatted.rjust(13)

# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry


def generate_header_row(locale):
    if locale == 'en_US':
        return 'Date       | Description               | Change       '
    elif locale == 'nl_NL':
        return 'Datum      | Omschrijving              | Verandering  '
    else:
        raise ValueError("Invalid locale")


def format_date(entry_date, locale):
    if locale == 'en_US':
        return entry_date.strftime('%m/%d/%Y')
    elif locale == 'nl_NL':
        return entry_date.strftime('%d-%m-%Y')
    else:
        raise ValueError("Invalid locale")


def format_description(description):
    if len(description) > 25:
        return description[:22] + '...'
    else:
        return description.ljust(25)


def format_change(change, currency):
    if currency == 'USD':
        change_str = '${:,.2f}'.format(abs(change / 100))
        if change < 0:
            change_str = '(' + change_str + ')'
        else:
            change_str = ' ' + change_str
    elif currency == 'EUR':
        change_str = '€{:,.2f}'.format(abs(change / 100)).replace(',', 'X').replace('.', ',').replace('X', '.')
        if change < 0:
            change_str = '(' + change_str + ')'
        else:
            change_str = ' ' + change_str
    else:
        raise ValueError("Invalid currency")

    return change_str.rjust(13)


def format_entry(entry, currency, locale):
    formatted_date = format_date(entry.date, locale)
    formatted_description = format_description(entry.description)
    formatted_change = format_change(entry.change, currency)

    return f"{formatted_date} | {formatted_description} | {formatted_change}"


def format_entries(currency, locale, entries):
    table = generate_header_row(locale)
    sorted_entries = sorted(entries, key=lambda x: (x.date, x.change, x.description))

    for entry in sorted_entries:
        table += '\n' + format_entry(entry, currency, locale)

    return table
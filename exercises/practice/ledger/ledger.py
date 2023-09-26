# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry(date, description, change)
    return entry


def format_entries(currency, locale, entries):
    header = {
        'en_US': 'Date       | Description               | Change       ',
        'nl_NL': 'Datum      | Omschrijving              | Verandering  '
    }
    table = header[locale] + '\n'

    for entry in sorted(entries, key=lambda x: (x.date, x.change, x.description)):
        date_str = entry.date.strftime('%m/%d/%Y') if locale == 'en_US' else entry.date.strftime('%d-%m-%Y')
        description_str = entry.description[:25].ljust(25) if len(entry.description) > 25 else entry.description.ljust(25)
        change_str = format_currency(currency, entry.change)

        table += f"{date_str} | {description_str} | {change_str}\n"

    return table


def format_currency(currency, change):
    if currency == 'USD':
        return f"${abs(change) / 100:.2f}".rjust(13)

    if currency == 'EUR':
        return f"€{abs(change) / 100:.2f}".rjust(13)


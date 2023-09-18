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


def format_entries(currency, locale, entries):
    def generate_header_row(locale):
        if locale == 'en_US':
            return 'Date       | Description          | Change       '
        elif locale == 'nl_NL':
            return 'Datum      | Omschrijving         | Verandering  '

    def find_next_entry(entries):
        return min(entries, key=lambda x: (x.date, x.change, x.description))

    def format_date(entry_date, locale):
        if locale == 'en_US':
            return entry_date.strftime('%m/%d/%Y')
        elif locale == 'nl_NL':
            return entry_date.strftime('%d-%m-%Y')

    def format_description(description):
        return description[:25].ljust(25)

    def format_change(change, currency):
        change_str = ''
        sign = '-' if change < 0 else ' '
        change = abs(change)
        if currency == 'USD':
            formatted_change = f'{change // 100:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
            change_str = f'{sign}${formatted_change}'
        elif currency == 'EUR':
            formatted_change = f'{change // 100:,.2f}'.replace(',', 'X').replace('.', 'X').replace('X', ',')
            change_str = f'{sign}€{formatted_change}'
        return change_str.rjust(13)

    table = generate_header_row(locale)
    sorted_entries = sorted(entries, key=lambda x: (x.date, x.change, x.description))

    for entry in sorted_entries:
        date_str = format_date(entry.date, locale)
        description_str = format_description(entry.description)
        change_str = format_change(entry.change, currency)
        table += f'\n{date_str} | {description_str} | {change_str}'

    return table
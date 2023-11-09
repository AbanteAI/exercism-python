# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description
        self.change = change


def create_entry(date, description, change):
    return LedgerEntry(date, description, change)
def format_date(entry, locale):
    if locale == 'en_US':
        return entry.date.strftime('%m/%d/%Y')
    elif locale == 'nl_NL':
        return entry.date.strftime('%d-%m-%Y')

def format_description(entry):
    description = entry.description
    if len(description) > 25:
        return description[:22] + '...'
    return description.ljust(25)

def format_change(entry, currency, locale):
    change = entry.change
    if currency == 'USD':
        symbol = '$' if locale == 'en_US' else '$ '
        template = '({})' if change < 0 else '{} '
        decimal_separator = '.' if locale == 'en_US' else ','
        thousand_separator = ',' if locale == 'en_US' else '.'
    elif currency == 'EUR':
        symbol = u'€' if locale == 'nl_NL' else u'€ '
        template = '({})' if change < 0 else '{} '
        decimal_separator = ',' if locale == 'nl_NL' else '.'
        thousand_separator = '.' if locale == 'nl_NL' else ','

    change_str = format(abs(change) / 100.0, f',.2f').replace(',', thousand_separator).replace('.', decimal_separator)
    return template.format(symbol + change_str).rjust(13)

def sort_entries(entries):
    return sorted(entries, key=lambda e: (e.date, e.change, e.description))


def format_entries(currency, locale, entries):
    header = {
        'en_US': 'Date       | Description               | Change       ',
        'nl_NL': 'Datum      | Omschrijving              | Verandering  '
    }

    entries = sort_entries(entries)
    lines = [header[locale]]

    for entry in entries:
        date_str = format_date(entry, locale)
        description_str = format_description(entry)
        change_str = format_change(entry, currency, locale)
        lines.append(f"{date_str} | {description_str} | {change_str}")

    return '\n'.join(lines)

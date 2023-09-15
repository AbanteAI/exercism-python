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


def format_date(entry, locale):
    if locale == 'en_US':
        return entry.date.strftime('%m/%d/%Y')
    elif locale == 'nl_NL':
        return entry.date.strftime('%d-%m-%Y')


def format_description(entry):
    description = entry.description[:22] + '...' if len(entry.description) > 25 else entry.description
    return description.ljust(25)


def format_change(entry, currency, locale):
    change_str = ''
    if entry.change < 0:
        change_str += '(' if locale == 'en_US' else '-'

    if currency == 'USD':
        change_str += '$'
    elif currency == 'EUR':
        change_str += '€'

    change_value = abs(entry.change) / 100.0
    if locale == 'en_US':
        change_str += '{:,.2f}'.format(change_value)
    elif locale == 'nl_NL':
        change_str += '{:,.2f}'.format(change_value).replace('.', 'x').replace(',', '.').replace('x', ',')

    if entry.change < 0 and locale == 'en_US':
        change_str += ')'

    return change_str.rjust(13)


def format_entries(currency, locale, entries):
    entries = sorted(entries, key=lambda x: (x.date, x.change, x.description))

    header = {
        'en_US': 'Date       | Description               | Change       ',
        'nl_NL': 'Datum      | Omschrijving              | Verandering  '
    }

    table = [header[locale]]

    for entry in entries:
        formatted_entry = ' | '.join([
            format_date(entry, locale),
            format_description(entry),
            format_change(entry, currency, locale)
        ])
        table.append(formatted_entry)

    return '\n'.join(table)
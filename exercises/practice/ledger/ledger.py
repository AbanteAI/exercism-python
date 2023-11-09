# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description
        self.change = change


def create_entry(date, description, change):
    return LedgerEntry(date, description, change)


def format_date(entry_date, locale):
    if locale == 'en_US':
        return entry_date.strftime('%m/%d/%Y')
    elif locale == 'nl_NL':
        return entry_date.strftime('%d-%m-%Y')

def format_description(description):
    if len(description) > 25:
        return description[:22] + '...'
    else:
        return description.ljust(25)

def format_change(change, currency, locale):
    sign = '-' if change < 0 else ''
    if currency == 'USD':
        symbol = '$'
    elif currency == 'EUR':
        symbol = u'€'

    if locale == 'en_US':
        formatted_change = f"{symbol}{abs(change):,.2f}"
        if change < 0:
            formatted_change = f"({formatted_change})"
    elif locale == 'nl_NL':
        formatted_change = f"{symbol}{abs(change):,.2f}".replace(',', 'TEMP').replace('.', ',').replace('TEMP', '.')
        if change < 0:
            formatted_change = f"{sign}{formatted_change}"

    return formatted_change.rjust(13)

def format_entries(currency, locale, entries):
    entries.sort(key=lambda x: (x.date, x.change, x.description))

    header = {
        'en_US': 'Date       | Description               | Change       ',
        'nl_NL': 'Datum      | Omschrijving              | Verandering  '
    }

    lines = [header[locale]]
    for entry in entries:
        date_str = format_date(entry.date, locale)
        description_str = format_description(entry.description)
        change_str = format_change(entry.change, currency, locale)
        lines.append(f"{date_str} | {description_str} | {change_str}")

    return '\n'.join(lines)

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
    table = ''
    header_row = {
        'en_US': 'Date             | Description               | Change       ',
        'nl_NL': 'Datum    | Omschrijving           | Verandering  '
    }
    table += header_row[locale]
    
    for entry in sorted(entries, key=lambda e: (e.date, e.change, e.description)):
        date_str = entry.date.strftime('%m/%d/%Y') if locale == 'en_US' else entry.date.strftime('%d-%m-%Y')
        description_str = entry.description[:25] + '...' if len(entry.description) > 25 else entry.description.ljust(25)
        
        if currency == 'USD':
            change_str = f'${abs(entry.change / 100):,.2f}'
        elif currency == 'EUR':
            change_str = f'€{abs(entry.change / 100):,.2f}'
        
        if entry.change < 0:
            change_str = f'({change_str})'
        else:
            change_str = f' {change_str} '
        
        table += f'\n{date_str} | {description_str} | {change_str}'
    
    return table

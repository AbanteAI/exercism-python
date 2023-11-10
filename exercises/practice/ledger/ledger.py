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
    # Format the change amount based on currency and locale
    sign = '-' if change < 0 else ''
    change = abs(change)
    if currency == 'USD':
        symbol = '$'
    elif currency == 'EUR':
        symbol = '€'
    else:
        symbol = ''
    
    if locale == 'en_US':
        formatted_change = f"{symbol}{sign}{change // 100}.{change % 100:02}"
    elif locale == 'nl_NL':
        formatted_change = f"{sign}{change // 100},{change % 100:02} {symbol}"
    
    return formatted_change.rjust(13)

def sort_entries(entries):
    return sorted(entries, key=lambda x: (x.date, x.change, x.description))

def format_entries(currency, locale, entries):
    # Sort the entries first
    sorted_entries = sort_entries(entries)
    
    # Header row
    if locale == 'en_US':
        header = f"{'Date':<10} | {'Description':<25} | {'Change':>13}"
    elif locale == 'nl_NL':
        header = f"{'Datum':<10} | {'Omschrijving':<25} | {'Verandering':>13}"
    
    # Entry rows
    rows = [header]
    for entry in sorted_entries:
        formatted_date = format_date(entry.date, locale)
        formatted_description = format_description(entry.description)
        formatted_change = format_change(entry.change, currency, locale)
        rows.append(f"{formatted_date} | {formatted_description} | {formatted_change}")
    
    return '\n'.join(rows)
def format_change(change, currency, locale):
    # This function will be implemented to format the change according to the currency and locale
    pass

def sort_entries(entries):
    # This function will be implemented to sort the entries
    pass
# The entire existing format_entries function will be refactored to use the new helper functions.
# This will include removing duplicated code and improving readability.
# The exact changes will be provided in the next steps.


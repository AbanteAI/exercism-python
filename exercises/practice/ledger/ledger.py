# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = date
        self.description = description
        self.change = change

def create_entry(date, description, change):
    date = datetime.strptime(date, '%Y-%m-%d')
    return LedgerEntry(date, description, change)


def format_entries(currency, locale, entries):
    # Helper functions
    def format_header(locale):
        if locale == 'en_US':
            return "Date       | Description               | Change       "
        elif locale == 'nl_NL':
            return "Datum      | Omschrijving              | Verandering  "

    def format_date(date, locale):
        if locale == 'en_US':
            return date.strftime('%m/%d/%Y')
        elif locale == 'nl_NL':
            return date.strftime('%d-%m-%Y')

    def format_description(description):
        return description[:25].ljust(25)

    def format_change(change, currency, locale):
        sign = '-' if change < 0 else ''
        amount = f"{abs(change) / 100:.2f}"
        if currency == 'USD':
            formatted = f"{sign}${amount}"
        elif currency == 'EUR':
            formatted = f"{sign}€{amount}"

        if locale == 'en_US':
            formatted = formatted.rjust(13)
            if change < 0:
                formatted = f"({formatted.strip()})"
        elif locale == 'nl_NL':
            formatted = formatted.replace('.', ',').rjust(12)
            if change < 0:
                formatted = f" {formatted.strip()}"

        return formatted

    # Generate the ledger
    header = format_header(locale)
    sorted_entries = sorted(entries, key=lambda x: (x.date, x.change, x.description))
    formatted_entries = [
        f"{format_date(entry.date, locale)} | {format_description(entry.description)} | {format_change(entry.change, currency, locale)}"
        for entry in sorted_entries
    ]

    return '\n'.join([header] + formatted_entries)
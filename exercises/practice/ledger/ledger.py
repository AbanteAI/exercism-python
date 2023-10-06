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
    return entry.description[:22] + '...' if len(entry.description) > 25 else entry.description


def format_change(entry, currency, locale):
    change_str = ''
    change_sign = '-' if entry.change < 0 else ''
    change_abs = abs(entry.change)
    change_whole = change_abs // 100
    change_fraction = change_abs % 100

    if currency == 'USD':
        currency_symbol = '$'
        if locale == 'en_US':
            change_str = f'{currency_symbol}{change_sign}{change_whole:,.2f}'
        elif locale == 'nl_NL':
            change_str = f'{currency_symbol}{change_sign}{change_whole:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    elif currency == 'EUR':
        currency_symbol = '€'
        if locale == 'en_US':
            change_str = f'{currency_symbol}{change_sign}{change_whole:,.2f}'
        elif locale == 'nl_NL':
            change_str = f'{currency_symbol}{change_sign}{change_whole:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

    if entry.change < 0:
        change_str = f'({change_str})'
    else:
        change_str = f' {change_str}'

    return change_str.rjust(13)

    return change_str


def format_entries(currency, locale, entries):
    entries.sort(key=lambda x: (x.date, x.change, x.description))

    header_mapping = {
        'en_US': 'Date       | Description               | Change       ',
        'nl_NL': 'Datum      | Omschrijving              | Verandering  '
    }

    table = [header_mapping[locale]]

    for entry in entries:
        date_str = format_date(entry, locale)
        description_str = format_description(entry)
        change_str = format_change(entry, currency, locale)

        table.append(f'{date_str} | {description_str:25} | {change_str:>13}')

    return '\n'.join(table)
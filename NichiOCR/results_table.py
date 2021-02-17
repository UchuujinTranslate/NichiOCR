from rich.console import Console
from rich.table import Table


def results_table(results):

    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Source", style="dim")
    table.add_column("Content")

    # Stats
    table.add_row(
        "Script",
        results['script'],
    )
    table.add_row(
        "JSON ID",
        str(results['id']),
    )
    table.add_row(
        "Similarity Ratio",
        str(results['similarity_ratio']),
    )
    table.add_row()

    # OCR
    table.add_row(
        "OCR Speaker",
        results['ocr_speaker'],
    )
    table.add_row(
        "OCR String",
        results['ocr_string'],
    )
    table.add_row()

    # Weblate
    table.add_row(
        "Weblate Speaker",
        results['weblate_speaker']
    )
    table.add_row(
        "Weblate String",
        results['weblate_string']
    )
    table.add_row()

    # English
    table.add_row(
        "Weblate Eng Speaker",
        results['eng_speaker']
    )
    table.add_row(
        "Weblate Eng String",
        results['eng_string']
    )
    table.add_row()
    table.add_row(
        "Weblate URL",
        results['weblate_url']
    )

    console.print(table)
    return table

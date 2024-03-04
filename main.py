import os
import argparse
import re
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Search for files or directories containing a specific regex pattern, with options for case sensitivity and search scope.")
    parser.add_argument("search_path", type=str, help="The path to search within.")
    parser.add_argument("search_pattern", type=str, help="The regex pattern to search for in file or directory names.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--files", action="store_true", help="Search only file names.")
    group.add_argument("-d", "--directories", action="store_true", help="Search only directory names.")
    parser.add_argument("-c", "--case-sensitive", action="store_true", help="Perform a case-sensitive search.")
    return parser.parse_args()

def search_and_print_matches(search_path, search_pattern, search_files, search_directories, case_sensitive, progress):
    """Search files or directories for a given regex pattern and print matches with rich formatting."""
    flags = 0 if case_sensitive else re.IGNORECASE
    pattern = re.compile(f"^{search_pattern}$", flags=flags)
    match_count = 0

    for root, dirs, files in os.walk(search_path):
        if search_directories:
            for d in dirs:
                if match := pattern.search(d):
                    print_match(progress, root, d, match, 'D')
                    match_count += 1
        if search_files:
            for f in files:
                if match := pattern.search(f):
                    print_match(progress, root, f, match, 'F')
                    match_count += 1

    return match_count

def print_match(progress, root, name, match, indicator):
    """Highlight and print the matching file or directory."""
    start, end = match.span()
    highlighted_name = f"{name[:start]}[bold green]{name[start:end]}[/]{name[end:]}"
    highlighted_path = os.path.join(root, highlighted_name)
    indicator_str = '[bold yellow]F[/]' if indicator == 'F' else '[bold blue]D[/]'
    progress.console.print(f"{indicator_str} {highlighted_path}")

def main():
    args = parse_arguments()
    console = Console()
    search_files = not args.directories if (args.files or args.directories) else True
    search_directories = not args.files if (args.files or args.directories) else True

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
        entry_types = '[bold yellow]files[/]' if search_files else '[bold blue]directories[/]'
        searching_message = f"Searching for {entry_types} within '[bold magenta]{args.search_path}[/]' containing [bold green]'{args.search_pattern}'[/] {'[bold]with case sensitivity[/]' if args.case_sensitive else ''}"
        task_id = progress.add_task(searching_message, start=False)
        match_count = search_and_print_matches(args.search_path, args.search_pattern, search_files, search_directories, args.case_sensitive, progress)
        progress.remove_task(task_id)

    result_word = 'result' if match_count == 1 else 'results'
    console.print(f"[bold green]{match_count}[/] {result_word} found.")

if __name__ == "__main__":
    main()

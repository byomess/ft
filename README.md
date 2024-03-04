<p align="center">
    <img width="200px" src="https://github.com/felipechierice/ft/blob/main/images/logo.png?raw=true" align="center" alt="Find Turbo Logo" />
    <h2 align="center">ft - Find Turbo</h2>
    <p align="center">Your <code>find</code> command on <strong>turbo</strong></p>
</p>

<p align="center">
    <a href="https://github.com/felipechierice/ft/stargazers">
        <img src="https://img.shields.io/github/stars/felipechierice/ft?style=social" alt="GitHub stars">
    </a>
    <a href="https://github.com/felipechierice/ft/network/members">
        <img src="https://img.shields.io/github/forks/felipechierice/ft?style=social" alt="GitHub forks">
    </a>
    <a href="https://github.com/felipechierice/ft/issues">
        <img src="https://img.shields.io/github/issues/felipechierice/ft" alt="GitHub issues">
    </a>
    <a href="https://github.com/felipechierice/ft/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/felipechierice/ft" alt="GitHub license">
    </a>
    <a href="https://github.com/felipechierice/ft/graphs/contributors">
        <img src="https://img.shields.io/github/contributors/felipechierice/ft" alt="GitHub contributors">
    </a>
    <a href="https://github.com/felipechierice/ft/commits/main">
        <img src="https://img.shields.io/github/last-commit/felipechierice/ft" alt="GitHub last commit">
    </a>
</p>

`ft` (Find Turbo) is simple command-line tool designed to enhance the file/directory search capabilities for Unix-based systems.

Initially, my objective was simply to create a wrapper for the standard Linux `find` command to prevent it from returning "Permission denied" errors as part of its results, when it tries to read files the user don't own. However, as you see, I ended up doing something more.

Much like its inspiration, `ft` aims to provide a more efficient, user-friendly, and visually appealing experience for searching files and directories. It leverages the power of regex patterns for search criteria and the [Rich library](https://github.com/willmcgugan/rich) for elegant formatting, making your search results not only precise but also easier to read and interpret.

## Key Features

- **Rich Formatting**: With the Rich library integration, search results are displayed with syntax highlighting and beautiful formatting, making them more accessible and informative.
- **Regex Pattern Searches**: Use regular expressions to define complex search patterns for file and directory names, offering you nuanced control over search results.
- **Flexible Search Options**: Choose between searching **file** names, **directory** names, or **both**, with additional options for **case sensitivity**, providing a tailored search experience to fit your needs.
- **Intuitive Progress Display**: Features a fancy progress animation with rich visual feedback during search operations, keeping you informed of the ongoing process.

## Why Use ft?

`ft` is built for anyone who regularly works with files and directories and needs an enhanced search tool that goes beyond the capabilities of the traditional `find` command. Whether you're a developer, system administrator, or just a user who loves organizing and navigating through extensive file systems efficiently, `ft` offers:

- Enhanced search precision through regex patterns.
- A visually pleasing and informative output of search results.
- Customizable search parameters to suit various needs and preferences.

## Installation

You can install `ft` using curl, wget, or by manually cloning the repository and installing dependencies. 

### Using Curl

```bash
curl -sSL "https://raw.githubusercontent.com/felipechierice/ft/main/install.sh" | sh -s -- --clone
```

### Using Wget

```bash
wget -qO- "https://raw.githubusercontent.com/felipechierice/ft/main/install.sh" | sh -s -- --clone
```

### Manual Installation

If you prefer to install `ft` manually, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/felipechierice/ft
```

2. Navigate to the `ft` directory:

```bash
cd ft
```

3. Execute the installation script

```bash
./install.sh
```

Ensure you have Python 3.6 or later installed on your system to use `ft`.

## Usage

`ft` is simple to use, with a syntax that allows for versatile search configurations.

### Basic Usage

- **Search for files or directories containing a specific pattern**: Replace `<search_path>` with your target directory and `<search_pattern>` with your regex pattern.

  ```bash
  ft <search_path> <search_pattern>
  ```

### Advanced Options

- **Case-sensitive search**: Add the `-c` or `--case-sensitive` flag for case-sensitive searches.
  
  ```bash
  ft <search_path> <search_pattern> -c
  ```

- **Search only files or directories**: Use `-f` or `--files` to search only file names, and `-d` or `--directories` for directory names.
  
  ```bash
  ft <search_path> <search_pattern> -f
  ft <search_path> <search_pattern> -d
  ```

### Examples

```bash
# Search for all Python files in the current directory
ft . "\.py$" -f

# Case-sensitive search for directories matching 'Data'
ft /home/user "Data" -d -c
```

## Uninstalling

It is as simple as executing the following script:

```bash
~/.local/share/ft/uninstall.sh
```

If you have installed `ft` in a different directory, just make sure you change it in the command.

## Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to fork the repository and submit pull requests.

## License

`ft` is open-source software licensed under the MIT license, making it freely available for personal and commercial use.
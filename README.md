# Port Scanner

This Python script performs a basic port scan on a target URL or IP address. It is intended solely for educational and authorized network security testing purposes.

## Features

-   **Targets Specific Ports**: Scans a predefined list of common ports.
-   **Simple Input**: Takes a target URL or IP address as input.
-   **Clear Output**: Displays whether each scanned port is open or closed using colored text.
-   **Summarizes Results**: Lists all open ports found at the end of the scan.
-   **Educational Tool**: Useful for learning basic network scanning concepts with Python's `socket` library.

## Prerequisites

To run this script, you need to have:

-   Python 3.x installed
-   Basic understanding of networking concepts

## Installation

1.  Save the Python script code to a file (e.g., `port_scanner.py`).
2.  No external libraries are required beyond standard Python modules.

## Usage

1.  Navigate to the directory where you saved the script using your terminal.
2.  Run the script using Python:

    ```bash
    python port_scanner.py
    ```

3.  When prompted, enter the target URL or IP address you wish to scan (ensure you have permission).
4.  The script will then attempt to connect to the predefined ports on the target and print the status for each.
5.  Finally, it will list all the ports found to be open.

**Scanned Ports:** 19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Unauthorized use of this tool to scan networks or devices without explicit permission may violate laws and regulations. Use responsibly.

## Contributing

While this is a simple script, suggestions for improvements are welcome. If you have ideas:

1.  Consider forking if it were in a repository.
2.  Propose changes or enhancements.

## License

This script can be considered under the MIT License if distributed.

## Author

medjahdi
```markdown

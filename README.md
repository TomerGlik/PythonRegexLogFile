# PythonRegexLogFile
# 🧾 Transaction Log Analyzer

This Python script processes a log file (`exam.log`) to extract useful metrics about transaction activity and error events.

## 🔍 What It Does

- Parses the log file line by line
- Extracts and counts all lines with `"ERROR"` status
- Detects the beginning and end of transactions using regex patterns like:
  - `transaction 123 begin`
  - `end transaction 123`
- Matches each transaction's start and end time
- Calculates the **average transaction duration** in milliseconds

## 📂 Expected Log Format (per line)
DD-MM-YYYY HH:MM:SS.mmm<TAB>LEVEL<TAB>...<TAB>...<TAB>message

Example:

    12-05-2024 14:33:22.123 INFO ... ... transaction 123 begin
    12-05-2024 14:33:23.456 INFO ... ... end transaction 123

      


## 📊 Output

- List of log headers (first line, split by tab)
- Total number of `"ERROR"` lines
- Total number of completed transactions
- Average transaction duration in milliseconds (computed from start-end timestamps)

## ⚠️ Notes

- Log file must be named `exam.log` and located in the same directory as the script
- Timestamps are parsed using the format: `%d%m%Y %H:%M:%S.%f` (after removing dashes from date)
- Each transaction ID must appear once as "begin" and once as "end"


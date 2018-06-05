Resulting file will be stored in books/books.json
# Setup
1. Install Python 3.6
2. `pip install -r requirements.txt`
# Launch
1. Open books folder
2. Enter command `scrapy crawl books`.

It will take ~1 minute to execute
# Possible issues
When running the spider on Windows 10, it is possible that the next error will occur:
`ImportError: No module named win32api.`
Enter this command to fix it:
`pip install pypiwin32`
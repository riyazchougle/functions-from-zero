import wikipedia

# Patch the old wikipedia package so it uses HTTPS + a real User-Agent
wikipedia.wikipedia.API_URL = "https://en.wikipedia.org/w/api.php"
wikipedia.wikipedia.USER_AGENT = (
    "functions-from-zero-course/0.1 "
    "(https://github.com/riyazchougle/functions-from-zero; riyazedu786@gmail.com)"
)
def scrape(name="Microsoft", length=1):
    result = wikipedia.summary(name, sentences=length)
    return result
    
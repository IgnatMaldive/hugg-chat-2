from hugchat import hugchat
from hugchat.login import Login


# Log in to huggingface and grant authorization to huggingchat
sign = Login("ignatiusmaldive@gmail.com", "hu&LO8f&e34")
cookies = sign.login()

# Save cookies to the local directory (optional)
# cookie_path_dir = "./cookies_snapshot"
# sign.saveCookiesToDir(cookie_path_dir)

# Create a ChatBot
chatbot = hugchat.ChatBot(cookies)  # or cookie_path="usercookies/<email>.json"


def hugg_chat_query(query):

    # Perform the query
    if query:
        query_result = chatbot.query(query)
        # Convert query_result to string if necessary
        return str(query_result)  # Adjust this line as needed based on the format of query_result
    else:
        return "No query provided."
